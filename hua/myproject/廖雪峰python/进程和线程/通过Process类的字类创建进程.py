#创建新的进程还能够使用类的方式，可以自定义一个类，“继承Process类”，每次实例化这个类的时候，就等同于实例化一个进程对象

import multiprocessing
import time

class ClockProcess(multiprocessing.Process):
    def run(self):
        n=5
        while n>0:
            print(n)
            time.sleep(1)
            n-=1

if __name__=='__main__':
    p=ClockProcess()
    p.start()
    p.join()

