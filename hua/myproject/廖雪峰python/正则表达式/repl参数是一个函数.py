#以下实例中将字符串中的匹配的数字乘于 2：
import re
#将匹配的数字乘2
def double(matched):
    value = int(matched.group('value'))
    return str(value*2)

s = 'A55G4HFD567'
print(re.sub('(?P<value>\d+)', double, s))

