#1.找到url（网站链接）
url = 'https://www.qiushibaike.com/text/'
#2.解析url，得到网页源代码
import requests

r = requests.get(url).content.decode()

#print(r)
#<Response [200]> 200状态码，请求成功
#print(r.content)
#能够得到我们当前这个url的网页源代码，它是一个二进制数据类型
#print(r.content.decode())
#把二进制数据类型转换成字符串数据类型

import re

#3.提取数据 正则表达，对象必须为字符串
#ret=re.findall('表达式',针对的对象)
ret = re.findall('<div class="content">.*?<span>(.*?)</span>.*?</div>',r,re.S)
#print(ret)
#4.保存数据   如果要保存数据，我们不能直接保存列表对象，要保存字符串


for i in ret:
    #print(i)
    with open('qiubai.txt','a',encoding='utf-8') as f:
        i=re.sub('<br/>',' ',i)
        f.write(i)






