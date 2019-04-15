#我们先定义一个Student类，打印一个实例：
class Student(object):
    def __init__(self,name):
        self.name=name

print(Student('zhangzhonghua'))

#打印出一堆<__main__.Student object at 0x109afb190>，不好看。
#怎么才能打印得好看呢？只需要定义好__str__()方法，返回一个好看的字符串就可以了：

class Student(object):
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return 'Student object name is %s' % self.name
    __repr__=__str__
print(Student('zzh'))






