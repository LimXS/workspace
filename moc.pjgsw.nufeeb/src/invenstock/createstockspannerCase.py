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

class createstockspannerTest(unittest.TestCase):
    u'''库存-生成组装单'''
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


    def assernote(self,num1,num2,note,noteok,flag):
        try:
            self.assertEqual(num1,num2,msg=note)
            print noteok
        except AssertionError,msg:
            print msg
            print flag
            print num1
            print num2

    def testcreatestockSpanner(self):
        u'''库存-生成组装单'''
        dom = xml.dom.minidom.parse(r'C:\workspace\moc.pjgsw.nufeeb\src\data\invenstockdata')
        module='module'
        modulename=browser.xmlRead(self.driver,dom,module,5)
        moduledetail=browser.xmlRead(self.driver,dom,'moduledetail',5)

        browser.openModule2(self.driver,modulename,moduledetail)
        try:
            #发货仓库
            transendcate=browser.xmlRead(self.driver,dom,"transendcate",1)
            transecaselect=browser.xmlRead(self.driver,dom,"transecaselect",1)
            transecaseok=browser.xmlRead(self.driver,dom,"transecaseok",1)
            browser.setheader(self.driver,transendcate,transecaselect,transecaseok)

            #经手人
            trpeople=browser.xmlRead(self.driver,dom,"trpeople",1)
            trselectpeo=browser.xmlRead(self.driver,dom,"trselectpeo",1)
            trsepeook=browser.xmlRead(self.driver,dom,"trsepeook",1)
            browser.setheader(self.driver,trpeople,trselectpeo,trsepeook)

            #部门
            trandepartment=browser.xmlRead(self.driver,dom,"trandepartment",1)
            trandeselect=browser.xmlRead(self.driver,dom,"trandeselect",1)
            trandeseok=browser.xmlRead(self.driver,dom,"trandeseok",1)
            browser.setheader(self.driver,trandepartment,trandeselect,trandeseok)

            #收货仓库
            tranincate=browser.xmlRead(self.driver,dom,"tranincate",1)
            trabinselectcate=browser.xmlRead(self.driver,dom,"trabinselectcate",1)
            traninsecateok=browser.xmlRead(self.driver,dom,"traninsecateok",1)
            browser.setheader(self.driver,tranincate,trabinselectcate,traninsecateok)

            #摘要
            transummary=browser.xmlRead(self.driver,dom,"transummary",1)
            browser.findXpath(self.driver,transummary).send_keys(u"我是摘要生成组装单23333333333................")

            #附加说明
            trancomment=browser.xmlRead(self.driver,dom,"trancomment",1)
            browser.findXpath(self.driver,trancomment).send_keys(u"我是附加说明生成组装单23333333333................")

        except:
            print u"单据头设置失败"
            print(traceback.format_exc())

        try:
            #出库商品名称
            tranitemname=browser.xmlRead(self.driver,dom,"tranitemname",1)
            tranitemsele=browser.xmlRead(self.driver,dom,"tranitemsele",1)
            traniteminput=browser.xmlRead(self.driver,dom,"traniteminput",1)
            tranitemok=browser.xmlRead(self.driver,dom,"tranitemok",1)

            browser.openModule4(self.driver,tranitemname,tranitemsele,traniteminput,tranitemok)

            #数量
            tranitemnumbers=browser.xmlRead(self.driver,dom,"tranitemnumbers",1)
            browser.findXpath(self.driver,tranitemnumbers).send_keys("3")

        except:
            print u"单据明细出库商品信息设置失败"
            print(traceback.format_exc())

        try:
            #入库商品名称
            tranitemname=browser.xmlRead(self.driver,dom,"tranitemname",2)
            tranitemsele=browser.xmlRead(self.driver,dom,"tranitemsele",2)
            traniteminput=browser.xmlRead(self.driver,dom,"traniteminput",2)
            tranitemok=browser.xmlRead(self.driver,dom,"tranitemok",2)

            browser.openModule4(self.driver,tranitemname,tranitemsele,traniteminput,tranitemok)

            #数量
            tranitemnumbers=browser.xmlRead(self.driver,dom,"tranitemnumbers",2)
            browser.findXpath(self.driver,tranitemnumbers).send_keys("3")

            #价格
            tranprice=browser.xmlRead(self.driver,dom,"tranprice",0)
            browser.findXpath(self.driver,tranprice).click()
            tranpricesend=browser.xmlRead(self.driver,dom,"tranpricesend",0)
            browser.findXpath(self.driver,tranpricesend).send_keys("15.00")

        except:
            print u"单据明细入库商品信息设置失败"
            print(traceback.format_exc())

        #保存单据
        try:
            transaveandexit=browser.xmlRead(self.driver,dom,"transaveandexit",1)
            browser.findXpath(self.driver,transaveandexit).click()
            transaveok=browser.xmlRead(self.driver,dom,"transaveok",1)
            browser.findXpath(self.driver,transaveok).click()
        except:
            print u"单据保存失败"
            print(traceback.format_exc())

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
