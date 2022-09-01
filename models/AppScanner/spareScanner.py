import nmap

def spareScan(target,result):
    ip=target[0]
    port=target[1]
    
    nm = nmap.PortScanner()
    try:
        nm.scan(ip,str(port),timeout=8)
    except:
        print('Timeout! Start EasyScan')
        nm.scan(ip,str(port),arguments='')
    # nm.command_line()#本次扫描的命令
    # nm.all_hosts()#扫描的所有主机
    # nm.scaninfo()#扫描的信息列出一个结构
    # nm.csv()#返回值用csv输出
    # print(nm.command_line())
    # print(nm.csv())
    info=nm[ip].tcp(port)
    # 端口全部信息
    # print(info)

    # product=info["product"]
    # version=info["version"]
    # cpe=info["cpe"]

    result["service"]=info["name"]

    if info["version"] !='':
        result["version"]=info["version"]
        return result
    if info["product"] !='':
        result["version"]=info["product"]
        return result
    if info["cpe"] !='':
        result["version"]=info["cpe"]
        return result

    return result

if __name__ == '__main__':
    target=['10.122.214.150',25]
    result = {"service": "", "version": ""}
    # print(spareScan(target,result))