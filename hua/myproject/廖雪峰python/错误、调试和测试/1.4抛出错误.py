#因为错误是class，捕获一个错误就是捕获到该class的一个实例。
#如果要抛出错误，首先根据需要，可以定义一个错误的class，选择好继承关系，然后，用raise语句抛出一个错误的实例：
class FooError(ValueError):
    pass
def foo(s):
    n=int(s)
    if n==0:
        raise FooError('invalid value:%s' % s)
    return  10/ n
def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError!')
        raise

bar()