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

class entruststockselTest(unittest.TestCase):
    u'''批零-委托代销-委托库存查询'''

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


    def testentruststockSel(self):
        u'''批零-委托代销-委托库存查询'''
        header={'cookie':self.cookiestr,"Content-Type": "application/json"}
        comdom=xml.dom.minidom.parse(r'C:\workspace\proxynufeeb.button\data\commonlocation')
        dom = xml.dom.minidom.parse(r'C:\workspace\proxynufeeb.button\saleretail\salelocation')

        modulename=browser.xmlRead(dom,"module",0)
        moduledetail=browser.xmlRead(dom,'moduledetail',6)
        moduledd=browser.xmlRead(dom,'moduledd',3)

        browser.openModule3(self.driver,modulename,moduledetail,moduledd)

        cookies=browser.cookieSave(self.driver)
        header3={'cookie':cookies,"Content-Type": "application/json"}
        header4={'cookie':cookies,"Content-Type": "application/x-www-form-urlencoded"}

        #页面id
        pageurl=browser.xmlRead(dom,"enstockurl",0)
        pageid=browser.getalertid(pageurl,header)
        #print pageid

        #commid,id
        commid=browser.getallcommonid(comdom)
        #id=browser.getcommonid(dom)

        try:
            #往来单位
            companyid=pageid+browser.xmlRead(dom,'edBType',0)
            #print companyid
            browser.delaytime(1,self.driver)
            browser.doubleclick(self.driver,companyid)
            #-翻页
            browser.pagechoice(self.driver)
            browser.exjscommin(self.driver,"选中")
            browser.doubleclick(self.driver,companyid)
            browser.exjscommin(self.driver,"查看单位基本信息")
            browser.exjscommin(self.driver,"关闭")
            browser.exjscommin(self.driver,"全部")
            browser.doubleclick(self.driver,companyid)
            browser.exjscommin(self.driver,"关闭")

            #单位分布表
            browser.exjscommin(self.driver,"单位分布表")
            browser.exjscommin(self.driver,"退出")

            #明细账本
            browser.exjscommin(self.driver,"明细账本")
            browser.exjscommin(self.driver,"关闭")
            browser.exjscommin(self.driver,"明细账本")
            browser.exjscommin(self.driver,"确定")
            browser.exjscommin(self.driver,"查看单据")
            browser.exjscommin(self.driver,"退出")
            browser.exjscommin(self.driver,"退出")

            #列表
            browser.exjscommin(self.driver,"列表")
            browser.exjscommin(self.driver,"取消")
            browser.exjscommin(self.driver,"列表")
            browser.exjscommin(self.driver,"确定")
            browser.exjscommin(self.driver,"明细账本")
            browser.exjscommin(self.driver,"关闭")
            browser.exjscommin(self.driver,"明细账本")
            browser.exjscommin(self.driver,"确定")
            browser.exjscommin(self.driver,"查看单据")
            browser.exjscommin(self.driver,"退出")
            browser.exjscommin(self.driver,"退出")
            browser.exjscommin(self.driver,"退出")

            #翻页
            browser.pagechoice(self.driver)

            #筛选
            js1="$(\"input[id$=edColumns]\").attr(\"id\",\"selid\")"
            js2="$(\"div:contains('商品编号')\").last().attr(\"id\",\"seitid\")"
            js3="$(\"input[id$=edValue]\").attr(\"value\",\"a1\")"
            browser.selectit(self.driver,js1,"selid",js2,"seitid",js3)

            #打印

            #退出
            exid=pageid+commid["selclose"]
            browser.findId(self.driver,exid).click()
            browser.openModule3(self.driver,modulename,moduledetail,moduledd)

        except:
            print traceback.format_exc()
            filename=browser.xmlRead(dom,'filename',0)
            #print filename+u"常用-单据草稿.png"
            #browser.getpicture(self.driver,filename+u"notedraft.png")
            browser.getpicture(self.driver,filename+u"批零-委托代销-委托库存查询.png")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
