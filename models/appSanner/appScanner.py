# -*- coding =utf-8 -*-
# @time:2022/8/29
import sys
import traceback
from TCP_NULL import TCP_Scan
from ExtraScanMain import ExtraScan
from spareScanner import spareScan

def main(target):
    result = {"service": "", "version": ""}
    result = TCP_Scan(target, result)  # Step1: TCP空包探查
    try:
        if result["service"] != '':
            print("空探针识别结果:"+str(result))
            return result
        else:
            print("Step 1 Fail!")
            # Step2: TCP特殊探针探查
            result = ExtraScan(target,result)
            if result["service"] != '':
                print("特殊探针识别结果:"+str(result))
                return result
            else:
                print("Step 2 Fail!")
                #Step2: TCP特殊探针探查
                result = spareScan(target,result)
                if result["service"] != '':
                    print("特殊探针识别结果:"+str(result))
                    return result
                else:
                    print("Step 3 Fail!")
                    print("Scan Service Fail!")
                    return result

    except:
        traceback.print_exc()
        print("Scan Service Fail!")
        return result



if __name__ == '__main__':
    target = ['10.21.145.59',80]
    # target = ['10.122.214.150',135]
    main(target)






#1.除80端口外的端口，会报连接错误，次数过多就不让扫了
#基于上述问题，可能需要融合别人的代码
#2.漏洞查询模块，有的版本爬不到具体漏洞，所以可以考虑只取版本号的第一位或，只用服务名称
#4.某些服务