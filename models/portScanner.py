import time
import asyncio
import threading

port_list = []
class PortScan(object):
    """docstring for PortScan"""
    def __init__(self, ip_list=["127.0.0.1"], all_ports=False, rate=2000):
        super(PortScan, self).__init__()
        self.ip_list = ip_list
        self.rate = rate
        self.all_ports = all_ports
        self.open_list = {}

    async def async_port_check(self, semaphore, ip_port):
        async with semaphore:
            ip,port = ip_port
            conn = asyncio.open_connection(ip, port)
            try:
                reader, writer = await asyncio.wait_for(conn, timeout=50)
                return (ip, port, 'open')
            except Exception as e:
                # print(e)
                return (ip, port, 'close')

    def callback(self, future):
        ip,port,status = future.result()
        if status == "open":
            #print(port)
            global port_list
            port_list.append(port)
            # try:
            #     if ip_addr in self.open_list:
            #         self.open_list[ip_addr].append(port)
            #     else:
            #         self.open_list[ip_addr] = [port]
            # except Exception as e:
            #     print(e)
        else:
            pass

    def async_tcp_port_scan(self):
        ports = [port for port in range(0,65535)]
        ip_port_list = [(ip,int(port)) for ip in self.ip_list for port in ports]

        sem = asyncio.Semaphore(self.rate) # 限制并发量
        loop = asyncio.get_event_loop()

        tasks = list()
        for ip_port in ip_port_list:
            task = asyncio.ensure_future(self.async_port_check(sem, ip_port))
            task.add_done_callback(self.callback)
            tasks.append(task)

        loop.run_until_complete(asyncio.wait(tasks))
        global port_list
        print(port_list)
        return port_list
        #print(self.open_list)


def main(target):
    #target为传入IP,rate为并发频率
    # 暂时开启了输出端口列表
    rate = 1000
    #now = time.time

    #start_ip = now()
    ps = PortScan(target,True,rate)
    ps.async_tcp_port_scan()
    #print("Time:",now()-start_ip)
if __name__ == '__main__':
    target = ["127.0.0.1"]
    main(target)