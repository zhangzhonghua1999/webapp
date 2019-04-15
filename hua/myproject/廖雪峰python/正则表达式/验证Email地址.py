'''
练习
请尝试写一个验证Email地址的正则表达式。版本一应该可以验证出类似的Email：
someone@gmail.com
bill.gates@microsoft.com
'''
import re
def is_valid_email(addr):
    if re.findall(r'^[\w.]+@[\w]+\.com$',addr):
    # 正则解释：     字母一个以上 .一个或没有 字母一个以上 @ 字母不限 .com
        return True
assert is_valid_email('someone@gmail.com')
assert is_valid_email('1145530136@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('ok')