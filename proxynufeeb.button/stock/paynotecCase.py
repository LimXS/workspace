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

class stockpayTest(unittest.TestCase):
    u'''进货-付款单'''

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

    def teststockPay(self):
        u'''进货-付款单.'''
        header={'cookie':self.cookiestr,"Content-Type": "application/json"}
        comdom=xml.dom.minidom.parse(r'C:\workspace\proxynufeeb.button\data\commonlocation')
        dom = xml.dom.minidom.parse(r'C:\workspace\proxynufeeb.button\stock\stocklocation')

        modulename=browser.xmlRead(dom,"module",0)
        moduledetail=browser.xmlRead(dom,'moduledetail',5)

        browser.openModule2(self.driver,modulename,moduledetail)

        #页面id
        pageurl=browser.xmlRead(dom,"stpayurl",0)
        pageid=browser.getalertid(pageurl,header)
        #print pageid

        #commid,id
        commid=browser.getallcommonid(comdom)


        try:
            #付款账户名称
            itemgrid=browser.xmlRead(dom,"itemgrid",0)
            payxpath=commid["basetype"]+pageid+itemgrid+str(4)+"]"
            browser.findXpath(self.driver,payxpath).click()

            paygridid=pageid+commid["grid_fullname"]
            whichjs="$(\"div[class=GridBodyCellText]:contains('全部银行存款')\").attr(\"id\",\"allbankacc\")"
            browser.delaytime(1)
            browser.nebecompany(self.driver,paygridid,whichjs)

            #金额
            paymonxpath=commid["basetype"]+pageid+itemgrid+str(5)+"]"
            browser.delaytime(1)
            browser.findXpath(self.driver,paymonxpath).click()

            pamonid=pageid+commid["grid_total"]
            browser.findId(self.driver,pamonid).send_keys("8.88")

            #收款单位
            payid=pageid+browser.xmlRead(dom,'edBType',0)
            #print payid
            browser.delaytime(1)
            browser.nebecompany(self.driver,payid)

            #经手人
            peoid=pageid+browser.xmlRead(dom,'edEType',0)
            browser.peoplesel(self.driver,peoid,1)


            #部门
            depid=pageid+browser.xmlRead(dom,'edDept',0)
            browser.passpeople(self.driver,depid)

            #摘要
            summid=pageid+browser.xmlRead(dom,'edSummary',0)
            browser.findId(self.driver,summid).send_keys(u"中文测试饕餮壹贰123！@#￥%……&*（）()； abcstock paynote  summary")

            #附加说明
            commentid=pageid+browser.xmlRead(dom,'edComment',0)
            browser.findId(self.driver,commentid).send_keys(u"stock paynote commentid中文测试饕餮壹贰123！@#￥%……&*（）()； abc")

            #配置>>
            configid=pageid+browser.xmlRead(dom,'btnMore',0)
            jsentype="$(\"td[class=MenuCaption]:contains('结算方式配置')\").last().click()"
            jsconbil="$(\"td[class=MenuCaption]:contains('录单配置')\").last().click()"
            browser.contype(self.driver,configid,jsentype,jsconbil)

            #保存退出
            saexid=pageid+commid["selclose"]
            browser.savedraftexit(self.driver,saexid,payxpath,paygridid,1)
            browser.openModule2(self.driver,modulename,moduledetail)


        except:
            print traceback.format_exc()
            filename=browser.xmlRead(dom,'filename',0)
            #print filename+u"常用-单据草稿.png"
            #browser.getpicture(self.driver,filename+u"notedraft.png")
            browser.getpicture(self.driver,filename+u"进货-付款单.png")



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
