'''
登录抽屉并且实现点赞
由于抽屉比较特殊实现步骤为：
1、抓取首次GET访问主页返回的cookies；
2、POST访问登录页，需要带上步骤1的cookies，进行授权；
3、后续点赞等登录后操作，只需要带上步骤1的cookies，步骤2返回的cookies没用；
'''
import requests
from bs4 import BeautifulSoup

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

rsp1 = requests.get(url = 'https://dig.chouti.com/', headers = headers)
cook_1 = rsp1.cookies.get_dict()

rsp2 = requests.post(url = login, headers = headers, data = login_dic, cookies = cook_1)

vote = requests.post(url = 'https://dig.chouti.com/link/vote?linksId=23851466', headers = headers, cookies = {'gpsd': cook_1.get('gpsd')})
print(vote.text)