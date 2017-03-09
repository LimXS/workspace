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

class itemcombineTest(unittest.TestCase):
    u'''商品-商品合并'''

    def setUp(self):
        self.driver=browser.startBrowser('chrome')
        browser.set_up(self.driver)
        cookie = [item["name"] + "=" + item["value"] for item in self.driver.get_cookies()]
        #print cookie
        self.cookiestr = ';'.join(item for item in cookie)
        browser.delaytime(2)
        pass


    def tearDown(self):
        print "test over"
        self.driver.close()
        pass



    def testitemCombine(self):
        u'''商品-商品合并'''

        dom = xml.dom.minidom.parse(r'C:\workspace\nufeeb.button\itemmodule\itemlocation')
        modulename=browser.xmlRead(dom,"module",0)
        moduledetail=browser.xmlRead(dom,'moduledetail',3)

        try:
            pageid=browser.xmlRead(dom,"combinid",0)
            #print pageid


            browser.openModule2(self.driver,modulename,moduledetail)
            #commid
            commid=browser.getcommonid(dom)
            #print commid

            #查询
            itemsel=pageid+commid["button"]+str(1)
            browser.findId(self.driver,itemsel).click()

            #翻页
            browser.pagewhich(self.driver,commid["basetype"],pageid,commid["pnext"],commid["topebefore"],commid["before"],commid["topnext"])

            #确定
            itemcomfirm=pageid+commid["button"]+str(2)
            browser.findId(self.driver,itemcomfirm).click()
            browser.accAlert(self.driver,1)

            #退出
            itemcancel=pageid+commid["btnexit"]
            browser.findId(self.driver,itemcancel).click()
            browser.openModule2(self.driver,modulename,moduledetail)

            #合并
            combine=commid["basetype"]+pageid+browser.xmlRead(dom,"combinebtn",0)
            browser.findXpath(self.driver,combine).click()
            browser.accAlert(self.driver,1)
            browser.openModule2(self.driver,modulename,moduledetail)
        except:
            print traceback.format_exc()
            filename=browser.xmlRead(dom,'filename',0)
            #print filename+u"常用-单据草稿.png"
            #browser.getpicture(self.driver,filename+u"notedraft.png")
            browser.getpicture(self.driver,filename+u"商品-商品合并.png")



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
