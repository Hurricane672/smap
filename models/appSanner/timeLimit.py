import time
import traceback
import eventlet
from wrapt_timeout_decorator import timeout
from func_timeout import func_set_timeout
#导入eventlet这个模块
# eventlet.monkey_patch()#必须加这条代码

# with eventlet.Timeout(5,False):#设置超时时间为5秒
#     time.sleep(8)
#     print('没有跳过这条输出')
# print('跳过了输出')

###########函数方式#######################
def timeou(name,_time):
    eventlet.monkey_patch()#必须加这条代码
    with eventlet.Timeout(_time,False):#设置超时间
        while True:
            a=1
            a=a+1
            eventlet.sleep()
        print('没有跳过这条输出')
    print('不好意思函数调用超时')

@func_set_timeout(3)
def loop():
    while True:
        a=1
        a=a+1



if __name__ == '__main__':
    try:
        loop()
    except:
        traceback.print_exc()
        print('假装我是后续代码1')
        # print("错误信息:",e)
    print("hi")     
    print(timeou('你好靓女！',4))