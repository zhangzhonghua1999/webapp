import re
pattern=re.compile(r'([a-z]+) ([a-z]+)',re.I)
m=pattern.search('Hello World Wide Wrb')
print(m)
print(m.group(0))                            # 返回匹配成功的整个子串
print( m.span(0))                             # 返回匹配成功的整个子串的索引
print(m.group(1))                            # 返回第一个分组匹配成功的子串
print(m.span(1))                             # 返回第一个分组匹配成功的子串的索引
print( m.group(2))                      # 返回第二个分组匹配成功的子串
print(m.span(2))                            # 返回第二个分组匹配成功的子串
print(m.groups())                            # 等价于 (m.group(1), m.group(2), ...)
#m.group(3) # 不存在第三个分组

