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

class salenoteselTest(unittest.TestCase):
    u'''批零-销售开票'''

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


    def testsalenoteSel(self):
        u'''批零-销售开票'''
        header={'cookie':self.cookiestr,"Content-Type": "application/json"}
        comdom=xml.dom.minidom.parse(r'C:\workspace\proxynufeeb.button\data\commonlocation')
        dom = xml.dom.minidom.parse(r'C:\workspace\proxynufeeb.button\saleretail\salelocation')

        modulename=browser.xmlRead(dom,"module",0)
        moduledetail=browser.xmlRead(dom,'moduledetail',9)


        browser.openModule2(self.driver,modulename,moduledetail)


        #commid,id
        commid=browser.getallcommonid(comdom)
        #id=browser.getcommonid(dom)

        try:
            browser.exjscommin(self.driver,"关闭")
            browser.openModule2(self.driver,modulename,moduledetail)
            browser.exjscommin(self.driver,"确定")

            #查看单据
            browser.exjscommin(self.driver,"查看单据")
            browser.exjscommin(self.driver,"退出")

            #修改开票金额
            browser.exjscommin(self.driver,"修改开票金额")
            browser.exjscommin(self.driver,"关闭")
            browser.exjscommin(self.driver,"修改开票金额")
            js="$(\"input[id$=nvoicetotal]\").val('25')"
            browser.delaytime(1)
            browser.excutejs(self.driver,js)
            browser.exjscommin(self.driver,"确定")

            #筛选
            js1="$(\"input[id$=edColumns]\").attr(\"id\",\"selid\")"
            js2="$(\"div:contains('商品编号')\").last().attr(\"id\",\"seitid\")"
            js3="$(\"input[id$=edValue]\").attr(\"value\",\"a1\")"
            browser.selectit(self.driver,js1,"selid",js2,"seitid",js3)

            #查询条件
            browser.exjscommin(self.driver,"查询条件")
            js="$(\"input[id$=edbType]\").attr(\"id\",\"edbType\")"
            browser.delaytime(1)
            browser.excutejs(self.driver,js)
            browser.buycompanysel(self.driver,"edbType",1)
            browser.exjscommin(self.driver,"确定")

            #退出
            browser.exjscommin(self.driver,"退出")
            browser.openModule2(self.driver,modulename,moduledetail)
            browser.exjscommin(self.driver,"确定")
            #翻页
            browser.pagechoice(self.driver)
            browser.exjscommin(self.driver,"退出")
            browser.openModule2(self.driver,modulename,moduledetail)

        except:
            print traceback.format_exc()
            filename=browser.xmlRead(dom,'filename',0)
            #print filename+u"常用-单据草稿.png"
            #browser.getpicture(self.driver,filename+u"notedraft.png")
            browser.getpicture(self.driver,filename+u"批零-销售开票.png")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
