#从environ里读取PATH_INFO，这样可以显示更加动态的内容：
def application(environ,start_response):
    start_response('200 OK',[('Content-Type','text/html')])
    body='<h1>Hello,%s</h1>' % (environ['PATH_INFO'][1:] or 'Web')
    return [body.encode('utf-8')]