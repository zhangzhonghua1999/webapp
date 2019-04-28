#由于aiohttp作为一个Web框架比较底层，我们还需要基于aiohttp编写一个更方便处理URL的Web框架。
import asyncio, os, inspect, logging, functools

from urllib import parse

from aiohttp import web

## apis是处理分页的模块
## APIError 是指API调用时发生逻辑错误
from apis import APIError

#编写装饰函数@get()

def get(path):
    ##Define decorator @get('/path')
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            return func(*args,**kw)
        wrapper.__method__='GET'
        wrapper.__route__=path
        return wrapper
    return decorator

#编写装饰函数@post()

def post(path):

    #Define decorator @post('/path')

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            return func(*args, **kw)
        wrapper.__method__ = 'POST'
        wrapper.__route__ = path
        return wrapper
    return decorator

'''
--使用inspect模块中的signature方法来获取函数的参数，实现一些复用功能--
inspect.Parameter 的类型有5种：
    POSITIONAL_ONLY          只能是位置参数
    KEYWORD_ONLY             关键字参数且提供了key
    VAR_POSITIONAL           相当于是 *args
    VAR_KEYWORD              相当于是 **kw
    POSITIONAL_OR_KEYWORD    可以是位置参数也可以是关键字参数
'''

## 以下是RequestHandler需要定义的一些函数

def get_required_kw_args(fn):
    args=[]
    params = inspect.signature(fn).parameters

    ## 如果url处理函数需要传入关键字参数，且默认是空的话，获取这个key
    for name,param in params.items():
        if param.kind== inspect.Parameter.KEYWORD_ONLY and param.default==inspect.Parameter.empty:
            args.append(name)
    return tuple(args)


def get_named_kw_args(fn):
    args=[]
    params = inspect.signature(fn).parameters

    # 如果url处理函数需要传入关键字参数，且默认是空的话，获取这个key
    for name,param in params.items():
        if param.kind == inspect.Parameter.KEYWORD_ONLY:
            args.append(name)
    return tuple(args)

def has_named_kw_args(fn):
    params=inspect.signature(fn).parameters

    # 判断是否有关键字参数
    for name,param in params.items():
        if param.kind == inspect.Parameter.KEYWORD_ONLY:
            return True

def has_var_kw_arg(fn):
    params=inspect.signature(fn).parameters

    # 判断是否有关键字变长参数，VAR_KEYWORD对应**kw
    for name,param in params.items():
        if param.kind == inspect.Parameter.VAR_KEYWORD:
            return True


def has_request_arg(fn):
    sig = inspect.signature(fn)
    params=sig.parameters
    found=False

    # 判断是否存在一个参数叫做request，并且该参数要在其他普通的位置参数之后
    for name,param in params.items():
        if name == 'request':
            found=True
            continue
        if found and (param.kind != inspect.Parameter.VAR_POSITIONAL and param.kind != inspect.Parameter.KEYWORD_ONLY
        and param.kind != inspect.Parameter.VAR_KEYWORD):
            # 如果判断为True，则表明param只能是位置参数POSITIONAL_ONLY
            raise ValueError('request parameter must be the last named parameter in function: %s%s'
                             % (fn.__name__, str(sig)))
    return found


# RequestHandler目的就是从URL处理函数（如handlers.index）中分析其需要接收的参数，从web.request对象中获取必要的参数，
# 调用URL处理函数，然后把结果转换为web.Response对象，这样，就完全符合aiohttp框架的要求

class RequestHandler(object):
    def __init__(self,app,fn):
        self._app =app
        self._func=fn
        self._has_request_arg=has_request_arg(fn)
        self._has_var_kw_arg=has_var_kw_arg(fn)
        self._has_named_kw_args=has_named_kw_args(fn)
        self._get_required_kw_args=get_required_kw_args(fn)
        self._get_named_kw_args = get_named_kw_args(fn)

    # 1.定义kw对象，用于保存参数
    # 2.判断URL处理函数是否存在参数，如果存在则根据是POST还是GET方法将request请求内容保存到kw
    # 3.如果kw为空(说明request没有请求内容)，则将match_info列表里面的资源映射表赋值给kw；如果不为空则把命名关键字参数的内容给kw
    # 4.完善_has_request_arg和_required_kw_args属性

    async def __call__(self,request):
        kw = None

        # 如果有需要处理的参数
        if self._has_named_kw_args or self._requied_kw_args or self._has_var_kw_arg:
            if request.method == 'POST':
                if not request.content_type:
                    return  web.HTTPBadRequest('Missing Content-Type.')
                ct = request.content_type.lower()
                if ct.startswith('application/json'):
                    params=await request.json()
                    if not isinstance(params,dict):
                        return web.HTTPBadRequest('JSON body must be object.')
                    kw = params
                elif ct.startswith('application/x-www-form-urlencoded') or ct.startswith('multipart/form-data'):
                    params = await  request.post()
                    kw=dict(**params)
                else:
                    return web.HTTPBadRequest('Unsupported Content - Type:%s' % request.content_type)
            if request.method =='GET':
                qs = request.query_string
                if qs:
                    kw = dict()

                    # 解析url中?后面的键值对内容保存到request_content
                    '''
                  qs = 'first=f,s&second=s'
                  parse.parse_qs(qs, True).items()
                  >>> dict([('first', ['f,s']), ('second', ['s'])])
                  '''
                    for k,v in parse.parse_qs(qs,True).items():
                        kw[k] = v[0]
        if kw is None:

            # 参数为空说明没有从request对象中获取到参数,或者URL处理函数没有参数
            '''
                       def hello(request):
                               text = '<h1>hello, %s!</h1>' % request.match_info['name']
                               return web.Response()
                       app.router.add_route('GET', '/hello/{name}', hello)
           '''
            '''if not self._has_var_kw_arg and not self._has_kw_arg and not self._required_kw_args:
                # 当URL处理函数没有参数时，将request.match_info设为空，防止调用出错
                request_content = dict()
           '''

            kw =dict(**request.match_info)
        else:
            if not self._has_var_kw_arg and self._named_kw_args:

                # remove all unamed kw:从request_content中删除URL处理函数中所有不需要的参数
                copy = dict()
                for name in self._named_kw_args:
                    if name in kw :
                        copy[name] = kw[name]
                    kw=copy

                # check named arg: 检查关键字参数的名字是否和match_info中的重复
                for k,v in request.match_info.items():
                    if k in kw:
                        logging.warning('Duplicate arg name in named arg and kw args:%s' % k)
                        kw[k]=v
            if self._has_request_arg:
                kw['request'] = request

            # check required kw: 检查是否有必须关键字参数
            if self._required_kw_args:
                for name in self._required_kw_args:
                    if not name in kw:
                        return web.HTTPBadRequest('Missing argument:%s ' % name)
            logging.info('can with args: %s' % str(kw))
            try:
                r=await self._func(**kw)
                return r
            except APIError as e:
                return dict(error = e.error, data = e.data, message =e.message)

# 添加CSS等静态文件所在路径
#定义add_static函数，来注册static文件夹下的文件
def add_static(app):
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),'static')
    app.router.add_static('/static/',path)
    logging.info('add static %s => %s ' % ('/static/',path))

# 定义add_route函数，来注册一个URL处理函数
def add_route(app,fn):
    method = getattr(fn, '__method__',None)
    path = getattr(fn,'__route__',None)
    if path is None or method is None:
        raise ValueError('@get or @post not defined in %s.' % str(fn))
    if not asyncio.iscoroutinefunction(fn) and not inspect.iscoroutinefunction(fn):
        fn = asyncio.coroutine(fn)
    logging.info('add route %s %s => %s(%s)' % (method, path, fn.__name__, ', '.join(inspect.signature(fn).parameters.keys())))
    app.router.add_route(method, path, RequestHandler(app,fn))

# 定义add_routes函数，自动把handler模块的所有符合条件的URL函数注册了
def add_routes(app,module_name):
    n= module_name.rfind('.')

    if n ==(-1):
        mod = __import__(module_name, globals(), locals())
    else:
        name = module_name[n+1:]
        mod = getattr(__import__(module_name[:n],globals(),locals(),[name]),name)
    for attr in dir(mod):
        if attr.startswith('_'):
            continue
        fn = getattr(mod,attr)
        if callable(fn):
            method = getattr(fn,'__method__',None)
            path = getattr(fn,'__route__',None)
            if method and path:
                add_route(app,fn )
