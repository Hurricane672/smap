#!/bin/bash
# 需要ipcalc库,win端无法使用
FILENAME="ip_port.txt"
#获取ip段
read -p "请输入需要扫描的服务器ip:" server_ip
read -p "请输入掩码长度:" netmask
read -p "请输入扫描起始端口:" port_start
read -p "请输入扫描的结束端口:" port_end
#server_ip="10.0.0.1"
#netmask="24"
#port_start="80"
#port_end="443"
#检测输入合法性
#declare -i port_start
#declare -i port_end
touch $FILENAME

if [ ${port_start} -gt ${port_end} ]; then
  echo "输入格式出错,起始端口应小于结束端口"
  exit 1
elif [ $port_end -gt 65535 ]; then
  echo "输入格式出错，端口过大"
  exit 1
fi
#获取ip段信息
ipc_result=$(ipcalc -nb ${server_ip}/${netmask})
host_min=$(echo "${ipc_result}" | awk '/HostMin/ {print $2}')
host_max=$(echo "${ipc_result}" | awk '/HostMax/ {print $2}')
host_num=$(echo "${ipc_result}" | awk '/Hosts\/Net/ {print $2}')
netmask=$(echo "${ipc_result}" | awk '/Netmask/ {print $2}')
host_address=$(echo "${ipc_result}" | awk '/Address/ {print $2}')

if [ "$host_num" == "1" ]; then
host_min=$host_address
host_max=$host_address
fi
port_num=$(($port_end - $port_start + 1))
total_port_num=$((host_num * port_num))
continue_portnum=$port_start
scanned_port_num=0
#记录扫描耗时
start_time=$(date +%s)
echo "-------------------------------------------------------" >> $FILENAME
echo "开始进行扫描 ip范围:${host_min}~${host_max} 掩码长度:${netmask} 共有:${host_num}个ip" >> $FILENAME
echo "扫描端口范围:${port_start}~${port_end} 范围内:${port_num}个端口 总共:${total_port_num}个端口" >> $FILENAME
#暂时不考虑服务器禁止icmp
#ping超时设为1s
function pingCheck() {
  echo "检测${1}的在线情况"
  ping $1 -q -c2 -W 1  > /dev/null
  if [ $? -eq 0 ]; then
    echo "${1}在线"
    return 0
  else
    echo "${1}不在线"
    #端口进度要更新一下
    scanned_port_num=$continue_portnum
    return 1
  fi  
}
# echo "扫描端口范围:${port_start}~${port_end} 范围内:${port_num}个端口 总共:${total_port_num}个端口" | tee -a $FILENAME
trap 'onCtrlC' INT
function onCtrlC () {
  #之后可以考虑做成可以断点继续扫描的形式
  #现场保护 如果没扫描完就退出就创建一个临时文件
  if [ $scanned_port_num -ne $total_port_num ]; then
    touch ".${FILENAME}"
    #保存状态...其实有点麻烦..涉及到的数据有点多，暂时不做了
    #考虑到下面写入了服务器列表，所以这里不保存数组了，只保存当前扫描到的ip 最大的ip（或者剩下的ip数） 端口范围即可
    echo ${scan_ip} > ".${FILENAME}"
    echo ${host_max} >> ".${FILENAME}"
    echo ${port_start} >> ".${FILENAME}"
    echo ${port_end} >> ".${FILENAME}"
  fi
  # touch ".${FILENAME}_stat"
  end_time=$(date +%s)
  echo "服务器列表 ${find_servers[*]}" | tee -a $FILENAME
  echo -e "手动中止扫描,耗时$(($end_time - $start_time))秒,对${host_min}~${host_max}的${port_start}~${port_end}端口扫描,共找到${find_count}个可用端口${find_server_count}个可用服务器" | tee -a $FILENAME
  exit 0
}
#二重循环.扫描每个ip的指定端口范围
#循环扫描端口
find_count=0
find_server_count=0
find_servers=()
#要将字符串列表转变为数组，只需要在前面加()，所以关键是将分隔符转变为空格分隔，这个数组用于递增切换地址
scanip_arr=($(echo $host_min | tr '.' ' '))
sip=1
for ((j = 1; j <= $host_num ; j++))
do
#当前服务器不是中转服务器
find_server_flag=false
#拼接当前要扫的ip
scan_ip=$(echo ${scanip_arr[*]} | tr ' ' '.')
#为了加快扫描速度，先检查服务器是否可以ping通，暂时不考虑禁Iicmp情况
continue_portnum=$(($continue_portnum+$port_num))
pingCheck ${scan_ip}
pc=$?
#如果ping得通才扫描，不然跳过
if [ $pc -eq 0 ]; then
  echo "开始对ip:${scan_ip} 进行扫描 当前进度(${j}/${host_num})"
  sport=0
    for ((i = $port_start ; i <= $port_end ; i++))
    do
      let scanned_port_num++
      let sport++
      `nc -v -z -w 5 ${scan_ip} ${i}`
      res=$?
      #echo "$res  已经找到:$find_count个可用"
      if [ $res == "0" ]; then
        let find_count++
        #如果一个ip找到了开放端口，说明这个服务器可能有更多的端口开放，记录该服务器
        if [ $find_server_flag == false ]; then
          echo "发现新的服务器:${scan_ip}" >> $FILENAME
          find_server_flag=true
          let find_server_count++
          find_servers[${#find_servers[@]}]=$scan_ip
        fi
        #写入文件
        #echo "ip:${scan_ip} 端口:${i}可用"  | tee -a $FILENAME
        echo "ip:${scan_ip} 端口:${i}可用" >> $FILENAME
      fi
      #记录每个IP每个端口结果，默认只记录开放端口开放IP结果
      #echo "ip:${scan_ip} 端口:${i} 情况:${res}" >> $FILENAME
      percentage=$(echo "scale=2; $scanned_port_num / $total_port_num" | bc)
      clear
      echo -e "ip进度:(${sip}/${host_num}) 端口进度:(${sport}/${port_num})正在扫描端口$i 已经找到:$find_count个可用端口,$find_server_count个服务器 总进度:($scanned_port_num/$total_port_num) $percentage%"
    done
  fi
#之后要对iparr进行增加
let sip++
scanip_arr[3]=$((${scanip_arr[3]}+1))
if [ ${scanip_arr[3]} -gt 255 ]; then
  echo "C+1"
  scanip_arr[3]=1
  scanip_arr[2]=$((${scanip_arr[2]}+1))
fi
if [ ${scanip_arr[2]} -gt 255 ]; then
  echo "B+1"
  scanip_arr[2]=1
  scanip_arr[1]=$((${scanip_arr[1]}+1))
fi
if [ ${scanip_arr[1]} -gt 255 ]; then
  echo "A+1"
  scanip_arr[1]=1
  scanip_arr[0]=$((${scanip_arr[0]}+1))
fi
done
end_time=$(date +%s)
echo "服务器列表 ${find_servers[*]}" | tee -a $FILENAME
echo "耗时$(($end_time - $start_time))秒,完成对${host_min}~${host_max}的${port_start}~${port_end}端口扫描,共找到${find_count}个可用端口${find_server_count}个可用服务器" | tee -a $FILENAME
exit 0
