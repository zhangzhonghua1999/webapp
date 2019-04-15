import re
from datetime import datetime,timedelta,timezone

def to_timestamp(dt_str,tz_str):
    dt=datetime.strptime(dt_str,'%Y-%m-%d %H:%M:%S')#str转datetime
    r=re.search(r'([+-]+[\d]+)',tz_str)#提取数字
    tz_hour=int(r.group())
    tz=timezone(timedelta(hours=tz_hour))#创建时区
    dt=dt.replace(tzinfo=tz)#设置好时区
    return dt.timestamp()

t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('ok')
