from multiprocessing import Pool
import random, time

def work(num):#类里面是方法，类外面是函数
    print(random.random()*num)
    time.sleep(3)#间隔三秒
if __name__=='__main__':
    po = Pool(3)# 定义一个进程池，最大进程数为3，默认为cpu核数
    for i in range(10):#循环十次
        po.apply_async(work,(i,))  #apply_async选择要调用的目标，每次循环会用空出来的子进程去调用目标
    po.close()   #进程池关闭后不再接收新的请求
    po.join()   #等待po中所有子进程结束，碧玺放在close后面

#在多进程当中，主进程一般用来等待，真正的任务子进程中执行

