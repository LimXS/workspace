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
import instockClass
browser=instockClass.instockclass()

class seriesnotraceTest(unittest.TestCase):
    u'''库存-序列号管理-序列号跟踪'''

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

    def testseriesnoTrace(self):
        u'''库存-序列号管理-序列号跟踪'''
        dom = xml.dom.minidom.parse(r'C:\workspace\proxynufeeb.button\instock\instocklocation')

        modulename=browser.xmlRead(dom,"module",0)
        moduledetail=browser.xmlRead(dom,'moduledetail',11)
        moduledd=browser.xmlRead(dom,'moduledd',4)

        browser.openModule3(self.driver,modulename,moduledetail,moduledd)


        try:
            browser.exjscommin(self.driver,"取消")
            browser.openModule3(self.driver,modulename,moduledetail,moduledd)
            browser.exjscommin(self.driver,"确定")
            browser.exjscommin(self.driver,"取消")
            browser.openModule3(self.driver,modulename,moduledetail,moduledd)
            browser.exjscommin(self.driver,"确定")
            browser.exjscommin(self.driver,"确定")



            #查询条件
            browser.exjscommin(self.driver,"查询条件")
            jscom="$(\"input[id$=edBType]\").last().attr(\"id\",\"edBType\")"
            jscate="$(\"input[id$=edKType]\").last().attr(\"id\",\"edKType\")"
            jsitem="$(\"input[id$=edPType]\").last().attr(\"id\",\"edPType\")"
            browser.delaytime(1)
            browser.excutejs(self.driver,jscom)
            browser.excutejs(self.driver,jscate)
            browser.excutejs(self.driver,jsitem)

            browser.selcondition(self.driver,"edBType",1)
            browser.passpeoplesel(self.driver,"edKType")
            browser.selcondition(self.driver,"edPType")

            browser.exjscommin(self.driver,"确定")

            browser.exjscommin(self.driver,"查询条件")
            jsstrat="$(\"input[id$=StartDate]\").val('2016-10-22')"
            jsend="$(\"input[id$=EndDate]\").val('2016-10-28')"
            browser.delaytime(1)
            browser.excutejs(self.driver,jsstrat)
            browser.excutejs(self.driver,jsend)
            browser.exjscommin(self.driver,"确定")

            #查看单据
            browser.exjscommin(self.driver,"查看单据")
            browser.exjscommin(self.driver,"退出")

            #翻页
            browser.pagechoice(self.driver)

            #筛选
            '''
            js1="$(\"input[id$=edColumns]\").attr(\"id\",\"selid\")"
            js2="$(\"div:contains('商品编号')\").last().attr(\"id\",\"seitid\")"
            js3="$(\"input[id$=edValue]\").attr(\"value\",\"a1\")"
            '''
            browser.selectbycon(self.driver,u"商品编号",u"中文测试饕餮壹贰！@#￥%^ &*（）12；sdfs fsd")

            #退出
            browser.exjscommin(self.driver,"退出")
            browser.openModule3(self.driver,modulename,moduledetail,moduledd)



        except:
            print traceback.format_exc()
            filename=browser.xmlRead(dom,'filename',0)
            browser.getpicture(self.driver,filename+u"库存-序列号管理-序列号跟踪.png")



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
