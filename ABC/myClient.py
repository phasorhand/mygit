# -*- encoding:utf-8 -*-
import socket

# 客户端
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接
s.connect(('127.0.0.1', 9999))
# s.connect(s.recv(1024).decode('utf-8'))
for data in [b'Michael', b'Tracy', b'Sarahh']:
    # 发送数据
    s.send(data)
    print s.recv(1024).decode('utf-8')
s.send(b'exit')
s.close()