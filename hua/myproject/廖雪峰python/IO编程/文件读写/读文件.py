'''
try:

    file =open('C:/Users/11455/Desktop/python.txt','r')
    data=file.read()
    print(data)
finally:
    file.close()
'''
#with open('C:/Users/11455/Desktop/python.txt','r') as f:
    #print(f.read())
f=open('C:/Users/11455/Desktop/python.txt','r')
print(f.name)
print(f.readline())
for line in f.readlines():
    print(line.strip()) # 把末尾的'\n'删掉
f.close()