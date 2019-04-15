import os
print(os.name)# 操作系统类型
#如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统。

#在操作系统中定义的环境变量，全部保存在os.environ这个变量中，可以直接查看：
print(os.environ)

#要获取某个环境变量的值，可以调用os.environ.get('key')：
print(os.environ.get('PATH'))

print(os.environ.get('x','default'))
