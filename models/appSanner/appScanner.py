# -*- coding =utf-8 -*-
# @time:2022/8/29
import sys
import traceback
from TCP_NULL import TCP_Scan
from ExtraScanMain import ExtraScan

#target = ['10.21.145.59',80]
def appScan(target):
    #Step1: TCP空包探查
    result = TCP_Scan(target)
    try:
        if result["service"] != '':
            print("空探针识别结果:"+str(result))
            return result
        else:
            # Step2: TCP特殊探针探查
            result = ExtraScan(target)
            if result["service"] != '':
                print("特殊探针识别结果:"+str(result))
                return result
            else:
                print("Scan Service Fail!")
                return result


    except:
        traceback.print_exc()
        print("Scan Service Fail!")
        return result
        # print("The target computer actively refuses and cannot connect!")



if __name__ == '__main__':
    target = ['10.21.145.59',3306]
    print(appScan(target))
#1.除80端口外的端口，会报连接错误，次数过多就不让扫了
#基于上述问题，可能需要融合别人的代码
#2.漏洞查询模块，有的版本爬不到具体漏洞，所以可以考虑只取版本号的第一位或，只用服务名称
#3.接口调用main函数问题
#4.某些服务