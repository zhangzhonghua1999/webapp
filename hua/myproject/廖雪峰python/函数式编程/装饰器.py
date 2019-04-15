'''
def log(func):
    def wrapper(*args,**kw):
        print('call %s():' % func.__name__)
        return func(*args,**kw)
    return wrapper

@log
def now():
    print('2019-03-12')

now()
print(now.__name__)

'''
'''
def log(text):
    def decorator(func):
        def wrapper(*args,**kw):
            print('%s %s()' % (text,func.__name__))
            return func(*args,**kw)
        return wrapper
    return decorator

@log('ex')
def now():
    print('2019-03-12')

now()
print(now.__name__)
'''
'''
import functools
def log(func):
    @functools.wraps(func)
    def wrapper(*args,**kw):
        print('call %s ():' % func.__name__)
        return  func(*args,**kw)
    return wrapper
'''
'''
import functools

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


@log('ext')
def now():
    print('2019.03.12')

now()
print(now.__name__)
'''

import time, functools

def metric(fn):
    @functools.wraps(fn)
    def wrapper_func(*args,**kw):
        start = time.time()
        result = fn(*args,**kw)
        end = time.time()
        print('%s rxrcuted in %.2f s' % (fn.__name__,end-start))
        return result
    return wrapper_func


@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
print(f)
s = slow(11, 22, 33)
print(s)

if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')












