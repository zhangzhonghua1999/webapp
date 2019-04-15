#使用Python发送HTML格式的邮件
from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTP_SSL

#163邮箱smtp服务器
host_server = 'smtp.163.com'

#发件人邮箱
sender_163_mail='a19979313119@163.com'

#pwd为授权码
pwd='qq1145530136'

#收件人邮箱
receiver = '1145530136@qq.com'

#邮件正文内容
mail_content="你好,<p>这是使用python登录qq邮箱发送HTML格式邮件的测试：</p>" \
             "<p><a href='http://www.yiibai.com'>易百教程</a></p>"

#邮件标题
mail_title='张忠华的邮件'


#ssl登录
smtp = SMTP_SSL(host_server)

#set_debuglevel()是用来调试的。参数值为1表示开启调试模式，参数值为0关闭调试模式
smtp.set_debuglevel(1)
smtp.ehlo()
smtp.login(sender_163_mail,pwd)

msg=MIMEText(mail_content,'html','utf-8')
msg["Subject"] = Header(mail_title, 'utf-8')
msg["From"] = sender_163_mail
msg["To"] = Header("接收者测试", 'utf-8') ## 接收者的别名

smtp.sendmail(sender_163_mail, receiver, msg.as_string())
smtp.quit()
