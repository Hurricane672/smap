import os
import re
import json
import multiprocessing


def tracert(ip):
    result = os.popen("tracert " + ip).read()
    if "无法访问目标主机" in result:
        print("Target "+ip+" disconnect.")
        pass
    else:
        result = re.findall("\d{1,}.\d{1,}.\d{1,}.\d{1,}", result)[1:]
        f = open("temp", "a+", encoding="utf-8")
        f.write(json.dumps(result) + "\n")
        f.close()


def main(ips):
    ips = ["10.122.251.228", "10.122.210.19"]
    pool = multiprocessing.Pool()
    res = pool.map(tracert, ips)
    pool.close()
    pool.join()
    f = open("temp", "r+", encoding="utf-8")
    l = []
    for i in f.readlines():
        l.append(json.loads(i))
    print(l)
    f.close()
    os.remove("./temp")
    print("Tracert finished.")
    return l


if __name__ == '__main__':
    ips = ["10.122.251.228", "10.122.210.19"]
    main(ips)
