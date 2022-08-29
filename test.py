import os
import re
import json
import multiprocessing
import time

def tracert(ips, index):
    f = open("temp" + index, "w+", encoding="utf-8")
    for ip in ips:
        result = os.popen("tracert " + ip).read()
        result = re.findall("\d{1,}.\d{1,}.\d{1,}.\d{1,}", result)[1:]
        f.write(json.dumps(result) + "\n")
        print(result)



if __name__ == '__main__':
    ips = ["10.122.251.228", "10.122.210.19"]
    # num = len(ips)/4
    # ip1 = ips[0:num]
    # ip2 = ips[num:2*num]
    # ip3 = ips[2*num:3*num]
    # ip4 = ips[num:2*num]
    ip1 = []
    ip2 = []
    ip3 = []
    ip4 = []
    for i in range(len(ips)):
        if i % 4 == 0:
            ip1.append(ips[i])
        elif i % 4 == 1:
            ip2.append(ips[i])
        elif i % 4 == 2:
            ip3.append(ips[i])
        else:
            ip4.append(ips[i])
    print(ip1)
    print(ip2)
    print(ip3)
    print(ip4)
    p1 = multiprocessing.Process(target=tracert, args=(ip1, "1"))
    p2 = multiprocessing.Process(target=tracert, args=(ip2, "2"))
    p3 = multiprocessing.Process(target=tracert, args=(ip3, "3"))
    p4 = multiprocessing.Process(target=tracert, args=(ip4, "4"))
    p1.daemon = True
    p2.daemon = True
    p3.daemon = True
    p4.daemon = True
    p1.start()
    # p1.join()
    p2.start()
    # p2.join()
    p3.start()
    # p3.join()
    p4.start()
    # p4.join()
    l = []
    for i in range(1,5):
        f = open("temp"+str(i),"r+",encoding="utf-8")
        paths = f.readlines()
        for j in paths:
            l.append(json.loads(j))
    print(l)
    print("finished")
    # tracert(ips,"1")