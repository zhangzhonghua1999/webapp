#re.match 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none。
#语法，re.match(pattern匹配的正则表达式，string要匹配的字符串，flags匹配方式）
#re.M   将所有行的尾字母输出
#re.I   忽略大小写
import re
print(re.match('ww','www.runoob.com'))#在起始位置匹配
print(re.match('no','www.runoob.com'))#不在起始位置匹配

line='Cats are smarter than dogs'
# .* 表示任意匹配除换行符（\n、\r）之外的任何单个或多个字符
matchObj=re.match(r'(.*) smarter (.*?) .*',line,re.M|re.I)
if matchObj:
   print ("matchObj.group() : ", matchObj.group())
   print ("matchObj.group(1) : ", matchObj.group(1))
   print ("matchObj.group(2) : ", matchObj.group(2))
else:
   print ("No match!!")
