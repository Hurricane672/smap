# -*- coding: utf-8 -*-
from urllib.parse import quote
import re
import requests
from random import randint
 
 
# 获取网页内容
from flask import jsonify


def get_html_content(url):
    user_agent = ['Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.7113.93 Safari/537.36',
                  'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0',
                  'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4482.0 Safari/537.36 Edg/92.0.874.0']
    try:
        response = requests.get(url, headers={'User-Agent':user_agent[randint(0,1)]})
        if response.status_code == 200:
            # print(response.text)
            return response.text
        else:
            print('Response Error!')
    except Exception:
        print('NetWork Error!')
        return
 
 
# 使用正则表达式提取cve信息字段
def show_cve_content(res):
    match = re.compile(r'<tr>.*?target="_blank">(.*?)</a></td>.*?<td>(.*?)</td>.*?<button.*?>(.*?)</button>.*?nowrap="nowrap">(.*?)</td>.*?<button.*?(".?CVE.*?)>.*?</button>.*?</tr>', re.S)
    contents = re.findall(match, res)
    # print(contents)
    return contents
 
 
# 主函数
def main(Keywords):
    num=0
    similarSearch=True
    briefSearch=False
    matchware=r'([A-Z,a-z]+) *'
 
    Keyword=quote(Keywords)
    pagemax=1
    page=1
    contents=[]
    while page<=pagemax:
        url = 'https://avd.aliyun.com/search?q=' + str(Keyword)+'&page='+str(page)
        response = get_html_content(url)
        
        # print(html)
        if pagemax==1:
            match=re.compile(r'第.*?/ (.*?) 页')
            pagemax=int(re.findall(match,response)[0])

        
        for content in show_cve_content(response):
            # print(content)
            content = list(content)
            for i in range(0, len(content)):
                content[i] = content[i].strip()  # 去除字符串中的空格
            filt=re.compile(r'C+\w*-\d+-\d+',re.S)
            # print(content[4].startswith('C'))
            flag=len(re.findall(filt,content[1]))
            if flag==0 and content[4]=='"无CVE"':
                continue
            if briefSearch==True:
                if content[3]!='' and int(content[3][:4])<2019:
                    break
            Vulnerability=[content[4],content[1],content[3]]
        
            print(Vulnerability)
            num+=1
            contents.append(Vulnerability)
        page+=1
    # print(json.dumps(contents))
        #返回的是json字符串，用loads恢复为list
    if num!=0 or similarSearch==False:
        return contents
    if num>10:
        return contents
    print('开始近似搜索，耗时较多')
    softWare=re.findall(matchware,Keywords)
    version=re.findall(r'([0-9]+\.?[0-9]?\.?.*?[0-9])',Keywords)
    if len(version)>0:
        version=version[0]
    else:
        version=''
    #print((softWare[0],version))

    version=version.replace('.','\.')

    # Keywords=quote(Keywords)
    Keywords=quote(softWare[0])
    pagemax=1
    page=1
    contents=[]
    while page<=pagemax:
        url = 'https://avd.aliyun.com/search?q=' + str(Keywords)+'&page='+str(page)
        response = get_html_content(url)
        
        # print(html)
        if pagemax==1:
            match=re.compile(r'第.*?/ (.*?) 页')
            pagemax=int(re.findall(match,response)[0])

        
        for content in show_cve_content(response):
            # print(content)
            content = list(content)
            for i in range(0, len(content)):
                content[i] = content[i].strip()  # 去除字符串中的空格
            filt=re.compile(r'C+\w*-\d+-\d+',re.S)
            # print(content[4].startswith('C'))
            flag=len(re.findall(filt,content[1]))
            if flag==0 and content[4]=='"无CVE"' or content[3]=='':
                continue
            if briefSearch==True:
                if content[3]!='' and int(content[3][:4])<2019:
                    break
            if '.x' in content[1]:
                for i in range(0,10):
                    tmp=content[1].replace('.x','.%d' %i)
                    if len(re.findall(version,tmp))!=0:
                        Vulnerability=[content[4],content[1],content[3]]
                    
                        print(Vulnerability)
                        num+=1
                        contents.append(Vulnerability)
                        continue
                continue
            match=re.compile(version,re.S)
            if len(re.findall(match,content[1]))!=0:
                Vulnerability=[content[4],content[1],content[3]]
            
                print(Vulnerability)
                num+=1
                contents.append(Vulnerability)
        page+=1
        if num==0 and page==pagemax and similarSearch==True:
            version=version[0:3]
            page=1
            similarSearch=False
        if num>10:
            return contents
    # print(json.dumps(contents))
        #返回的是json字符串，用loads恢复为list
    print(contents)
    return contents
    # return json.dumps(contents)

if __name__ == "__main__":
    result=main(Keywords='jquery 1.4.2')
    # print(re.findall(r'3\.4\.1','html 34.1'))