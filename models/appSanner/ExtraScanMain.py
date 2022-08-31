import json
import socket
import re
import eventlet
import time
import traceback
import eventlet
from wrapt_timeout_decorator import timeout
from func_timeout import func_set_timeout


#读取json文件
# 要用项目根的相对路径
with open('models/appSanner/nmap.json', encoding='utf-8') as jsonfile:
    # 读取json文件至代码中
    probeJson = json.load(jsonfile)
    # print(probeJson)
    # print(type(probeJson))

def ExtraScan(target):
    ip=target[0]
    port=target[1]
    ip_port = (ip,port)
    print(ip_port)

    # socket.AF_INET 表示指定使用 IPv4 协议
    # SOCK_STREAM 指定使用面向流的 TCP 协议
    tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_client_socket.connect(ip_port)
    #设定tcp接收限时
    # tcp_client_socket.setblocking(False)
    tcp_client_socket.settimeout(5)

    length=len(probeJson)
    for i in range(length):
        ports=probeJson[i]['ports']
        sslports=probeJson[i]['sslports']
        ports.extend(sslports)
        #如果该端口在某个probe的ports中，即发送该probe
        if str(port) in ports:

            print("探针名字："+probeJson[i]['probename'])

            send=probeJson[i]['probestring']

            # print(send.encode("utf-8")+b'\x00')
            # tcp_client_socket.sendall(send.encode("utf-8")+b'\x00')

            send = eval(repr(send).replace('\\\\', '\\'))
            # print(send)
            try:
                tcp_client_socket.sendall(send.encode("utf-8"))
            except:
                traceback.print_exc()
                print('发送出错')
                continue
            # tcp_client_socket.shutdown(1)

            print("发送信息:" + send)
            # print(probeJson[i]['ports'])  
            # tcp_client_socket.shutdown()

            #编码为str
            # feedback = tcp_client_socket.recv(1024).decode("raw_unicode_escape")  # 每次最多接收1k字节
            try:
                feedback = tcp_client_socket.recv(1024).decode("raw_unicode_escape")  # 每次最多接收1k字节
                # feedback = tcp_client_socket.recv(1024).decode("utf-8")  # 每次最多接收1k字节
                print('接收到数据:', feedback)
            except:
                print('超时,跳过该探针')
                continue
            
            # print('接收到数据:', type(feedback))

            print("正则表达式匹配中")
            for match in probeJson[i]["matches"]:

                pattern = match["pattern"]
                # print("正则匹配式：" + pattern)

                Identif = re.match(pattern, feedback)

                if Identif != None:
                    print("匹配表达式:"+Identif.string)
                    result = match["name"]
                    verinfo=str(match["versioninfo"])
                    print("识别结果为：" + result+result)
                    tcp_client_socket.close()  # 关闭连接

                    return result #成功识别
    tcp_client_socket.close()
    return 0 #识别失败

if __name__ == '__main__':
    target = ['10.21.145.59',443]
    # target = ['jwgl.bupt.edu.cn',80]
    # target = ['10.122.220.161',80]
    ExtraScan(target)

    # main(target)

