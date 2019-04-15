import threading
import asyncio
@asyncio.coroutine
def hello():
    print('hello world (%s)' % threading.currentThread())
    yield from asyncio.sleep(1)
    print('hello again (%s)' % threading.currentThread())

loop=asyncio.get_event_loop()
tasks=[hello(),hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

'''
打印结果
hello world (<_MainThread(MainThread, started 7356)>)
hello world (<_MainThread(MainThread, started 7356)>)
（暂停约1秒）
hello again (<_MainThread(MainThread, started 7356)>)
hello again (<_MainThread(MainThread, started 7356)>)

'''
#由打印的当前线程名称可以看出，两个coroutine是由同一个线程并发执行的。