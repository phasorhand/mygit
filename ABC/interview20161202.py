
# 要求：重难点
# 字符串 取两个list相同部分
seq1 = 'scem'
seq2 = 'scpm'
res = []
fro x in seq1:
	if x in seq2:
		res.append(x)
print res
# 时间和日期
time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time.time()))

# 进程 线程 协程
# 垃圾回收

# 核心编程
# 数据类型
	'''
3 Python基础
	3.5 内存管理（变量无需事先声明：变量无需指定类型、程序员不用关心内存管理、变量名会被“回收”、del语句能够直接释放资源。
		变量定义：变量在第一次被赋值时自动声明
		动态类型：变量名无需事先声明，也无需类型声明，对象的类型和内存占用都在运行时确定
		内存分配：Python解释器去做
		引用计数：减少引用计数，del语句
		垃圾收集：垃圾收集器（引用计数器+循环垃圾收集器-分配总量很大或未通过引用计数销毁的对象），解释器暂停，试图清理所有未引用的对象
		注意：使用局部变量替换模块变量（减少对模块的访问）

4 Python对象
	Python对象都有
		身份(只读，唯一，id（））、
		 id一致，值不一定一致，反之则否
		类型（只读，type())
		值（mutability）
		一部分有属性、值或相关联的可执行代码（如method)
		数据属性 b1p57 ?
	标准类型
		数字（ 
		字符串 String
		列表 List
		元组 Tuple
		字典 Dictionary
	其他内建类型
	内部类型
	标准类型操作符
		对象值比较 < > <= >= == != <> (字符串按字符序列值比较)
		对象身份比较 is  is not（先将变量名看做对象的链接） 注意：缓存整形范围
		布尔类型 not and or
	标准类型内建函数
		cmp (返回整形i<0, >0, ==0)
		rerp(obj)|'obj' (返回对象字符串表示 两个的内在相同)
		str(obj) (返回对象可读性好的字符串表示)
		type(obj) (得到一个对象的类型，并返回相应的type对象)
		注意：Python不支持方法或函数重载
	4.7类型工厂函数
		int(), long(), float(), complex()
		str(), unicode(), basestring()
		list(), tuple()
		type()

		dict(); bool(); set(), frozenset(); object(); classmethod(); staticmethod(); super(); property(); file()
	4.8 标准类型分类
		存储模型
			原子存：数值， 字符串，注意：字符串是原子存储，因为Python没有字符类型
			容量存储；列表， 元组， 字典
		更新模型
			可变类型： 列表， 字典
			不可变类型： 数字、字符串、元组
		访问模型
			直接访问 数字
			顺序访问 字符串，列表，元组
			映射访问 字典 
		数字   标量 不可更改 直接访问
		字符串 标量 不可更改 顺序访问
		列表   容量 可更改   顺序访问
		元组   容量 不可更改 顺序访问
		字典   容量 可更改   映射访问
	4.9 不支持的类
		char/byte -- 长度为1的字符串
		指针 -- id() 注意：只是相似
		int/short/long -- 整形与长整形自动转换
		float double -- 双浮点， Decimals（任意精度，但得导入）
5 数字
6 序列：字符串、列表、元组
	6.1序列（相同的访问模式）
		标准类型操作符
		序列类型操作符
			成员关系 in、not in
			连接 +
			重复 *
			切片 [], [:], [: :]
			步长操作符 s[::-1];s[::2]
			切片索引更多内容
				'''
				s = 'abcde'
				i = -1
				for i in range(-1, -len(s), -1)
					print s[:i]

				abcd
				abc 
				ab 
				a 

				for i in None + range()
				'''
		内建函数（BIF）
			类型转换 list(iter), str(obj), unicode(obj), basestring(), tuple(iter)
			可操作 
				enumerate(iter)>>index+item的元组
				len(seq)
				max(iter,key=None) or max(arg0,arg1...,key=None) 注意：key必须是一个可以传给sort()犯法的，用于比较的回调函数？
				min(iter,key=None) or max(arg0,arg1...,key=None) 注意：key必须是一个可以传给sort()犯法的，用于比较的回调函数？
				reversed(seq)>>返回一个以逆序访问的迭代器
				sorted(iter,func=None,key=None,reverse=False)>>返回一个有序列表
				sum(seq,init=00)>>返回seq和可选参数init的综合，效果等同用于reduce（operator.add,seq,init)
				zip([it0,it1,...itN])>>返回一个列表，其第一个元素是it0、it1..这些元素的第一个元素组成一个元组，第二个...一次类推？？
	6.2 字符串（不可变：改变需要新建一个字符串 basestring>str & unicode)
		字符串创建和赋值
		访问字符串里的值
		改变字符串 1p108
		删除字符串（赋空或del）
	6.3 字符串和操作符
		标准类型操作符（比较：ASCII值大小）
		序列操作符切片
			成员操作符（string模块.uppercase;.lowercase;.letters;.digits;.upper())
				标识符检查（idcheck.py)
				注意：循环里不要用重复操作作为参数，应当提前定义
			连接符
			编译时字符串连接
				'''
				f = urllib.urlopen('http://' # protocol 
					'localhost'              # hostname
					':8000'                  # port
					'/cgi-bin/friends.py'	 # file
					)
				'''
			普通字符串转化为Unicode字符串
				+ u''
				拷贝*（原字符串不变）
	6.4 只适用于字符串的操作符--6.10
	6.13 列表
		pop, empt, sort, reverse
		对一个元素或者多个元素：insert/update/remove

9 文件和输入输出
	9.2 文件内建函数open() file()
		'''
		file_object = open(file_name, access_mode='r', buffering=-1)
		# r w a + 
		# rU|Ua r+ w+ a+ rb wb ab rb+ wb+ ab+ a.
		fp = open('/etc/motd') # 读
		fp = open('test', 'w') # 写
		fp = open('data', 'r+') # 读写
		fp = open(r'c:\io.sys', 'rb') # 二进制读
		'''
	9.3 文件内建方法（输入输出文件内移动以及杂项）
		输入
			read() 
			readline() 整行包括行结束符
			readlines() 读取所有行然后把他们作为一个字符串列表返回
			file.xreadlines() 每次读取一块，for循环时可以减少对内存的占用。它和使用iter（file）效果一样 for eachLine in file; 废弃
			注意：不会自动删除行结束符

		输出
			write()
			writelines() 针对列表的操作，接受一个字符串列表作为参数，把它们写入文件，行结束符并不会被自动加入，所以调用writelines（）前给每行结尾加上行结束符
			无writeline(),因其等价于write()写入有行结束符的单行字符串
			注意：不会自动加上行结束符
		'''
		f = open('myFile', 'r')
		data = [line.strip() for line in f.readlines()]
		f.close()
		'''

		9.3.3-末尾
	9.4 文件内建属性-末尾

11 函数和函数式编程
		11.3.6 函数（与方法）装饰器？
			装饰器是在函数调用之上的修饰，这些修饰仅是当生命一个函数或者方法的时候，才会应用的额外调用
			'''
			@decorator(dec_opt_args)
			def func2Bdecorated(func_opt_args):
				pass
			'''
			灵感： 静态方法和类方法
			此外可以如函数调用一样堆叠起来

			有参数和无参数
			'''
			@deco
			def foo()： pass
			# foo = deco(foo)

			@decomaker(deco_args)
			def foo(): pass
			# 需要自己返回以函数作为参数的装饰器。or decomaker()用deco_args做了些事并返回函数对象，而改函数对象正是以foo作为其参数的装饰器
			# foo = decomaker(deco_args)(foo)

			@deco1(deco_args)
			@deco2
			def func(): pass
			# func = deco1(deco_args(deco2(func)))
			'''

			what is fucking decorator
			实现在合适的时间对何时的函数在它执行之前运行一些预备代码
			可以考虑在装饰器中置入通用的代码来降低程序复杂度，如：
				引入日志
				增加计时逻辑来检测性能
				给函数加入事务的能力
				'''
				from time ctiem, sleep

				def tsfunc(func):
					def wrappedFunc():
						print '[%s] %s() called' % (
							ctime(), func.__name__)
						return func()
					return wrappedFunc

				@tsfunc
				def foo(): pass

				foo()

				sleep(4)

				for i in range(2):
					sleep(i)
					foo()
				'''
		来源网络：http://python.jobbole.com/86859/
			类装饰器（如果类装饰器有参数，则__init__接收参数，而__call__接收func
			'''
			class Bold(object):
				def __init__(self, func): # 接收一个函数作为参数
					self.func = func

				def __call__(self, *arg, **kw): # 让类对象可调用
					return '<b>' + self.func(*arg, **kw) + '<b>'

			@Bold
			def hello(name):
				return 'hello %s' % name

			# hello('world') >>'<b>hello world</b>'
			'''
			副作用：名称不再是原来的名称
			'''
			from functools import wraps

			def makeitalic(func):
				@wraps(func)
				def wrapped():
					return ...
				return wrapped
			'''
			事实上，装饰器就是闭包的一种应用，但它比较特别，接收被装饰函数为参数，并返回一个函数，赋给被装饰函数，闭包则没这种限制。

	11.9 递归（函数包含了对自身的调用）
		'''
		# 阶乘
		def fac(n):
			if n == 0 or n == 1: # 0!=1!=1
				return 1
			else:
				return (n*factorial(n-1)) 
		'''
	11.10 生成器（实现next() 实现协程） ?
		协同程序是可以运行的独立函数调用，可以暂停或者挂起，并从程序离开的地方继续或者重新开始
		挂起返回中间值并多次继续的协同程序被称为生成器。 返回值而非阻塞
		句法上讲，生成器是一个带有yield语句的函数，返回一个值给调用者并暂停执行，当生成器的next()方法被调用的时候，它会准确滴从离开地方继续

		简单的生成器特性
			无下一个next（）时抛出stop异常
			'''
			def simpleGen():
				yield 1
				yield '2 -->punch!'
			# myG = simpleGen(); myG.next(); myG.next(); myG.next()
			'''

			使用： 当你正迭代穿越一个巨大的数据集合，而重复迭代这个数据集合石一个很麻烦的事情，就记住位置
		加强的生成器特性
			接收一个进入的对象
			'''
			def counter(start_at=0)；
				count = start_at = start_at
				while True:
					val = (yield count) if val is not None:
						count = val
					else:
						count += 1
			# 终止需调用close()方法
			# count = counter(5); count.next(); count.next(); count.send(9); count.next(); count.close(); count.next()
			'''
			意犹未尽？？

13 面向对象编程
	13.8 静态方法和类方法？

	廖 
		访问限制
			在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问
			相应可增加get方法来供获取私有变量，set方法来供修改私有变量

			在Python中，变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，特殊变量是可以直接访问的，不是private变量，所以，不能用__name__、__score__这样的变量名。

			有些时候，你会看到以一个下划线开头的实例变量名，比如_name，这样的实例变量外部是可以访问的，但是，按照约定俗成的规定，当你看到这样的变量时，意思就是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”。

			双下划线开头的实例变量是不是一定不能从外部访问呢？其实也不是。不能直接访问__name是因为Python解释器对外把__name变量改成了_Student__name，所以，仍然可以通过_Student__name来访问__name变量：
			表面上看，外部代码“成功”地设置了__name变量，但实际上这个__name变量和class内部的__name变量不是一个变量！内部的__name变量已经被Python解释器自动改成了_Student__name，而外部代码给bart新增了一个__name变量。？
		继承和多态
			“开闭”原则：

				对扩展开放：允许新增Animal子类；

				对修改封闭：不需要修改依赖Animal类型的run_twice()等函数。
			继承可以把父类的所有功能都直接拿过来，这样就不必重零做起，子类只需要新增自己特有的方法，也可以把父类不适合的方法覆盖重写。

			动态语言的鸭子类型特点决定了继承不像静态语言那样是必须的。？
		获取对象的属性和方法
			type()
			isinstance()
			dir()
			def readImage(fp):
			    if hasattr(fp, 'read'):
			        return readData(fp)
			    return None

			假设我们希望从文件流fp中读取图像，我们首先要判断该fp对象是否存在read方法，如果存在，则该对象是一个流，如果不存在，则无法读取。hasattr()就派上了用场。

			请注意，在Python这类动态语言中，根据鸭子类型，有read()方法，不代表该fp对象就是一个文件流，它也可能是网络流，也可能是内存中的一个字节流，但只要read()方法返回的是有效的图像数据，就不影响读取图像的功能。?
		__slots__ = ('name', 'age') 限制属性添加
		@property 把一个方法变成属性:@property @score.setter
		'''
			class Student(object):

			    @property
			    def score(self):
			        return self._score

			    @score.setter
			    def score(self, value):
			        if not isinstance(value, int):
			            raise ValueError('score must be an integer!')
			        if value < 0 or value > 100:
			            raise ValueError('score must between 0 ~ 100!')
			        self._score = value

		'''
		多重继承
		定制类__str__ __iter__ __getitem__
				__getattr__ ? __call__
		拒绝变量：枚举类型定义一个class类型，然后，每个常量都是class的一个唯一实例。Python提供了Enum类来实现这个功
			@unique 判断是否有重复
			Enum可以把一组相关常量定义在一个class中，且class不可变，而且成员可以直接比较。
		metaclass允许你创建类或者修改类。换句话说，你可以把类看成是metaclass创建出来的“实例”。
				metaclass是Python中非常具有魔术性的对象，它可以改变类创建时的行为。这种强大的功能使用起来务必小心。
18 多线程编程 + 协程
	18.1 并行处理可大幅度提升整个任务的效率
	18.2 线程和进程
		进程是程序的一次执行，每个都有自己的
		命名空间，内存，数据栈以及其他记录其运行轨迹的辅助数据。操作系统管理在其上运行的所有进程，并为这些进程公平地
		分配时间。进程也可以通过fork和spawn操作来完成其他的任务。
		不过各个进程有自己的内存空间数据栈等，所以只能够使用进程间通讯（IPC),而不能直接共享信息

		线程跟进程相似，不同：所有线程运行在同一个进程中，共享相同的运行环境（可以
		想象成主线程中并行运行的迷你线程
		线程有开始、循序执行、结束三部分，它有一个自己的指令指针，记录自己运行到了
		哪里，它的运行可能被抢占（中断）或暂时挂起（睡眠）让其他线程运行（让步），一
		个进程中各个线程之间共享一片数据空间，比进程之间更方便地共享数据以及相互通讯，
		线程一般并发执行，它们的并行和数据共享机制使得多任务的合作变得可能。单cpu中真
		正的并发是不可能的，在进程中的整个运行过程中，每个线程都只做自己的事情，在需要
		的时候跟其他的线程共享运行的结果。
		静态条件（race condition） 由于数据访问的顺序不一样
		阻塞 cpu的时间分配有所倾斜
	18.3 Python、线程、全局解释锁
		网络：http://blog.sina.com.cn/s/blog_9f488855010198vn.html
		    join：如在一个线程B中调用threada.join()，则threada结束后，线程B才会接着threada.join()往后运行。
		    setDaemon：主线程A启动了子线程B，调用b.setDaemaon(True)，则主线程结束时，会把子线程B也杀死，与C/C++中得默认效果是一样的。
		网络： http://python.jobbole.com/86909/ ？
		全局解释锁GIL：保证同一时刻只有一个线程在运行
			设置GIL
			切换到一个线程运行
			运行
				指定数量的字节码指令，或者
				线程主动让出控制（可以调用time.sleep())
			把线程设置为睡眠状态
			解锁GIL
			再次重复以上所有步骤
			
			IO密集型的Python程序比计算密集型的程序更充分利用多线程环境的好处（等待IO的时候会释放锁供其他线程使用）
		退出线程
			thread.exit()/sys.exit()/SystemExit异常
			threading相对thread能确保所有重要子线程退出后结束进程
			主线程应该是一个很好的管理者
		使用线程
		没有线程支持的情况
	threading模块（相对thread有更多的同步原语）
	18.4 thread模块
	18.5 threading模块（守护线程-不重要的线程setDaemon())
		threading模块对象
			Thread 一个线程的执行对象
			Lock 锁原语对象
			Rlock 可重入锁对象。使单线程可以再次获得已经获得了的锁（递归锁定）
			Condition 条件变量对象能让一个线程停下来，等待其他线程满足了某个条件
			Event 通用的条件变量，多个事件可以等待某个事件的发生，在事件发生后，所有线程都会被激活
			Semaphore 为等待锁的线程提供一个类似“等候室”的结构
			BoundedSemaphore 它相对上面不允许超过初始值
			Timer 与Thread相似，只是，它要等待一段时间后才开始工作
		Thread类 ？
			函数：
				start() 开启线程的执行
				run() 定义线程的功能的函数（一般会被子类重写）
				join(timeout=None) 程序挂起，知道线程结束：如果给了timeout， 则最多阻塞timeout秒
				getName() 返回线程名字
				setName(name) 设置线程名字
				isAlive() 布尔标志，表示这个线程是否还在运行中
				isDaemon() 返回线程的daemon标志
				setDaemon(daemonic) 把线程的daemon设置为daemonic（在start()之前调用）

			创建一个Thread实例，传给它一个函数
			创建一个Thread实例，传给它一个可调用的类对象
			从Thread派生出一个子类，创建一个这个子类的实例
		菲波那切数列，阶乘，累加和
			'''
			# !/usr/bin/env python

			from myThread import MyThread 
			from time import ctime, sleep

			def fib(x);
				sleep(0.005)
				if x < 2:
					return 1
			return (fib(x-2) + fib(x-1))

			def fac(x):
				sleep(0.1)
				if x < 2:
					return 1
			return (x * fac(x-1))

			def sum(x):
				sleep(0.1)
				if x < 2:
					return 1
			return (x + sum(x-1))

			funcs = [fib, fac, sum]
			n = 12

			def main()：
				nfuncs = range(len(funcs))

				print '*** SINGLE THREAD'
				for i in nfuncs:
					print 'starting', funcs[i],__name__, 'at:', \
					ctime()
					print funcs[i](n)
					print funcs[i].__name__, 'finished at:', \
					ctime()

			print '\n*** MULTIPLE THREADS'
			threads = []
			for i in nfuncs:
				t = MyThread(func[i], (n,),
					funcs[i].__name__)
				threads.append(t)

			for i in nfuncs:
				threads[i].start()

			for i in nfunce:
				threads[i].join()
				print threads[i].getResult()

			print 'all DONE'

			if __name__ == '__main__':
				main()
				'''
		threading模块中的其他函数
			activeCount() 当前活动线程对象的数量
			currentThread() 返回当前线程对象
			enumerate() 返回当前活动线程列表
			settrace(func) 为所有线程设置一个跟踪函数
			setprofile(func) 为所有线程设置一个profile函数
		生产者-消费者问题和Queue模块
			Queue模块函数
				queue(size) 创建一个大小为size的Queue对象
			Queue对象函数
				qsize() 返回队列的大小（近似值因返回时可能被其他线程修改）
				empty() 如果队列为空返回True
				full() 如果队列已满返回True
				put(item, block=0) 把item放到队列中，block不为0函数会一直阻塞到队列中有空间为止
				get(block=0) 从队列中取一个对象，block不为0函数会一直阻塞到队列中有函数为止

			Queue可以用来进行线程间通讯，让各个线程之间共享数据
				'''
				#!/usr/bin/env python

				from random import randint
				from time import sleep
				from Queue import Queue
				from myThread import MyThread

				def writeQ(queue):
					print 'prducing object for Q ...'
					queue.put('xxx', 1)
					print 'size now:', queue.qsize()

				def readQ(queue):
					val = queue.get(1)
					print 'consumed object from Q... size now', \
						queue.qsize()

				def writer(queue, loops)
					for i in range(loops):
						writeQ(queue)
						sleep(randint(1, 3))

				def read(queue, loops):
					for i in range(loops):
						readQ(queue)
						sleep(randint(2, 5))

				funcs = [writer, reader]
				nfuncs = range(len(funcs))

				def main():
					nloops = randint(2, 5)
					q = Queue(32)

					threads = []
					for i in nfuncs:
						t = MyThread(funcs[i], (q, nloops),
							funcs[i].__name__)
						threads.append(t)

					for i in nfuncs:
						threads[i].start()

					for i in nfuncs:
						threads[i].join()

					print 'all DONE'

				if __main__ == '__main__':
					main()
					'''
			一个要完成多任务的程序，可以考虑每个任务使用一个线程
			但是Python解释器是单线程的
	18.6 相关模块
		thread 基本的，底级别的线程模块
		threading 高级别的线程和同步对象
		Queue 供多线程使用的同步先进先出（FIFO）队列
		mutex 互斥对象
		SocketServer 具有线程控制的TCP和UDP管理器
	18.7 廖 协程
	18.8 应用
		Supervisord
		runit

	'''


集合
  
简历及编码能力一步步深入


http


业务：

爬虫
类
网络编程
sql
正则表达式



考点：
python二分查找、二叉树层序遍历
消息对接为queue add和delete方法
多并发、异步处理、协程

算法题
二分树层序遍历 快排 装饰器 静态与动态的区别
循环引用
'''