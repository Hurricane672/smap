# -*- coding =utf-8 -*-
# @time:2022/8/29
# import socket
# while True:
#     s = socket.socket()
#     s.settimeout(10)
#
#     port = input("请输入端口号：")
#
#     try:
#         s.connect(('192.168.223.128',int(port)))
#         print(s.recv(1024))
#         s.close()
#     except Exception as e:
#         print(">>>扫描错误：",e)

import socket
from unittest import result
import re
from xml.dom.minidom import Identified


# def main(target):
#     result = ["apache 2.5", "vue 1.0"]
#     return result


def appScan(target):
    # ip=target[0]
    # port=target[1]
    ip_port = (target[0], target[1])
    print(ip_port)




    # 以空包(第一步)测试，
    probe = [
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
                    "pattern": "^SSH-([\\d.]+)-OpenSSH_([\\w._-]+) Debian-(\\S*maemo\\S*)\\r?\\n",
                    "name": "ssh",
                    "pattern_flag": "",
                    "versioninfo": {
                        "cpename": "o:linux:linux_kernel",
                        "devicetype": "",
                        "hostname": "",
                        "info": "Nokia Maemo tablet; protocol $1",
                        "operatingsystem": "Linux",
                        "vendorproductname": "OpenSSH",
                        "version": "$2 Debian $3"
                    }
                },
                {
                    "pattern": "^SSH-([\\d.]+)-OpenSSH_([\\w._-]+)[ -]{1,2}Debian[ -_](.*ubuntu.*)\\r\\n",
                    "name": "ssh",
                    "pattern_flag": "",
                    "versioninfo": {
                        "cpename": "o:linux:linux_kernel",
                        "devicetype": "",
                        "hostname": "",
                        "info": "Ubuntu Linux; protocol $1",
                        "operatingsystem": "Linux",
                        "vendorproductname": "OpenSSH",
                        "version": "$2 Debian $3"
                    }
                },
                {
                    "pattern": "^SSH-([\\d.]+)-OpenSSH_([\\w._-]+)[ -]{1,2}Ubuntu[ -_]([^\\r\\n]+)\\r?\\n",
                    "name": "ssh",
                    "pattern_flag": "",
                    "versioninfo": {
                        "cpename": "o:linux:linux_kernel",
                        "devicetype": "",
                        "hostname": "",
                        "info": "Ubuntu Linux; protocol $1",
                        "operatingsystem": "Linux",
                        "vendorproductname": "OpenSSH",
                        "version": "$2 Ubuntu $3"
                    }
                },
                {
                    "pattern": "^SSH-([\\d.]+)-OpenSSH_([\\w._-]+)[ -]{1,2}Debian[ -_]([^\\r\\n]+)\\r?\\n",
                    "name": "ssh",
                    "pattern_flag": "",
                    "versioninfo": {
                        "cpename": "o:linux:linux_kernel",
                        "devicetype": "",
                        "hostname": "",
                        "info": "protocol $1",
                        "operatingsystem": "Linux",
                        "vendorproductname": "OpenSSH",
                        "version": "$2 Debian $3"
                    }
                },
                {
                    "pattern": "^SSH-([\\d.]+)-OpenSSH_[\\w.]+-FC-([\\w.-]+)\\.fc(\\d+)\\r\\n",
                    "name": "ssh",
                    "pattern_flag": "",
                    "versioninfo": {
                        "cpename": "o:fedoraproject:fedora_core:$3",
                        "devicetype": "",
                        "hostname": "",
                        "info": "Fedora Core $3; protocol $1",
                        "operatingsystem": "Linux",
                        "vendorproductname": "OpenSSH",
                        "version": "$2 Fedora"
                    }
                },
                {
                    "pattern": "^SSH-([\\d.]+)-OpenSSH_([\\w._-]+) FreeBSD-([\\d]+)\\r?\\n",
                    "name": "ssh",
                    "pattern_flag": "",
                    "versioninfo": {
                        "cpename": "o:freebsd:freebsd",
                        "devicetype": "",
                        "hostname": "",
                        "info": "FreeBSD $3; protocol $1",
                        "operatingsystem": "FreeBSD",
                        "vendorproductname": "OpenSSH",
                        "version": "$2"
                    }
                },
                {
                    "pattern": "^SSH-([\\d.]+)-OpenSSH_([\\w._-]+) FreeBSD localisations (\\d+)\\r?\\n",
                    "name": "ssh",
                    "pattern_flag": "",
                    "versioninfo": {
                        "cpename": "o:freebsd:freebsd",
                        "devicetype": "",
                        "hostname": "",
                        "info": "FreeBSD $3; protocol $1",
                        "operatingsystem": "FreeBSD",
                        "vendorproductname": "OpenSSH",
                        "version": "$2"
                    }
                },
                {
                    "pattern": "^SSH-([\\d.]+)-OpenSSH_([\\w._-]+) FreeBSD-openssh-portable-(?:base-|amd64-)?[\\w.,]+\\r?\\n",
                    "name": "ssh",
                    "pattern_flag": "",
                    "versioninfo": {
                        "cpename": "o:freebsd:freebsd",
                        "devicetype": "",
                        "hostname": "",
                        "info": "protocol $1",
                        "operatingsystem": "FreeBSD",
                        "vendorproductname": "OpenSSH",
                        "version": "$2"
                    }
                },
                {
                    "pattern": "^SSH-([\\d.]+)-OpenSSH_([\\w._-]+) FreeBSD-openssh-portable-overwrite-base",
                    "name": "ssh",
                    "pattern_flag": "",
                    "versioninfo": {
                        "cpename": "o:freebsd:freebsd",
                        "devicetype": "",
                        "hostname": "",
                        "info": "protocol $1; overwrite base SSH",
                        "operatingsystem": "FreeBSD",
                        "vendorproductname": "OpenSSH",
                        "version": "$2"
                    }
                },
                {
                    "pattern": "^SSH-([\\d.]+)-OpenSSH_([\\w._-]+) FreeBSD-openssh-gssapi-",
                    "name": "ssh",
                    "pattern_flag": "",
                    "versioninfo": {
                        "cpename": "o:freebsd:freebsd",
                        "devicetype": "",
                        "hostname": "",
                        "info": "gssapi; protocol $1",
                        "operatingsystem": "FreeBSD",
                        "vendorproductname": "OpenSSH",
                        "version": "$2"
                    }
                },
                {
                    "pattern": "^SSH-([\\d.]+)-OpenSSH_([\\w._-]+) FreeBSD\\n",
                    "name": "ssh",
                    "pattern_flag": "",
                    "versioninfo": {
                        "cpename": "o:freebsd:freebsd",
                        "devicetype": "",
                        "hostname": "",
                        "info": "protocol $1",
                        "operatingsystem": "FreeBSD",
                        "vendorproductname": "OpenSSH",
                        "version": "$2"
                    }
                },
                {
                    "pattern": "^SSH-([\\d.]+)-OpenSSH_([\\w._-]+) miniBSD-([\\d]+)\\r?\\n",
                    "name": "ssh",
                    "pattern_flag": "",
                    "versioninfo": {
                        "cpename": "a:openbsd:openssh:$2",
                        "devicetype": "",
                        "hostname": "",
                        "info": "MiniBSD $3; protocol $1",
                        "operatingsystem": "MiniBSD",
                        "vendorproductname": "OpenSSH",
                        "version": "$2"
                    }
                },
                {
                    "pattern": "^SSH-([\\d.]+)-OpenSSH_([\\w._-]+) NetBSD_Secure_Shell-([\\w._+-]+)\\r?\\n",
                    "name": "ssh",
                    "pattern_flag": "",
                    "versioninfo": {
                        "cpename": "o:netbsd:netbsd",
                        "devicetype": "",
                        "hostname": "",
                        "info": "NetBSD $3; protocol $1",
                        "operatingsystem": "NetBSD",
                        "vendorproductname": "OpenSSH",
                        "version": "$2"
                    }
                },
                {
                    "pattern": "^SSH-([\\d.]+)-OpenSSH_([\\w._-]+)_Mikrotik_v([\\d.]+)\\r?\\n",
                    "name": "ssh",
                    "pattern_flag": "",
                    "versioninfo": {
                        "cpename": "a:openbsd:openssh:$2",
                        "devicetype": "router",
                        "hostname": "",
                        "info": "protocol $1",
                        "operatingsystem": "",
                        "vendorproductname": "OpenSSH",
                        "version": "$2 mikrotik $3"
                    }
                },
                {
                    "pattern": "^SSH-([\\d.]+)-OpenSSH_([\\w._-]+) in RemotelyAnywhere ([\\d.]+)\\r?\\n",
                    "name": "ssh",
                    "pattern_flag": "",
                    "versioninfo": {
                        "cpename": "o:microsoft:windows",
                        "devicetype": "",
                        "hostname": "",
                        "info": "RemotelyAnywhere $3; protocol $1",
                        "operatingsystem": "Windows",
                        "vendorproductname": "OpenSSH",
                        "version": "$2"
                    }
                },
                {
                    "pattern": "^SSH-([\\d.]+)-OpenSSH_([\\w._-]+)\\+CAN-2004-0175\\r?\\n",
                    "name": "ssh",
                    "pattern_flag": "",
                    "versioninfo": {
                        "cpename": "a:openbsd:openssh:$2",
                        "devicetype": "",
                        "hostname": "",
                        "info": "protocol $1",
                        "operatingsystem": "",
                        "vendorproductname": "OpenSSH",
                        "version": "$2+CAN-2004-0175"
                    }
                },
                {
                    "pattern": "^SSH-([\\d.]+)-OpenSSH_([\\w._-]+) NCSA_GSSAPI_20040818 KRB5\\r?\\n",
                    "name": "ssh",
                    "pattern_flag": "",
                    "versioninfo": {
                        "cpename": "a:openbsd:openssh:$2",
                        "devicetype": "",
                        "hostname": "",
                        "info": "protocol $1",
                        "operatingsystem": "",
                        "vendorproductname": "OpenSSH",
                        "version": "$2 NCSA_GSSAPI_20040818 KRB5"
                    }
                },
                {
                    "pattern": "^SSH-([\\d.]+)-OpenSSH_([\\w._-]+)[-_]hpn(\\w+) *(?:\\\"\\\")?\\r?\\n",
                    "name": "ssh",
                    "pattern_flag": "",
                    "versioninfo": {
                        "cpename": "a:openbsd:openssh:$2",
                        "devicetype": "",
                        "hostname": "",
                        "info": "protocol $1; HPN-SSH patch $3",
                        "operatingsystem": "",
                        "vendorproductname": "OpenSSH",
                        "version": "$2"
                    }
                },
                {
                    "pattern": "^SSH-([\\d.]+)-OpenSSH_([\\w._-]+\\+sftpfilecontrol-v[\\d.]+-hpn\\w+)\\r?\\n",
                    "name": "ssh",
                    "pattern_flag": "",
                    "versioninfo": {
                        "cpename": "a:openbsd:openssh:$2",
                        "devicetype": "",
                        "hostname": "",
                        "info": "protocol $1",
                        "operatingsystem": "",
                        "vendorproductname": "OpenSSH",
                        "version": "$2"
                    }
                },
                {
                    "pattern": "^SSH-([\\d.]+)-OpenSSH_([\\w._-]+-hpn) NCSA_GSSAPI_\\d+ KRB5\\r?\\n",
                    "name": "ssh",
                    "pattern_flag": "",
                    "versioninfo": {
                        "cpename": "a:openbsd:openssh:$2",
                        "devicetype": "",
                        "hostname": "",
                        "info": "protocol $1; kerberos support",
                        "operatingsystem": "",
                        "vendorproductname": "OpenSSH",
                        "version": "$2"
                    }
                },
                {
                    "pattern": "^SSH-([\\d.]+)-OpenSSH_3\\.4\\+p1\\+gssapi\\+OpenSSH_3\\.7\\.1buf_fix\\+2006100301\\r?\\n",
                    "name": "ssh",
                    "pattern_flag": "",
                    "versioninfo": {
                        "cpename": "a:openbsd:openssh:3.4p1",
                        "devicetype": "",
                        "hostname": "",
                        "info": "protocol $1",
                        "operatingsystem": "",
                        "vendorproductname": "OpenSSH",
                        "version": "3.4p1 with CMU Andrew patches"
                    }
                },
                {
                    "pattern": "^SSH-([\\d.]+)-OpenSSH_([\\w._-]+\\.RL)\\r?\\n",
                    "name": "ssh",
                    "pattern_flag": "",
                    "versioninfo": {
                        "cpename": "a:openbsd:openssh:$2",
                        "devicetype": "switch",
                        "hostname": "",
                        "info": "protocol $1",
                        "operatingsystem": "",
                        "vendorproductname": "OpenSSH",
                        "version": "$2 Allied Telesis"
                    }
                },
                {
                    "pattern": "^SSH-([\\d.]+)-OpenSSH_([\\w._-]+-CERN\\d+)\\r?\\n",
                    "name": "ssh",
                    "pattern_flag": "",
                    "versioninfo": {
                        "cpename": "a:openbsd:openssh:$2",
                        "devicetype": "",
                        "hostname": "",
                        "info": "protocol $1",
                        "operatingsystem": "",
                        "vendorproductname": "OpenSSH",
                        "version": "$2"
                    }
                },
                {
                    "pattern": "^SSH-([\\d.]+)-OpenSSH_([\\w._-]+\\.cern-hpn)",
                    "name": "ssh",
                    "pattern_flag": "",
                    "versioninfo": {
                        "cpename": "a:openbsd:openssh:$2",
                        "devicetype": "",
                        "hostname": "",
                        "info": "protocol $1",
                        "operatingsystem": "",
                        "vendorproductname": "OpenSSH",
                        "version": "$2"
                    }
                },
                {
                    "pattern": "^SSH-([\\d.]+)-OpenSSH_([\\w._-]+-hpn)\\r?\\n",
                    "name": "ssh",
                    "pattern_flag": "",
                    "versioninfo": {
                        "cpename": "a:openbsd:openssh:$2",
                        "devicetype": "",
                        "hostname": "",
                        "info": "protocol $1",
                        "operatingsystem": "",
                        "vendorproductname": "OpenSSH",
                        "version": "$2"
                    }
                },
                {
                    "pattern": "^SSH-([\\d.]+)-OpenSSH_([\\w._-]+-pwexp\\d+)\\r?\\n",
                    "name": "ssh",
                    "pattern_flag": "",
                    "versioninfo": {
                        "cpename": "o:ibm:aix",
                        "devicetype": "",
                        "hostname": "",
                        "info": "protocol $1",
                        "operatingsystem": "AIX",
                        "vendorproductname": "OpenSSH",
                        "version": "$2"
                    }
                },
                {
                    "pattern": "^SSH-([\\d.]+)-OpenSSH_([\\w._-]+)-chrootssh\\n",
                    "name": "ssh",
                    "pattern_flag": "",
                    "versioninfo": {
                        "cpename": "a:openbsd:openssh:$2",
                        "devicetype": "",
                        "hostname": "",
                        "info": "protocol $1",
                        "operatingsystem": "",
                        "vendorproductname": "OpenSSH",
                        "version": "$2"
                    }
                },
                {
                    "pattern": "^SSH-([\\d.]+)-Nortel\\r?\\n",
                    "name": "ssh",
                    "pattern_flag": "",
                    "versioninfo": {
                        "cpename": "a:openbsd:openssh",
                        "devicetype": "switch",
                        "hostname": "",
                        "info": "protocol $1",
                        "operatingsystem": "",
                        "vendorproductname": "Nortel SSH",
                        "version": ""
                    }
                },
                {
                    "pattern": "^SSH-([\\d.]+)-OpenSSH_([\\w.]+)[-_]hpn(\\w+) DragonFly-",
                    "name": "ssh",
                    "pattern_flag": "",
                    "versioninfo": {
                        "cpename": "a:openbsd:openssh:$2",
                        "devicetype": "",
                        "hostname": "",
                        "info": "protocol $1; HPN-SSH patch $3",
                        "operatingsystem": "DragonFlyBSD",
                        "vendorproductname": "OpenSSH",
                        "version": "$2"
                    }
                },
                {
                    "pattern": "^SSH-([\\d.]+)-OpenSSH_([\\w.]+) DragonFly-",
                    "name": "ssh",
                    "pattern_flag": "",
                    "versioninfo": {
                        "cpename": "a:openbsd:openssh:$2",
                        "devicetype": "",
                        "hostname": "",
                        "info": "protocol $1",
                        "operatingsystem": "DragonFlyBSD",
                        "vendorproductname": "OpenSSH",
                        "version": "$2"
                    }
                },
                {
                    "pattern": "^SSH-([\\d.]+)-OpenSSH_([\\w_.-]+) FIPS\\n",
                    "name": "ssh",
                    "pattern_flag": "",
                    "versioninfo": {
                        "cpename": "a:openbsd:openssh:$2",
                        "devicetype": "firewall",
                        "hostname": "",
                        "info": "protocol $1; Imperva SecureSphere firewall",
                        "operatingsystem": "",
                        "vendorproductname": "OpenSSH",
                        "version": "$2"
                    }
                },
                {
                    "pattern": "^SSH-([\\d.]+)-OpenSSH_([\\w_.-]+) FIPS\\r\\n",
                    "name": "ssh",
                    "pattern_flag": "",
                    "versioninfo": {
                        "cpename": "a:openbsd:openssh:$2",
                        "devicetype": "switch",
                        "hostname": "",
                        "info": "protocol $1; Cisco NX-OS",
                        "operatingsystem": "",
                        "vendorproductname": "OpenSSH",
                        "version": "$2"
                    }
                },
                {
                    "pattern": "^SSH-([\\d.]+)-OpenSSH_([\\w_.-]+) NCSA_GSSAPI_GPT_([-\\w_.]+) GSI\\n",
                    "name": "ssh",
                    "pattern_flag": "",
                    "versioninfo": {
                        "cpename": "a:openbsd:openssh:$2",
                        "devicetype": "",
                        "hostname": "",
                        "info": "protocol $1; NCSA GSSAPI authentication patch $3",
                        "operatingsystem": "",
                        "vendorproductname": "OpenSSH",
                        "version": "$2"
                    }
                },
                {
                    "pattern": "^SSH-([\\d.]+)-OpenSSH_([\\w._-]+) \\.\\n",
                    "name": "ssh",
                    "pattern_flag": "",
                    "versioninfo": {
                        "cpename": "a:openbsd:openssh:$2",
                        "devicetype": "",
                        "hostname": "",
                        "info": "protocol $1",
                        "operatingsystem": "",
                        "vendorproductname": "OpenSSH",
                        "version": "$2"
                    }
                },
                {
                    "pattern": "^SSH-([\\d.]+)-OpenSSH_([\\w._-]+) PKIX\\r\\n",
                    "name": "ssh",
                    "pattern_flag": "",
                    "versioninfo": {
                        "cpename": "a:openbsd:openssh:$2",
                        "devicetype": "",
                        "hostname": "",
                        "info": "protocol $1; X.509 v3 certificate support",
                        "operatingsystem": "",
                        "vendorproductname": "OpenSSH",
                        "version": "$2"
                    }
                },
                {
                    "pattern": "^SSH-([\\d.]+)-OpenSSH_([\\w._-]+)-FIPS\\(capable\\)\\r\\n",
                    "name": "ssh",
                    "pattern_flag": "",
                    "versioninfo": {
                        "cpename": "a:openbsd:openssh:$2",
                        "devicetype": "",
                        "hostname": "",
                        "info": "protocol $1; FIPS capable",
                        "operatingsystem": "",
                        "vendorproductname": "OpenSSH",
                        "version": "$2"
                    }
                },
                {
                    "pattern": "^SSH-([\\d.]+)-OpenSSH_([\\w._-]+)-sshjail\\n",
                    "name": "ssh",
                    "pattern_flag": "",
                    "versioninfo": {
                        "cpename": "a:openbsd:openssh:$2",
                        "devicetype": "",
                        "hostname": "",
                        "info": "protocol $1; sshjail patch",
                        "operatingsystem": "",
                        "vendorproductname": "OpenSSH",
                        "version": "$2"
                    }
                },
                {
                    "pattern": "^SSH-([\\d.]+)-OpenSSH_([\\w._-]+) Raspbian-([^\\r\\n]+)\\r?\\n",
                    "name": "ssh",
                    "pattern_flag": "",
                    "versioninfo": {
                        "cpename": "o:linux:linux_kernel",
                        "devicetype": "",
                        "hostname": "",
                        "info": "protocol $1",
                        "operatingsystem": "Linux",
                        "vendorproductname": "OpenSSH",
                        "version": "$2 Raspbian $3"
                    }
                },
                {
                    "pattern": "^SSH-([\\d.]+)-OpenSSH_([\\w._-]+) OVH-rescue\\r\\n",
                    "name": "ssh",
                    "pattern_flag": "",
                    "versioninfo": {
                        "cpename": "a:openbsd:openssh:$2",
                        "devicetype": "",
                        "hostname": "",
                        "info": "protocol $1; OVH hosting rescue",
                        "operatingsystem": "",
                        "vendorproductname": "OpenSSH",
                        "version": "$2"
                    }
                },
                {
                    "pattern": "^SSH-([\\d.]+)-OpenSSH_([\\w._-]+) Trisquel_GNU/linux_([\\d.]+)(?:-\\d+)?\\r\\n",
                    "name": "ssh",
                    "pattern_flag": "",
                    "versioninfo": {
                        "cpename": "o:trisquel_project:trisquel_gnu%2flinux:$3",
                        "devicetype": "",
                        "hostname": "",
                        "info": "protocol $1; Trisquel $3",
                        "operatingsystem": "Linux",
                        "vendorproductname": "OpenSSH",
                        "version": "$2"
                    }
                },
                {
                    "pattern": "^SSH-([\\d.]+)-OpenSSH_([\\w._-]+) \\+ILOM\\.2015-5600\\r\\n",
                    "name": "ssh",
                    "pattern_flag": "",
                    "versioninfo": {
                        "cpename": "h:oracle:integrated_lights-out",
                        "devicetype": "",
                        "hostname": "",
                        "info": "protocol $1; ILOM patched CVE-2015-5600",
                        "operatingsystem": "",
                        "vendorproductname": "OpenSSH",
                        "version": "$2"
                    }
                },
                {
                    "pattern": "^SSH-([\\d.]+)-OpenSSH_([\\w._-]+) SolidFire Element \\r\\n",
                    "name": "ssh",
                    "pattern_flag": "",
                    "versioninfo": {
                        "cpename": "o:netapp:element_software",
                        "devicetype": "",
                        "hostname": "",
                        "info": "protocol $1; NetApp SolidFire storage node",
                        "operatingsystem": "",
                        "vendorproductname": "OpenSSH",
                        "version": "$2"
                    }
                },
                {
                    "pattern": "^SSH-([\\d.]+)-OpenSSH[_-]([\\w.]+)\\s*\\r?\\n",
                    "name": "ssh",
                    "pattern_flag": "i",
                    "versioninfo": {
                        "cpename": "a:openbsd:openssh:$2",
                        "devicetype": "",
                        "hostname": "",
                        "info": "protocol $1",
                        "operatingsystem": "",
                        "vendorproductname": "OpenSSH",
                        "version": "$2"
                    }
                },
                {
                    "pattern": "^SSH-2\\.0-OpenSSH\\r?\\n",
                    "name": "ssh",
                    "pattern_flag": "",
                    "versioninfo": {
                        "cpename": "",
                        "devicetype": "router",
                        "hostname": "",
                        "info": "protocol 2.0",
                        "operatingsystem": "",
                        "vendorproductname": "Linksys WRT45G modified dropbear sshd",
                        "version": ""
                    }
                },
                {
                    "pattern": "^SSH-2\\.0-OpenSSH_3\\.6p1\\r?\\n",
                    "name": "ssh",
                    "pattern_flag": "",
                    "versioninfo": {
                        "cpename": "",
                        "devicetype": "",
                        "hostname": "",
                        "info": "",
                        "operatingsystem": "",
                        "vendorproductname": "",
                        "version": ""
                    }
                },
            ]
        }
    ]

    # socket.AF_INET 表示指定使用 IPv4 协议
    # SOCK_STREAM 指定使用面向流的 TCP 协议
    tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_client_socket.connect(ip_port)

    # send=input("请输⼊需要发送数据：")

    send = probe[0]["probestring"]
    print("发送信息:" + send)
    tcp_client_socket.send(send.encode("utf-8"))  # 将str类型转为bytes类型

    feedback = tcp_client_socket.recv(1024).decode("utf-8")  # 每次最多接收1k字节

    print('接收到数据:', feedback)
    print('接收到数据:', type(feedback))


    for i in probe[0]["matches"]:

        pattern = i["pattern"]
        print("正则匹配式：" + pattern)

        Identif = re.match(pattern, feedback)

        if Identif != None:
            print(Identif)
            result = i["name"]
            print("识别结果为：" + result + " " + Identif.string)
            tcp_client_socket.close()  # 关闭连接

            return 1

    return 0

if __name__ == '__main__':
    target = ['10.21.145.59', 443]
    # print(type(str(43)))
    appScan(target)

    # main(target)
