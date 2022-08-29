from models import hostScanner
from models import portScanner


def main():
    # targets = input("Enter the ip range: ")
    targets = "192.168.1.2-192.168.2.2"
    info = hostScanner.main(targets)
    print(info)
    d = {}
    for ip, sys in info.items():
        ports = portScanner.main(ip)
        d[ip] = [sys]+ports
    print(d)


if __name__ == '__main__':
    main()
