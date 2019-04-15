import os

#查看当前目录的绝对路径
print(os.path.abspath('.'))
#把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数，
# 这样可以正确处理不同操作系统的路径分隔符。
#在某个目录下创建一个新目录，首先把新目录的完整路径表示出来：
print(os.path.join('D:\windows','testdir'))
# 然后创建一个目录:
os.mkdir('D:\windows\\testdir')

# 删掉一个目录:
os.rmdir('D:\windows\\testdir')

#同样的道理，要拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数，
#这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名：
print(os.path.split('D:\windows\\testdir'))

#os.path.splitext()可以直接让你得到文件扩展名，很多时候非常方便：
print(os.path.splitext('D:\windows\zz.txt'))

#这些合并、拆分路径的函数并不要求目录和文件要真实存在，它们只对字符串进行操作。



print([x for x in os.listdir('.') if os.path.isdir(x)])
#比如我们要列出当前目录下的所有目录
#'.'是当前目录  可换乘其他目录。   if os.path.isdir('其他目录'+x)

#要列出当前目录下所有的.py文件，只需一行代码：
#'C:\Users\11455\Desktop\py'

[x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py']

#要列出其他目录下所有的.py文件，也只需一行代码：
[x for x in os.listdir('C:\\Users\\11455\\Desktop\\py') if os.path.isfile(os.path.join('C:\\Users\\11455\\Desktop\\py\\lianxi.py')) and os.path.splitext(x)[1] == '.py']
[x for x in os.listdir('C:\\Users\\11455\\Desktop\\py') if os.path.isfile(os.path.join('C:\\Users\\11455\\Desktop\\py','lianxi.py')) and os.path.splitext(x)[1] == '.py']


