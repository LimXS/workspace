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

class stockintocateTest(unittest.TestCase):
    u'''进货-进货入库单'''

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

    def testitemseriesCate(self):
        u'''进货-进货入库单-序列号商品.'''
        header={'cookie':self.cookiestr,"Content-Type": "application/json"}
        comdom=xml.dom.minidom.parse(r'C:\workspace\proxynufeeb.button\data\commonlocation')
        dom = xml.dom.minidom.parse(r'C:\workspace\proxynufeeb.button\stock\stocklocation')

        modulename=browser.xmlRead(dom,"module",0)
        moduledetail=browser.xmlRead(dom,'moduledetail',2)

        browser.openModule2(self.driver,modulename,moduledetail)

        #页面id
        pageurl=browser.xmlRead(dom,"stincateurl",0)
        pageid=browser.getalertid(pageurl,header)
        #print pageid

        #commid,id
        commid=browser.getallcommonid(comdom)
        try:
            #序列号商品
            itemone=commid["basetype"]+pageid+browser.xmlRead(dom,"nitemname",0)
            browser.delaytime(1)
            browser.findXpath(self.driver,itemone).click()
            itemsel=pageid+commid["grid_pfullname"]
            browser.doubleclick(self.driver,itemsel)
            js="$(\"div[class=GridBodyCellText]:contains('Series')\").last().attr(\"id\",\"seitemid\")"
            browser.delaytime(1)
            browser.excutejs(self.driver,js)
            browser.findId(self.driver,"seitemid").click()
            browser.exjscommin(self.driver,"选中并关闭")
            browser.exjscommin(self.driver,"关闭")

            browser.findXpath(self.driver,itemone).click()
            browser.doubleclick(self.driver,itemsel)
            browser.delaytime(1)
            browser.excutejs(self.driver,js)
            browser.findId(self.driver,"seitemid").click()
            browser.exjscommin(self.driver,"选中并关闭")

            itemser=browser.getrandnumber()
            f=open(r'C:\workspace\proxynufeeb.button\stock\seriesNoitem','w')
            f.write(itemser)
            f.close()

            js="$(\"input[id$=snnoTxt]\").val('"+itemser+"')"
            browser.delaytime(1)
            browser.excutejs(self.driver,js)
            browser.exjscommin(self.driver,"添加",1)
            browser.exjscommin(self.driver,"删除当前行")
            browser.exjscommin(self.driver,"添加",1)
            browser.exjscommin(self.driver,"删除全部")


            browser.exjscommin(self.driver,"导入")
            browser.exjscommin(self.driver,"导入文件")
            browser.accAlert(self.driver,1)
            browser.exjscommin(self.driver,"取消")


            js="$(\"input[id$=snnostartTxt]\").val('"+itemser+"')"
            browser.delaytime(1)
            browser.excutejs(self.driver,js)
            browser.exjscommin(self.driver,"批量添加")
            browser.exjscommin(self.driver,"完成")


            #供货单位
            edBType=pageid+browser.xmlRead(dom,"edBType",0)
            browser.doubleclick(self.driver,edBType)
            browser.exjscommin(self.driver,"选中")

            #经手人
            edEType=pageid+browser.xmlRead(dom,"edEType",0)
            browser.doubleclick(self.driver,edEType)
            browser.exjscommin(self.driver,"选中")

            #部门
            edDept=pageid+browser.xmlRead(dom,"edDept",0)
            browser.doubleclick(self.driver,edDept)
            browser.exjscommin(self.driver,"选中")

            #收货仓库
            edKType=pageid+browser.xmlRead(dom,"edKType",0)
            browser.doubleclick(self.driver,edKType)
            browser.exjscommin(self.driver,"选中")

            #摘要
            edSummary=pageid+browser.xmlRead(dom,"edSummary",0)
            browser.findId(self.driver,edSummary).send_keys(u"中文测试饕餮壹贰123！@#￥%……&*（）()； abcButton stockinto series item summary")

            #附加说明
            edComment=pageid+browser.xmlRead(dom,"edComment",0)
            browser.findId(self.driver,edComment).send_keys(u"中文测试饕餮壹贰123！@#￥%……&*（）()； abcButton stockinto series item comment")

            browser.exjscommin(self.driver,"退出")
            browser.exjscommin(self.driver,"保存单据")
            browser.doubleclick(self.driver,edBType)


        except:
            print traceback.format_exc()
            filename=browser.xmlRead(dom,'filename',0)
            browser.delaytime(1)
            browser.getpicture(self.driver,filename+u"进货-进货入库单-序列号商品.png")



    def teststockintoCate(self):
        u'''进货-进货入库单-普通商品.'''
        header={'cookie':self.cookiestr,"Content-Type": "application/json"}
        comdom=xml.dom.minidom.parse(r'C:\workspace\proxynufeeb.button\data\commonlocation')
        dom = xml.dom.minidom.parse(r'C:\workspace\proxynufeeb.button\stock\stocklocation')

        modulename=browser.xmlRead(dom,"module",0)
        moduledetail=browser.xmlRead(dom,'moduledetail',2)

        browser.openModule2(self.driver,modulename,moduledetail)
        cookies=browser.cookieSave(self.driver)
        header3={'cookie':cookies,"Content-Type": "application/json"}

        #页面id
        pageurl=browser.xmlRead(dom,"stincateurl",0)
        pageid=browser.getalertid(pageurl,header)
        #print pageid

        #commid,id
        commid=browser.getallcommonid(comdom)


        try:
            #item
            #编号
            itemone=commid["basetype"]+pageid+browser.xmlRead(dom,"nitemname",0)

            browser.findXpath(self.driver,itemone).click()
            browser.delaytime(1)
            itemsel=pageid+commid["grid_pfullname"]
            #browser.doubleclick(self.driver,itemsel)

            #-库存商品选择框
            browser.cateitemsel(self.driver,itemsel)

            #单位
            js="$(\"div:contains('个')\").last().attr(\"id\",\"itunid\")"
            browser.delaytime(1)
            browser.excutejs(self.driver,js)
            browser.itemunit(self.driver,"itunid")

            #数量
            itemgrid=browser.xmlRead(dom,"itemgrid",0)
            itqty=commid["basetype"]+pageid+itemgrid+str(24)+"]"
            browser.delaytime(1)
            browser.findXpath(self.driver,itqty).click()

            qtyid=pageid+browser.xmlRead(dom,"grid_assqty",0)
            browser.delaytime(1)
            browser.itemnums(self.driver,qtyid)

            #折前单价
            dpprice=commid["basetype"]+pageid+itemgrid+str(28)+"]"
            browser.delaytime(1)
            browser.findXpath(self.driver,dpprice).click()

            dppriceid=pageid+browser.xmlRead(dom,"grid_assdpprice",0)
            browser.itemunit(self.driver,dppriceid)

            #供货单位
            edBType=pageid+browser.xmlRead(dom,"edBType",0)
            browser.delaytime(1)
            browser.doubleclick(self.driver,edBType)
            companyurl="http://dba.wsgjp.com.cn/Beefun/Selector/BTypeSelector.gspx?Add=True&HideStoppedItem=True&ShowFreight=false&Bcategory=1&FilterStr="
            companyid=browser.getalertid(companyurl,header3)
            #print companyid

            browser.catesel(self.driver,commid,edBType,companyid)


            #经手人
            edEType=pageid+browser.xmlRead(dom,"edEType",0)
            browser.doubleclick(self.driver,edEType)

            #-添加 ，-关闭
            js="$(\"input[class=ButtonEdit]\").last().attr(\"id\",\"tempid\");"
            browser.catesel(self.driver,js,"tempid")

            #-选中
            browser.doubleclick(self.driver,edEType)
            js="$(\"button:contains('选中')\").click()"
            time.sleep(1)
            browser.excutejs(self.driver,js)

            #部门
            edDept=pageid+browser.xmlRead(dom,"edDept",0)
            browser.delaytime(1)
            browser.departsel(self.driver,edDept)

            #收货仓库
            edKType=pageid+browser.xmlRead(dom,"edKType",0)
            browser.doubleclick(self.driver,edKType)

            #-添加，-关闭
            browser.catesel(self.driver)
            browser.doubleclick(self.driver,edKType)

            #-选中
            js="$(\"button:contains('选中')\").click()"
            time.sleep(1)
            browser.excutejs(self.driver,js)

            #摘要
            edSummary=pageid+browser.xmlRead(dom,"edSummary",0)
            browser.findId(self.driver,edSummary).send_keys("Button stockinto summary")

            #附加说明
            edComment=pageid+browser.xmlRead(dom,"edComment",0)
            browser.findId(self.driver,edComment).send_keys("Button stockinto comment")

            #付款账户
            edAType=pageid+browser.xmlRead(dom,"edAType",0)
            browser.delaytime(1)
            browser.departsel(self.driver,edAType)

            #录单配置
            billcon=pageid+browser.xmlRead(dom,"btnBillConfig",0)
            browser.delaytime(1)
            browser.conbill(self.driver,billcon)
            browser.delaytime(1)
            browser.accAlert(self.driver,1)

            #费用结算
            moneyend=pageid+browser.xmlRead(dom,"ShowFreight",0)
            browser.delaytime(1)
            browser.moneyend(self.driver,moneyend)

            #导入商品明细
            importdetail=pageid+browser.xmlRead(dom,"ImportDetail",0)
            browser.delaytime(1)
            browser.findId(self.driver,importdetail).click()

            js="$(\"button:contains('导入文件')\").click()"
            browser.delaytime(1)
            browser.excutejs(self.driver,js)
            browser.accAlert(self.driver,1)

            js="$(\"button:contains('取消')\").click()"
            browser.delaytime(1)
            browser.excutejs(self.driver,js)

            #进货订单
            StockOrder=pageid+browser.xmlRead(dom,"StockOrder",0)
            browser.delaytime(1)
            browser.findId(self.driver,StockOrder).click()

            #-选择单据
            #-关闭
            browser.exjscommin(self.driver,"关闭")
            #-查询条件
            browser.findId(self.driver,StockOrder).click()
            browser.exjscommin(self.driver,"查询条件")

            #--取消
            browser.exjscommin(self.driver,"取消")
            browser.exjscommin(self.driver,"查询条件")



            #--经手人
            js="$(\"input[id$=edEType]\").last().attr(\"id\",\"papeoid\")"
            browser.delaytime(1)
            browser.excutejs(self.driver,js)
            browser.passpeople(self.driver,"papeoid")

            #--存货仓库
            js="$(\"input[id$=edKType]\").last().attr(\"id\",\"cateid\")"
            browser.delaytime(1)
            browser.excutejs(self.driver,js)
            browser.passpeople(self.driver,"cateid")

            #--商品
            js="$(\"input[id$=edKPype]\").last().attr(\"id\",\"itemid\")"
            browser.delaytime(1)
            browser.excutejs(self.driver,js)
            browser.passpeople(self.driver,"itemid",1)
            #print "商品"

            #--确定
            browser.exjscommin(self.driver,"确定")
            #print "确定"

            browser.exjscommin(self.driver,"关闭")
            browser.exjscommin(self.driver,"进货订单")

            #-确认选择
            js="$(\"input[type=checkbox]\").eq(5).click()"
            browser.delaytime(1)
            browser.excutejs(self.driver,js)
            browser.exjscommin(self.driver,"确认选择")

            #打印
            #保存|退出
            browser.delaytime(1)
            browser.exjscommin(self.driver,"退出")
            browser.exjscommin(self.driver,"保存单据")

            browser.findId(self.driver,StockOrder).click()
            browser.delaytime(2,self.driver)
            browser.exjscommin(self.driver,"确认选择")
            browser.exjscommin(self.driver,"退出")
            browser.exjscommin(self.driver,"存入草稿")

            browser.findId(self.driver,StockOrder).click()
            browser.delaytime(2,self.driver)
            browser.exjscommin(self.driver,"确认选择")
            browser.exjscommin(self.driver,"退出")
            browser.exjscommin(self.driver,"废弃退出")

            browser.openModule2(self.driver,modulename,moduledetail)

        except:
            print traceback.format_exc()
            filename=browser.xmlRead(dom,'filename',0)
            browser.delaytime(1)
            browser.getpicture(self.driver,filename+u"进货-进货入库单-普通商品.png")



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
