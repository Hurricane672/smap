import json
import socket
import re
def ExtraScan(target,result):

    # with open('models/appSanner/nmap.json', encoding='utf-8') as jsonfile:
    with open('./AppScanner/nmap.json', encoding='utf-8') as jsonfile:
    # 读取json文件至代码中
        probeJson = json.load(jsonfile)

    ip=target[0]
    port=target[1]
    ip_port = (ip,port)
    # print(ip_port)

    # socket.AF_INET 表示指定使用 IPv4 协议
    # SOCK_STREAM 指定使用面向流的 TCP 协议
    tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_client_socket.connect(ip_port)

    tcp_client_socket.settimeout(50)
    length=len(probeJson)

    for i in range(length):
        ports=probeJson[i]['ports']
        sslports=probeJson[i]['sslports']
        ports.extend(sslports)
        #如果该端口在某个probe的ports中，即发送该probe
        if str(port) in ports:
            # print("探针名字："+probeJson[i]['probename'])
            send=probeJson[i]['probestring']
            send = eval(repr(send).replace('\\\\', '\\'))

            try:
                tcp_client_socket.sendall(send.encode("utf-8"))
            except:
                # traceback.print_exc()
                # print("Scan Service Fail!")
                # print('发送出错')
                continue
            # tcp_client_socket.shutdown(1)

            # print("发送信息:" + send)

            try:
                feedback = tcp_client_socket.recv(1024).decode("raw_unicode_escape")  # 每次最多接收1k字节
                # print('接收到数据:', feedback)
            except:
                # print("Scan Service Fail!")
                # print('超时,跳过该探针')
                continue
            
            # print("正则表达式匹配中")
            for match in probeJson[i]["matches"]:

                pattern = match["pattern"]
                # print("正则匹配式：" + pattern)
                p = re.compile(pattern)
                # 匹配identify结果
                Identify = p.search(feedback)

                if Identify != None:
                    # print(Identify)
                    result["service"] = match["name"]
                    # print(result["service"])

                    #正则表达式编译
                    p = re.compile(r'\d+\.(?:\d+\.)*\d+')
                    #匹配版本号
                    Identify = p.search(Identify.group())
                    if(Identify!=None):
                        result["version"] = Identify.group()
                    else:
                        result["version"] = ''
                    # print(result["version"])

                    # print("识别结果为："+str(result))
                    tcp_client_socket.close()  # 关闭连接

                    return result #成功识别
    tcp_client_socket.close()
    return result #识别失败

