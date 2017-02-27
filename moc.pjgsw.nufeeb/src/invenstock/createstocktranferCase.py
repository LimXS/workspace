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

class createstocktranferTest(unittest.TestCase):
    u'''库存-调拨单'''
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

    def testcreatestockTranfer(self):
        u'''库存-调拨单'''
        dom = xml.dom.minidom.parse(r'C:\workspace\moc.pjgsw.nufeeb\src\data\invenstockdata')
        module='module'
        modulename=browser.xmlRead(self.driver,dom,module,4)
        moduledetail=browser.xmlRead(self.driver,dom,'moduledetail',4)

        browser.openModule2(self.driver,modulename,moduledetail)

        try:
            #发货仓库
            transendcate=browser.xmlRead(self.driver,dom,"transendcate",0)
            transecaselect=browser.xmlRead(self.driver,dom,"transecaselect",0)
            transecaseok=browser.xmlRead(self.driver,dom,"transecaseok",0)

            browser.findXpath(self.driver,transendcate).click()
            browser.findXpath(self.driver,transecaselect).click()
            browser.findXpath(self.driver,transecaseok).click()

            #经手人
            trpeople=browser.xmlRead(self.driver,dom,"trpeople",0)
            trselectpeo=browser.xmlRead(self.driver,dom,"trselectpeo",0)
            trsepeook=browser.xmlRead(self.driver,dom,"trsepeook",0)

            browser.findXpath(self.driver,trpeople).click()
            browser.findXpath(self.driver,trselectpeo).click()
            browser.findXpath(self.driver,trsepeook).click()

            #部门
            trandepartment=browser.xmlRead(self.driver,dom,"trandepartment",0)
            trandeselect=browser.xmlRead(self.driver,dom,"trandeselect",0)
            trandeseok=browser.xmlRead(self.driver,dom,"trandeseok",0)

            browser.findXpath(self.driver,trandepartment).click()
            browser.findXpath(self.driver,trandeselect).click()
            browser.findXpath(self.driver,trandeseok).click()

            #收货仓库
            tranincate=browser.xmlRead(self.driver,dom,"tranincate",0)
            trabinselectcate=browser.xmlRead(self.driver,dom,"trabinselectcate",0)
            traninsecateok=browser.xmlRead(self.driver,dom,"traninsecateok",0)

            browser.findXpath(self.driver,tranincate).click()
            browser.findXpath(self.driver,trabinselectcate).click()
            browser.findXpath(self.driver,traninsecateok).click()

            #摘要
            transummary=browser.xmlRead(self.driver,dom,"transummary",0)
            browser.findXpath(self.driver,transummary).send_keys(u"我是摘要调拨单23333333333................")

            #附加说明
            trancomment=browser.xmlRead(self.driver,dom,"trancomment",0)
            browser.findXpath(self.driver,trancomment).send_keys(u"我是附加说明调拨单23333333333................")


        except:
            print u"单据头设置失败"
            print(traceback.format_exc())


        try:
            #商品名称
            tranitemname=browser.xmlRead(self.driver,dom,"tranitemname",0)
            tranitemsele=browser.xmlRead(self.driver,dom,"tranitemsele",0)
            traniteminput=browser.xmlRead(self.driver,dom,"traniteminput",0)
            tranitemok=browser.xmlRead(self.driver,dom,"tranitemok",0)

            browser.findXpath(self.driver,tranitemname).click()
            browser.findXpath(self.driver,tranitemsele).click()
            time.sleep(2)
            browser.findXpath(self.driver,traniteminput).click()
            browser.findXpath(self.driver,tranitemok).click()

            #数量
            tranitemnumbers=browser.xmlRead(self.driver,dom,"tranitemnumbers",0)
            browser.findXpath(self.driver,tranitemnumbers).send_keys("3")

        except:
            print u"单据明细商品信息设置失败"
            print(traceback.format_exc())

        #保存单据
        try:
            transaveandexit=browser.xmlRead(self.driver,dom,"transaveandexit",0)
            browser.findXpath(self.driver,transaveandexit).click()
            transaveok=browser.xmlRead(self.driver,dom,"transaveok",0)
            browser.findXpath(self.driver,transaveok).click()
        except:
            print u"单据保存失败"
            print(traceback.format_exc())


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
