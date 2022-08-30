import os
import re
import json
import multiprocessing
import time
res = []

def tracert(ips, index):
    f = open("temp" + index, "w+", encoding="utf-8")
    for ip in ips:
        result = os.popen("tracert " + ip).read()
        result = re.findall("\d{1,}.\d{1,}.\d{1,}.\d{1,}", result)[1:]
        f.write(json.dumps(result) + "\n")
        print(result)

def tracert1(ip):
    result = os.popen("tracert " + ip).read()
    result = re.findall("\d{1,}.\d{1,}.\d{1,}.\d{1,}", result)[1:]
    res.append(list(result))
    print(result)
    f = open("temp","a+",encoding="utf-8")
    f.write(json.dumps(result)+"\n")
    f.close()

def main(ips):
    ips = ["10.122.251.228", "10.122.210.19"]
    # num = len(ips)/4
    # ip1 = ips[0:num]
    # ip2 = ips[num:2*num]
    # ip3 = ips[2*num:3*num]
    # ip4 = ips[num:2*num]
    # tracert1(ips)
    pool = multiprocessing.Pool()
    res = pool.map(tracert1, ips)
    pool.close()
    pool.join()

    # ip = [[], [], [], []]
    # for i in range(len(ips)):
    #     if i % 4 == 0:
    #         ip[0].append(ips[i])
    #     elif i % 4 == 1:
    #         ip[1].append(ips[i])
    #     elif i % 4 == 2:
    #         ip[2].append(ips[i])
    #     else:
    #         ip[3].append(ips[i])
    # p = []
    # for i in range(0, 4):
    #     print(ip[i])
    #     p.append(multiprocessing.Process(target=tracert, args=(ip[i], str(i))))
    #     p[i].daemon = False
    #     p[i].start()
    #
    # l = []
    # for i in range(0, 4):
    #     f = open("temp" + str(i), "r+", encoding="utf-8")
    #     paths = f.readlines()
    #     for j in paths:
    #         l.append(json.loads(j))
    # print(l)
    f = open("temp", "r+", encoding="utf-8")
    l = []
    for i in f.readlines():
        l.append(json.loads(i))
    print(l)
    f.close()
    os.remove("./temp")
    print("finished")
    # tracert(ips,"1")


if __name__ == '__main__':
    ips = ["10.122.251.228", "10.122.210.19"]
    main(ips)
