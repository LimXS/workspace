#*-* coding:UTF-8 *-*
import time
import unittest
import  xml.dom.minidom
import traceback
import requests
import re
import json
from common import browserClass
browser=browserClass.browser()

class salemonthTest(unittest.TestCase):
    u'''报表-批发零售报表-商品销售统计月报'''

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
        #self.driver.close()
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


    def testSalemonth(self):
        u'''报表-批发零售报表-商品销售统计月报'''

        header={'cookie':self.cookiestr,"Content-Type": "application/json"}
        header2={'cookie':self.cookiestr,"Content-Type": "application/x-www-form-urlencoded"}

        stamp=browser.gettimestamp(1)

        #报表页面
        dom = xml.dom.minidom.parse(r'C:\workspace\moc.pjgsw.nufeeb\src\salereports\salereportsxpath')

        module1=browser.xmlRead(self.driver,dom,"module",2)
        module2=browser.xmlRead(self.driver,dom,'moduledetail',2)
        module3=browser.xmlRead(self.driver,dom,'moduledetail2',2)
        #browser.openModule3(self.driver,module1,module2,module3)
        browser.findXpath(self.driver,module1).click()
        browser.findXpath(self.driver,module2).click()
        browser.findXpath(self.driver,module3).click()

        time.sleep(2)
        cookie2 = [item["name"] + "=" + item["value"] for item in self.driver.get_cookies()]
        #print cookie
        cookiestr2 = ';'.join(item for item in cookie2)
        header3={'cookie':cookiestr2,"Content-Type": "application/json"}
        header4={'cookie':cookiestr2,"Content-Type": "application/x-www-form-urlencoded"}

        #页面Id
        reurlid="http://beefun.wsgjp.com/Beefun/VipMember/VipMemberIntegralRecodList.gspx"
        retext=browser.handleorderRead(self.driver,reurlid,header3)
        #print retext
        repageid=browser.getpageid(retext,1)
        print repageid

        #report list
        reurl="http://beefun.wsgjp.com/Carpa.Web/Carpa.Web.Script.DataService.ajax/GetPagerData"
        data={"pagerId":repageid,"queryParams":None,"orders":None,"filter":None,"first":0,"count":100000}
        repadetail=browser.pagedetail(reurl,data,header3)
        print repadetail


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()