from models import tracert


def main(targets):
    results = tracert.main(targets)
    results = [['192.168.1.2', '192.168.1.1'], ['192.168.1.2'], ['192.168.1.2', '192.168.1.3']]
    # 输出文件到/images文件夹
    return 0


if __name__ == '__main__':
    targets = ["10.122.251.228", "10.122.210.19"]
    main(targets)
