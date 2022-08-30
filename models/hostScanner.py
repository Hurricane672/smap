import ipaddress
from ping3 import ping
import encodings.idna
import subprocess
import re
import prettytable
import sys
import threading


def get_ip_range(start_ip, end_ip):
    start = ipaddress.ip_address(start_ip)
    end = ipaddress.ip_address(end_ip)
    ip_range = []
    ipAddr = start
    while ipAddr <= end:
        ip_range.append(str(ipAddr))
        ipAddr += 1
    return ip_range


def get_hostname(ip):
    cmd = subprocess.check_output("ping -a -n 1 {}".format(ip))
    cmd = cmd.decode("gbk")
    if cmd:
        lines = cmd.split("\n")
        pattern = r".*Ping (.*) \["
        names = re.findall(pattern, lines[1])
        return names[0]


def get_mac(ip):
    cmd = subprocess.check_output("nbtstat -A {}".format(ip))
    cmd = cmd.decode("gbk")
    mac = []
    if cmd:
        pattern = "MAC 地址 = (.*)\r"
        mac = re.findall(pattern, cmd)
    return mac


class Scan(threading.Thread):
    def __init__(self, ip, data: list):
        self.ip = ip
        self.data = data
        threading.Thread.__init__(self)

    def run(self):
        delay = ping(dest_addr=self.ip, timeout=1)
        if delay:
            delay = str(int(delay * 1000)) + "ms"
            mac = get_mac(self.ip)
            try:
                hostname = get_hostname(self.ip)
            except:
                hostname = "unknown"
            # print("{}, 在线, 名称: {}|".format(self.ip, hostname))
            self.data.append((self.ip, hostname, mac, delay))
        else:
            # print("{}, 不在线|".format(self.ip))
            pass


def check_thread_alive():
    for th in thread:
        if th.is_alive():
            return True


def main():
    ipaddrs = get_ip_range(start, end)
    data = []
    thread = []
    for ip in ipaddrs:
        _thread = Scan(ip=ip, data=data)
        _threadth.start()
        thread.append(_thread)
    while 1:
        if not check_thread_alive():
            break
    return data


if __name__ == "__main__":
    start = "10.122.210.0"
    end = "10.122.210.255"
    # start=sys.argv[0]
    # end=sys.argv[1]
    ipaddrs = get_ip_range(start, end)
    pt = prettytable.PrettyTable(field_names=("IP", "机器名", "MAC地址", "延时"))
    data = []
    thread = []
    for ip in ipaddrs:
        th = Scan(ip=ip, data=data)
        th.start()
        thread.append(th)
    while 1:
        if not check_thread_alive():
            break
    for row in data:
        pt.add_row(row)
        print(row)
    print(pt)
