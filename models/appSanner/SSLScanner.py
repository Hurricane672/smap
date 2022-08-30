import json
import socket
import re
import ssl
import eventlet

def SSLScan(target):
    # ip_addr=target[0]
    # port=target[1]
    ip_port=(target[0],target[1])
    print(ip_port)
    with open('models/appSanner/ssl.json', encoding='utf-8') as jsonfile:
    # 读取json文件至代码中
        probeJson = json.load(jsonfile)
    #socket.AF_INET 表示指定使用 IPv4 协议
    #SOCK_STREAM 指定使用面向流的 TCP 协议
    tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ssltcp_client_socket = ssl.wrap_socket(tcp_client_socket, cert_reqs=ssl.CERT_NONE)

    ssltcp_client_socket.connect(ip_port)

    length=len(probeJson)
    for i in range(length):
        if '443' in probeJson[i]['ports']:
            #如果该端口在某个probe的ports中，即发送该probe
            print("探针名字："+probeJson[i]['probename'])

            send=probeJson[i]['probestring']
            ssltcp_client_socket.send(send.encode("utf-8"))

            print("发送信息:" + send)
            # print(probeJson[i]['ports'])  

            #编码为str
            eventlet.monkey_patch()#必须加这条代码
            with eventlet.Timeout(3,False):#设置超时时间为3s
                feedback = ssltcp_client_socket.recv(1024).decode("utf-8")  # 每次最多接收1k字节
                print('接收到数据:', feedback)
            print('超时,跳过该探针')
            # print('接收到数据:', type(feedback))

            for match in probeJson[i]["matches"]:

                pattern = match["pattern"]
                print("正则匹配式：" + pattern)

                Identif = re.match(pattern, feedback)

                if Identif != None:
                    print("匹配表达式:"+Identif)
                    result = match["name"]
                    print("识别结果为：" + result + " " + Identif.string)
                    tcp_client_socket.close()  # 关闭连接

                    return 1 #成功识别
    tcp_client_socket.close()
    print('识别失败')
    return 0 #识别失败


if __name__ == '__main__':
    target = ['10.3.9.161',443]
    SSLScan(target)

    # main(target)

    