'''
def log(func):
    def wrapper(*args,**kw):
        print('begin call %s:' % func.__name__)
        result=func(*args,**kw)
        print('end call %s:' % func.__name__)
        return result
    return wrapper

@log
def now():
    print('2019.03.12')
print(now())

'''

import functools
def log(text=''):
    def decorator(func):
        def wrapper(*args,**kw):
            print('%s ')


