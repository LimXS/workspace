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

class seriesnostateselTest(unittest.TestCase):
    u'''库存-序列号管理-序列号状态查询'''

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

    def testseriesnostateSale(self):
        u'''库存-序列号管理-序列号状态查询'''
        header={'cookie':self.cookiestr,"Content-Type": "application/json"}
        comdom=xml.dom.minidom.parse(r'C:\workspace\nufeeb.button\data\commonlocation')
        dom = xml.dom.minidom.parse(r'C:\workspace\nufeeb.button\instock\instocklocation')

        modulename=browser.xmlRead(dom,"module",0)
        moduledetail=browser.xmlRead(dom,'moduledetail',11)
        moduledd=browser.xmlRead(dom,'moduledd',5)

        browser.openModule3(self.driver,modulename,moduledetail,moduledd)
        cookies=browser.cookieSave(self.driver)


        #页面id
        #pageurl=browser.xmlRead(dom,"chprurl",0)
        #pageid=browser.getalertid(pageurl,header)
        #print pageid

        #commid,id
        commid=browser.getallcommonid(comdom)


        try:
            browser.exjscommin(self.driver,"取消")
            browser.openModule3(self.driver,modulename,moduledetail,moduledd)
            browser.exjscommin(self.driver,"另存为")
            browser.exjscommin(self.driver,"取消")
            browser.exjscommin(self.driver,"另存为")
            js="$(\"input[id$=txtconfigname]\").last().val('solution"+str(browser.getrandnumber())+"')"
            browser.delaytime(1)
            browser.excutejs(self.driver,js)
            browser.exjscommin(self.driver,"确定")
            browser.exjscommin(self.driver,"删除")
            js="$(\"input[id$=DateType_radio1]\").click()"
            browser.delaytime(1)
            browser.excutejs(self.driver,js)
            browser.exjscommin(self.driver,"确定")
            browser.exjscommin(self.driver,"序列号跟踪")
            browser.exjscommin(self.driver,"退出")
            browser.exjscommin(self.driver,"查询")

            jssupp="$(\"input[id$=edBTypeSupply]\").last().attr(\"id\",\"suppid\");$(\"input[id$=edBTypeConsume]\").last().attr(\"id\",\"conid\");"
            jscate="$(\"input[id$=edKType]\").last().attr(\"id\",\"edKType\");$(\"input[id$=edPType]\").last().attr(\"id\",\"edPType\");"
            browser.delaytime(1)
            browser.excutejs(self.driver,jssupp)
            browser.excutejs(self.driver,jscate)

            #来源
            browser.selcondition(self.driver,"suppid",1)

            #去向
            browser.selcondition(self.driver,"conid",1)

            #仓库
            browser.passpeoplesel(self.driver,"edKType")

            #商品
            browser.selcondition(self.driver,"edPType")

            browser.exjscommin(self.driver,"确定")

            #筛选
            js1="$(\"input[id$=edColumns]\").attr(\"id\",\"selid\")"
            js2="$(\"div:contains('商品编号')\").last().attr(\"id\",\"seitid\")"
            js3="$(\"input[id$=edValue]\").attr(\"value\",\"a1\")"
            browser.selectit(self.driver,js1,"selid",js2,"seitid",js3)

            #退出
            browser.exjscommin(self.driver,"退出")
            browser.openModule3(self.driver,modulename,moduledetail,moduledd)


        except:
            print traceback.format_exc()
            filename=browser.xmlRead(dom,'filename',0)
            browser.getpicture(self.driver,filename+u"库存-序列号管理-序列号状态查询.png")



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
