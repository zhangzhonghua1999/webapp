#subprocess模块可以让我们非常方便的启动一个子进程，然后控制其输入和输出。
#下面的例子演示了如何在Python代码中运行命令nslookup www.python.org，这和命令行直接运行的效果是一样的：
import subprocess
print('$ nslookup www.python.org')
r=subprocess.call(['nslookup','www.python.org'])
print('Exit code:',r)
