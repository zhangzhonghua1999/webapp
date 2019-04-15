from hi import Hi
h=Hi()
h.hi()
print(type(Hi))
print(type(h))

#type()函数既可以返回一个对象的类型，又可以创建出新的类型
#我们可以通过type()函数创建出Hello类，而无需通过class Hello(object)...的定义：
def fn(self,name='world'):  #先定义函数
    print('hello,%s' % name)
#使用方法：类名=type(类名,继承的父类集合)
Hello=type('Hello',(object,),dict(hello=fn))#创建Hello class
hh=Hello()
hh.hello()

print(type(hh))
print(type(Hello))

'''
要创建一个class对象，type()函数依次传入3个参数：
class的名称；
继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。
'''


