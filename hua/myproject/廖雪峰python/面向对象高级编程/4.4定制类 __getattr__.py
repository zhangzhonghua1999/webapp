#正常情况下，当我们调用类的方法或属性时，如果不存在，就会报错。

class Student(object):
    def __init__(self):
        self.name='zhang'

  #写一个__getattr__()方法，动态返回一个属性。

    def __getattr__(self, item):
        if item == 'score':
            return 99
        if item == 'age':
            return lambda: 25
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % item)
s=Student()
print(s.name)
print(s.score)
print(s.age())
#print(s.abc)
#利用完全动态的__getattr__，我们可以写出一个链式调用：

class Person:
	def name(self,name):
	    self.name=name
	    return self
	def age(self,age):
		self.age=age
		return self
	def show(self):
		print('my name is',self.name,'and I am',self.age,'years old')

p=Person()
p.name('zhangzhonghua').age(20).show()


