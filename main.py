from models import hostScanner
from models import portScanner
from models import tracert
from models import appScanner
from models import topoDrawer
from models import vulFinder
import multiprocessing


def topo(ips):
    topoDrawer.main(ips)


def main():
    # targets = input("Enter the ip range: ")
    targets = "192.168.1.2-192.168.2.2"
    info = hostScanner.main(targets)
    ips = info.keys()
    print(info)
    # p = multiprocessing.Process(targets=topo,args=(ips,))
    # p.daemon = True
    # p.start()
    d0 = {}
    for ip, sys in info.items():
        ports = portScanner.main(ip)
        d0[ip] = [sys] + ports
    print(d0)
    d1 = {}
    for ip, ports in d0.items():
        l0 = [ports[0]]
        for i in ports[1:]:
            l1 = []
            service = appScanner.main([ip, i])
            for j in service:
                vul = vulFinder.main(j)
                l1.append({j: vul})
            l0.append({str(i): l1})
        d1[ip] = l0
    print(d1)


if __name__ == '__main__':
    main()
