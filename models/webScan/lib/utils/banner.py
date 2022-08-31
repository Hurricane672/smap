import time

from colorama import Fore, Style

from lib import __version__ as version

class Banner:
    r = Fore.RED
    y = Fore.YELLOW
    ny = Fore.YELLOW
    nw = Fore.WHITE
    g = Fore.GREEN
    e = Style.RESET_ALL

    def banner(self):
        pass

    @classmethod
    def preamble(cls, url):
        pass

    @classmethod
    def postscript(cls):
        pass

    def version(self):
        return self.g + "~/#" + self.e + " webScan (" + version + ")\n"
