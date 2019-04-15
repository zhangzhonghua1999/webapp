import os
if os.path.isfile(os.path.join('C:\\Users\\11455\\Desktop\\py','lianxi.py')):
    print(True)
else:
    print(False)
[x for x in os.listdir('C:\\Users\\11455\\Desktop\\py') if os.path.isfile(os.path.join('C:\\Users\\11455\\Desktop\\py\\lianxi.py')) and os.path.splitext(x)[1] == '.py']
[x for x in os.listdir('C:\\Users\\11455\\Desktop\\py') if os.path.isfile(os.path.join('C:\\Users\\11455\\Desktop\\py','lianxi.py')) and os.path.splitext(x)[1] == '.py']

def query(path,s):
    L = [x for x in os.listdir(path) if x.find(s) != -1]
    if len(L):
        for x in L:
            print(os.path.join(path, os.path.basename(x)))

def index(s):
    abspath = os.path.abspath('.')
    query(abspath,s)
    for x in os.listdir(abspath):
        if os.path.isdir(x):
            query(os.path.join(abspath, os.path.basename(x)),s)

index('txt')




