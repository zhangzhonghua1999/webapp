#服务器首先绑定端口
import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)#创建Socket时，SOCK_DGRAM指定了这个Socket的类型是UDP。
#绑定端口
s.bind(('127.0.0.1',9999))
print('Bind UDP on 9999...')
while True:
    # 接收数据:
    data, addr = s.recvfrom(1024)
    print('Received from %s:%s.' % addr)
    s.sendto(b'Hello, %s!' % data, addr)