#re.search 扫描整个字符串并返回第一个成功的匹配
#语法  re.search(pattern匹配的正则表达式，string要匹配的字符串，flags=0标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等。)
#re.M   将所有行的尾字母输出
#re.I   忽略大小写
import re

print(re.search('www','www,runoob.com').span())
print(re.search('run','www.runoob.com'))

line='Cats are smarter than dogs'
# .* 表示任意匹配除换行符（\n、\r）之外的任何单个或多个字符
searchObj=re.search(r'(.*) are (.*?) .*',line,re.M|re.I)
if searchObj:
   print ("searchObj.group() : ", searchObj.group())
   print ("searchObj.group(1) : ", searchObj.group(1))
   print ("searchObj.group(2) : ", searchObj.group(2))
else:
   print ("No search!")

