#经过Salt处理的MD5口令，只要Salt不被黑客知道，即使用户输入简单口令，也很难通过MD5反推明文口令。

#def calc_md5(password):
#    return get_md5(password + 'the-Salt')

'''
但是如果有两个用户都使用了相同的简单口令比如123456，在数据库中，
将存储两条相同的MD5值，这说明这两个用户的口令是一样的。
有没有办法让使用相同口令的用户存储不同的MD5呢？
如果假定用户无法修改登录名，就可以通过把登录名作为Salt的一部分来计算MD5，
从而实现相同口令的用户也存储不同的MD5。
'''

#根据用户输入的登录名和口令模拟用户注册，计算更安全的MD5:
#然后，根据修改后的MD5算法实现用户登陆的验证:
import random,hashlib
def get_md5(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()

class User(object):
    def __init__(self,username,password):
        self.username=username
        self.salt=''.join([chr(random.randint(48,122)) for i in range(20)])
        self.password=get_md5(password + self.salt)

db = {
    'michael': User('michael', '123456'),
    'bob': User('bob', 'abc999'),
    'alice': User('alice', 'alice2008')
}

def login(username,password):
    user=db[username]
    return  user.password==get_md5(password + user.salt)


assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')