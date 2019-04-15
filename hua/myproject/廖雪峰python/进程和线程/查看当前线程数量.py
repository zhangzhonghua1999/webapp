import threading
import time

def sing():
    for i in range(3):
        print("正在唱歌... %d" % i)
        time.sleep(1)

def dance():
    for i in range(2):
        print("正在跳舞...%d " % i)
        time.sleep(1)


if __name__=='__main__':
    print("开始: %s "% time.time())
    t1=threading.Thread(target=sing)
    t2=threading.Thread(target=dance)
    t1.start()
    t2.start()


while True:
    length=len(threading.enumerate())
    #threading.enumerate():返回当前运行中的Thread对象列表
    print("当前线程数为：%d" % length)
    if length<=1:
        break
    time.sleep(1)
