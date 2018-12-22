'''
用session管理cookies,实现登录抽屉并点赞功能
'''

import requests
from bs4 import BeautifulSoup

home = 'https://dig.chouti.com/'
login = 'https://dig.chouti.com/login'  #登录地址
#登录需要POST的数据
login_dic = {
    'jid': 'wazryffd',
    'password': '15058318183ffd',
    'oneMonth': 1
}
#伪装请求头
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}

session = requests.session()
session.get(url = home,headers = headers)
session.post(url = login, data = login_dic,headers = headers)
vote = session.post(url = 'https://dig.chouti.com/link/vote?linksId=23851466',headers = headers)
print(vote.text)
