'''
def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax
print(calc_sum(1,2,3,4))
def lazy_sum(*args):
    def sum():
        ax=0
        for n in args:
            ax =ax + n
        return ax
    return  sum

f=lazy_sum(1,2,3,4,5)
f1=lazy_sum(1,2,3,4,5)
print(f())
print(f==f1)
'''
'''
#闭包
def addx(x):
    def adder(y):
        return x+y
    return adder


c=addx(8)
print(type(c))
print(c.__name__)
print(c(10))
'''

'''
def count():
    def f(j):
        def g():
            return j*j
        return g
    fs=[]
    for i in range(2,4):
        fs.append(f(i))
    return fs

f1,f2=count()
print(f1())
print(f2())
'''

#练习
'''
def createCounter():
    n=0
    def Counter():
        nonlocal n
        n=n+1
        return n
    return Counter
'''

def createCounter():
    f=[0]
    def counter():
        f[0] +=1
        return f[0]
    return counter



counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')



