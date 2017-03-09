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

class receiptnoteTest(unittest.TestCase):
    u'''财务-收款单'''

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


    def test_receiptNote(self):
        u'''财务-收款单'''
        #零售出库单要在第一个
        header={'cookie':self.cookiestr,"Content-Type": "application/json"}
        comdom=xml.dom.minidom.parse(r'C:\workspace\nufeeb.button\data\commonlocation')
        dom = xml.dom.minidom.parse(r'C:\workspace\nufeeb.button\finance\financelocation')
        dom2 = xml.dom.minidom.parse(r'C:\workspace\nufeeb.button\saleretail\salelocation')
        module=browser.xmlRead(dom,'module',0)
        moduledetail=browser.xmlRead(dom,'moduledetail',7)

        browser.openModule2(self.driver,module,moduledetail)


        #页面id
        pageurl=browser.xmlRead(dom,"receipturl",0)
        pageid=browser.getalertid(pageurl,header)
        #print pageid

        #commid,id
        commid=browser.getallcommonid(comdom)


        try:
            #付款单位
            payid=pageid+browser.xmlRead(dom2,'edBType',0)
            #print payid
            browser.delaytime(1)
            browser.nebecompany(self.driver,payid)

            #经手人
            peoid=pageid+browser.xmlRead(dom2,'edEType',0)
            browser.passpeoplesel(self.driver,peoid)

            #部门
            depid=pageid+browser.xmlRead(dom2,'edDept',0)
            browser.passpeople(self.driver,depid)

            #摘要
            summid=pageid+browser.xmlRead(dom2,'edSummary',0)
            browser.findId(self.driver,summid).send_keys(u"中文蘩軆饕餮！@#￥%……&*（）？； 。.finance receipt note summary")

            #附加说明
            commentid=pageid+browser.xmlRead(dom2,'edComment',0)
            browser.findId(self.driver,commentid).send_keys(u"finance receipt note commentid中文蘩軆饕餮！@#￥%……&*（）？； 。.")

            #收款账户名称
            itemgrid=browser.xmlRead(dom2,"partitna",0)
            payxpath=commid["basetype"]+pageid+itemgrid+str(3)+"]"
            #print payxpath
            browser.findXpath(self.driver,payxpath).click()

            paygridid=pageid+commid["grid_fullname"]
            whichjs="$(\"div[class=GridBodyCellText]:contains('全部银行存款')\").attr(\"id\",\"allbankacc\")"
            browser.delaytime(1)
            browser.nebecompany(self.driver,paygridid,whichjs)

            #金额
            paymonxpath=commid["basetype"]+pageid+itemgrid+str(4)+"]"
            browser.findXpath(self.driver,paymonxpath).click()

            pamonid=pageid+commid["grid_total"]
            browser.findId(self.driver,pamonid).send_keys("88.88")

            #配置>>
            configid=pageid+commid["btnMore"]
            jsentype="$(\"td[class=MenuCaption]:contains('结算方式配置')\").last().click()"
            jsconbil="$(\"td[class=MenuCaption]:contains('录单配置')\").last().click()"
            browser.contype(self.driver,configid,jsentype,jsconbil)

            #保存退出
            saexid=pageid+commid["selclose"]
            browser.findId(self.driver,saexid).click()
            browser.exjscommin(self.driver,"保存单据")
            browser.openModule2(self.driver,module,moduledetail)
            browser.findXpath(self.driver,payxpath).click()
            browser.doubleclick(self.driver,paygridid)
            browser.exjscommin(self.driver,"选中")
            browser.findId(self.driver,saexid).click()
            browser.exjscommin(self.driver,"存入草稿")
            browser.openModule2(self.driver,module,moduledetail)
            browser.findXpath(self.driver,payxpath).click()
            browser.doubleclick(self.driver,paygridid)
            browser.exjscommin(self.driver,"选中")
            browser.findId(self.driver,saexid).click()
            browser.exjscommin(self.driver,"废弃退出")
            browser.openModule2(self.driver,module,moduledetail)
        except:
            print traceback.format_exc()
            filename=browser.xmlRead(dom,'filename',0)
            browser.delaytime(1)
            browser.getpicture(self.driver,filename+u"财务-收款单.png")



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
