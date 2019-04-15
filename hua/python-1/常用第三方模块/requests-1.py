import requests
'''
#通过get访问一个页面
re=requests.get('https://www.douban.com/')
print(re.status_code)
#print(re.text)

#对于带参数的url,传入一个dict作为params参数：
r= requests.get('https://www.douban.com/search',params={'q':'python','cat':'1001'})
print(r.url)#实际传入的参数为https://www.douban.com/search?q=python&cat=1001
print(r.content)#无论响应是文本还是二进制内容，我们都可以用content属性获得bytes对象：
print(r.encoding)#requests自动检测编码，可以使用encoding属性查看
'''

#1.发送get请求
import json,requests
url='http://api.nnzhp.cn/api/user/stu_info?stu_name=张忠华'
req=requests.get(url)#发送get请求
print(req.text)#获取结果
print(type(req.text))
print('----------------------------------------------------')
print(req.json())
print(type(req.json()))

print('2+++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
#2，发送post请求
url1='http://api.nnzhp.cn/api/user/login'
data1= {'username':'niuhanyang','passwd':'aA123456'}
req1=requests.post(url1,data1)#发送post请求，第一个参数是url，第二个参数是请求的数据
print(req1.json())

print('3++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
#发送post请求，入参是json格式
url2='http://api.nnzhp.cn/api/user/add_stu'
data2={'name':'张忠华','grade':'白羊座','phone':19979313119}
req2=requests.post(url2,json=data2)#发送post请求，第一个参数是url，第二个参数是请求的数据
print(req2.json())

print('4++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
#添加cookie
url3='http://api.nnzhp.cn/api/user/gold_add'
data3={'stu_id':1,'gold':10000}
cookie={'niuhanyang':'8cddec0ae482ae542d595684c0f78f12'}
req3=requests.post(url3,data3,cookies=cookie)
print(req3.json())

print('5++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
#五，添加header
import json ,requests
url4='http://api.nnzhp.cn/api/user/all_stu'
header = {'Referer':'http://api.nnzhp.cn/','User-Agent':'Chore'}
req4 = requests.get(url4,headers=header)
print(req4.json())
print('6+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
#6.上传文件
url5='http://api.nnzhp.cn/api/file/file_upload'
f={'file':open('1.jpg','rb')}
req5=requests.post(url5,files=f)
print(req5.json())

print('7+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
#保存网页import json ,requests
url = 'http://www.nnzhp.cn/archives/630'
r = requests.get(url)
f = open('nnzhp.html','wb')
f.write(r.content)
f.close()