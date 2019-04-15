#和我们自定义的加salt算法不同，Hmac算法针对所有哈希算法都通用，无论是MD5还是SHA-1。
# 采用Hmac替代我们自己的salt算法，可以使程序算法更标准化，也更安全。

#我们首先需要准备待计算的原始消息message，随机key，哈希算法，这里采用MD5，使用hmac的代码如下：

import hmac
message=b'Hello,world!'
key=b'secret'
h=hmac.new(key,message,digestmod='MD5')
print(h.hexdigest())
#可见使用hmac和普通hash算法非常类似。hmac输出的长度和原始哈希算法的长度一致。
# 需要注意传入的key和message都是bytes类型，str类型需要首先编码为bytes。

