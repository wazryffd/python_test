'''
爬取百度翻译案例
'''
from urllib import request,parse
import json
import gzip

url = "https://fanyi.baidu.com/sug" #百度翻译请求地址
def main():
    #构建请求数据
    data = {
        'kw': kw #'kw'是百度翻译的关键词
    }
    data = parse.urlencode(data).encode('utf-8') #对关键词编码
    #访问请求头，内容通过浏览器F12抄取
    head = {
        'Content-Lenght': len(data),
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
        'Accept':'application/json, text/javascript, */*; q=0.01',
        #'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,zh-TW;q=0.8',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'fanyi.baidu.com',
        'Origin': 'https://fanyi.baidu.com',
        'Referer': 'https://fanyi.baidu.com/',
        'X-Requested-With': 'XMLHttpRequest'
    }
    #构建请求地址，请求数据，请求头后开始发送请求
    req = request.Request(url, data = data, headers= head)
    rst = request.urlopen(req)
    rst = rst.read()
    result = rst.decode('utf-8','ignore')
    #result = gzip.decompress(rst).decode("utf-8",'ignore')
    #返回的是json格式，需要利用json包载入数据进行解码
    json_result = json.loads(result)
    #print(json_result)
    #打印返回的结果
    for i in json_result['data']:
        print(i['k'] + "  --->  " + i['v'] + '\n')

if __name__ == '__main__':
    while True:
        kw = input('输入要查询的单词(退出输入ESC)：')
        if kw == "ESC":
            break
        main()
