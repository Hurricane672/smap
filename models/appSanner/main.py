# -*- coding =utf-8 -*-
# @time:2022/8/29
import sys
from TCP_NULL import TCP_Scan
from extraScan import  ExtraScan

if __name__ == '__main__':
    target = ['10.122.214.150', 3306]

    try:
        # Step1: TCP空包探查
        result = TCP_Scan(target)
        if result != 0:
            print(result)
            sys.exit()
        else:
            # Step2: TCP特殊探针探查
            result == ExtraScan(target)

        if result != 0:
            print(result)
            sys.exit()
        else:
            # Step3: 如果探测到应用程序是SSL，那么调用openSSL进一步的侦查运行在SSL之上的具体的应用类型
            result == SSL_Scan(target)

        if result != 0:
            print(result)
            sys.exit()
        else:
            print("Scan Service Fail!")

    except:
        print("The target computer actively refuses and cannot connect!")



