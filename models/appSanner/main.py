# -*- coding =utf-8 -*-
# @time:2022/8/29
import sys
import traceback
from TCP_NULL import TCP_Scan
from ExtraScanMain import ExtraScan


if __name__ == '__main__':
    target = ['10.21.145.59',80]

    try:
        result=0
        #Step1: TCP空包探查
        # result = TCP_Scan(target)
        if result != 0:
            print(result)
            sys.exit()
        else:
            # Step2: TCP特殊探针探查
            result = ExtraScan(target)
            
            # if result != 0:
            #     print(result)
            #     sys.exit()
            # else:
            #     # Step3: 如果探测到应用程序是SSL，那么调用openSSL进一步的侦查运行在SSL之上的具体的应用类型
            #     result == SSL_Scan(target)
            
        if result != 0:
            print(result)
            sys.exit()
        else:
            print("Scan Service Fail!")

    except:
        traceback.print_exc()
        print("The target computer actively refuses and cannot connect!")



