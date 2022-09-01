from models import hostScanner
from models import portScanner
from models import routeGetter
from models import appScanner
from models import topoDrawer
from models import vulFinder
from models import webScanner
import multiprocessing


def topo(ips):
    topoDrawer.main(ips)


def main():
    # start_ip = input("Enter the start_ip: ")
    # end_ip = input("Enter the end_ip: ")
    start_ip = "10.122.210.19"
    end_ip = "10.122.210.19"
    info = hostScanner.main(start_ip, end_ip)
    print(info)


    # ip_list = []
    # for item in info.keys():
    #     ip_list.append(item)
    # res = routeGetter.main(['10.20.0.5', '10.20.0.6', '10.20.0.7', '10.20.0.8'])
    # print(res)

    d0 = {}
    for ip, sys in info.items():
        ports = portScanner.main(ip)
        d0[ip] = [sys] + [ports]
    print(d0)

    for ip, info in d0.items():
        ip_list = info[1]
        res = webScanner.main(ip, ip_list, 1)
        print(res)

    # d1 = {}
    # for ip, ports in d0.items():
    #     l0 = [ports[0]]
    #     for i in ports[1:]:
    #         l1 = []
    #         service = appScanner.main([ip, i])
    #         for j in service:
    #             vul = vulFinder.main(j)
    #             l1.append({j: vul})
    #         l0.append({str(i): l1})
    #     d1[ip] = l0
    # print(d1)


if __name__ == '__main__':
    main()
