from wsgiref.simple_server import make_server
from WSGI_3 import application

httpd=make_server('' ,8000,application)
print('serving HTTP on port 8000...')
httpd.serve_forever()
#你可以在地址栏输入用户名作为URL的一部分，将返回Hello, xxx!：