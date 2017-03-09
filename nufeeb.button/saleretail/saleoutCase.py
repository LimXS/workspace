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

class saleoutTest(unittest.TestCase):
    u'''批零-销售出库单'''

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

    def testsaleitemseriseOut(self):
        u'''批零-销售出库单-序列号商品'''
        header={'cookie':self.cookiestr,"Content-Type": "application/json"}
        comdom=xml.dom.minidom.parse(r'C:\workspace\nufeeb.button\data\commonlocation')
        dom = xml.dom.minidom.parse(r'C:\workspace\nufeeb.button\saleretail\salelocation')

        modulename=browser.xmlRead(dom,"module",0)
        moduledetail=browser.xmlRead(dom,'moduledetail',2)

        browser.openModule2(self.driver,modulename,moduledetail)

        #页面id
        pageurl=browser.xmlRead(dom,"saleouturl",0)
        pageid=browser.getalertid(pageurl,header)
        #print pageid

        #commid,id
        commid=browser.getallcommonid(comdom)

        try:
            itnaid=commid["basetype"]+pageid+browser.xmlRead(dom,"partitna",0)+str(5)+"]"
            browser.findXpath(self.driver,itnaid).click()
            itemid=pageid+commid["grid_pfullname"]
            browser.doubleclick(self.driver,itemid)
            js="$(\"div[class=GridBodyCellText]:contains('Series')\").last().attr(\"id\",\"seitemid\")"
            browser.delaytime(1)
            browser.excutejs(self.driver,js)
            browser.findId(self.driver,"seitemid").click()
            browser.exjscommin(self.driver,"选中并关闭")
            browser.exjscommin(self.driver,"关闭")

            browser.findXpath(self.driver,itnaid).click()
            browser.doubleclick(self.driver,itemid)
            browser.exjscommin(self.driver,"选中并关闭")

            browser.exjscommin(self.driver,"选择")
            browser.exjscommin(self.driver,"选中")
            browser.exjscommin(self.driver,"删除当前行")


            itemser=browser.getrandnumber()
            browser.exjscommin(self.driver,"选择")
            js="$(\"input[id$=edFilterStr]\").val('222')"
            js2="$(\"div[id$=btnFilter]\").last().click()"
            browser.delaytime(1)
            browser.excutejs(self.driver,js)
            browser.excutejs(self.driver,js2)
            browser.exjscommin(self.driver,"全部")

            js="$(\"input[id$=snnoTxt]\").val('"+itemser+"')"
            browser.delaytime(1)
            browser.excutejs(self.driver,js)
            browser.exjscommin(self.driver,"添加",1)
            browser.exjscommin(self.driver,"删除全部")

            browser.exjscommin(self.driver,"导入")
            browser.exjscommin(self.driver,"导入文件")
            browser.accAlert(self.driver,1)
            browser.exjscommin(self.driver,"取消")

            f=open(r'C:\workspace\nufeeb.button\stock\seriesNoitem','r')
            checkNo=f.read()

            js="$(\"input[id$=snnostartTxt]\").val('"+checkNo+"')"
            browser.delaytime(1)
            browser.excutejs(self.driver,js)
            browser.exjscommin(self.driver,"批量添加")
            browser.exjscommin(self.driver,"完成")


            #购买单位
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

            #发货仓库
            edKType=pageid+browser.xmlRead(dom,"edKType",0)
            browser.doubleclick(self.driver,edKType)
            browser.exjscommin(self.driver,"选中")

            #摘要
            edSummary=pageid+browser.xmlRead(dom,"edSummary",0)
            browser.findId(self.driver,edSummary).send_keys(u"中文蘩軆饕餮！@#￥%……&*（）？； 。.Button saleout series item summary")

            #附加说明
            edComment=pageid+browser.xmlRead(dom,"edComment",0)
            browser.findId(self.driver,edComment).send_keys(u"Button saleout series item comment中文蘩軆饕餮！@#￥%……&*（）？； 。.")

            browser.exjscommin(self.driver,"退出")
            browser.exjscommin(self.driver,"保存单据")
            browser.doubleclick(self.driver,edBType)

        except:
            print traceback.format_exc()
            filename=browser.xmlRead(dom,'filename',0)
            browser.delaytime(1)
            browser.getpicture(self.driver,filename+u"批零-销售出库单-序列号商品.png")


    def testsaleOut(self):
        u'''批零-销售出库单-普通商品'''
        header={'cookie':self.cookiestr,"Content-Type": "application/json"}
        comdom=xml.dom.minidom.parse(r'C:\workspace\nufeeb.button\data\commonlocation')
        dom = xml.dom.minidom.parse(r'C:\workspace\nufeeb.button\saleretail\salelocation')

        modulename=browser.xmlRead(dom,"module",0)
        moduledetail=browser.xmlRead(dom,'moduledetail',2)

        browser.openModule2(self.driver,modulename,moduledetail)

        #页面id
        pageurl=browser.xmlRead(dom,"saleouturl",0)
        pageid=browser.getalertid(pageurl,header)
        #print pageid

        #commid,id
        commid=browser.getallcommonid(comdom)

        try:
            #人员核算
            browser.exjscommin(self.driver,"人员核算")
            browser.exjscommin(self.driver,"关闭")
            browser.exjscommin(self.driver,"人员核算")
            js="$(\"input[id$=grid_etypeid_etypename]\").attr(\"id\",\"peocheckid\")"
            browser.delaytime(1)
            browser.excutejs(self.driver,js)
            browser.peoplesel(self.driver,"peocheckid",1)
            js="$(\"div[class=GridBodyCellText]:contains('0')\").text('10')"
            browser.delaytime(1)
            browser.excutejs(self.driver,js)
            browser.exjscommin(self.driver,"确认")

            #购买单位
            companyid=pageid+browser.xmlRead(dom,'edBType',0)
            #print companyid
            browser.buycompanysel(self.driver,companyid)

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
            browser.findId(self.driver,summid).send_keys(u"中文蘩軆饕餮！@#￥%……&*（）？； 。.sale out summary")

            #附加说明
            commentid=pageid+browser.xmlRead(dom,'edComment',0)
            browser.findId(self.driver,commentid).send_keys(u"sale out commentid中文蘩軆饕餮！@#￥%……&*（）？； 。.")

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
            itqty=commid["basetype"]+pageid+itemgrid+str(25)+"]"
            browser.findXpath(self.driver,itqty).click()

            qtyid=pageid+commid["grid_assqty"]
            browser.itemnums(self.driver,qtyid)

            #折前单价
            dpprice=commid["basetype"]+pageid+itemgrid+str(30)+"]"
            browser.delaytime(1)
            browser.findXpath(self.driver,dpprice).click()

            dppriceid=pageid+commid["grid_assdpprice"]
            browser.itemunit(self.driver,dppriceid)

            #录单配置
            conbillid=pageid+browser.xmlRead(dom,"btnBillConfig",0)
            browser.conbill(self.driver,conbillid)
            browser.delaytime(2,self.driver)
            browser.accAlert(self.driver,1)




            #运费结算
            freightid=pageid+browser.xmlRead(dom,"ShowFreight",0)
            browser.freghtend(self.driver,freightid)

             #自义定配置
            selfcon=pageid+commid["button"]+str(1)

            #选择套餐
            choicepackid=pageid+browser.xmlRead(dom,"btnAddSuit",0)
            browser.itempacksel(self.driver,choicepackid)

            #导入商品明细
            imitid=pageid+browser.xmlRead(dom,"btnImportDetail",0)
            browser.impitemdetail(self.driver,imitid)

            #销售订单
            saorid=pageid+browser.xmlRead(dom,"btnSaleOrder",0)

            #-选择单据
            #-关闭
            browser.exjscommin(self.driver,"关闭")
            #-查询条件
            browser.findId(self.driver,saorid).click()
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

            #-确认选择
            js="$(\"input[type=checkbox]\").eq(3).click()"
            browser.delaytime(1)
            browser.excutejs(self.driver,js)
            browser.exjscommin(self.driver,"确认选择")
            browser.delaytime(1)

            #打印

            #物流单打印
            browser.exjscommin(self.driver,"物流单打印")
            browser.exjscommin(self.driver,"执行")
            browser.delaytime(1)
            browser.accAlert(self.driver,1)
            browser.exjscommin(self.driver,"取消")

            #收款账户
            accmonid=pageid+browser.xmlRead(dom,"edAType",0)
            browser.delaytime(1)
            browser.departsel(self.driver,accmonid)


            #保存退出
            saexid=pageid+commid["selclose"]
            browser.findId(self.driver,saexid).click()
            browser.exjscommin(self.driver,"保存单据")
            browser.delaytime(1)

            browser.findXpath(self.driver,itnaid).click()
            browser.doubleclick(self.driver,itemid)
            browser.exjscommin(self.driver,"选中并关闭")
            browser.findId(self.driver,saexid).click()
            browser.exjscommin(self.driver,"存入草稿")
            browser.delaytime(1)

            browser.findXpath(self.driver,itnaid).click()
            browser.doubleclick(self.driver,itemid)
            browser.exjscommin(self.driver,"选中并关闭")
            browser.findId(self.driver,saexid).click()
            browser.exjscommin(self.driver,"废弃退出")
            browser.delaytime(1)

            browser.openModule2(self.driver,modulename,moduledetail)

        except:
            print traceback.format_exc()
            filename=browser.xmlRead(dom,'filename',0)
            browser.delaytime(1)
            browser.getpicture(self.driver,filename+"批零-销售出库单-普通商品.png")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
