import re
from lib.modules.fingerprints import FingerprintPlugin


class Jquery(FingerprintPlugin):
    def process(self, headers, content):
        print(content)
        res1 = re.findall(r'jquery-([0-9\-.]+).js|jquery', content, re.I)
        res2 = re.findall(r'jquery/([0-9\-.]+)/', content, re.I)
        if res is not None:
            for item in res1:
                if item != "":
                    return "jquery" + item
            for item in res2:
                if item != "":
                    return "jquery" + item
            return "jquery"
