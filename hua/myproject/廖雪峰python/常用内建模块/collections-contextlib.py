#@contextmanager
#编写__enter__和__exit__仍然很繁琐，因此Python的标准库contextlib提供了更简单的写法，上面的代码可以改写如下：
from contextlib import contextmanager
class Query(object):
    def __init__(self,name):
        self.name=name

    def query(self):
        print('Query info about %s...' % self.name)

@contextmanager
def create_query(name):
    print('Begin')
    q=Query(name)
    yield q
    print('End')
with create_query('Bob') as q:
    q.query()
print('---------------------------------------------------------------------')
#很多时候，我们希望在某段代码执行前后自动执行特定代码，也可以用@contextmanager实现
@contextmanager
def tag(name):
    print("<%s>" % name)
    yield
    print("</%s>" % name)
with tag("h1"):
    print('hello')
    print('world')
'''
代码的执行顺序是：
1.with语句首先执行yield之前的语句，因此打印出<h1>；
2.yield调用会执行with语句内部的所有语句，因此打印出hello和world；
3.最后执行yield之后的语句，打印出</h1>。
因此，@contextmanager让我们通过编写generator来简化上下文管理。
'''

print('----------------------------------------------------------------------')
#  @closing
#如果一个对象没有实现上下文，我们就不能把它用于with语句。这个时候，可以用closing()来把该对象变为上下文对象。
# 例如，用with语句使用urlopen()：
from contextlib import closing
from urllib.request import urlopen

with closing(urlopen('https://www.baidu.com')) as page:
    for line in page:
        print(line)
#closing也是一个经过@contextmanager装饰的generator，这个generator编写起来其实非常简单：
@contextmanager
def closing(thing):
    try:
        yield thing
    finally:
        thing.close()