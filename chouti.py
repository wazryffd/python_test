'''
登录抽屉并且实现点赞
由于抽屉比较特殊实现步骤为：
1、抓取首次GET访问主页返回的cookies；
2、POST访问登录页，需要带上步骤1的cookies，进行授权；
3、后续点赞等登录后操作，只需要带上步骤1的cookies，步骤2返回的cookies没用；
注：不表示所有都需要这样操作；
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
#get访问主页
rsp1 = requests.get(url = 'https://dig.chouti.com/', headers = headers)
#抓取返回的cookies对象，通过get_dict()获取cookies字典
cook_1 = rsp1.cookies.get_dict()
#POST访问登录页，发送数据并带上第一次返回的coodies
rsp2 = requests.post(url = login, headers = headers, data = login_dic, cookies = cook_1)
#POST发送点赞请求
vote = requests.post(url = 'https://dig.chouti.com/link/vote?linksId=23851466', headers = headers, cookies = {'gpsd': cook_1['gpsd']})
#打印返回数据
print(vote.text)
