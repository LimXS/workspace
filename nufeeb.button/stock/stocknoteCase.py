#*-* coding:UTF-8 *-*
import time
import re
import datetime
import unittest
import  xml.dom.minidom
import traceback
import requests
import json
from common import browserClass
browser=browserClass.browser()

class stocknoteTest(unittest.TestCase):
    u'''进货-进货开票'''

    def setUp(self):
        self.driver=browser.startBrowser('chrome')
        browser.set_up(self.driver)
        cookie = [item["name"] + "=" + item["value"] for item in self.driver.get_cookies()]
        #print cookie
        self.cookiestr = ';'.join(item for item in cookie)

        time.sleep(2)
        pass


    def tearDown(self):
        print "test over"
        self.driver.close()
        pass



    def teststockNote(self):
        u'''进货-进货开票.'''
        header={'cookie':self.cookiestr,"Content-Type": "application/json"}
        comdom=xml.dom.minidom.parse(r'C:\workspace\nufeeb.button\data\commonlocation')
        dom = xml.dom.minidom.parse(r'C:\workspace\nufeeb.button\stock\stocklocation')

        modulename=browser.xmlRead(dom,"module",0)
        moduledetail=browser.xmlRead(dom,'moduledetail',6)

        browser.openModule2(self.driver,modulename,moduledetail)
        cookies=browser.cookieSave(self.driver)
        header3={'cookie':cookies,"Content-Type": "application/json"}
        header4={'cookie':cookies,"Content-Type": "application/x-www-form-urlencoded"}


        #commid,id
        commid=browser.getallcommonid(comdom)

        try:
            browser.exjscommin(self.driver,"关闭")
            browser.openModule2(self.driver,modulename,moduledetail)
            browser.exjscommin(self.driver,"确定")

            #查询条件
            browser.exjscommin(self.driver,"查询条件")
            browser.exjscommin(self.driver,"关闭")
            browser.exjscommin(self.driver,"查询条件")
            browser.exjscommin(self.driver,"确定")

            #查看单据
            browser.exjscommin(self.driver,"查看单据")
            browser.openModule2(self.driver,modulename,moduledetail)
            browser.exjscommin(self.driver,"确定")


            #修改开票金额
            browser.exjscommin(self.driver,"修改开票金额")
            browser.exjscommin(self.driver,"关闭")
            browser.exjscommin(self.driver,"修改开票金额")
            browser.exjscommin(self.driver,"确定")

            #筛选
            js="$(\"span:contains('筛选')\").click()"
            browser.excutejs(self.driver,js)
            browser.exjscommin(self.driver,"取消")
            browser.excutejs(self.driver,js)
            js="$(\"input[id$=edColumns]\").attr(\"id\",\"selid\")"
            browser.excutejs(self.driver,js)
            browser.doubleclick(self.driver,"selid")
            js="$(\"div:contains('单位名称')\").last().click()"
            browser.excutejs(self.driver,js)
            browser.exjscommin(self.driver,"筛选")

            #翻页
            browser.pagechoice(self.driver)

            #退出
            browser.exjscommin(self.driver,"退出")
            browser.openModule2(self.driver,modulename,moduledetail)
            browser.exjscommin(self.driver,"确定")


        except:
            print traceback.format_exc()
            filename=browser.xmlRead(dom,'filename',0)
            #print filename+u"常用-单据草稿.png"
            #browser.getpicture(self.driver,filename+u"notedraft.png")
            browser.getpicture(self.driver,filename+u"进货-进货开票.png")



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
