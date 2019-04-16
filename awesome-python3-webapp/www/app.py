import logging; logging.basicConfig(level=logging.INFO)
import asyncio
from aiohttp import web

#定义服务器响应请求返回为“Awesom Website"
async def index(request):
    return web.Response(body=b'<h1>Awesome Website<h1>',content_type='text/html')

#建立服务器应用，持续监听本地9000端口的http请求，对首页"/"进行响应
def init():
    app=web.Application()
    app.router.add_get('/',index)
    web.run_app(app,host='127.0.0.1',port=9000)

if __name__=='__main__':
    init()
'''
在www目录下运行这个 app.py, 服务器将在9000端口持续监听 http 请求，并异步对首页 / 进行响应：

打开浏览器输入地址 http://127.0.0.1:9000 进行测试，如果返回我们设定好的Awesome Website字符串，
就说明我们网站服务器应用的框架已经搭好了。
'''