#进程池创建的进程之间通信：如果要使用Pool创建进程，仅需要使用multiprocessing.Manager()中的Queue()
#而不是multiprocessing.Queue()

from multiprocessing import Manager,Pool
import time

def writer(q):
    for i in "welcome":
        print("开始写入",i)
        q.put(i)

def reader(q):
    time.sleep(3)
    for i in range(q.qsize()):
        print("得到消息",q.get())



if __name__=='__main__':
    print('主进程启动')
    q=Manager().Queue()
    po=Pool()
    po.apply_async(writer(q))
    po.apply_async(reader(q))
    po.close()
    po.join()

