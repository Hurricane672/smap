# -*- coding =utf-8 -*-
# @time:2022/8/30

import re
import socket


# dic =  {
#         "protocol": "TCP",
#         "probename": "GetRequest",
#         "probestring": "\\x80\\0\\0\\x28\\x72\\xFE\\x1D\\x13\\0\\0\\0\\0\\0\\0\\0\\x02\\0\\x01\\x86\\xA0\\0\\x01\\x97\\x7C\\0\\0\\0\\0\\0\\0\\0\\0\\0\\0\\0\\0\\0\\0\\0\\0\\0\\0\\0\\0"}

# url = '127.0.0.1'
# port = 80

# # 创建TCP socket
# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# # 连接服务端
# sock.connect((url, port))
# # 创建请求消息头
# request_url = dic["probestring"]
# request_url="\\x61"
# print(repr(request_url)) # 原始的
# print(repr(request_url).replace('\\\\', '\\')) #删完之后的
# request_url = eval(repr(request_url).replace('\\\\', '\\'))

# print(type(request_url))
# print((request_url))
# print(request_url.encode())# 字节流形式的

pattern ="\\x09"
p = re.compile(pattern)
Identify = p.search("\x09")
print(Identify)

# if Identify != None:
# result["service"] = i["name"]
# p = re.compile(r'\d+\.(?:\d+\.)*\d+')