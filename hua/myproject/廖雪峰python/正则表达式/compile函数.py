#compile函数用于编译正则表达式，生成一个正则表达式（Pattern）对象，供match（）和search（）这两个函数使用
#语法格式为： re.compile(pattern[,flags]
'''
参数：
pattern : 一个字符串形式的正则表达式
flags 可选，表示匹配模式，比如忽略大小写，多行模式等，具体参数为：
re.I 忽略大小写
re.L 表示特殊字符集 \w, \W, \b, \B, \s, \S 依赖于当前环境
re.M 多行模式
re.S 即为' . '并且包括换行符在内的任意字符（' . '不包括换行符）
re.U 表示特殊字符集 \w, \W, \b, \B, \d, \D, \s, \S 依赖于 Unicode 字符属性数据库
re.X 为了增加可读性，忽略空格和' # '后面的注释
'''

import re
pattern=re.compile(r'\d+')  #至少匹配一个数字
m=pattern.match('one12twothree34four')#查找头部，没有匹配
print(m)

m=pattern.match('one12twothree34four',2)# 从'e'的位置开始匹配，没有匹配
print(m)
m=pattern.match('one12twothree34four',3) # 从'1'的位置开始匹配，正好匹配
print(m)                                    # 返回一个 Match 对象
print('**********************************************')
print(m.group())#返回匹配的整个表达式的字符串
print(m.start())#开始位置
print(m.end())#结束位置
print(m.span())#位置

'''
在上面，当匹配成功时返回一个 Match 对象，其中：
    group([group1, …]) 方法用于获得一个或多个分组匹配的字符串，当要获得整个匹配的子串时，
可直接使用 group() 或 group(0)；
    start([group]) 方法用于获取分组匹配的子串在整个字符串中的起始位置（子串第一个字符的索引），
参数默认值为 0；
    end([group]) 方法用于获取分组匹配的子串在整个字符串中的结束位置（子串最后一个字符的索引+1），
参数默认值为 0；
    span([group]) 方法返回 (start(group), end(group))。
'''