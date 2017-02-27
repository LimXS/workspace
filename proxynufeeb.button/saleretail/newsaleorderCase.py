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

class newsaleorderTest(unittest.TestCase):
    u'''批零-新增销售订单'''

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



    def testnewsaleOrder(self):
        u'''批零-新增销售订单.'''
        header={'cookie':self.cookiestr,"Content-Type": "application/json"}
        comdom=xml.dom.minidom.parse(r'C:\workspace\proxynufeeb.button\data\commonlocation')
        dom = xml.dom.minidom.parse(r'C:\workspace\proxynufeeb.button\saleretail\salelocation')

        modulename=browser.xmlRead(dom,"module",0)
        moduledetail=browser.xmlRead(dom,'moduledetail',0)

        browser.openModule2(self.driver,modulename,moduledetail)
        cookies=browser.cookieSave(self.driver)
        header3={'cookie':cookies,"Content-Type": "application/json"}
        header4={'cookie':cookies,"Content-Type": "application/x-www-form-urlencoded"}

        #页面id
        pageurl=browser.xmlRead(dom,"newsaleurl",0)
        pageid=browser.getalertid(pageurl,header)

        pageid=pageid[:-2]
        #print pageid

        #commid,id
        commid=browser.getallcommonid(comdom)

        try:
            #选择商品
            itnaid=commid["basetype"]+pageid+browser.xmlRead(dom,"partitna",0)+str(4)+"]"
            browser.delaytime(1)
            browser.findXpath(self.driver,itnaid).click()
            itemid=pageid+commid["grid_pfullname"]
            browser.cateitemsel(self.driver,itemid)

            #单位
            js="$(\"div:contains('个')\").last().attr(\"id\",\"itunid\")"
            browser.delaytime(1)
            browser.excutejs(self.driver,js)
            browser.itemunit(self.driver,"itunid")

            #数量
            itemgrid=browser.xmlRead(dom,"partitna",0)
            itqty=commid["basetype"]+pageid+itemgrid+str(25)+"]"
            browser.findXpath(self.driver,itqty).click()

            qtyid=pageid+commid["grid_assqty"]
            browser.itemnums(self.driver,qtyid)

            #折前单价
            dpprice=commid["basetype"]+pageid+itemgrid+str(30)+"]"
            browser.delaytime(1)
            browser.findXpath(self.driver,dpprice).click()

            dppriceid=pageid+commid["grid_assdpprice"]
            browser.delaytime(1)
            browser.itemunit(self.driver,dppriceid)

            #发货仓库
            cateid=pageid+browser.xmlRead(dom,"edKType",0)
            browser.delaytime(1)
            browser.peoplesel(self.driver,cateid)
            #print "cate ok"

            #经手人
            papeoid=pageid+browser.xmlRead(dom,"edEType",0)
            browser.delaytime(1)
            browser.peoplesel(self.driver,papeoid,1)
            #print "people ok"

            #购买单位
            buycomid=pageid+browser.xmlRead(dom,"edBType",0)
            browser.delaytime(1)
            browser.buycompanysel(self.driver,buycomid)



            #摘要
            sumid=pageid+browser.xmlRead(dom,"edSummary",0)
            browser.findId(self.driver,sumid).send_keys(u"中文测试饕餮壹贰123！@#￥%……&*（）()； abcsale sum")

            #附加说明
            commentid=pageid+browser.xmlRead(dom,"edComment",0)
            browser.findId(self.driver,commentid).send_keys(u"中文测试饕餮壹贰123！@#￥%……&*（）()； abcsale comm")


            #发货信息
            sendinfoid=pageid+browser.xmlRead(dom,"btnDeliveryInfo",0)
            browser.delaytime(1)
            browser.sendinfo(self.driver,sendinfoid,"$(\"input[id$=edDeliveryInfo]\").last().attr(\"id\",\"seinfinputid\")","seinfinputid")



            #选择套餐
            choicepackid=pageid+browser.xmlRead(dom,"btnAddSuit",0)
            browser.delaytime(1)
            browser.itempacksel(self.driver,choicepackid)

            #录单配置
            conbillid=pageid+browser.xmlRead(dom,"btnBillConfig",0)
            browser.delaytime(1)
            browser.conbill(self.driver,conbillid)
            browser.delaytime(1)
            browser.accAlert(self.driver,1)

            #导入商品明细
            imitid=pageid+browser.xmlRead(dom,"btnImportDetail",0)
            browser.delaytime(1)
            browser.impitemdetail(self.driver,imitid)

            #保存退出
            browser.exjscommin(self.driver,"保存")
            #-保存单据
            browser.exjscommin(self.driver,"保存单据")
            #废弃退出
            browser.findXpath(self.driver,itnaid).click()
            itemid=pageid+commid["grid_pfullname"]
            browser.doubleclick(self.driver,itemid)
            browser.exjscommin(self.driver,"选中并关闭")
            browser.exjscommin(self.driver,"保存")
            browser.exjscommin(self.driver,"废弃退出")
            browser.openModule2(self.driver,modulename,moduledetail)

            #收订金
            browser.exjscommin(self.driver,"收订金")
            browser.accAlert(self.driver,1)


            browser.findXpath(self.driver,itnaid).click()
            browser.doubleclick(self.driver,itemid)
            browser.exjscommin(self.driver,"选中并关闭")

            browser.doubleclick(self.driver,cateid)
            browser.exjscommin(self.driver,"选中")
            browser.doubleclick(self.driver,buycomid)
            browser.exjscommin(self.driver,"选中")
            browser.exjscommin(self.driver,"收订金")
            browser.exjscommin(self.driver,"退出")
            browser.exjscommin(self.driver,"存入草稿")
            browser.exjscommin(self.driver,"退出")
            browser.openModule2(self.driver,modulename,moduledetail)


            #打印

        except:
            print traceback.format_exc()
            filename=browser.xmlRead(dom,'filename',0)
            browser.delaytime(1)
            browser.getpicture(self.driver,filename+u"批零-新增销售订单.png")



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
