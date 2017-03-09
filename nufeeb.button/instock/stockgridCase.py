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

class stockgridTest(unittest.TestCase):
    u'''库存-库存分布表'''

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

    def teststockGrid(self):
        u'''库存-库存分布表.'''
        header={'cookie':self.cookiestr,"Content-Type": "application/json"}
        comdom=xml.dom.minidom.parse(r'C:\workspace\nufeeb.button\data\commonlocation')
        dom = xml.dom.minidom.parse(r'C:\workspace\nufeeb.button\instock\instocklocation')

        modulename=browser.xmlRead(dom,"module",0)
        moduledetail=browser.xmlRead(dom,'moduledetail',7)

        browser.openModule2(self.driver,modulename,moduledetail)
        cookies=browser.cookieSave(self.driver)


        #页面id
        #pageurl=browser.xmlRead(dom,"chprurl",0)
        #pageid=browser.getalertid(pageurl,header)
        #print pageid

        #commid,id
        commid=browser.getallcommonid(comdom)


        try:
            browser.exjscommin(self.driver,"关闭")
            browser.openModule2(self.driver,modulename,moduledetail)
            browser.exjscommin(self.driver,"确定")

            #翻页
            browser.delaytime(1,self.driver)
            browser.pagechoice(self.driver)

            #筛选
            js1="$(\"input[id$=edColumns]\").attr(\"id\",\"selid\")"
            js2="$(\"div:contains('商品编号')\").last().attr(\"id\",\"seitid\")"
            js3="$(\"input[id$=edValue]\").attr(\"value\",\"a1\")"
            browser.selectit(self.driver,js1,"selid",js2,"seitid",js3)
            browser.exjscommin(self.driver,"退出")

            browser.openModule2(self.driver,modulename,moduledetail)
            browser.exjscommin(self.driver,"确定")

            #价格方式
            browser.exjscommin(self.driver,"价格方式")
            browser.exjscommin(self.driver,"取消")
            browser.exjscommin(self.driver,"价格方式")
            browser.exjscommin(self.driver,"确定")
            browser.exjscommin(self.driver,"价格方式")
            js="$(\"label[for$=pricemode_radio1]\").click()"
            browser.delaytime(1)
            browser.excutejs(self.driver,js)
            browser.exjscommin(self.driver,"确定")

            #明细账本
            browser.elementcontains(self.driver,"div","a1x","seliditem")
            browser.findId(self.driver,"seliditem").click()
            jsdetail="$(\"button[id$=btnDetail]\").attr(\"id\",\"detailid\")"
            browser.delaytime(1)
            browser.excutejs(self.driver,jsdetail)
            browser.detailaccbook(self.driver,"detailid")

            #查询条件
            js1="$(\"input[id$=edPType]\").attr(\"id\",\"selitid\")"
            browser.delaytime(2)
            browser.selcon(self.driver,js1,"selitid")

            #退出
            browser.exjscommin(self.driver,"退出")
            browser.openModule2(self.driver,modulename,moduledetail)
            browser.exjscommin(self.driver,"确定")



        except:
            print traceback.format_exc()
            filename=browser.xmlRead(dom,'filename',0)
            browser.getpicture(self.driver,filename+u"库存-库存分布表.png")



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
