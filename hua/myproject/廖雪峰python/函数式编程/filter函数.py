'''
def is_odd(n):
    return n % 2 == 0
L=list(filter(is_odd,[1,2,3,4,5,6,7]))
print(L)
'''
'''
#把一个序列中的空字符串删掉
def not_empty(s):
    return s and s.strip()
L=list(filter(not_empty,['A',' ','','C',None]))
print(L)
'''
'''
#用filter求素数
def _odd_iter():
    n=1
    while True:
        n=n+2
        yield n

def _not_divisible(n):
    return lambda x:x % n>0
def primes():
    yield 2
    it = _odd_iter()
    while True:
        n= next(it)
        yield n
        it = filter(_not_divisible(n),it)
for n in primes():
    if n < 1000:
        print(n)
    else:
        break
'''
'''
#求回数
def is_palindrome(n):
    return n==int(str(n)[::-1])
#output = filter(is_palindrome, range(1, 1000))
#print('1~1000:', list(output))
L=list(filter(is_palindrome, range(1, 100000)))
print(L)
'''