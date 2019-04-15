'''
class Student(object):
    pass

s=Student()
s.name='zhangzhonghua'# 动态给实例绑定一个属性
print(s.name)

#尝试绑定一个方法
def set_age(self,age):#定义一个函数作为实例方法
    self.age=age

from types import MethodType
s.set_age=MethodType(set_age,s)# 给实例绑定一个方法

s.set_age(25)# 调用实例方法

print(s.age)# 测试结果

#为了给所有实例都绑定方法，可以给class绑定方法
def set_score(self,score):
    self.score=score

Student.set_score=set_score

s.set_score(100)

print(s.score)
'''

#__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：
class Student(object):
    __slots__ = ('name','age')#只允许对Student实例添加name和age属性。

s= Student() #创建新的实例
s.name='zhangzhonghua'#绑定属性name
s.age=20    #绑定属性age
#s.score=100  #绑定属性score，因为slots里面并没有score这个属性，所以运行会出错

class expe(Student):
    pass

e=expe()
e.score=100
g=e.score
print(g)






