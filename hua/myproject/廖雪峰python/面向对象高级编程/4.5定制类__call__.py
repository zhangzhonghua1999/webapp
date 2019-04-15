#任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用。
class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('my name is %s' % self.name)

s=Student('zhangzhonghua')
s()
#能被调用的对象就是一个Callable对象，比如函数和我们上面定义的带有__call__()的类实例：
print(callable(Student))


