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
    send = probe["probestring"]
    # send的数据需为bytes类型
    tcp_client_socket.send(send.encode("utf-8"))
    # 每次最多接收1k字节,转化为str
    feedback = tcp_client_socket.recv(1024).decode('UTF-8', 'ignore') # 若发完包后没有返回数据，会停留等待很长时间

    # print('接收到数据:', feedback)

    for i in probe["matches"]:
        pattern = i["pattern"]
        # print("正则匹配式：" + pattern)
        Identify = re.match(pattern, feedback)

        if Identify != None:
            result["service"] = i["name"]
            result["version"] = Identify.string.strip()
            # print("识别结果为：" + service + " " + Identify.string)
            tcp_client_socket.close()  # 关闭连接
            return result
    return 0
