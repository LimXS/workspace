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

class itempricemanTest(unittest.TestCase):
    u'''批零-物价管理'''

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


    def testitempriceMan(self):
        u'''批零-物价管理'''
        dom = xml.dom.minidom.parse(r'C:\workspace\nufeeb.button\saleretail\salelocation')
        modulename=browser.xmlRead(dom,"module",0)
        moduledetail=browser.xmlRead(dom,'moduledetail',10)

        browser.openModule2(self.driver,modulename,moduledetail)
        browser.delaytime(3,self.driver)

        try:
            #翻页
            browser.pagechoice(self.driver)
            browser.exjscommin(self.driver,"关闭")
            browser.openModule2(self.driver,modulename,moduledetail)
            browser.exjscommin(self.driver,"选中")
            #修改售价
            browser.exjscommin(self.driver,"修改售价")
            browser.exjscommin(self.driver,"取消")
            browser.exjscommin(self.driver,"修改售价")
            js="$(\"input[id$=preprice]\").val('30')"
            browser.delaytime(1)
            browser.excutejs(self.driver,js)
            browser.exjscommin(self.driver,"确定")
            browser.exjscommin(self.driver,"选择商品")
            browser.exjscommin(self.driver,"关闭")
            browser.exjscommin(self.driver,"退出")

            browser.openModule2(self.driver,modulename,moduledetail)
            browser.exjscommin(self.driver,"选择一类")
            browser.exjscommin(self.driver,"选择商品")
            browser.exjscommin(self.driver,"全部")
            #翻页
            browser.pagechoice(self.driver)
            #批量修改
            jschone="$(\"input[type=checkbox]\").eq(4).click()"
            jschtwo="$(\"input[type=checkbox]\").eq(5).click()"
            browser.delaytime(1)
            browser.excutejs(self.driver,jschone)
            browser.excutejs(self.driver,jschtwo)
            browser.exjscommin(self.driver,"批量修改")
            browser.exjscommin(self.driver,"取消")
            browser.exjscommin(self.driver,"批量修改")
            browser.exjscommin(self.driver,"确定")

            #筛选
            js1="$(\"input[id$=edColumns]\").attr(\"id\",\"selid\")"
            js2="$(\"div:contains('商品编号')\").last().attr(\"id\",\"seitid\")"
            js3="$(\"input[id$=edValue]\").attr(\"value\",\"a1\")"
            browser.selectit(self.driver,js1,"selid",js2,"seitid",js3)

            #退出
            browser.exjscommin(self.driver,"退出")
            browser.openModule2(self.driver,modulename,moduledetail)



        except:
            print traceback.format_exc()
            filename=browser.xmlRead(dom,'filename',0)
            #print filename+u"常用-单据草稿.png"
            #browser.getpicture(self.driver,filename+u"notedraft.png")
            browser.getpicture(self.driver,filename+u"批零-物价管理.png")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
