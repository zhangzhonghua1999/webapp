import urllib,re,requests
import importlib,sys
importlib.reload(sys)

url_name = []
def get():
    hd = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}
    url='https://www.itbaizhan.cn/course/id/6620.html'
    html = requests.get(url, headers=hd).text
    url_content = re.compile(r'(<div class="j-r-list-c">.*?</div>.*?</div>)', re.S)  # 编译
    url_contents = re.findall(url_content, html)  # 匹配
    for i in url_contents:
        url_reg = r'data-mp4="(.*?)"'  # 视频地址
        url_items = re.findall(url_reg, i)
     # print url_items
        if url_items:  # 判断视频是否存在
            name_reg = re.compile(r'<a href="/detail-.{8}?.html">(.*?)</a>', re.S)
            name_items = re.findall(name_reg, i)
         # print name_items[0]
            for i, k in zip(name_items, url_items):
                url_name.append([i, k])
                print(i, k)
    for i in url_name:  # i[1]=url i[0]=name
        urllib.urlretrieve(i[1], 'video\\%s.mp4' % (i[0].decode('utf-8')))

if __name__ == "__main__":
    get()



