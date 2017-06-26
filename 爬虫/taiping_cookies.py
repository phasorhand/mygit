# coding:utf8
import requests


cookies = []
is_overdue_url = r'https://car.tpi.cntaiping.com:8001//casserver/pswRemind?userCode=802437'
loginURL = r'https://car.tpi.cntaiping.com:8001/casserver/login?service=https%3A%2F%2Fcar.tpi.cntaiping.com%3A8002%2Fj_acegi_security_check'
postData = {
'macNo:':'',
'username':'802437',
'password1':'Bj123456.',
'_eventId':'submit',
'password':'93ca441fc0b7e1c79a3a031d962cbea2',
'imageField.x':'42',
'imageField.y':'8',
# 'lt':'_cC4E7154D-B41E-D0F8-30BE-A134AC18969A_kDDED7DA2-24C6-BD65-529A-F39B0D96E573',
}
headers = {
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Accept-Encoding':'gzip, deflate, br',
'Accept-Language':'zh-CN,zh;q=0.8',
'Cache-Control':'max-age=0',
'Connection':'keep-alive',
'Content-Length':'211',
'Content-Type':'application/x-www-form-urlencoded',
# 'Cookie':'JSESSIONID=_xLi9rbCmgvOBEFIBm5Rq7PL3xu9Km1-jg2ZyvsGpU02mVdZsPEb!-2116955981!338788716; chinainsuranceJSESSIONID=w2v3ZQnHPwx0pxlC6Kx0Qh2NDTYqxlKK5yTKZtcntVQNW6pw715L!1614272018; chinainsuranceVisaJSESSIONID=c1dbZQ7GTWS3VDGsZJP9xC1wQ5pN7ybqjv0p8sBw1Bdvj25ypNTK!-1450721921; chinainsuranceSimpleJSESSIONID=JRHYZQ7KcyZ9FlGcdqbC4TC77CtL2hM9jMdph9xpz8fzpNchjjpp!-1510967554'
'Host':'car.tpi.cntaiping.com:8001',
'Origin':'https://car.tpi.cntaiping.com:8001',
'Referer':'https://car.tpi.cntaiping.com:8001/casserver/login?service=https%3A%2F%2Fcar.tpi.cntaiping.com%3A8002%2Fj_acegi_security_check',
'Upgrade-Insecure-Requests':'1',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
}
session = requests.Session()
print('风雨前：', session.get(loginURL, verify=False).text)
print('密码是否过期：', session.post(is_overdue_url, verify=False).text)
print("""
	爬取前。。。。
	---------------------------------------
	爬取后。。。。
""")
r = session.post(loginURL, verify=False, data=postData, headers = headers)
print('r.text:', r.text)
# print(session.cookies.get_dict())
print('风雨后：', session.get(loginURL, verify=False).text)
