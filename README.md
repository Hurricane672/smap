# smap接口文档

## 一、多主机总体扫描部分

### 1、ip地址接口 hostScanner

**In**：

    内容描述：ip网段
    
    举例说明：(start_ip, end_ip)
    形如 (192.168.1.1, 192.168.2.128)
    
    数据类型：字符串

**Out：**

    内容描述：该网段中存活的ip地址列表
    
    举例说明：{"ip1":["hostname", "mac_address", "vendor","delay"], "ip2":["hostname", "mac_address", "vendor", "delay"], ...}
    
    数据类型：字典dict{key1: list1, key2: list2}其中value为列表


### 2、端口扫描接口 portScanner

**In**：

    内容描述：ip地址
    
    举例说明：形如 192.168.1.1
    
    数据类型：字符串

**Out：**

    内容描述：该ip中存活的端口列表
    
    举例说明：[port1,port2,port3,port4......]
    
    数据类型：list(int)

## 二、拓扑图生成部分

### 1、拓扑链路生成 routeGetter

**In**：

    内容描述：存活ip列表列表
    
    举例说明：形如，[ip2,ip3,ipn...]
    
    数据类型：list(str)

**Out：**

    内容描述：ip链路列表列表
    
    举例说明：形如，[[ip2,ip3,ipn...ip1],[ip5,ip3,ipn...ip2],[...ip3],[...ip4]...]，简单的说，就是从扫描机出发，经过ip2、ip3、ipn和等等，可以联通到ip1；从扫描机出发，经过。。。，可以到达ip2；以此类推
    
    数据类型：list(list(str))

### 1改、拓扑链路生成 routeGetter

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



### 2、拓扑图绘制  topoDrawer

**In**：

    内容描述：ip链路列表列表
    
    举例说明：形如，[[ip2,ip3,ipn...ip1],[ip5,ip3,ipn...ip2],[...ip3],[...ip4]...]，简单的说，就是从扫描机出发，经过ip2、ip3、ipn和等等，可以联通到ip1；从扫描机出发，经过。。。，可以到达ip2；以此类推
    
    数据类型：list(list(str))

**Out：**

    内容描述：生成的拓扑图图片
    
    举例说明：a.png
    
    数据类型：能实现输出文件到对应目录即可



## 三、单套接字扫描部分 appScanner

**In**：

    内容描述：ip加端口
    
    举例说明：['192.169.0.1',22]
    
    数据类型：list ,第一个元素为str，第二个元素为int

**Out：**

    内容描述：涉及到的应用服务和版本
    
    举例说明：{"service":"", "version":""}
    
    数据类型：dict{str,str}，注意，英文名称和版本号之间使用空格隔开！



## 四、web应用扫描部分 webScanner

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



## 五、漏洞查询部分 vulFinder

**In**：

    内容描述：应用名称等相关信息（支持中文）
    
    举例说明：形如 ‘apache  远程代码执行‘  ’apache log4j‘
    
    数据类型：字符串

**Out：**

    内容描述：可能存在的漏洞名称列表 !如果能查询到日期会给出日期，如果没有则为空，一个字符串为一个列表元素
    
    举例说明：['"CVE-2022-34305" Apache Tomcat 跨站脚本漏洞（CVE-2022-34305） 2022-06-24 , "无CVE" Apache Tomcat拒绝服务漏洞（CNVD-2012-7096）']
    
    数据类型：list[str]



# 前后端接口设计文档

In表示前端向后端请求，out表示

## 一、拓扑图接口 topoList

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



## 二、单ip查询接口

- 主机基本物理信息
- 主机端口列表 --> 对应的服务列表
- web服务列表



### 1、基本物理信息 basicInform

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



### 2、端口对应的服务信息 appInform

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

### 3、web应用信息 webInform

```
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
```



## 三、关键字查询接口 findVul

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

