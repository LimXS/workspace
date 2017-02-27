import os
import sys
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)


from common import browserClass
browser=browserClass.browser()
filesize=browser.getdirsize(r'D:\screentestpic')
To1="1206626163@qq.com"
To2="625499968@qq.com"
To3="1344875134@qq.com"
if filesize>0:
    browser.zip_dir(r"D:\\screentestpic",r"D:\\beefunbutton.zip")
    browser.sendemail(To1,2)
    browser.sendemail(To1)
    browser.sendemail(To2,2)
    print "send mail ok..."

else:
    browser.sendemail(To1)
    print "test ok..."

