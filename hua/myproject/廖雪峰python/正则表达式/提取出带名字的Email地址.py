import re
def name_of_email(addr):
    m = re.match(
        r'<([\w\s]+)>\s[\w\.]+@[\w]+\.[a-zA-Z]{2,3}', addr)
    if m:
        return m.group(1)
    elif re.match('(\w+)@(\w+)',addr):
        m = re.match('(\w+)@(\w+)',addr)
        return m.group(1)
assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('bob@example.com ') == 'bob'
print('ok')
