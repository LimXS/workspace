# -*- coding: utf-8 -*-  
import smtplib  
import email.MIMEMultipart# import MIMEMultipart  
import email.MIMEText# import MIMEText  
import email.MIMEBase# import MIMEBase  
import os.path
import time
  
import mimetypes  
#import email.MIMEImage# import MIMEImage

timeStamp=time.time()
timeArray = time.localtime(timeStamp)
otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S" , timeArray)

From = "xusxue@grasp.com.cn"
To = "1206626163@qq.com"
file_name = "D:/beefunresault.html"#附件名
host='61.139.77.221'
server = smtplib.SMTP(host,25)
server.login("xusxue@grasp.com.cn","abcd+123456789") #仅smtp服务器需要验证时
  
# 构造MIMEMultipart对象做为根容器  
main_msg = email.MIMEMultipart.MIMEMultipart()  
  
# 构造MIMEText对象做为邮件显示内容并附加到根容器  
text_msg = email.MIMEText.MIMEText(u"进销存报告，请下载后查看",_charset="utf-8")
main_msg.attach(text_msg)  
  
# 构造MIMEBase对象做为文件附件内容并附加到根容器  
ctype,encoding = mimetypes.guess_type(file_name)  
if ctype is None or encoding is not None:  
    ctype='application/octet-stream'  
maintype,subtype = ctype.split('/',1)  
file_msg=email.MIMEImage.MIMEImage(open(file_name,'rb').read(),subtype)
print ctype,encoding  
  
## 设置附件头  
basename = os.path.basename(file_name)  
file_msg.add_header('Content-Disposition','attachment', filename = basename)#修改邮件头  
main_msg.attach(file_msg)  
  
# 设置根容器属性  
main_msg['From'] = From  
main_msg['To'] = To  
main_msg['Subject'] = "beenfun report"+otherStyleTime
main_msg['Date'] = email.Utils.formatdate( )  
  
# 得到格式化后的完整文本  
fullText = main_msg.as_string( )  
  
# 用smtp发送邮件  
try:  
    server.sendmail(From, To, fullText)  
finally:  
    server.quit()