#多进程之间，默认是不共享数据的
#通过Queue（队列Q）可以实现进程间的数据传递
#Q本身是一个消息队列
#如何添加消息（入队操作）
#Queue.qsize():返回当前队列包含的消息数量
#Queue.empty():如果队列为空，返回True
#Queue.full():如果队列满了，返回True
#Queue.get([block,[timeout]]):获取队列中的一条信息，然后将其从队列中一出，block默认值为True
#Queue.put('')添加的消息类型不限
from multiprocessing import Queue,Process
import time

def write(q):
    for value in ['a','b','c']:
        print("开始写入：",value)
        q.put(value)
        time.sleep(1)

def read(q):
    while True:
        if not q.empty():
            print('pr读取到的是：',q.get())
            time.sleep(1)
        else:
            break
def read2(q):
    while True:
        if not q.empty():
            print('pr2读取到的是：', q.get())
            time.sleep(1)
        else:
            break

if __name__=='__main__':
    q=Queue()
    pw= Process(target=write,args=(q,))
    pr= Process(target=read,args=(q,))
    pr2=Process(target=read2,args=(q,))
    pw.start()
    pw.join()#等待接收完毕

    pr.start()
    pr2.start()
    pr.join()
    pr2.terminate()
    print('接收完毕')




