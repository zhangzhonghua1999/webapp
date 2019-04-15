from multiprocessing import Process
#多进程默认不共享数据，进程之间数据是独立的

num=10
def run1():
    global num
    num +=5
    print('子进程1运行中 num=%d' % num)


def run2():
    global num
    num += 2
    print('子进程2运行中 num=%d' % num)

if __name__=='__main__':
    print('父进程正在启动')
    p1=Process(target=run1)
    p2=Process(target=run2)
    #target表示调用对象，args表示调用对象的位置参数元组
    #注意：（ 元组中只有一个元素是结尾要加，）
    print('子进程1将要执行')
    print('子进程2将要执行')
    p1.start()
    p2.start()
    print(p1.name) #p.pid
    print(p2.name)
    print('子进程1结束')
    print('子进程2结束')
    print('***************************************')

