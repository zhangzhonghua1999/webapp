#Python内置了一个WSGI服务器，这个模块叫wsgiref，它是用纯Python编写的WSGI服务器的参考实现。
# 所谓“参考实现”是指该实现完全符合WSGI标准，但是不考虑任何运行效率，仅供开发和测试使用。
#运行WSGI服务
#实现Web应用程序的WSGI处理函数：
def application(environ,start_response):
    start_response('200 OK',[('Content-Type','text/html')])
    return [b'<h1>Hello,web!</h1>']


