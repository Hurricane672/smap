from lib.config import settings

from lib.modules.fingerprints import Fingerprints


def fingerprints(modules, url, cookie):
    plugins = ['cms', 'system', 'framework', 'frontend', 'header', 'lang', 'server', 'waf'] #['cms', 'system', 'framework', 'frontend', 'header', 'language', 'server', 'waf']
    if modules is not None:
        plugins = modules
    res = Fingerprints(
        url=url,
        cookie=cookie
    ).run(plugins)
    return res

