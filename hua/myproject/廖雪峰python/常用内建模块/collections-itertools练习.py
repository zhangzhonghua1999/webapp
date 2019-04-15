#计算圆周率可以根据公式：
#利用Python提供的itertools模块，我们来计算这个序列的前N项和：
import itertools

def pi(N):
    sum=0
    a=1
    L=itertools.count(1,2)
    ns=list(itertools.takewhile(lambda x: x<=2*N-1,L))
    for i in ns:
        sum+=(4/i)*a
        a=-a
    return sum


print(pi(10))
print(pi(100))
print(pi(1000))
print(pi(10000))
assert 3.04 < pi(10) < 3.05
assert 3.13 < pi(100) < 3.14
assert 3.140 < pi(1000) < 3.141
assert 3.1414 < pi(10000) < 3.1415
print('ok')