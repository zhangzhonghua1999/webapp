#Python内置的json模块提供了非常完善的Python对象到JSON格式的转换。
# 我们先看看如何把Python对象变成一个JSON：

#json.dumps     将 Python 对象编码成 JSON 字符串
#json.loads      将已编码的 JSON 字符串解码为 Python 对象

import json
d=dict(name='Bob',age=20,score=88)
json_str=json.dumps(d)
print('原始数据',d)
print('json 对象：',json_str)
# 将 JSON 对象转换为 Python 字典
print(json.loads(json_str))

#如果你要处理的是文件而不是字符串，你可以使用 json.dump() 和 json.load() 来编码和解码JSON数据

# 写入 JSON 数据
with open('d.json','w') as f:
    json.dump(d,f)

# 读取数据
with open('d.json', 'r') as f:
    data = json.load(f)
print(data)