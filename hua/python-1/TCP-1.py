#Socket是网络编程的一个抽象概念。通常我们用一个Socket表示“打开了一个网络链接”，
#而打开一个Socket需要知道目标计算机的IP地址和端口号，再指定协议类型即可。
import socket#导入socket库
#k客户端
#创建一个socket
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('www.baidu.com',80))
s.send((b'GET / HTTP/1.1\r\nHost: www.baidu.com\r\nConnection: close\r\n\r\n'))

# 接收数据:
buffer=[]
while True:
    # 每次最多接收1k字节:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = b''.join(buffer)
s.close()
header, html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))
# 把接收的数据写入文件:
with open('baidu.html', 'wb') as f:
    f.write(html)