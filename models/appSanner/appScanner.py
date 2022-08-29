import socket
from unittest import result
import re
from xml.dom.minidom import Identified

def main(target):

    result = ["apache 2.5","vue 1.0"]
    return result

def appScan(target):
    # ip=target[0]
    # port=target[1]
    ip_port=(target[0],target[1])
    print(ip_port)
    

#以空包(第一步)测试，
    probe=[
        {
            "protocol": "TCP",
            "probename": "NULL",
            "probestring": "",
            "ports": [],
            "sslports": [],
            "totalwaitms": "3000",
            "tcpwrappedms": "",
            "rarity": "",
            "fallback": "",
            "matches": [
                {
                    "pattern": "^.\\0\\0\\0\\xff..Host .* is not allowed to connect to this MySQL server$",
                    "name": "mysql",
                    "pattern_flag": "s",
                    "versioninfo": {
                        "cpename": "a:mysql:mysql",
                        "devicetype": "",
                        "hostname": "",
                        "info": "unauthorized",
                        "operatingsystem": "",
                        "vendorproductname": "MySQL",
                        "version": ""
                     }
                }
            ]
        }
    ]
                

    #socket.AF_INET 表示指定使用 IPv4 协议
    #SOCK_STREAM 指定使用面向流的 TCP 协议
    tcp_client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
    tcp_client_socket.connect(ip_port)

    # send=input("请输⼊需要发送数据：")
    
    send=probe[0]["probestring"]
    print("发送信息:"+send)
    tcp_client_socket.send(send.encode("utf-8"))#将str类型转为bytes类型

    feedback=tcp_client_socket.recv(1024) #每次最多接收1k字节

    print('接收到数据:', feedback)
    print('接收到数据:', type(feedback))
    # print('接收到数据:', feedback.decode('utf-8'))
    # print('接收到数据:', str(feedback,encoding='utf-8'))


    pattern=probe[0]["matches"][0]["pattern"]
    print("正则匹配式："+pattern)
    #由于现在我没办法把收到的bytes类型转化为str，所以这一步我没办法看出这个正则表达式能不能很好的使用
    Identif=re.match(pattern,"Host 'LAPTOP-INEUBO8I' is not allowed to connect to this MySQL server")
    print(Identif)

    result=probe[0]["matches"][0]["name"]
    print("识别结果为："+result)
    tcp_client_socket.close() #关闭连接
    return result

if __name__ == '__main__':
    target = ['10.122.251.228',3306]
    appScan(target)

    main(target)

    