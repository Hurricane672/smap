# SMAP说明文档

## 后端模块接口文档

### 一、多主机总体扫描部分

#### 1、ip地址接口 hostScanner

**In**：

    内容描述：ip网段
    
    举例说明：(start_ip, end_ip)
    形如 (192.168.1.1, 192.168.2.128)
    
    数据类型：字符串

**Out：**

    内容描述：该网段中存活的ip地址列表
    
    举例说明：{"ip1":["hostname", "mac_address", "vendor","delay"], "ip2":["hostname", "mac_address", "vendor", "delay"], ...}
    
    数据类型：字典dict{key1: list1, key2: list2}其中value为列表


#### 2、端口扫描接口 portScanner

**In**：

    内容描述：ip地址
    
    举例说明：形如 192.168.1.1
    
    数据类型：字符串

**Out：**

    内容描述：该ip中存活的端口列表
    
    举例说明：[port1,port2,port3,port4......]
    
    数据类型：list(int)

### 二、拓扑图生成部分

#### 1、拓扑链路生成 routeGetter

**In**：

    内容描述：存活ip列表列表
    
    举例说明：形如，[ip2,ip3,ipn...]
    
    数据类型：list(str)

**Out：**

    内容描述：ip链路列表列表
    
    举例说明：形如，[[ip2,ip3,ipn...ip1],[ip5,ip3,ipn...ip2],[...ip3],[...ip4]...]，简单的说，就是从扫描机出发，经过ip2、ip3、ipn和等等，可以联通到ip1；从扫描机出发，经过。。。，可以到达ip2；以此类推
    
    数据类型：list(list(str))

#### 1改、拓扑链路生成 routeGetter

**In**：

    内容描述：存活ip列表列表
    
    举例说明：形如，[ip2,ip3,ipn...]
    
    数据类型：list(str)

**Out：**

    内容描述：ip连接矩阵表示
    
    举例说明：[
    	{"from":"192.168.1.2","to":"192.168.1.1"},
    	{"from":"192.168.1.3","to":"192.168.1.1"},
    	{"from":"192.168.1.4","to":"192.168.1.1"},
    ]
    
    数据类型：list(dict(str,str))



#### 2、拓扑图绘制  topoDrawer

**In**：

    内容描述：ip链路列表列表
    
    举例说明：形如，[[ip2,ip3,ipn...ip1],[ip5,ip3,ipn...ip2],[...ip3],[...ip4]...]，简单的说，就是从扫描机出发，经过ip2、ip3、ipn和等等，可以联通到ip1；从扫描机出发，经过。。。，可以到达ip2；以此类推
    
    数据类型：list(list(str))

**Out：**

    内容描述：生成的拓扑图图片
    
    举例说明：a.png
    
    数据类型：能实现输出文件到对应目录即可



### 三、单套接字扫描部分 appScanner

**In**：

    内容描述：ip加端口
    
    举例说明：['192.169.0.1',22]
    
    数据类型：list ,第一个元素为str，第二个元素为int

**Out：**

    内容描述：涉及到的应用服务和版本
    
    举例说明：{"service":"", "version":""}
    
    数据类型：dict{str,str}，注意，英文名称和版本号之间使用空格隔开！



### 四、web应用扫描部分 webScanner

**In:**

```
内容描述：ip加端口列表（两个参数）
举例说明："192.168.1.1",[22，34，56，80，1000，1390，3306，65000]
数据类型：str,list(int)
```

**Out:**

```
内容描述：端口对应的指纹列表
举例说明：
注意：只返回扫描到的web服务
[
	{
    	"port":"22",
        "cdn":"cdnxxxx",
        "cms":"cmsxxxx",
        "framework":"frameworkxxxx",
        "frontend":"frontendxxxx", 
        "lang":"langxxx",
        "server":"serverxxxx",
        "system":"systemxxxx",
        "waf":"wafxxxx"
    },
    {
    	"port":"80",
        "cdn":"cdnxxxx",
        "cms":"cmsxxxx",
        "framework":"frameworkxxxx",
        "frontend":"frontendxxxx", 
        "lang":"langxxx",
        "server":"serverxxxx",
        "system":"systemxxxx",
        "waf":"wafxxxx"
    },
    {
    	"port":"9999",
        "cdn":"cdnxxxx",
        "cms":"cmsxxxx",
        "framework":"frameworkxxxx",
        "frontend":"frontendxxxx", 
        "lang":"langxxx",
        "server":"serverxxxx",
        "system":"systemxxxx",
        "waf":"wafxxxx"
    },
]
数据类型： list(dict{str:str})
```



### 五、漏洞查询部分 vulFinder

**In**：

    内容描述：应用名称等相关信息（支持中文）
    
    举例说明：形如 ‘apache  远程代码执行‘  ’apache log4j‘
    
    数据类型：字符串

**Out：**

    内容描述：可能存在的漏洞名称列表 !如果能查询到日期会给出日期，如果没有则为空，一个字符串为一个列表元素
    
    举例说明：['"CVE-2022-34305" Apache Tomcat 跨站脚本漏洞（CVE-2022-34305） 2022-06-24 , "无CVE" Apache Tomcat拒绝服务漏洞（CNVD-2012-7096）']
    
    数据类型：list[str]



## 前后端接口设计文档

In表示前端向后端请求，out表示

### 一、拓扑图接口 topoList

```
In:
	{
	"fromIp":"192.168.1.1",
	"toIp":"192.168.1.5"
	}

#id和label相同
out:
	{
        "nodesArray":[
            {"id":"192.168.1.1", label:"192.168.1.1"},
            {"id":"192.168.1.2", label:"192.168.1.2"},
            {"id":"192.168.1.3", label:"192.168.1.3"},
            {"id":"192.168.1.4", label:"192.168.1.4"},
        ],
        "edgesArray":[
            {"from":"192.168.1.1", "to":"192.168.1.1"}
            {"from":"192.168.1.2", "to":"192.168.1.1"}
            {"from":"192.168.1.3", "to":"192.168.1.1"}
            {"from":"192.168.1.2", "to":"192.168.1.1"}
        ]
	}
```



### 二、单ip查询接口

- 主机基本物理信息
- 主机端口列表 --> 对应的服务列表
- web服务列表



#### 1、基本物理信息 basicInform

```
In:
	{
	"ipAddress":"192.168.1.1",
	}

out:
	{
       "hostname":"xxxx",
       "mac_address":""xxxx,
       "vendor":"xxxx",
       "delay":"xxxx"
	}
```



#### 2、端口对应的服务信息 appInform

```
In:
	{
	"ipAddress":"192.168.1.1",
	}

out:
	{
       "appInform":[
        {
       		"port":22,
       		"service":"ssh"
       		"version":"openssh 2.3.3"
       },{
       		"port":23,
       		"service":"ssh"
       		"version":"openssh 2.3.3"
       },{
       		"port":24,
       		"service":"ssh"
       		"version":"openssh 2.3.3"
       },{
       		"port":25s,
       		"service":"ssh"
       		"version":"openssh 2.3.3"
       }....
       ]
	}
```

#### 3、web应用信息 webInform


In:
	{
	"ipAddress":"192.168.1.1"
	}
Out:
	{
		webInform:[
            {
                "port":"22",
                "cdn":"cdnxxxx",
                "cms":"cmsxxxx",
                "framework":"frameworkxxxx",
                "frontend":"frontendxxxx", 
                "lang":"langxxx",
                "server":"serverxxxx",
                "system":"systemxxxx",
                "waf":"wafxxxx"
            },
            {
                "port":"80",
                "cdn":"cdnxxxx",
                "cms":"cmsxxxx",
                "framework":"frameworkxxxx",
                "frontend":"frontendxxxx", 
                "lang":"langxxx",
                "server":"serverxxxx",
                "system":"systemxxxx",
                "waf":"wafxxxx"
            },
            {
                "port":"9999",
                "cdn":"cdnxxxx",
                "cms":"cmsxxxx",
                "framework":"frameworkxxxx",
                "frontend":"frontendxxxx", 
                "lang":"langxxx",
                "server":"serverxxxx",
                "system":"systemxxxx",
                "waf":"wafxxxx"
            },
        ]
		
	}




### 三、关键字查询接口 findVul

```
In:
	{
		keyword:["apache","2.2.2"...]
	}
Out:
	{
		vuls:["xxxxxxx","xxxxxxxx"]
	}
```



## 指纹扫描策略

### 一、常见端口

- 常见端口及对应服务

  | 端口号       | 功能                                                         | 请求/响应                                                    |
  | ------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
  | 7            | Echo<br/>说明：能看到许多人搜索Fraggle放大器时，发送到X.X.X.0和X.X.X.255的信息。 |                                                              |
  | 19           | 服务：Character Generator<br/>说明：这是一种仅仅发送字符的服务。UDP版本将会在收到UDP包后回应含有垃圾字符的包。TCP连接时会发送含有垃圾字符的数据流直到连接关闭。 | HACKER利用IP欺骗可以发动DoS攻击。伪造两个chargen服务器之间的UDP包。同样FraggleDoS攻击向目标地址的这个端口广播一个带有伪造受害者IP的数据包，受害者为了回应这些数据而过载。 |
  | 20           | ftp数据端口                                                  |                                                              |
  | 21端口       | 21端口主要用于FTP（File Transfer Protocol，文件传输协议）服务。 | 爆破/匿名访问/资源嗅探/后门Linux的vsftp某版本/6.10.1 IIS FTP远程溢出漏洞/跳转攻击 |
  | 22端口       | ssh 服务                                                     | 弱口令/28退格漏洞、OpenSSL漏洞                               |
  | 23端口       | 23端口主要用于Telnet（远程登录）服务                         |                                                              |
  | 25端口       | 25端口为SMTP（Simple Mail Transfer Protocol，简单邮件传输协议）服务器所开放， |                                                              |
  | 31           | MSG  Authentication                                          |                                                              |
  | 42           | WINS Replication WINS复制                                    |                                                              |
  | 53端口       | 53端口为DNS（Domain Name Server，域名服务器）服务器所开放，主要用于域名解析，DNS服务在NT系统中使用的最为广泛。 |                                                              |
  | 67、68端口   | 67、68端口分别是为Bootp服务的Bootstrap Protocol Server（引导程序协议服务端）和Bootstrap Protocol Client（引导程序协议客户端）开放的端口。DHCP | 通过DSL和Cable modem的防火墙常会看见大量发送到广播地址255.255.255.255的数据。这些机器在向DHCP服务器请求一个地址。HACKER常进入它们，分配一个地址把自己作为局部路由器而发起大量中间人（man-in-middle）攻击。客户端向68端口广播请求配置，服务器向67端口广播回应请求。这种回应使用广播是因为客户端还不知道可以发送的IP地址。 |
  | 69端口       | TFTP服务，（小型文件传输协议）                               | 许多服务器与bootp一起提供这项服务，便于从系统下载启动代码。但是它们常常由于错误配置而使入侵者能从系统中窃取任何 文件。它们也可用于系统写入文件。 |
  | 79端口       | 79端口是为Finger服务开放的，主要用于查询远程主机在线用户、操作系统类型以及是否缓冲区溢出等用户的详细信息。 | 入侵者用于获得用户信息，查询操作系统，探测已知的缓冲区溢出错误，回应从自己机器到其他机器Finger扫描。 |
  | 80端口       | 80端口是为HTTP（HyperText Transport Protocol，超文本传输协议） |                                                              |
  | 88           | Kerberos krb5。另外TCP的88端口也是这个用途。                 |                                                              |
  | 99端口       | 99端口是用于一个名为“Metagram Relay”（亚对策延时）的服务，该服务比较少见，一般是用不到的。 | 后门程序ncx99开放此端口。                                    |
  | 109、110端口 | 109端口是为POP2（Post Office Protocol Version 2，邮局协议2）服务开放的，110端口是为POP3（邮件协议3）服务开放的 | POP3服务器开放此端口，用于接收邮件，客户端访问服务器端的邮件服务。POP3服务有许多公认的弱点。关于用户名和密码交 换缓冲区溢出的弱点至少有20个，这意味着入侵者可以在真正登陆前进入系统。成功登陆后还有其他缓冲区溢出错误。 |
  | 111端口      | 111端口是SUN公司的RPC（Remote Procedure Call，远程过程调用）服务所开放的端口，主要用于分布式系统中不同计算机的内部进程通信，RPC在多种网络服务中都是很重要的组件。 | 常见RPC服务有rpc.mountd、NFS、rpc.statd、rpc.csmd、rpc.ttybd、amd等 |
  | 113端口      | 113端口主要用于Windows的“Authentication Service”（验证服务）。 |                                                              |
  | 119端口      | 119端口是为“Network News Transfer Protocol”（网络新闻组传输协议，简称NNTP）开放的。 |                                                              |
  | 135端口      | 135端口主要用于使用RPC（Remote Procedure Call，远程过程调用）协议并提供DCOM（分布式组件对象模型）服务，通过RPC可以保证在一台计算机上运行的程序可以顺利地执行远程计算机上的代码；使用DCOM可以通过网络直接进行通信，能够跨包括HTTP协议在内的多种网络传输。 |                                                              |
  | 137.138端口  | 137、138是UDP端口，当通过网上邻居传输文件时用这个端口。137端口主要用于“NetBIOS Name Service”（NetBIOS名称服务），属于UDP端口， | 使用者只需要向局域网或互联网上的某台计算机的137端口发送一个请求，就可以获取该计算机的名称、注册用户名，以及是否安装主域控制器、IIS是否正在运行等信息。<br />爆破：弱口令（爆破工具采用hydra）hydra -l username -P |
  | 139端口      | Samba服务。在Windows中要在局域网中进行文件的共享，必须使用该服务。 |                                                              |
  | 143端口      | 143端口主要是用于“Internet Message Access Protocol”v2（Internet消息访问协议，简称IMAP）。 | 和POP3的安全问题一样，许多IMAP服务器存在有缓冲区溢出漏洞。记住：一种LINUX蠕虫（admv0rm）会通过这个端口繁殖，因此许多这个端口的扫描来自不知情的已经被感染的用户。 |
  | 161端口      | 161端口是用于“Simple Network Management Protocol”（简单网络管理协议，简称SNMP）。 | SNMP允许远程管理设备。所有配置和运行信息的储存在数据库中，通过SNMP可获得这些信息。许多管理员的错误配置将被暴露在Internet。Cackers将试图使用默认的密码public、private访问系统。 |
  | 162          | SNMP Trap（SNMP陷阱）                                        |                                                              |
  | 177          | X Display Manager Control Protocol                           | 说明：许多入侵者通过它访问X-windows操作台，它同时需要打开6000端口。 |
  | 389          | LDAP、ILS                                                    | 说明：轻型目录访问协议和NetMeeting Internet Locator Server共用这一端口/爆破/盲注 |
  | 443端口      | 443端口即网页浏览端口，主要是用于HTTPS服务，是提供加密和通过安全端口传输的另一种HTTP。 |                                                              |
  | 445          | Common Internet File System(CIFS)（公共Internet文件系统）    |                                                              |
  | 464          | Kerberos kpasswd(v5)。另外TCP的464端口也是这个用途。         |                                                              |
  | 500          | Internet Key Exchange(IKE)（Internet密钥交换）               |                                                              |
  | 512/513/514  | linux r                                                      |                                                              |
  | 553          | CORBA IIOP （UDP）                                           | 使用cable modem、DSL或VLAN将会看到这个端口的广播。CORBA是一种面向对象的RPC系统。入侵者可以利用这些信息进入系统。 |
  | 554端口      | 554端口默认情况下用于“Real Time Streaming Protocol”（实时流协议，简称RTSP）。 |                                                              |
  | 636          | LDAP (带SSL的ldap）                                          | 389，一个是636，前者是普通连接，后者是[SSL](https://so.csdn.net/so/search?q=SSL&spm=1001.2101.3001.7020)，不同的连接能做的操作是不同的 |
  | 873          | **Rsync服务**                                                |                                                              |
  | 993          | 带SSL的IMAP                                                  |                                                              |
  | 1024端口     | 1024端口一般不固定分配给某个服务，在英文中的解释是“Reserved”（保留）。 | 它是动态端口的开始，许多程序并不在乎用哪个端口连接网络，它们请求系统为它们分配下一个闲置端口。基于这一点分配从端口1024开始。这就是说第一个向系统发出请求的会分配到1024端口。你可以重启机器，打开Telnet，再打开一个窗口运行natstat -a 将会看到Telnet被分配1024端口。还有SQL session也用此端口和5000端口。 |
  | 1080端口     | 1080端口是Socks代理服务使用的端口，大家平时上网使用的WWW服务使用的是HTTP协议的代理服务。（socket代理） | 这一协议以通道方式穿过防火墙，允许防火墙后面的人通过一个IP地址访问INTERNET。理论上它应该只允许内部的通信向外到达INTERNET。但是由于错误的配置，它会允许位于防火墙外部的攻击穿过防火墙。 |
  | 1090/1099    | java的RMI服务                                                |                                                              |
  | 1433         | MSSQL，Microsoft的SQL服务开放的端口。                        |                                                              |
  | 1521         | oracle                                                       |                                                              |
  | 1755端口     | 1755端口默认情况下用于“Microsoft Media Server”（微软媒体服务器，简称MMS）。 |                                                              |
  | 1801，3527   | Microsoft Message Queue Server(Microsoft消息队列服务器)。还有TCP的135、1801、2101、2103、2105也是同样的用途。 |                                                              |
  | 2049         | NFS程序常运行于这个端口。通常需要访问Portmapper查询这个服务运行于哪个端口。 | 未授权访问：未限制IP以及用户权限设置错误                     |
  | 2181         | **Zookeeper服务**                                            |                                                              |
  | 2500         | RPC client using a fixed port session replication            | 应用固定端口会话复制的RPC客户                                |
  | 3389         | windows上进行远程连接的端口                                  |                                                              |
  | 4000端口     | QQ客户端端口，再细说就是为QQ客户端开放的端口，QQ服务端使用的端口是8000。 |                                                              |
  | 5554端口     | 针对微软lsass服务的新蠕虫病毒——震荡波（Worm.Sasser），该病毒可以利用TCP 5554端口开启一个FTP服务，主要被用于病毒的传播。 |                                                              |
  | 5632端口     | PyAnywhere服务：一款远控工具，有点类似vnc的功能；这个服务在以前很多黑客发的视频里面都有，利用pcanywhere来进行提权； |                                                              |
  | 7001         | WebLogic                                                     |                                                              |
  | 8000         | OICQ QQ服务端端口                                            |                                                              |
  | 8069         | **Zabbix服务**                                               |                                                              |
  | 8080端口     | 8080端口同80端口，常用WWW代理端口                            | **Apache/Tomcat/Nginx/Axis2**                                |
  | 9200/9300    | **elasticsearch服务**                                        |                                                              |
  |              |                                                              |                                                              |

### 二、常见web服务及端口

- 常见web服务及端口

  | 服务                          | 常用端口                                                     |      |
  | ----------------------------- | ------------------------------------------------------------ | ---- |
  | **IIS服务**                   | 80/81/443                                                    |      |
  | **Apache/Tomcat/Nginx/Axis2** | 80/8080                                                      |      |
  | **WebLogic**                  | 7001                                                         |      |
  | **Jboss**                     | 默认端口8080；其他端口1098/1099/4444/4445/8080/8009/8083/8093 |      |
  | **Websphere**                 | 默认端口：908*；第一个应用就是9080，第二个就是9081；控制台9090 |      |
  | **GlassFish**                 | 默认端口：http 8080；IIOP 3700；控制台4848                   |      |
  | **Jenkins**                   | 默认端口：8080、8089                                         |      |
  | **Resin**                     | 8080                                                         |      |
  | **Jetty**                     | 8080                                                         |      |
  | **Lotus**                     | 默认端口：1352                                               |      |

### 三、常见数据库服务及端口

- 常见数据库服务及端口

  | 服务                 | 常用端口                                                     |      |
  | -------------------- | ------------------------------------------------------------ | ---- |
  | **MySQL数据库**      | 默认端口：3306                                               |      |
  | **MSSQL数据库**      | 默认端口：1433（Server 数据库服务）、1434（Monitor 数据库监控） |      |
  | **Oracle数据库**     | 默认端口：1521（数据库端口）、1158（Oracle EMCTL端口）、8080（Oracle XDB数据库）、210（Oracle XDB FTP服务） |      |
  | **PostgreSQL数据库** | 默认端口：5432                                               |      |
  | **MongoDB数据库**    | 默认端口：27017                                              |      |
  | Redis数据库          | 默认端口：6379                                               |      |
  | **SysBase数据库**    | 默认端口：服务端口5000；监听端口4100；备份端口：4200         |      |
  | **DB2数据库**        | 默认端口：5000                                               |      |

### 四、web应用细分内容

- web应用细分内容

  - 开发框架

    **Java**

    Spring框架+Spring Boot

    Shiro

    Log4j 

    Struts

    **Python**

    Django

    Flask

    Tornado

    **C/C++**

    

    **PHP**

    ThinkPHP

    laravel

    fastadmin

    CakePHP

    **Ruby**

    rails

    **JavaScript**

    Node.js

    Express.js

    **Golang**

    Fiber

    

  - 中间件

  1. **消息中间件**：RabbitMQ、ActiveMQ、Kafka、RocketMQ
  2. **分布式事务中间件**：Seata。
  3. **分布式数据库中间件**：MyCat。
  4. **服务器中间件**（容器）： IIS、Apache、Nginx、Tomcat、jboss、weblogic、websphere

