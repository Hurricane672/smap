import sys
sys.path.append('webScan')
sys.path.append('models/webScan')
from models.webScan import Scanner



def main(ip, ports):
    web_list = []
    for port in ports:
        target = ip + port
        dic = dict()
        dic['ip'] = ip
        dic['port'] = port
        res = Scanner.Scan(target).main()
        for item in res:
            if item[1] is not None:
                dic[item[0]] = item[1]
        web_list.append(dic)
    return web_list
