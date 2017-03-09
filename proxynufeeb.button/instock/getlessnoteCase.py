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

class getlessnoteTest(unittest.TestCase):
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

    def testgetitemseriesLess(self):
        u'''库存-报损单-序列号商品'''
        header={'cookie':self.cookiestr,"Content-Type": "application/json"}
        comdom=xml.dom.minidom.parse(r'C:\workspace\proxynufeeb.button\data\commonlocation')
        dom = xml.dom.minidom.parse(r'C:\workspace\proxynufeeb.button\instock\instocklocation')

        modulename=browser.xmlRead(dom,"module",0)
        moduledetail=browser.xmlRead(dom,'moduledetail',0)

        browser.openModule2(self.driver,modulename,moduledetail)

        #页面id
        pageurl=browser.xmlRead(dom,"lessurl",0)
        pageid=browser.getalertid(pageurl,header)
        #print pageid

        #commid,id
        commid=browser.getallcommonid(comdom)

        try:
            #商品
            itnaid=commid["basetype"]+pageid+browser.xmlRead(dom,"itemgrid",0)+str(4)+"]"
            #print itnaid
            browser.findXpath(self.driver,itnaid).click()
            itemid=pageid+commid["grid_pfullname"]
            f=open(r'C:\workspace\proxynufeeb.button\instock\instockortherseries','r')
            checkNo=f.read()
            f.close()
            browser.delaytime(1)
            browser.seriesitemout(self.driver,itemid,itnaid,checkNo)

            #经手人
            peoid=pageid+browser.xmlRead(dom,'edEType',0)
            browser.doubleclick(self.driver,peoid)
            browser.exjscommin(self.driver,"选中")

            #部门
            depid=pageid+browser.xmlRead(dom,'edDept',0)
            browser.doubleclick(self.driver,depid)
            browser.exjscommin(self.driver,"选中")

            #出货仓库
            cateid=pageid+browser.xmlRead(dom,'edKType',0)
            browser.doubleclick(self.driver,cateid)
            browser.exjscommin(self.driver,"选中")

            #摘要
            summid=pageid+browser.xmlRead(dom,'edSummary',0)
            browser.findId(self.driver,summid).send_keys(u"中文测试饕餮壹贰！@#￥%……&*（）12；less note item series summary")

            #附加说明
            commentid=pageid+browser.xmlRead(dom,'edComment',0)
            browser.findId(self.driver,commentid).send_keys(u"less note item series comment中文测试饕餮壹贰！@#￥%……&*（）12；")

            browser.exjscommin(self.driver,"退出")
            browser.exjscommin(self.driver,"保存单据")
            browser.doubleclick(self.driver,peoid)


        except:
            print traceback.format_exc()
            filename=browser.xmlRead(dom,'filename',0)
            browser.getpicture(self.driver,filename+u"库存-报损单-序列号商品.png")


    def testgetlessNote(self):
        u'''库存-报损单-普通商品'''
        header={'cookie':self.cookiestr,"Content-Type": "application/json"}
        comdom=xml.dom.minidom.parse(r'C:\workspace\proxynufeeb.button\data\commonlocation')
        dom = xml.dom.minidom.parse(r'C:\workspace\proxynufeeb.button\instock\instocklocation')

        modulename=browser.xmlRead(dom,"module",0)
        moduledetail=browser.xmlRead(dom,'moduledetail',0)

        browser.openModule2(self.driver,modulename,moduledetail)

        #页面id
        pageurl=browser.xmlRead(dom,"lessurl",0)
        pageid=browser.getalertid(pageurl,header)
        #print pageid

        #commid,id
        commid=browser.getallcommonid(comdom)


        try:
            #商品名字
            itnaid=commid["basetype"]+pageid+browser.xmlRead(dom,"itemgrid",0)+str(4)+"]"
            #print itnaid
            browser.findXpath(self.driver,itnaid).click()
            itemid=pageid+commid["grid_pfullname"]
            #print itemid
            browser.delaytime(1,self.driver)
            browser.cateitemsel(self.driver,itemid)

            #单位
            js="$(\"div:contains('个')\").last().attr(\"id\",\"itunid\")"
            browser.excutejs(self.driver,js)
            browser.delaytime(1)
            browser.itemunit(self.driver,"itunid")

            #数量
            itemgrid=browser.xmlRead(dom,"itemgrid",0)
            itqty=commid["basetype"]+pageid+itemgrid+str(18)+"]"
            browser.findXpath(self.driver,itqty).click()

            qtyid=pageid+commid["grid_assqty"]
            browser.itemnums(self.driver,qtyid)

            #经手人
            peoid=pageid+browser.xmlRead(dom,'edEType',0)
            browser.peoplesel(self.driver,peoid,1)

            #部门
            depid=pageid+browser.xmlRead(dom,'edDept',0)
            browser.passpeople(self.driver,depid)

            #发货仓库
            cateid=pageid+browser.xmlRead(dom,'edKType',0)
            browser.peoplesel(self.driver,cateid)

            #摘要
            summid=pageid+browser.xmlRead(dom,'edSummary',0)
            browser.findId(self.driver,summid).send_keys(u"中文测试饕餮壹贰！@#￥%……&*（）12；less note  summary")

            #附加说明
            commentid=pageid+browser.xmlRead(dom,'edComment',0)
            browser.findId(self.driver,commentid).send_keys(u"less note comment中文测试饕餮壹贰！@#￥%……&*（）12；")

            conbillid=pageid+browser.xmlRead(dom,"btnBillConfig",0)
            browser.conbill(self.driver,conbillid)
            browser.accAlert(self.driver,1)

            #保存退出
            saexid=pageid+commid["selclose"]
            browser.savedraftexit(self.driver,saexid,itnaid,itemid,1)
            browser.openModule2(self.driver,modulename,moduledetail)

        except:
            print traceback.format_exc()
            filename=browser.xmlRead(dom,'filename',0)
            browser.getpicture(self.driver,filename+u"库存-报损单-普通商品.png")



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
