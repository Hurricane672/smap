# -*- coding: utf-8 -*-
from urllib.parse import quote
import re
import requests
from random import randint
import json
 
 
# 获取网页内容
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
def Search(Keywords):
    Keywords=quote(Keywords)
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
            if flag==0 and content[4]=='"无CVE"':
                continue
            
            Vulnerability=' '.join((content[4],content[1],content[3]))
            print(Vulnerability)
            contents.append(Vulnerability)
        page+=1
    # print(json.dumps(contents))
        #返回的是json字符串，用loads恢复为list
    return contents
 
if __name__ == "__main__":
    result=Search(Keywords='Apache tomcat ')
    # print(json.loads(result))