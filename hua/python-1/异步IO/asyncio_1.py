import asyncio
@asyncio.coroutine
def hello():
    print('hello world')
    #异步调用sayncio.sleep(1):
    r= yield from asyncio.sleep(1)
    print('hello again')

#获取EventLoop:
loop =asyncio.get_event_loop()
#执行coroutine
loop.run_until_complete(hello())
loop.close()

