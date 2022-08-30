import ipaddress
from ping3 import ping
import encodings.idna
import subprocess
import re
import prettytable
import sys
import threading


def get_ip_range(start_ip, end_ip):
    start_ip = ipaddress.ip_address(start_ip)
    end_ip = ipaddress.ip_address(end_ip)
    ip_range = []
    ip_addr = start_ip
    while ip_addr <= end_ip:
        ip_range.append(str(ip_addr))
        ip_addr += 1
    return ip_range


def get_hostname(ip_addr):
    cmd = subprocess.check_output("ping -a -n 1 {}".format(ip_addr))
    cmd = cmd.decode("gbk")
    if cmd:
        lines = cmd.split("\n")
        pattern = r".*Ping (.*) \["
        names = re.findall(pattern, lines[1])
        return names[0]


def get_mac(ip_addr):
    cmd = subprocess.check_output("nbtstat -A {}".format(ip_addr))
    cmd = cmd.decode("gbk")
    mac = []
    if cmd:
        pattern = "MAC 地址 = (.*)\r"
        mac = re.findall(pattern, cmd)
    return mac


class Scan(threading.Thread):
    def __init__(self, ip_addr, host_info: list):
        self.ip = ip_addr
        self.data = host_info
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
            # print("{}, 在线, 名称: {}|".format(self.ip_addr, hostname))
            self.data.append({self.ip: [hostname, mac, delay]})
        else:
            # print("{}, 不在线|".format(self.ip_addr))
            pass


def check_thread_alive():
    for th in thread:
        if th.is_alive():
            return True


def main(start_ip, end_ip):
    ip_addrs = get_ip_range(start_ip, end_ip)
    info = []
    thread = []
    for ip_addr in ip_addrs:
        _thread = Scan(ip_addr=ip_addr, host_info=info)
        _thread.start()
        thread.append(_thread)
    return info


if __name__ == "__main__":
    pass
    # ipaddrs = get_ip_range(start, end)
    # pt = prettytable.PrettyTable(field_names=("IP", "机器名", "MAC地址", "延时"))
    # data = []
    # thread = []
    # for ip in ipaddrs:
    #     th = Scan(ip_addr=ip, host_info=data)
    #     th.start()
    #     thread.append(th)
    # while 1:
    #     if not check_thread_alive():
    #         break
    # for row in data:
    #     pt.add_row(row)
    #     print(row)
    # print(pt)
