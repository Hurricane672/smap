from models import hostScanner
from models import portScanner
from models import topoDrawer
from models import vulFinder
from models import appScanner
import threading


def output(text):
    print(text)


def main():
    # start_ip = input("Enter the start_ip:")
    # end_ip = input("Enter the end_ip:")
    start = "10.122.210.1"
    end = "10.122.210.20"
    info = hostScanner.main(start, end)
    output(info)
    ipPortDict = {}
    ip_list = []
    for item in info:
        ip_list.append(list(item.keys())[0])
    for ip in ip_list:
        ports = portScanner.main(ip)
        ipPortDict[ip] = ports
    print(ipPortDict)


if __name__ == '__main__':
    main()
