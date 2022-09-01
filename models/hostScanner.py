import ipaddress
from ping3 import ping
import subprocess
import re
import prettytable
import sys
import threading
import requests


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
    cmd = subprocess.check_output("arp -a {}".format(ip_addr))
    cmd = cmd.decode("gbk")
    mac = []
    if cmd:
        pattern = r"([a-f0-9]{2}-){5}[a-f0-9]{2}"
        mac = re.search(pattern, cmd)
        mac = mac.group()
    if len(mac) != 0:
        return mac
    else:
        return ""


def get_vendor(mac_addr):
    res = requests.get(url=r'https://mac.bmcx.com/' + mac_addr + '__mac/')
    pattern = r"<td bgcolor=\"#FFFFFF\" style=\"font-size:16px;\">(.*)</td>"
    vendor = re.findall(pattern, res.text)
    if len(vendor) != 0:
        return vendor[0]
    else:
        return ""

class Scan(threading.Thread):
    def __init__(self, ip_addr, host_info: list):
        self.ip = ip_addr
        self.data = host_info
        threading.Thread.__init__(self)

    def run(self):
        delay = ping(dest_addr=self.ip, timeout=5)
        if delay:
            # print("发现在线主机" + self.ip)
            delay = str(int(delay * 1000)) + "ms"
            mac = get_mac(self.ip)
            print(mac)
            vendor = ""
            try:
                hostname = get_hostname(self.ip)
            except:
                hostname = "unknown"
            if len(mac) != 0:
                vendor = get_vendor(mac)
            self.data[self.ip] = ([hostname, mac, vendor, delay])
            #self.data[self.ip].append([hostname, mac, vendor, delay])
        else:
            pass


def check_thread_alive(thread):
    for td in thread:
        if td.is_alive():
            return True


def main(start_ip, end_ip):
    ip_addrs = get_ip_range(start_ip, end_ip)
    info = {}
    thread = []
    for ip_addr in ip_addrs:
        td = Scan(ip_addr=ip_addr, host_info=info)
        td.start()
        thread.append(td)
    while 1:
        if not check_thread_alive(thread):
            break
    return info


if __name__ == "__main__":
    start = "10.122.220.0"
    end = "10.122.220.255"
    print(main(start,end))
    #lhl_2507 9.1 finish testing
    #{'10.122.220.34': ['O6FE68W37RBANVY', '80-00-0B-D9-BF-F2', 'Intel Corporate（英特尔）', '15ms'], '10.122.220.2': ['LAPTOP-K6QN67KN', 'B0-60-88-EE-DD-56', 'Intel Corporate（英特尔）', '18ms'], '10.122.220.161': ['DESKTOP-SUNTM9A', '', '', '11ms'], '10.122.220.17': ['unknown', '', '', '24ms'], '10.122.220.12': ['unknown', '', '', '20ms'], '10.122.220.13': ['unknown', '', '', '22ms'], '10.122.220.3': ['unknown', '', '', '209ms'], '10.122.220.10': ['unknown', '', '', '129ms'], '10.122.220.49': ['unknown', '', '', '200ms'], '10.122.220.27': ['unknown', '', '', '694ms'], '10.122.220.8': ['unknown', '', '', '32ms'], '10.122.220.28': ['unknown', '', '', '56ms']}


    # ipaddrs = get_ip_range(start, end)
    # pt = prettytable.PrettyTable(field_names=("IP", "机器名", "MAC地址", "生产厂商", "延时"))
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
