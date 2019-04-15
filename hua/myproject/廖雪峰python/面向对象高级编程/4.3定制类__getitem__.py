#要表现得像list那样按照下标取出元素，需要实现__getitem__()方法：n self.a # 返回下一个值
'''
class Fib(object):
    def __getitem__(self, item):
        a,b=1,1
        for x in range(item):
            a,b=b,a+b
        return a

f=Fib()
print(f[1])
list(range(100))[5:10]
'''
#但是list有个神奇的切片方法：
#对于Fib却报错。原因是__getitem__()传入的参数可能是一个int，也可能是一个切片对象slice
class Fib(object):
    def __getitem__(self, item):
        if isinstance(item,int):#item是索引
            a,b=1,1
            for x in range(item):
                a,b=b,a+b
            return a
        if isinstance(item,slice): #item是切片
            start=item.start
            stop=item.stop
            if start is None:
                start=0
            a,b=1,1
            L=[]
            for x in range(stop):
                if x >=start:
                    L.append(a)
                a,b=b,a+b
            return L

f=Fib()
print(f[0])

print(f[5])

print(f[100])

print(f[0:5])

print(f[:10])



