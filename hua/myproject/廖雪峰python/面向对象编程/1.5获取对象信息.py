#使用type
print(type(123))
print(type('str'))
print(type(None))
print(type(abs))

#判断一个对象是否为函数
import types
def fn():
    pass

print(type(fn)==types.FunctionType)

#使用isinstance()
print(isinstance('ste',str))
print(isinstance((1, 2, 3), (list, tuple)))
print(isinstance([1, 2, 3], (tuple)))


#使用dir()
print(dir('ABC'))

print(len('abc'))
'abcd'.__len__()



