#操作图像
from PIL import Image
#在当前路径下打开一个jpg图像文件
im=Image.open('1.jpg')
#im.show()
w,h=im.size#获得图像尺寸
print("Original image size: %sx%s" % (w,h))

im.thumbnail((w*2,h*2))#放大两倍
print('Resize image to: %sx%s' % (w*2,h*2))
im.save('thumbnail.jpg','png')#把放大后的图片以png的格式保存

from PIL import Image,ImageFilter
im2=im.filter(ImageFilter.BLUR)# 应用模糊滤镜:
im2.save('im2.jpg','jpeg')




#PIL的ImageDraw提供了一系列绘图方法，让我们可以直接绘图。比如要生成字母验证码图片：
from PIL import Image,ImageDraw,ImageFont,ImageFilter
import random

#随机字母
def rndChar():
    return chr(random.randint(65,90))

#随机颜色
def rndColor():
    return (random.randint(64,255),random.randint(64,255),random.randint(64,255))

#随机颜色2
def rndColor2():
    return (random.randint(32,127),random.randint(32,127),random.randint(32,127))

#长 宽
width = 60*4
height=60
image=Image.new('RGB',(width,height),(255,255,255))

#创建Font对象：
font=ImageFont.truetype('arial.ttf',36)

#创建Draw对象
draw=ImageDraw.Draw(image)

#填充每个像素
for x in range(width):
    for y in range(height):
        draw.point((x,y),fill=rndColor())

#输出文字
for t in range(4):
    draw.text((60*t +10, 10),rndChar(),font=font,fill=rndColor2())
# 模糊:
#image = image.filter(ImageFilter.BLUR)
image.save('code.jpg', 'jpeg')







