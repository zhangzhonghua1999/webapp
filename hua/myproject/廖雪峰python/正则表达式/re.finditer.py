#和 findall 类似，在字符串中找到正则表达式所匹配的所有子串，并把它们作为一个迭代器返回。
#re.finditer(pattern,string,flags=0)
import re
it = re.finditer(r'\D+','12a32bc43jf3')
print('it:',it)

for i in it:
    print(i.group())


