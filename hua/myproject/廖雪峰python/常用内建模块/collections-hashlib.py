#                摘要算法简介

#Python的hashlib提供了常见的摘要算法，如MD5，SHA1等等。
#摘要算法就是通过摘要函数f()对任意长度的数据data计算出固定长度的摘要digest，目的是为了发现原始数据是否被人篡改过。
#摘要算法之所以能指出数据是否被篡改过，就是因为摘要函数是一个单向函数，计算f(data)很容易，但通过digest反推data却非常困难。
# 而且，对原始数据做一个bit的修改，都会导致计算出的摘要完全不同。


#我们以常见的摘要算法MD5为例，计算出一个字符串的MD5值：

import hashlib
md5=hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5.hexdigest())

md5.update('how to use md5 in python hashli?'.encode('utf-8'))#改动一个字母，结果完全不同
print(md5.hexdigest())


#MD5是最常见的摘要算法，速度很快，生成结果是固定的128 bit字节，通常用一个32位的16进制字符串表示。
print('--------------------------------------------------------------------------------')


#另一种常见的摘要算法是SHA1，调用SHA1和调用MD5完全类似：

import hashlib
sha1=hashlib.sha1()
sha1.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(sha1.hexdigest())

#SHA1的结果是160 bit字节，通常用一个40位的16进制字符串表示。


