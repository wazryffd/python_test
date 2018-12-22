import requests
from bs4 import BeautifulSoup
import uuid
import os
import string

#请求网站，返回response
rsp = requests.get(url='http://www.autohome.com.cn/news/')
#response编码
rsp.encoding = rsp.apparent_encoding
'''
rsp.text返回网站字符串
用返回的字符串通过beautisoup生成对象
'''
soup = BeautifulSoup(rsp.text,features = "html.parser")
#查找目标代码，find方法找到第一个满足条件
target = soup.find(id = 'auto-channel-lazyload-article')

li_list = target.find_all('li')
os.chdir('img')
for i in li_list:
    a = i.find('a')
    if a:
        title = a.find('h3').text
        del_word = '\/:*?"<>| '

        trantable = str.maketrans('','',del_word)
        title = title.translate(trantable)
        print(title)
        detail = 'http:' + a.attrs.get('href')
        # print(detail)
        img_url ='http:' + a.find('img').attrs.get('src')
        # print(img_url)
        img_rsp = requests.get(img_url)
        file_name = str(uuid.uuid4()) + '.jpg'
        os.mkdir(title)
        os.chdir(title)
        with open(file_name,'wb') as f:
            f.write(img_rsp.content)
        os.chdir('..')
