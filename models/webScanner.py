import sys

sys.path.append('webScan')
sys.path.append('models/webScan')
from models.webScan import Scanner


def main(ip, ports, is_IP):
    web_list = []
    for port in ports:
        if is_IP:
            if port == 443:
                target = "https://" + ip + ":" + str(port)
            else:
                target = "http://" + ip + ":" + str(port)
        else:
            target = ip
        dic = dict()
        dic['port'] = port
        dic['cdn'] = ""
        dic["cms"] = ""
        dic["framework"] = ""
        dic["frontend"] = ""
        dic["lang"] = ""
        dic["server"] = ""
        dic["system"] = ""
        dic["waf"] = ""
        res = Scanner.Scan(target).main()
        if res is None:
            continue
        for item in res:
            if item[1] is not None:
                dic[item[0]] = item[1]
        web_list.append(dic)
    print(web_list)
    return web_list


