#*-* coding:UTF-8 *-*
'''
Created on 2016��4��5��

@author: xsx
'''

import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

import unittest
import HTMLTestRunner
import time,os
import smtplib
from email.mime.text import MIMEText

from common import base

from weidian import orderweiCase
from weidian import itemsweiCase

from mengdian import ordermengCase
from mengdian import itemsmengCase

from rerendian import orderrenrenCase
from rerendian import itemsrenrenCase


from youzan import orderyouzanCase
from youzan import itemsyouzanCase

from mushroomstreet import ordermushroomCase
from mushroomstreet import itemsmushroomCase
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


testunit.addTest(unittest.makeSuite(itemsweiCase.itemsweiTest))
#testunit.addTest(unittest.makeSuite(itemsmengCase.itemsmengTest))
testunit.addTest(unittest.makeSuite(itemsrenrenCase.itemsrenrenTest))
testunit.addTest(unittest.makeSuite(itemsyouzanCase.itemsyouzanTest))
testunit.addTest(unittest.makeSuite(itemsmushroomCase.itemsmushroomTest))


testunit.addTest(unittest.makeSuite(orderweiCase.orderweiTest))
'''

testunit.addTest(unittest.makeSuite(ordermengCase.orderMengTest))

'''
testunit.addTest(unittest.makeSuite(orderrenrenCase.orderrenrenTest))


testunit.addTest(unittest.makeSuite(orderyouzanCase.orderyouzanTest))


testunit.addTest(unittest.makeSuite(ordermushroomCase.ordermushroomTest))

'''
runner=unittest.TextTestRunner()
runner.run(testunit)
'''
filename='D:\\apiresault.html'
fp=file(filename,'wb')
runner=HTMLTestRunner.HTMLTestRunner(
       stream=fp,
       title=u'测试报告',
       description=u'用例执行情况'                              
                                     )
runner.run(testunit)