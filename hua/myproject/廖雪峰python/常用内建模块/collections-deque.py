#          deque
#使用list存储数据时，按索引访问元素很快，但是插入和删除元素就很慢了，
# 因为list是线性存储，数据量大的时候，插入和删除效率很低。

#deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈：

from collections import deque
q=deque(['a','b','c'])
q.append('x')#插入元素x
q.appendleft('y')#从头部插入元素y
print(q)
q.popleft()#从头部删除一个元素
print(q)
print('--------------------------------------------------------------------')