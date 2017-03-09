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

class saleexchangeTest(unittest.TestCase):
    u'''批零-销售换货单'''

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



    def testsaleExchange(self):
        u'''批零-销售换货单.'''
        header={'cookie':self.cookiestr,"Content-Type": "application/json"}
        comdom=xml.dom.minidom.parse(r'C:\workspace\proxynufeeb.button\data\commonlocation')
        dom = xml.dom.minidom.parse(r'C:\workspace\proxynufeeb.button\saleretail\salelocation')

        modulename=browser.xmlRead(dom,"module",0)
        moduledetail=browser.xmlRead(dom,'moduledetail',4)

        browser.openModule2(self.driver,modulename,moduledetail)
        cookies=browser.cookieSave(self.driver)
        header3={'cookie':cookies,"Content-Type": "application/json"}
        header4={'cookie':cookies,"Content-Type": "application/x-www-form-urlencoded"}

        #页面id
        pageurl=browser.xmlRead(dom,"saleexchurl",0)
        pageid=browser.getalertid(pageurl,header)
        #print pageid

        #commid,id
        commid=browser.getallcommonid(comdom)
        #id=browser.getcommonid(dom)


        try:
            #选择换出商品套餐
            outconbid=pageid+browser.xmlRead(dom,"btnAddOutSuit",0)
            browser.itempacksel(self.driver,outconbid)

            #换出商品
            outitemxpath=commid["basetype"]+pageid+commid["outitempart"]+str(3)+"]"
            #print outitemxpath
            browser.findXpath(self.driver,outitemxpath).click()
            outitemid=pageid+"out"+"G"+commid["grid_pfullname"][1:]
            #print outitemid
            browser.cateitemsel(self.driver,outitemid)

            #单位
            js="$(\"div:contains('个')\").last().attr(\"id\",\"itunid\")"
            browser.excutejs(self.driver,js)
            browser.delaytime(1)
            browser.itemunit(self.driver,"itunid")

            #数量
            itemgrid=commid["outitempart"]
            outitqty=commid["basetype"]+pageid+itemgrid+str(22)+"]"
            #print outitqty
            browser.delaytime(1)
            browser.findXpath(self.driver,outitqty).click()

            outqtyid=pageid+"out"+"G"+commid["grid_assqty"][1:]
            #print outqtyid
            browser.itemnums(self.driver,outqtyid)

            #折前单价
            oudpprice=commid["basetype"]+pageid+itemgrid+str(24)+"]"
            browser.findXpath(self.driver,oudpprice).click()

            outdppriceid=pageid+"out"+"G"+commid["grid_assdpprice"][1:]
            browser.itemunit(self.driver,outdppriceid)

            #换入商品
            initemxpath=commid["basetype"]+pageid+commid["initempart"]+str(3)+"]"
            browser.findXpath(self.driver,initemxpath).click()
            initemid=pageid+"in"+"G"+commid["grid_pfullname"][1:]
            browser.cateitemsel(self.driver,initemid)

            #单位
            js="$(\"div:contains('个')\").last().attr(\"id\",\"itunid\")"
            browser.excutejs(self.driver,js)
            browser.delaytime(1)
            browser.itemunit(self.driver,"itunid")

            #数量
            initemgrid=commid["initempart"]
            initqty=commid["basetype"]+pageid+initemgrid+str(22)+"]"
            #print initqty
            browser.findXpath(self.driver,initqty).click()

            inqtyid=pageid+"in"+"G"+commid["grid_assqty"][1:]
            browser.itemnums(self.driver,inqtyid)

            #折前单价
            indpprice=commid["basetype"]+pageid+initemgrid+str(24)+"]"
            #print indpprice
            browser.findXpath(self.driver,indpprice).click()

            indppriceid=pageid+"in"+"G"+commid["grid_assdpprice"][1:]
            #print indppriceid
            browser.itemunit(self.driver,indppriceid)

            #供货单位
            companyid=pageid+browser.xmlRead(dom,'edBType',0)
            #print companyid
            browser.delaytime(1,self.driver)
            browser.buycompanysel(self.driver,companyid)

            #经手人
            peoid=pageid+browser.xmlRead(dom,'edEType',0)
            browser.peoplesel(self.driver,peoid,1)

            #部门
            depid=pageid+browser.xmlRead(dom,'edDept',0)
            browser.passpeople(self.driver,depid)

            #换出仓库
            cateid=pageid+browser.xmlRead(dom,'edKType',0)
            browser.peoplesel(self.driver,cateid)

            #换入仓库
            cateid=pageid+browser.xmlRead(dom,'edKType',0)+str(2)
            browser.peoplesel(self.driver,cateid)

            #摘要
            summid=pageid+browser.xmlRead(dom,'edSummary',0)
            browser.findId(self.driver,summid).send_keys(u"中文测试饕餮壹贰123！@#￥%……&*（）()； abcsale exchange  summary")

            #附加说明
            commentid=pageid+browser.xmlRead(dom,'edComment',0)
            browser.findId(self.driver,commentid).send_keys(u"中文测试饕餮壹贰123！@#￥%……&*（）()； abcsale exchange comment")

            #付款账户
            edAType=pageid+browser.xmlRead(dom,"edAType",0)
            browser.departsel(self.driver,edAType)

            #录单配置
            billcon=pageid+browser.xmlRead(dom,"btnBillConfig",0)
            browser.conbill(self.driver,billcon)
            browser.delaytime(1)
            browser.accAlert(self.driver,1)

            #保存|退出
            saexid=pageid+commid["selclose"]
            browser.savedraftexit(self.driver,saexid,outitemxpath,outitemid)
            browser.openModule2(self.driver,modulename,moduledetail)

        except:
            print traceback.format_exc()
            filename=browser.xmlRead(dom,'filename',0)
            browser.delaytime(1)
            browser.getpicture(self.driver,filename+u"批零-销售换货单.png")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
