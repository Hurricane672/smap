def main(targets):
    result = {"192.168.1.123":"Linux 4.4","192.168.2.2":"Microsoft Windows Server 2008"}
    return result


if __name__ == '__main__':
    targets = "192.168.1.2-192.168.2.2"
    main(targets)