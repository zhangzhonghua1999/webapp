from multiprocessing import Process

def run(name):
    print('子进程运行中，name=%s' % name)
if __name__=='__main__':
    print('父进程正在启动')
    p=Process(target=run,args=('test',))
    #target表示调用对象，args表示调用对象的位置参数元组
    #注意：（ 元组中只有一个元素是结尾要加，）
    print('子进程将要执行')
    p.start()
    print(p.name) #p.pid
    p.join()
    print('子进程结束')
    print(p.is_alive())





