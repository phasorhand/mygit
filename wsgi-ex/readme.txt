server & hello:
命令行cd到相应目录，输入python server.py即可开启服务
浏览器输入localhost:8000即可访问，输入localhost:8000/dav返回hello，dav！
命令行 ctrl+c即可关闭服务

app:
flask

web_py:
web.py框架
命令行输入：python web_py 端口号

一定要把模板放到正确的templates目录下，templates和app.py在同级目录下：
app.py
templates
	template


无论多么复杂的Web应用程序，入口都是一个WSGI处理函数。
HTTP请求的所有输入信息都可以通过environ获得，HTTP响应的输出
都可以通过start_response()加上函数返回值作为Body。

复杂的Web应用程序，光靠一个WSGI函数来处理还是太底层了，
我们需要在WSGI之上再抽象出Web框架，进一步简化Web开发。