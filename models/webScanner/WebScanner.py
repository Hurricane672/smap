import argparse
import logging
import sys
import signal
from lib import __version__
from lib.config import settings
from lib.config.settings import Risk
from lib.request.request import SingleRequest
from lib.utils import banner, manager, output, validator
from lib.utils.container import Services
from lib.utils.datastore import Datastore
from lib.utils.output import Output


class Sitadel(object):
    bn = banner.Banner()
    ma = manager
    url = None
    attack = None
    config = 'config/config.yml'
    cookie = None
    fingerprint = ['cdn', 'cms', 'framework','frontend', 'header', 'language','server', 'system', 'waf']
    proxy = None
    redirect = False
    risk = None
    timeout = 30
    # URL = 'https://blog.csdn.net/'
    # URL = 'http://10.122.220.161:8976'
    URL = 'http://10.21.145.59/'
    # URL = 'https://flask.net.cn/'
    # URL = 'https://spring.io/'
    # URL = 'https://www.thinkphp.cn/'
    user_agent = 'WebScanner 1.0.0'
    verbosity = 0

    def __init__(self, URL):
        self.url = validator.validate_target(URL)

    def main(self):
        # self.url = validator.validate_target(self.URL)

        settings.from_yaml(self.config)
        if self.risk is not None:
            settings.risk = Risk(self.risk)

        logger = logging.getLogger("sitadelLog")
        logging.basicConfig(
            filename="sitadel.log",
            filemode="w",
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            datefmt="%d-%b-%y %H:%M:%S",
            level=(logging.CRITICAL - (self.verbosity * 10)),
        )

        # Create handlers
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.WARNING)

        # Create formatters and add it to handlers
        console_format = logging.Formatter("%(name)s - %(levelname)s - %(message)s")
        console_handler.setFormatter(console_format)

        file_format = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        # Add handlers to the logger
        logger.addHandler(console_handler)

        # Register services
        Services.register("datastore", Datastore(settings.datastore))
        Services.register("logger", logger)
        Services.register("output", Output())
        Services.register(
            "request_factory",
            SingleRequest(
                url=self.url,
                agent=self.user_agent,
                proxy=self.proxy,
                redirect=self.redirect,
                timeout=self.timeout,
            ),
        )

        self.bn.preamble(self.url)
        try:
            self.ma.fingerprints(
                self.fingerprint,
                self.url,
                self.cookie,
            )
        except KeyboardInterrupt:
            raise
        finally:
            self.bn.postscript()



def main(ip, port):
    for item in port:
        target = ip + item
        res = Sitadel(target).main()
        print(res)


if __name__ == "__main__":
    try:
        Sitadel('https://www.thinkphp.cn/').main()
    except KeyboardInterrupt:
        sys.exit(output.Output().error("Interruption by the user, Quitting..."))
