# 接口地址处理：get请求 + 带参数 + 设置cookie
import traceback # 异常捕获
import requests
from requests.cookies import RequestsCookieJar

pageUrl = 'http://match.yuanrenxue.com'
loginUrl = 'http://match.yuanrenxue.com/api/login'
loginInfo = 'http://match.yuanrenxue.com/api/loginInfo'
apiUrl = 'http://match.yuanrenxue.com/api/match/1'
url = 'http://match.yuanrenxue.com/api/match/1?m=2cc60837000fba037b4b92673e23c332%E4%B8%A81603120616'
headers = {
    'Host': 'match.yuanrenxue.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.80 Safari/537.36',
    'Referer': 'http://match.yuanrenxue.com/match/2'
}
loginData = {
  'username': 'yaogetxu',
  'password': 'Yaogetxu123'
}
  
#开启一个session会话
# session = requests.session()

# #设置请求头信息
# session.headers = headers

# #申明一个用于存储手动cookies的字典
# manual_cookies={}

#将cookiesJar赋值给会话
# session.cookies=cookiesJar
resLogin = requests.post(loginUrl, data=loginData)
print(resLogin.cookies)

resLoginInfo = requests.get(loginInfo, cookies=resLogin.cookies)
print(resLoginInfo, resLoginInfo.text)

res = requests.get(apiUrl, cookies=resLogin.cookies)
print(resLogin.cookies)
print(res)
print(res.text.encode('utf-8').decode('unicode-escape'))
# cookie_jar = RequestsCookieJar()
# resDist = requests.utils.dict_from_cookiejar(res.cookies)
# # 放开下面的，可查看cookie 的 key/value
# print(requests.utils.cookiejar_from_dict(resDist))
# print(resDist)
# for key in resDist:
#   print(key)
# cookie_jar.set('cookie[key]', 'cookie[value]', domain='域名')
# cookie_jar.set([key for key in resDist][0], resDist[[key for key in resDist][0]], domain='match.yuanrenxue.com')

