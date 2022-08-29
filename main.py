from models import hostScanner

def main():
    targets = input("Enter the ip range: ")
    targets = "192.168.1.2-192.168.2.2"
    info = hostScanner.main(targets)
    print(info)
    iplist = []


if __name__ == '__main__':
    main()