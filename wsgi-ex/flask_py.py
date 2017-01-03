# -*- coding:utf-8 -*-

# 导入类Flask
from flask import Flask
from flask import  request

# 创建实例，如果使用单一模块第一参数应为__name__,
# 如果以单独应用启动或作为模块导入，__main__ 对于实际导入的应用
app = Flask(__name__)

# 装饰器route()告诉Flask哪个URL才能出发我们的函数。
@app.route('/', methods=['GET', 'POST'])
def home():
    return '<h1>Home</h1>'
	
@app.route('/signin', methods=['GET'])
def signin_form():
    return '''<form action="/signin" method="post">
	          <p><input name="username"></p>
			  <p><input name="password" type="password"></p>
			  <p><button type="submit">Sign In</button></p>
			  </form>
		   '''
		   
@app.route('/signin', methods=['POST'])
def signin():
    # 需要从request对象读取表单内容：
	if request.form['username']=='admin' and request.form['password']=='password':
	    return '<h3>Hello, admin!</h3>'
	return '<h3>Bad username or password.</h3>'
	
# 确保服务器只会在改脚本被Python解释器直接执行的时候才会运行，而不是作为模块导入的时候
if __name__=='__main__':
    app.run()
	
'''
http://www.pythondoc.com/flask/quickstart.html
外部可见服务器：
    调试模式下，应用中的一个用户可以执行你计算机上的任意Python代码
	关闭debug或新人所在网络上的用户，便可让服务器对外可用，改变run()
	app.run(host='0.0.0.0')
	这让操作系统去监听所有公开的ip
开启调试模式（自动重启，调试器）
    app.debug = True
	app.run()
	----------
	app.run(debug=True)
attention:
	尽管交互式调试器不能在分叉( forking )环境上工作(这使得它几乎不可能在
	生产服务器上使用)， 它依然允许执行任意代码。这使它成为一个巨大的安全
	风险，因此它 绝对不能用于生成环境。
	
路由
	变量规则
	# 字段标记
	@app.route('/user/<username>')
	def show_user_profile(username):
	    retturn 'User %s' % username
	
	# 字段转换器
	@app.route('/post/<int:post_id>'):
	    return 'Post %d' % post_id
		
	
	唯一URLs/重定向行为：
		当用户访问页面时忘记结尾斜线时，这个行为允许关联的 URL 继续工作， 
		并且与 Apache 和其它的服务器的行为一致。
		另外，URL 会保持唯一，有助于避免搜索引擎索引同一个页面两次。
	@app.route('/projects/')
	def projects():
	    return 'The project page'
		
	# 重定向到带斜线的规范URL去
	@app.route('/about')
	def about():
	    return 'The about page
		
	
	构建URL
	
	
	HTTP方法
	默认路由只会响应GET请求
	@app.route('/login', methods=['GET', 'POST'])
	def login():
	    if request.method == 'POST':
		    do_the_login()
		else:
		    show_the_login_form()
	
	HTTP 方法（通常也称为“谓词”）告诉服务器客户端想要对请求的页面
	做 什么。下面这些方法是比较常见的：

	GET
		浏览器通知服务器只获取页面上的信息并且发送回来。
	HEAD
		浏览器告诉服务器获取信息，但是只对头信息感兴趣，
		不需要整个页面的内容。 应用应该处理起来像接收到一个 GET 
		请求但是不传递实际内容。在 Flask 中你完全不需要处理它， 
		底层的 Werkzeug 库会为你处理的。
	POST
		浏览器通知服务器它要在 URL 上 提交 一些信息，服务器必须保证
		数据被存储且只存储一次。 这是 HTML 表单通常发送数据到服务器的方法。
	PUT
		同 POST 类似，但是服务器可能触发了多次存储过程，多次覆盖掉旧值。
		现在你就会问这有什么用， 有许多理由需要如此去做。
		考虑下在传输过程中连接丢失：在这种情况下浏览器 和服务器之间的系统
		可能安全地第二次接收请求，而不破坏其它东西。对于 POST 是不可能实现的，
		因为 它只会被触发一次。
	DELETE
		移除给定位置的信息。
	OPTIONS
		给客户端提供一个快速的途径来指出这个 URL 支持哪些 HTTP 方法。
		从 Flask 0.6 开始，自动实现了它。 
	
	
    接收请求数据
		上下文作用域
		局部上下文
			Flask 中的某些对象是全局对象，但不是通常的类型。这些对象实际上
			是给定上下文的局部对象的代理。
			单元测试需要用到
		
		
	请求对象
		from flask import request
		
		@app.route('/login', method=['POST', 'GET')
		def logiin():
		    error = None
			if request.method == 'POST':
			    if valid_login(request.form['username'],
				               request.form['password']):
				    return log_the_user_in(request.form['username'])
				else:
				    error = 'Invalid username/password'
					
			# the code below this is executed if the request methos
			# was GET or the credentials were invalid
			return render_template('login.html', error=error)
			
		# 可以使用args属性接受再URL（？key=value)中提交的参数：
		searchword = request.args.get('key', '')
		
		
	关于响应
		
		如果返回的是一个合法的响应对象，它会被从视图直接返回。
		如果返回的是一个字符串，响应对象会用字符串数据和默认参数创建。
		如果返回的是一个元组而且元组中元素能够提供额外的信息。这样的元组必须是 (response, status, headers) 形式且至少含有一个元素。 status 值将会覆盖状态代码，headers 可以是一个列表或额外的消息头值字典。
		如果上述条件均不满足，Flask 会假设返回值是一个合法的 WSGI 应用程序，并转换为一个请求对象。
		@app.errorhandler(404)
		def not_found(error):
		    return render_template('error.html'), 404
			
		# 用 make_response() 封装返回表达式，获取结果对象并修改，然后返回它：
		@app.errorhandler(404)
		def not_found(error):
		    # 得到响应对象
			resp = make_response(render_template('error.html'), 404)
			resp.headers['X-Something'] = 'A value'
			retrun resp
		
	重定向和错误（可定制错误页面）
		