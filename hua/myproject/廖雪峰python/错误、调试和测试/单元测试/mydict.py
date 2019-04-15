'''
我们来编写一个Dict类，这个类的行为和dict一致，但是可以通过属性来访问，用起来就像下面这样：
d = Dict(a=1, b=2)
d['b']
#1
d.a
#1
'''
class Dict(dict):
    def __init__(self,**kw):
        super().__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key]=value

#为了编写单元测试，我们需要引入Python自带的unittest模块，编写mydict_test.py

d = Dict(a=2, b='testt')
print(d['b'])
print(d.a)

