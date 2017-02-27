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

class createstockotherintoTest(unittest.TestCase):
    u'''库存-其他入库单'''
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

    def testcreatestockotherInto(self):
        u'''库存-其他入库单'''
        dom = xml.dom.minidom.parse(r'C:\workspace\moc.pjgsw.nufeeb\src\data\invenstockdata')
        module='module'
        modulename=browser.xmlRead(self.driver,dom,module,2)
        moduledetail=browser.xmlRead(self.driver,dom,'moduledetail',2)

        browser.openModule2(self.driver,modulename,moduledetail)
        try:
            #供货单位
            othercompany=browser.xmlRead(self.driver,dom,"othercompany",0)
            othercomsele=browser.xmlRead(self.driver,dom,"othercomsele",0)
            othercoseok=browser.xmlRead(self.driver,dom,"othercoseok",0)

            browser.findXpath(self.driver,othercompany).click()
            browser.findXpath(self.driver,othercomsele).click()
            browser.findXpath(self.driver,othercoseok).click()

            #经手人
            otherpeople=browser.xmlRead(self.driver,dom,"otherpeople",0)
            otherpeosele=browser.xmlRead(self.driver,dom,"otherpeosele",0)
            otherpeook=browser.xmlRead(self.driver,dom,"otherpeook",0)

            browser.findXpath(self.driver,otherpeople).click()
            browser.findXpath(self.driver,otherpeosele).click()
            browser.findXpath(self.driver,otherpeook).click()

            #部门
            otherdepartment=browser.xmlRead(self.driver,dom,"otherdepartment",0)
            otherdeselect=browser.xmlRead(self.driver,dom,"otherdeselect",0)
            otherdeok=browser.xmlRead(self.driver,dom,"otherdeok",0)

            browser.findXpath(self.driver,otherdepartment).click()
            browser.findXpath(self.driver,otherdeselect).click()
            browser.findXpath(self.driver,otherdeok).click()

            #入库仓库
            othercate=browser.xmlRead(self.driver,dom,"othercate",0)
            othercateselect=browser.xmlRead(self.driver,dom,"othercateselect",0)
            othercaseok=browser.xmlRead(self.driver,dom,"othercaseok",0)

            browser.findXpath(self.driver,othercate).click()
            browser.findXpath(self.driver,othercateselect).click()
            browser.findXpath(self.driver,othercaseok).click()

            #摘要
            othersummary=browser.xmlRead(self.driver,dom,"othersummary",0)
            browser.findXpath(self.driver,othersummary).send_keys(u"我是摘要其他入库单23333333333................")

            #附加说明
            othercomment=browser.xmlRead(self.driver,dom,"othercomment",0)
            browser.findXpath(self.driver,othercomment).send_keys(u"我是附加说明其他入库单23333333333................")
        except:
            print u"单据头设置失败"
            print(traceback.format_exc())


        try:
            #商品名称
            otheritemname=browser.xmlRead(self.driver,dom,"otheritemname",0)
            otheritemsele=browser.xmlRead(self.driver,dom,"otheritemsele",0)
            otheriteminput=browser.xmlRead(self.driver,dom,"otheriteminput",0)
            otheritemok=browser.xmlRead(self.driver,dom,"otheritemok",0)

            browser.findXpath(self.driver,otheritemname).click()
            browser.findXpath(self.driver,otheritemsele).click()
            time.sleep(1)
            browser.findXpath(self.driver,otheriteminput).click()
            browser.findXpath(self.driver,otheritemok).click()

            #数量
            otheritemnumber=browser.xmlRead(self.driver,dom,"otheritemnumber",0)
            browser.findXpath(self.driver,otheritemnumber).send_keys("9")

        except:
            print u"单据明细商品信息设置失败"
            print(traceback.format_exc())

        #保存单据
        try:
            othersaveanexit=browser.xmlRead(self.driver,dom,"othersaveanexit",0)
            browser.findXpath(self.driver,othersaveanexit).click()
            othersaveok=browser.xmlRead(self.driver,dom,"othersaveok",0)
            browser.findXpath(self.driver,othersaveok).click()
        except:
            print u"单据保存失败"
            print(traceback.format_exc())



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
