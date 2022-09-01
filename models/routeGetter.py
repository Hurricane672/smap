import os
import re
import json
import multiprocessing

aaa = []
def tracert(ip):
    print("tracert -w 5 -h 5 " + ip)
    result = os.popen("tracert -w 5 -h 5 " + ip).read()
    if "无法访问目标主机" in result:
        print("Target " + ip + " disconnect.")
        pass
    else:
        result = ["127.0.0.1"] + re.findall("\d{1,}.\d{1,}.\d{1,}.\d{1,}", result)[1:]
        f = open("temp", "a+", encoding="utf-8")
        f.write(json.dumps(result) + "\n")
        f.close()


def process(l):
    r = []
    for route in l:
        if len(route) >= 2:
            for i in range(0, len(route) - 1):
                t0 = [route[i], route[i + 1]]
                t1 = [route[i + 1], route[i]]
                if t0 not in r and t1 not in r:
                    r.append(t0)
                else:
                    print(str(t0) + " is already in route list.")
        else:
            print("Skip invalid route " + str(route) + ".")
    result = []
    for i in r:
        d = {'from': i[0], 'to': i[1]}
        result.append(d)

    print(r)
    print(result)
    return result


def main(ips):
    f = open("temp", "a+", encoding="utf-8")
    f.close()
    # ips = ["10.122.251.228", "10.122.210.19", "10.122.214.150", "10.122.220.161"]
    pool = multiprocessing.Pool()
    pool.map(tracert, ips)
    pool.close()
    pool.join()
    f = open("temp", "r+", encoding="utf-8")
    l = []
    for i in f.readlines():
        if i == "\n":
            pass
        else:
            print(i)
            l.append(json.loads(i))
    print(l)
    f.close()
    os.remove("./temp")
    print("Tracert finished.")
    # l = [['0', '1', '2', '3'], ['0', '1', '5', '6'], ['0', '1', '5', '7'], ['0', '4', '1', '8'], ['0', '9'], ['0'],
    #      ['9']]
    l = process(l)
    return l


if __name__ == '__main__':
    ips = ['10.20.0.6', '10.20.0.3', '10.20.0.14', '10.20.0.7', '10.20.0.26', '10.20.0.15', '10.20.0.9', '10.20.0.29', '10.20.0.31', '10.20.0.1', '10.20.0.25', '10.20.0.5', '10.20.0.22', '10.20.0.21', '10.20.0.2', '10.20.0.10', '10.20.0.30']
    main(ips)
