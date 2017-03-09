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

class proasseTest(unittest.TestCase):
    u'''库存-生产组装单'''

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

    def testproAsse(self):
        u'''库存-生产组装单.'''
        header={'cookie':self.cookiestr,"Content-Type": "application/json"}
        comdom=xml.dom.minidom.parse(r'C:\workspace\nufeeb.button\data\commonlocation')
        dom = xml.dom.minidom.parse(r'C:\workspace\nufeeb.button\instock\instocklocation')

        modulename=browser.xmlRead(dom,"module",0)
        moduledetail=browser.xmlRead(dom,'moduledetail',4)

        browser.delaytime(1)
        browser.openModule2(self.driver,modulename,moduledetail)

        #页面id
        pageurl=browser.xmlRead(dom,"proasseurl",0)
        pageid=browser.getalertid(pageurl,header)
        #print pageid

        #commid,id
        commid=browser.getallcommonid(comdom)


        try:
            saexid=pageid+commid["selclose"]
            cateid=pageid+browser.xmlRead(dom,'edKType',0)
            cateid2=pageid+browser.xmlRead(dom,'edKType',0)+str(2)

            browser.delaytime(1)
            browser.doubleclick(self.driver,cateid)
            browser.exjscommin(self.driver,"选中")
            browser.delaytime(1)
            browser.doubleclick(self.driver,cateid2)
            browser.exjscommin(self.driver,"选中")

             #生产模板
            proassmodid=pageid+browser.xmlRead(dom,"btnPtypeProdure",0)
            browser.delaytime(1)
            browser.promoudle(self.driver,proassmodid)

            #生成生产组装单
            browser.exjscommin(self.driver,"生成生产组装单")
            js="$(\"td[class=MenuCaption]:contains('生成生产组装单')\").click()"
            browser.delaytime(1)
            browser.excutejs(self.driver,js)
            browser.exjscommin(self.driver,"确定")

            browser.findId(self.driver,saexid).click()
            browser.exjscommin(self.driver,"保存单据")


            browser.exjscommin(self.driver,"生产模板")
            browser.exjscommin(self.driver,"生成生产组装单")
            js="$(\"td[class=MenuCaption]:contains('生成生产拆装单')\").last().click()"
            browser.delaytime(1)
            browser.excutejs(self.driver,js)
            browser.exjscommin(self.driver,"确定")
            browser.findId(self.driver,saexid).click()
            browser.exjscommin(self.driver,"存入草稿")

            browser.exjscommin(self.driver,"生产模板")
            browser.exjscommin(self.driver,"生成生产组装单")
            js="$(\"td[class=MenuCaption]:contains('生成生产拆装单')\").eq(1).click()"
            browser.delaytime(1)
            browser.excutejs(self.driver,js)
            browser.exjscommin(self.driver,"确定")
            browser.findId(self.driver,saexid).click()
            browser.exjscommin(self.driver,"废弃退出")
            browser.openModule2(self.driver,modulename,moduledetail)

            #-筛选
            browser.exjscommin(self.driver,"生产模板")
            js1="$(\"input[id$=edColumns]\").attr(\"id\",\"selid\")"
            js2="$(\"div:contains('商品编号')\").last().attr(\"id\",\"seitid\")"
            js3="$(\"input[id$=edValue]\").attr(\"value\",\"a1\")"
            browser.delaytime(1)
            browser.selectit(self.driver,js1,"selid",js2,"seitid",js3)
            browser.exjscommin(self.driver,"退出")

            #-删除
            browser.findId(self.driver,proassmodid).click()
            browser.exjscommin(self.driver,"删除")
            browser.accAlert(self.driver,1)
            browser.exjscommin(self.driver,"删除")
            browser.accAlert(self.driver,0)
            browser.exjscommin(self.driver,"删除")
            browser.accAlert(self.driver,1)
            browser.exjscommin(self.driver,"退出")
            browser.openModule2(self.driver,modulename,moduledetail)

            #换出商品
            outitemxpath=commid["basetype"]+pageid+commid["outitempart"]+str(4)+"]"
            #print outitemxpath
            browser.findXpath(self.driver,outitemxpath).click()
            outitemid=pageid+"out"+"G"+commid["grid_pfullname"][1:]
            #print outitemid
            browser.doubleclick(self.driver,outitemid)

            item1="$(\"div[class=GridBodyCellText]:contains('M001')\").last().attr(\"id\",\"item1id\")"
            browser.delaytime(1)
            browser.excutejs(self.driver,item1)
            browser.findId(self.driver,"item1id").click()
            browser.exjscommin(self.driver,"选中并关闭")

            outitemxpath2=commid["basetype"]+pageid+commid["outitempart"][:-6]+str(2)+"]/td[4]"
            #print outitemxpath
            browser.findXpath(self.driver,outitemxpath2).click()
            browser.doubleclick(self.driver,outitemid)
            item2="$(\"div[class=GridBodyCellText]:contains('555')\").last().attr(\"id\",\"item2id\")"
            browser.delaytime(1)
            browser.excutejs(self.driver,item2)
            browser.findId(self.driver,"item2id").click()
            browser.exjscommin(self.driver,"选中并关闭")


            #换入商品
            initemxpath=commid["basetype"]+pageid+commid["initempart"]+str(4)+"]"
            browser.findXpath(self.driver,initemxpath).click()
            initemid=pageid+"in"+"G"+commid["grid_pfullname"][1:]
            browser.cateitemsel(self.driver,initemid)

            browser.findXpath(self.driver,initemxpath).click()
            browser.doubleclick(self.driver,initemid)
            item3="$(\"div[class=GridBodyCellText]:contains('a1x')\").last().attr(\"id\",\"item3id\")"
            browser.delaytime(1)
            browser.excutejs(self.driver,item3)
            browser.findId(self.driver,"item3id").click()
            browser.exjscommin(self.driver,"选中")

            #单位
            js="$(\"div:contains('个')\").last().attr(\"id\",\"itunid\")"
            browser.excutejs(self.driver,js)
            browser.delaytime(1)
            browser.itemunit(self.driver,"itunid")

            #数量
            initemgrid=commid["initempart"]
            initqty=commid["basetype"]+pageid+initemgrid+str(18)+"]"
            #print initqty
            browser.findXpath(self.driver,initqty).click()

            inqtyid=pageid+"in"+"G"+commid["grid_assqty"][1:]
            browser.itemnums(self.driver,inqtyid)

            #单价
            itprice=commid["basetype"]+pageid+initemgrid+str(20)+"]"
            browser.findXpath(self.driver,itprice).click()

            dppriceid=pageid+browser.xmlRead(dom,'inGrid_assprice',0)
            browser.findId(self.driver,dppriceid).send_keys("40.99")

            #发货仓库

            browser.peoplesel(self.driver,cateid)

            #经手人
            peoid=pageid+browser.xmlRead(dom,'edEType',0)
            browser.peoplesel(self.driver,peoid,1)

            #部门
            depid=pageid+browser.xmlRead(dom,'edDept',0)
            browser.passpeople(self.driver,depid)

            #收货仓库

            browser.doubleclick(self.driver,cateid2)
            browser.delaytime(1)
            js="$(\"div[class=GridBodyCellText]:contains('在途仓库')\").attr(\"id\",\"recateid\")"
            browser.delaytime(1)
            browser.excutejs(self.driver,js)
            browser.findId(self.driver,"recateid").click()
            browser.exjscommin(self.driver,"选中")

            #摘要
            summid=pageid+browser.xmlRead(dom,'edSummary',0)
            browser.findId(self.driver,summid).send_keys(u"proasse summary中文蘩軆饕餮！@#￥%……&*（）？； 。.")

            #附加说明
            commentid=pageid+browser.xmlRead(dom,'edComment',0)
            browser.findId(self.driver,commentid).send_keys(u"中文蘩軆饕餮！@#￥%……&*（）？； 。.proasse comment")

            #录单配置
            conbillid=pageid+browser.xmlRead(dom,"btnBillConfig",0)
            browser.conbill(self.driver,conbillid)
            browser.accAlert(self.driver,1)

            #保存退出

            browser.findId(self.driver,saexid).click()
            browser.exjscommin(self.driver,"保存单据")
            browser.openModule2(self.driver,modulename,moduledetail)



        except:
            print traceback.format_exc()
            filename=browser.xmlRead(dom,'filename',0)
            browser.delaytime(1)
            browser.getpicture(self.driver,filename+u"库存-生产组装单.png")



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
