#*-* coding:UTF-8 *-*
'''
Created on 2016��4��5��

@author: xsx
'''
import unittest
import order
import HTMLTestRunner
import time,os
import smtplib
from email.mime.text import MIMEText
import ordercreateandcheck
import ordersearch
'''
def sendmail(file_new):
    mail_from='xusxue@grasp.com.cn'
    mail_to='1206626163@qq.com'
    f=open(file_new,'b')
    mail_body=f.read()
    f.close()
    msg=MIMEText(mail_body,_subtype='html',_charset='utf-8')
    msg['Subject']=u'测试报告'
    msg['date']=time.strftime('%a, %d %b %Y %H:%M:%S %z')
    smtp=smtplib.SMTP()
    smtp.connect('61.139.77.221')
    #用户名密码
    smtp.login('xusxue@grasp.com.cn','abcd+123456789')
    smtp.sendmail(mail_from,mail_to,msg.as_string())
    smtp.quit()
    print 'email has send out !'
#查找测试报告，调用发邮件功能
def sendreport():
    result = 'D:\\resault.html'
    lists=os.listdir(result)
    lists.sort(key=lambda fn: os.path.getmtime(result+"\\"+fn) if not
    os.path.isdir(result+"\\"+fn) else 0)
    print (u'最新测试生成的报告： '+lists[-1])
    #找到最新生成的文件
    file_new = os.path.join(result,lists[-1])
    print file_new
    #调用发邮件模块
    sendmail(file_new)
    '''

testunit=unittest.TestSuite()
testunit.addTest(unittest.makeSuite(order.orderTest))
testunit.addTest(unittest.makeSuite(ordercreateandcheck.ordercreateandcheckTest))
testunit.addTest(unittest.makeSuite(ordersearch.orderSearchtest))
'''
runner=unittest.TextTestRunner()
runner.run(testunit)
'''
filename='D:\\resault.html'
fp=file(filename,'wb')
runner=HTMLTestRunner.HTMLTestRunner(
       stream=fp,
       title=u'测试报告',
       description=u'用例执行情况'                              
                                     )
runner.run(testunit)
#sendreport()
