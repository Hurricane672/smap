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
    start = "10.122.210.0"
    end = "10.122.210.255"
    info = hostScanner.main(start, end)
    output(info)
    ipPortDict = {}
    for item in info:
        ip = item.key
        ports = portScanner.main(ip)
        ipPortDict[ip] = [sysInfo] + ports
    print(ipPortDict)


if __name__ == '__main__':
    main()
