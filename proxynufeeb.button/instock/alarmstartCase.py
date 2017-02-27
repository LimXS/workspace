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

class alarmstartTest(unittest.TestCase):
    u'''库存-库存报警-启动库存薄'''

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

    def testalarmStart(self):
        u'''库存-库存报警-启动库存薄.'''
        dom = xml.dom.minidom.parse(r'C:\workspace\proxynufeeb.button\instock\instocklocation')

        modulename=browser.xmlRead(dom,"module",0)
        moduledetail=browser.xmlRead(dom,'moduledetail',10)
        moduledd=browser.xmlRead(dom,'moduledd',0)

        browser.openModule3(self.driver,modulename,moduledetail,moduledd)

        try:
            jsdown="$(\"div[class=TreeNodeText]:contains('下')\").click()"
            jsup="$(\"div[class=TreeNodeText]:contains('上')\").click()"
            jsall="$(\"div[class=TreeNodeText]:contains('列表')\").click()"

            browser.delaytime(1)
            browser.excutejs(self.driver,jsdown)
            browser.excutejs(self.driver,jsall)
            browser.excutejs(self.driver,jsup)
            browser.exjscommin(self.driver,"确")

            browser.openModule3(self.driver,modulename,moduledetail,moduledd)

        except:
            print traceback.format_exc()
            filename=browser.xmlRead(dom,'filename',0)
            browser.getpicture(self.driver,filename+u"库存-库存报警-启动库存薄.png")

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
