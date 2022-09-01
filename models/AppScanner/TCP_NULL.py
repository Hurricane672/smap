# -*- coding =utf-8 -*-
# @time:2022/8/30
import json
import socket
import re

def TCP_Scan(target,result):

    with open('models/AppScanner/nmap.json', encoding='utf-8') as jsonfile:
    # with open('/models/AppScanner/nmap.json', encoding='utf-8') as jsonfile:
    # with open('AppScanner/nmap.json', encoding='utf-8') as jsonfile:
        probeJson = json.load(jsonfile)

    ip_port = (target[0], target[1])
    probe = probeJson[0]
    tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        tcp_client_socket.connect(ip_port)
        tcp_client_socket.settimeout(1)
        feedback = tcp_client_socket.recv(1024).decode('utf-8', 'ignore') # 若发完包后没有返回数据，会停留等待很长时间
    except:
        return result

    for i in probe["matches"]:
        pattern = i["pattern"]
        p = re.compile(pattern)
        Identify = p.search(feedback)
        # print(Identify)
        if Identify != None:
            result["service"] = i["name"]
            p = re.compile(r'\d+\.(?:\d+\.)*\d+')
            Identify = p.search(Identify.group())
            if (Identify != None):
                result["version"] = Identify.group()
            else:
                result["version"] = ''
            # print("识别结果为：" + service + " " + Identify.string)
            tcp_client_socket.close()  # 关闭连接
            return result
    return result
