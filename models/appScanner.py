# -*- coding =utf-8 -*-
# @time:2022/8/29
import traceback
from AppScanner.TCP_NULL import TCP_Scan
from AppScanner.ExtraScanMain import ExtraScan
from AppScanner.spareScanner import spareScan

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
                # Step2: TCP特殊探针探查
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
    # target = ['10.21.145.59',80]
    target = ['127.0.0.1',80]
    main(target)
