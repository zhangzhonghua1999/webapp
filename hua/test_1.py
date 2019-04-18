'''
道生一，一生二，二生三，三生万物。
道 即是 type
一 即是 metaclass(元类，或者叫类生成器)
二 即是 class(类，或者叫实例生成器)
三 即是 instance(实例)
万物 即是 实例的各种属性与方法，我们平常使用python时，调用的就是它们。
'''
# 道生一：传入type
class SayMetaClass(type):
    # 传入三大永恒命题：类名称、父类、属性
    def __new__(cls, name,bases, attrs):
        # 创造“天赋”
        attrs['say_'+name] = lambda self,value,saying = name: print(saying+',' + value+ '!')
        # 传承三大永恒命题：类名称、父类、属性
        return type.__new__(cls,name,bases,attrs)

#一生二：创建类
class Hello(object,metaclass=SayMetaClass):
    pass

class Hi(object,metaclass=SayMetaClass):
    pass

class Sayolala(object,metaclass=SayMetaClass):
    pass

class Nihao(object,metaclass=SayMetaClass):
    pass

#二生三：创建实例
hello=Hello()
hi=Hi()
say=Sayolala()
n=Nihao()

#三生万物：调用实例方法
hello.say_Hello('world')
hi.say_Hi('world')
say.say_Sayolala('world')
n.say_Nihao('你好')


#道生一
class ListMetaclass(type):
    def __new__(cls, name, bases,attrs):
        #天赋：通过add方法将值绑定
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls,name,bases,attrs)

#一生二
class Mylist(list,metaclass=ListMetaclass):
    pass

m=Mylist()
m.add(1)
print(m)