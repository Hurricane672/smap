from models import hostScanner
from models import portScanner
from models import topoDrawer
from models import vulFinder
from models import appScanner
import threading

def output(text):
    print(text)

def main():
    # targets = input("Enter the ip range: ")
    targets = "192.168.1.2-192.168.2.2"
    info = hostScanner.main(targets)
    output(info)
    ipPortDict = {}
    for ip, sysInfo in info.items():
        ports = portScanner.main(ip)
        ipPortDict[ip] = [sysInfo]+ports
    print(ipPortDict)


if __name__ == '__main__':
    main()
