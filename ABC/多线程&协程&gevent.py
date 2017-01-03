
# coding: utf-8

# # Python中的异步IO和协程（Coroutine），并应用在爬虫中

# # 协程，what&how

# 解决IO密集型任务（打开多个网站）：多线程多进程。但是一台电脑中的线程数、进程数是
# 有限的，而且切换也比较浪费时间，所以就出现了"协程"。
# 协程允许一个执行过程A终端，然后转到B执行过程，在适当的时候再转回来，有点类似多线程
# 协程优势：
#     协程的数量理论上可以是无限个，而且没有线程之间的切换动作，执行效率比线程高。
#     协程不需要“锁”机制，即不需要lock和release过程，因为所有的协程都在一个线程中。
#     相对于线程，协程更容易调试debug，因为所有的代码都是顺序执行的。

# # Python中的一部IO和协程

# Python中的协程是通过“生成器（generator)”的概念实现的。

# In[3]:

def consumer():
    print("[Consumer] INit Consumer ...")
    r = "init ok"
    while True:
        n = yield r
        print("[Consumer] conusme n = %s, r = %s" % (n, r))
        r = "consume %s OK" % n

def produce(c):
    print("[Producer] Init Producer ...")
    r = c.send(None)
    print("{Producer} Start Consumer, return %s" % r)
    n = 0
    while n < 5:
        n += 1
        print("[Producer] While, Producing %s ..." % n)
        r = c.send(n)
        print("[Producer] Consumer return: %s" % r)
    c.close()
    print("[Producer] Close Producerr ...")

produce(consumer())              
            


# 异步IO，在Python3.4中可以使用asyncio标准库。该标准库支持一个时间循环模型（EventLoop），
# 我们声明写成功，然后将其加入到EventLOOP中，即可实现异步IO

# In[9]:

# 一部IO例子： 适配Python3.4， 使用asyncio库
@asyncio.coroutine
def hello(index): # 通过装饰器asyncio.coroutine定义协程
    print("hello world! index= %s, thread= %s" % (index, threading.currendThread())
    yield from asyncio.sleep(1) # 模拟IO任务
    print("hello again! index= %s, thread= %s" % (index, threading.currentThread))
    
loop = asyncio.get_event_loop() #得到一个事件循环模型
tasks = [hello(1), hello(2)] # 初始化任务列表
loop.run_until_complete(asyncio.wait(tasks)) # 执行任务
loop.close() # 关闭事件循环列表


# # Python3.5中引入了关于异步IO的新语法：async和awiat关键字

# In[1]:

async def hello(index): # 将一个函数声明为协程函数，函数执行时返回一个协程对象。
    print("hello world! index= %s, thread= %s"  % (index, threading.currentThread())
    await asyncio.sleep(1) # 模拟IO任务 ，awiat将暂停协程函数的执行，等待异步IO返回结果
    print("hello agagin! index= %s, thread = %s" % (index, threading.currentThread())

loop = asyncio.get_event_loop() # 得到一个事件循环模型
tasks = [hello(1), hello(2)] # 初始化任务列表
loop.run_until_complete(asyncio.wait(tasks)) # 执行任务
loop.close() # 关闭事件循环列表


# # 爬虫中使用协程实现异步IO

# 异步IO特别适合爬虫的工作，因为爬虫所有的请求都属于IO密集型任务，想得到比较好的爬虫效率，使用协程很重要。关于http异步请求，建议使用aiohttp库，一个异步的
# http客户端/服务器框架。

# In[2]:

async def get(url)：
async with aiohttp.ClientSession() as session:
async with session.get(url) as resp:
    print(url, resp.status)
    print(url, await resp.text())
    
loop = asyncio.get_event_loop()
tasks = [
    get("http1"),
    get("http2"),
    get("http3")
]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()


# # 廖http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/0013868328689835ecd883d910145dfa8227b539725e5ed000

# In[3]:

import time

def consumer():
    r = ""
    while True:
        n = yield r # 为什么要加 "n =" 
        if not n:
            return
        print("[consumer] Consuming %s" % n)
        time.sleep(1)
        r = "200 OK"
        
def produce(c):
    c.next()
    n = 0
    while n < 5:
        n += 1
        print("[Producer] Producing %s ..." % n)
        r = c.send(n)
        print("[Producer] Consumer return %s..." % r)
    c.close()
if __name__ == "__main__":
    c = consumer()
    produce(c)


# ## gevent

# Python通过yield提供了对协程的基本支持，但不完全，而第三方gevent为Pyhton提供了比较完全的协程支持gevent是第三方库，通过greenlet实现协程：当一个grennlet遇到IO操作的时候（比如访问网络）就自动切换到其他greenlet，等到IO操作完成，再在适当的时候切换回来
# 继续执行。由于IO非常耗时，经常使程序处于等待状态，有了gevent为我们自动切换协程，就保证总有greenlet在运行，而不是等待IO。由于切换是在IO操作时自动完成，所以gevent需要修改Python自带的一些标准库，这一过程在启动时通过monkey patch完成：

# In[5]:

from gevent import monkey; monkey.patch_socket()
import gevent

def f(n):
    for i in range(n):
        print gevent.getcurrent(), i
        
g1 = gevent.spawn(f, 5)
g2 = gevent.spawn(f, 5)
g3 = gevent.spawn(f, 5)
g1.join()
g2.join()
g3.join()


# 要使gevent交替运行只需通过gevent.sleep()交出控制权

# In[6]:

from gevent import monkey; monkey.patch_socket()
import gevent

def f(n):
    for i in range(n):
        print gevent.getcurrent(), i
        gevent.sleep(0)
        
g1 = gevent.spawn(f, 5)
g2 = gevent.spawn(f, 5)
g3 = gevent.spawn(f, 5)
g1.join()
g2.join()
g3.join()


# 实际上我们不用sleep()去切换，而gevent自动切换

# In[ ]:

from gevent import monkey; monkey.patch_all()
import gevent
import urllib2

def f(url):
    print("Get: %s" % url)
    resp = urllib2.urlopen(url)
    data = resp.read()
    print("%d bytes received from %s." % (len(data), url))

gevent.joinall([
        gevent.spawn(f, "http://www.baidu.org"),
        gevent.spawn(f, "http://www.sina.com"),
        gevent.spawn(f, "http://www.github.com")
    ])


# 由于gevent是基于IO切换的协程，所以最神奇的是，我们编写的Web App代码，不需要引入gevent的包，也不需要改任何代码，仅仅在部署的时候，用一个支持gevent的WSGI服务器，立刻就获得了数倍的性能提升。具体部署方式可以参考后续“实战”-“部署Web App”一节。

# In[ ]:



