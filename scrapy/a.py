#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Required
- requests (必须)
- pillow (可选)
Info
- author : "xchaoinfo"
- email  : "xchaoinfo@qq.com"
- date   : "2016.2.4"
Update
- name   : "wangmengcn"
- email  : "eclipse_sv@163.com"
- date   : "2016.4.21"
'''
import requests
try:
    import cookielib
except:
    import http.cookiejar as cookielib
import re
import time
import os.path
try:
    from PIL import Image
except:
    pass

'''
    伪造headers、cookie、xsrf
    输入url、data
    解决验证码
'''

# 构造 Request headers
agent = 'Mozilla/5.0 (Windows NT 5.1; rv:33.0) Gecko/20100101 Firefox/33.0'
headers = {
    "Host": "https://car.tpi.cntaiping.com:8002/index.jsp",
    "Referer": "https://car.tpi.cntaiping.com:8002/index.jsp",
    'User-Agent': agent
}

# 使用登录cookie信息
session = requests.session()
session.cookies = cookielib.LWPCookieJar(filename='cookies')
try:
    session.cookies.load(ignore_discard=True)
except:
    print("Cookie 未能加载")


def get_xsrf():
    '''_xsrf 是一个动态变化的参数'''
    index_url = 'https://car.tpi.cntaiping.com:8002/index.jsp'
    # 获取登录时需要用到的_xsrf ，跨站请求伪造
    index_page = session.get(index_url, headers=headers)
    html = index_page.text
    pattern = r'name="_xsrf" value="(.*?)"'
    # 这里的_xsrf 返回的是一个list
    _xsrf = re.findall(pattern, html)
    print 'xsrf:', _xsrf[0]
    return _xsrf[0]


# 获取验证码
def get_captcha():
    t = str(int(time.time() * 1000))
    captcha_url = 'https://www.zhihu.com/captcha.gif?r=' + t + "&type=login"
    r = session.get(captcha_url, headers=headers)
    with open('captcha.jpg', 'wb') as f:
        f.write(r.content)
        f.close()
    # 用pillow 的 Image 显示验证码
    # 如果没有安装 pillow 到源代码所在的目录去找到验证码然后手动输入
    try:
        im = Image.open('captcha.jpg')
        im.show()
        im.close()
    except:
        print(u'请到 %s 目录找到captcha.jpg 手动输入' % os.path.abspath('captcha.jpg'))
    captcha = input("please input the captcha\n>")
    return captcha


def isLogin():
    # 通过查看用户个人信息来判断是否已经登录
    url = "https://car.tpi.cntaiping.com:8003/platform/processGgUser.do?actionType=updatePasswd"
    login_code = session.get(url, headers=headers, allow_redirects=False).status_code
    if login_code == 200:
    	print '已经登陆！'
        return True
    else:
        return False


def login(secret, account):
	post_url = 'https://car.tpi.cntaiping.com:8002/index.jsp'
	postdata = {
        '_xsrf': get_xsrf(),
        'password1': secret,
        'remember_me': 'true',
        'username': account,
    }
	login_page = session.post(post_url, data=postdata, headers=headers)
	login_code = login_page.textprint(login_page.status_code)
	print(login_code)
	session.cookies.save()
# try:
#     input = raw_input
# except:
#     pass


if __name__ == '__main__':
        account = '802387'
        secret = 'Taiping1234'
        login(secret, account)


