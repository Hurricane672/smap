# -*- coding =utf-8 -*-
# @time:2022/8/30
import json
import socket
import re

def TCP_Scan(target):

    result = {"service": "", "version": ""}
    with open('./nmap.json', encoding='utf-8') as jsonfile:
        probeJson = json.load(jsonfile)
    ip_port = (target[0], target[1])
    # print(ip_port)

    # json文件中第一个为空探针
    probe = probeJson[0]

    tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_client_socket.connect(ip_port)
    # 设置延迟
    tcp_client_socket.settimeout(3)
    send = probe["probestring"]

    feedback = tcp_client_socket.recv(1024).decode('utf-8', 'ignore') # 若发完包后没有返回数据，会停留等待很长时间

    for i in probe["matches"]:

        pattern = i["pattern"]
        p = re.compile(pattern)
        Identify = p.search(feedback)
        # print(Identify)
        if Identify != None:
            result["service"] = i["name"]
            p = re.compile(r'\d+\.(?:\d+\.)*\d+')
            Identify = p.search(Identify.group())

            result["version"] = Identify.group()
            # print("识别结果为：" + service + " " + Identify.string)
            tcp_client_socket.close()  # 关闭连接
            return result
    return 0
