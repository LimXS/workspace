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

class createstockfewTest(unittest.TestCase):
    u'''库存-报损单'''
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

    def testcreatestockFew(self):
        u'''库存-报损单'''
        dom = xml.dom.minidom.parse(r'C:\workspace\moc.pjgsw.nufeeb\src\data\invenstockdata')
        module='module'
        modulename=browser.xmlRead(self.driver,dom,module,1)
        moduledetail=browser.xmlRead(self.driver,dom,'moduledetail',1)

        browser.openModule2(self.driver,modulename,moduledetail)

        try:
            #经手人
            handlepeople=browser.xmlRead(self.driver,dom,"handlepeople",1)
            selectpeople=browser.xmlRead(self.driver,dom,"selectpeople",1)
            selectpook=browser.xmlRead(self.driver,dom,"selectpook",1)

            browser.findXpath(self.driver,handlepeople).click()
            browser.findXpath(self.driver,selectpeople).click()
            browser.findXpath(self.driver,selectpook).click()

            #部门
            department=browser.xmlRead(self.driver,dom,"department",1)
            selectde=browser.xmlRead(self.driver,dom,"selectde",1)
            seldecok=browser.xmlRead(self.driver,dom,"seldecok",1)

            browser.findXpath(self.driver,department).click()
            browser.findXpath(self.driver,selectde).click()
            browser.findXpath(self.driver,seldecok).click()

            #出库仓库
            cate=browser.xmlRead(self.driver,dom,"cate",1)
            selectcate=browser.xmlRead(self.driver,dom,"selectcate",1)
            selectcaok=browser.xmlRead(self.driver,dom,"selectcaok",1)

            browser.findXpath(self.driver,cate).click()
            browser.findXpath(self.driver,selectcate).click()
            browser.findXpath(self.driver,selectcaok).click()

            #摘要
            summary=browser.xmlRead(self.driver,dom,"summary",1)
            browser.findXpath(self.driver,summary).send_keys(u"我是摘要报损单23333333333................")

            #附加说明
            comment=browser.xmlRead(self.driver,dom,"comment",1)
            browser.findXpath(self.driver,comment).send_keys(u"我是附加说明报损单23333333333................")

        except:
            print u"单据头设置失败"
            print(traceback.format_exc())

        try:
            #商品名称
            itemname=browser.xmlRead(self.driver,dom,"itemname",1)
            itemselect=browser.xmlRead(self.driver,dom,"itemselect",1)
            itemseleinput=browser.xmlRead(self.driver,dom,"itemseleinput",1)
            itemselectok=browser.xmlRead(self.driver,dom,"itemselectok",1)

            browser.findXpath(self.driver,itemname).click()
            browser.findXpath(self.driver,itemselect).click()
            time.sleep(2)
            browser.findXpath(self.driver,itemseleinput).click()
            browser.findXpath(self.driver,itemselectok).click()

            #数量
            itemnumber=browser.xmlRead(self.driver,dom,"itemnumber",1)
            browser.findXpath(self.driver,itemnumber).send_keys("2")

        except:
            print u"单据明细商品信息设置失败"
            print(traceback.format_exc())

        #保存单据
        try:
            saveorexit=browser.xmlRead(self.driver,dom,"saveorexit",1)
            browser.findXpath(self.driver,saveorexit).click()
            savenote=browser.xmlRead(self.driver,dom,"savenote",1)
            browser.findXpath(self.driver,savenote).click()
        except:
            print u"单据保存失败"
            print(traceback.format_exc())

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
