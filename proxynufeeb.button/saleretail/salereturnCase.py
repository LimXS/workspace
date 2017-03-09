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

class salereturnTest(unittest.TestCase):
    u'''批零-销售退货单'''

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


    def testsaleReturn(self):
        u'''批零-销售退货单.'''
        header={'cookie':self.cookiestr,"Content-Type": "application/json"}
        comdom=xml.dom.minidom.parse(r'C:\workspace\proxynufeeb.button\data\commonlocation')
        dom = xml.dom.minidom.parse(r'C:\workspace\proxynufeeb.button\saleretail\salelocation')

        modulename=browser.xmlRead(dom,"module",0)
        moduledetail=browser.xmlRead(dom,'moduledetail',3)

        browser.openModule2(self.driver,modulename,moduledetail)

        #页面id
        pageurl=browser.xmlRead(dom,"salereturnurl",0)
        pageid=browser.getalertid(pageurl,header)
        #print pageid

        #commid,id
        commid=browser.getallcommonid(comdom)
        #id=browser.getcommonid(dom)

        try:
            #退货单位
            companyid=pageid+browser.xmlRead(dom,'edBType',0)
            #print companyid
            browser.delaytime(1)
            browser.buycompanysel(self.driver,companyid)

            #经手人
            peoid=pageid+browser.xmlRead(dom,'edEType',0)
            browser.peoplesel(self.driver,peoid,1)

            #部门
            depid=pageid+browser.xmlRead(dom,'edDept',0)
            browser.passpeople(self.driver,depid)

            #收货仓库
            cateid=pageid+browser.xmlRead(dom,'edKType',0)
            browser.peoplesel(self.driver,cateid)


            #摘要
            summid=pageid+browser.xmlRead(dom,'edSummary',0)
            browser.findId(self.driver,summid).send_keys(u"中文测试饕餮壹贰123！@#￥%……&*（）()； abcsale return summary")

            #附加说明
            commentid=pageid+browser.xmlRead(dom,'edComment',0)
            browser.findId(self.driver,commentid).send_keys(u"sale return commentid中文测试饕餮壹贰123！@#￥%……&*（）()； abc")

            #商品名字
            itnaid=commid["basetype"]+pageid+browser.xmlRead(dom,"partitna",0)+str(5)+"]"
            #print itnaid
            browser.findXpath(self.driver,itnaid).click()
            itemid=pageid+commid["grid_pfullname"]
            browser.cateitemsel(self.driver,itemid)

            #单位
            js="$(\"div:contains('个')\").last().attr(\"id\",\"itunid\")"
            browser.excutejs(self.driver,js)
            browser.delaytime(1)
            browser.itemunit(self.driver,"itunid")

            #数量
            itemgrid=browser.xmlRead(dom,"partitna",0)
            itqty=commid["basetype"]+pageid+itemgrid+str(24)+"]"
            browser.findXpath(self.driver,itqty).click()

            qtyid=pageid+commid["grid_assqty"]
            browser.itemnums(self.driver,qtyid)

            #折前单价
            dpprice=commid["basetype"]+pageid+itemgrid+str(26)+"]"
            browser.findXpath(self.driver,dpprice).click()

            dppriceid=pageid+commid["grid_assdpprice"]
            browser.itemunit(self.driver,dppriceid)

            #录单配置
            conbillid=pageid+browser.xmlRead(dom,"btnBillConfig",0)
            browser.delaytime(1)
            browser.conbill(self.driver,conbillid)
            browser.delaytime(1)
            browser.accAlert(self.driver,1)

            #付款账户
            accmonid=pageid+browser.xmlRead(dom,"edAType",0)
            browser.departsel(self.driver,accmonid)


            #选择套餐
            choicepackid=pageid+browser.xmlRead(dom,"btnAddSuit",0)
            browser.itempacksel(self.driver,choicepackid)

            #导入商品明细
            imitid=pageid+browser.xmlRead(dom,"btnImportDetail",0)
            browser.impitemdetail(self.driver,imitid)

            #原单退货
            saorid=pageid+browser.xmlRead(dom,"btnSaleBill",0)
            browser.findId(self.driver,saorid).click()
            js="$(\"td[nowrap=true]:contains('查询')\").click()"
            browser.delaytime(1)
            browser.excutejs(self.driver,js)
            browser.pagechoice(self.driver)
            browser.exjscommin(self.driver,"关闭")
            browser.findId(self.driver,saorid).click()
            js="$(\"div[class=GridBodyCellText]:contains('sale out summary')\").first().attr(\"id\",\"prorderid\")"
            browser.delaytime(1)
            browser.excutejs(self.driver,js)
            browser.findId(self.driver,"prorderid").click()
            browser.exjscommin(self.driver,"选择")

            #打印

            #保存退出
            saexid=pageid+commid["selclose"]
            browser.savedraftexit(self.driver,saexid,itnaid,itemid)
            browser.openModule2(self.driver,modulename,moduledetail)


        except:
            print traceback.format_exc()
            filename=browser.xmlRead(dom,'filename',0)
            #print filename+u"常用-单据草稿.png"
            #browser.getpicture(self.driver,filename+u"notedraft.png")
            browser.getpicture(self.driver,filename+u"批零-销售退货单.png")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
