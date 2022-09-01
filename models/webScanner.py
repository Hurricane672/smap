import sys

sys.path.append('webScan')
sys.path.append('models/webScan')
from models.webScan import Scanner


def main(ip, ports):
    web_list = []
    for port in ports:
        target = "https://" + ip + ":" + str(port)
        dic = dict()
        dic['ip'] = ip
        dic['port'] = port
        res = Scanner.Scan(target).main()
        if res is None:
            continue
        for item in res:
            if item[1] is not None:
                dic[item[0]] = item[1]
        web_list.append(dic)
    return web_list


if __name__ == 'main':
    res = main("10.122.210.19", [25, 110, 135, 139, 443, 445, 902, 912])
    print(res)