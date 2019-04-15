#datetime是python处理时间和日期的标准库
#1.获取当前日期和时间
from datetime import datetime
now=datetime.now()#获取当前datetime
print('now',now)
print(type(now))
'''
注意到datetime是模块，datetime模块还包含一个datetime类，通过from datetime import datetime导入的才是datetime这个类。
如果仅导入import datetime，则必须引用全名datetime.datetime。
datetime.now()返回当前日期和时间，其类型是datetime。
'''
print('--------------------------------------------------------------------')
#获取指定日期和时间
dt = datetime(2019,4,12,12,00)#用指定日期时间创建datetime
print('dt',dt)
#datetime转换为timestamp
#把一个datetime类型转换为timestamp只需要简单调用timestamp()方法
print(dt.timestamp())
#Python的timestamp是一个浮点数。如果有小数位，小数位表示毫秒数。

#要把timestamp转换为datetime，使用datetime提供的fromtimestamp()方法：
t=1555041600.0
print('本地时间',datetime.fromtimestamp(t))#本地时间
print('UTC时间',datetime.utcfromtimestamp(t))#UTC时间
print('---------------------------------------------------------------')
#str转换为datetime
#转换方法是通过datetime.strptime()实现，需要一个日期和时间的格式化字符串：
#字符串'%Y-%m-%d %H:%M:%S'规定了日期和时间部分的格式。
cday=datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday)
#注意转换后的datetime是没有时区信息的。

print('----------------------------------------------------------------------')
#datetime转换为str 转换方法是通过strftime()实现的
print(now.strftime('%a,%b %d %H:%M'))
print('-----------分-------------------隔--------------------线-----------------')
#datetime加减
#对日期和时间进行加减实际上就是把datetime往后或往前计算，得到新的datetime。
# 加减可以直接用+和-运算符，不过需要导入timedelta这个类：
from datetime import timedelta
print(now + timedelta(hours=10))
print(now -timedelta(days=1))
print('-----------分-------------------隔--------------------线-----------------')
#本地时间转换为UTC时间
'''
本地时间是指系统设定时区的时间，例如北京时间是UTC+8:00时区的时间，而UTC时间指UTC+0:00时区的时间。
一个datetime类型有一个时区属性tzinfo，但是默认为None，所以无法区分这个datetime到底是哪个时区，
除非强行给datetime设置一个时区：
'''
from datetime import timezone
tz_utc_8 = timezone(timedelta(hours=8)) # 创建时区UTC+8:00
print(now)
dt=now.replace(tzinfo=tz_utc_8)# 强制设置为UTC+8:00
print(dt)
#如果系统时区恰好是UTC+8:00，那么上述代码就是正确的，否则，不能强制设置为UTC+8:00时区。
print('-----------分-------------------隔--------------------线-----------------')

#时区转换
#我们可以先通过utcnow()拿到当前的UTC时间，再转换为任意时区的时间：

utc_dt=datetime.utcnow().replace(tzinfo=timezone.utc)
# 拿到UTC时间，并强制设置时区为UTC+0:00:
print(utc_dt)

# astimezone()将转换时区为北京时间:
bj_dt=utc_dt.astimezone(timezone(timedelta(hours=8)))
print(bj_dt)
# astimezone()将bj_dt转换时区为东京时间:
tokyo_dt2 = bj_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt2)



