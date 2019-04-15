import  threading,time
#创建线程的两种方式
#第一种：通过threading.Thread直接在线程中运行函数；
def saySorry():
    print('子进程%s启动' % (threading.current_thread().name))
    #time.sleep(1)
    print('爸爸爱你')

if __name__=='__main__':
    print('主线程%s启动' % (threading.current_thread().name))
    for i in range(5):
        t=threading.Thread(target=saySorry)#Thread():指定线程要执行的代码
        t.start()

#第二种：通过继承threading.Thread类来创建线程
#这种方法只需要重载threading.Thread类的run方法，然后调用start()开启线程就可以了
import threading
class Mythread(threading.Thread):
    def run(self):
        for i in range(5):
            print(i)

if __name__=='__main__':
    t1=Mythread()
    t2=Mythread()
    t1.start()
    t2.start()



