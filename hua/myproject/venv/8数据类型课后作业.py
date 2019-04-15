dream8 = [
    {"姓名": "科比", "年龄": 31, "位置": "后卫", "身高": 1.98, "是否MVP": True},
    {"姓名": "韦德", "年龄": 29, "位置": "后卫", "身高": 1.93, "是否MVP": True},
    {"姓名": "波什", "年龄": 27, "位置": "大前锋", "身高": 2.11, "是否MVP": False},
    {"姓名": "霍华德", "年龄": 24, "位置": "中锋", "身高": 2.12, "是否MVP": False},
    {"姓名": "詹姆斯", "年龄": 29, "位置": "小前锋", "身高": 2.03, "是否MVP": True}
    ]
memername=input('你要查看的姓名')
for memerdict in dream8:
    if memername == memerdict["姓名"]:
        print('成员资料%s' % memerdict["姓名"])
        for infoItem in memerdict:
            print("%s: %s" % (infoItem, memerdict[infoItem]))