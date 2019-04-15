#给多个人发邮件
from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTP_SSL


host_server = 'smtp.qq.com'#qq邮箱smtp服务器

sender_qq = '1145530136@qq.com'#sender_qq为发件人的qq号码

pwd = 'levhyvzurhiebaai' ## levhyvzurhiebaai#pwd为qq邮箱的授权码

sender_qq_mail = '1145530136@qq.com'#发件人的邮箱

receivers = ['13426631994@163.com','a19979313119@163.com']#收件人邮箱

mail_content = '你好，这是使用python登录qq邮箱发邮件的测试'#邮件的正文内容

mail_title = '张忠华的邮件'#邮件标题

smtp = SMTP_SSL(host_server)#ssl登录

smtp.set_debuglevel(1)#set_debuglevel()是用来调试的。参数值为1表示开启调试模式，参数值为0关闭调试模式

smtp.ehlo(host_server)
smtp.login(sender_qq, pwd)

msg = MIMEText(mail_content, "plain", 'utf-8')
msg["Subject"] = Header(mail_title, 'utf-8')
msg["From"] = sender_qq_mail
msg["To"] = Header("接收者测试", 'utf-8')
smtp.sendmail(sender_qq_mail, receivers, msg.as_string())
smtp.quit()
