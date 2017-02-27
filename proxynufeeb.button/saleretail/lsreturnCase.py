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

class lsreturnTest(unittest.TestCase):
    u'''批零-零售退货'''

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


    def testlsReturn(self):
        u'''批零-零售退货.'''
        header={'cookie':self.cookiestr,"Content-Type": "application/json"}
        comdom=xml.dom.minidom.parse(r'C:\workspace\proxynufeeb.button\data\commonlocation')
        dom = xml.dom.minidom.parse(r'C:\workspace\proxynufeeb.button\saleretail\salelocation')

        modulename=browser.xmlRead(dom,"module",0)
        moduledetail=browser.xmlRead(dom,'moduledetail',8)

        browser.openModule2(self.driver,modulename,moduledetail)
        cookies=browser.cookieSave(self.driver)
        header3={'cookie':cookies,"Content-Type": "application/json"}
        header4={'cookie':cookies,"Content-Type": "application/x-www-form-urlencoded"}

        #页面id
        pageurl=browser.xmlRead(dom,"lsreurl",0)
        pageid=browser.getalertid(pageurl,header)
        #print pageid

        #commid,id
        commid=browser.getallcommonid(comdom)
        #id=browser.getcommonid(dom)

        try:
            #零售配置
            reid=pageid+browser.xmlRead(dom,"btnRetailConfig",0)
            browser.findId(self.driver,reid).click()
            browser.delaytime(3,self.driver)
            browser.exjscommin(self.driver,"关闭")
            browser.delaytime(2,self.driver)
            browser.findId(self.driver,reid).click()
            browser.delaytime(3,self.driver)
            js1="$(\"div[class=TabTopCaptionText]:contains('录帐')\").attr(\"id\",\"reaccid\")"
            js3="$(\"div[class=TabTopCaptionText]:contains('默认')\").attr(\"id\",\"slientruleid\")"
            browser.delaytime(1)
            browser.excutejs(self.driver,js1)
            browser.excutejs(self.driver,js3)
            browser.findId(self.driver,"reaccid").click()
            browser.findId(self.driver,"slientruleid").click()

            jscate="$(\"input[id$=edKType]\").last().attr(\"id\",\"edKType\")"
            jspeo="$(\"input[id$=edEType]\").last().attr(\"id\",\"edEType\")"
            jscom="$(\"input[id$=edBType]\").last().attr(\"id\",\"edBType\")"
            jsdep="$(\"input[id$=edDept]\").last().attr(\"id\",\"edDept\")"
            jsstore="$(\"input[id$=edStore]\").last().attr(\"id\",\"edStore\")"
            jspos="$(\"input[id$=edPos]\").last().attr(\"id\",\"edPos\")"

            browser.delaytime(1)
            browser.excutejs(self.driver,jscate)
            browser.excutejs(self.driver,jspeo)
            browser.excutejs(self.driver,jsdep)
            browser.excutejs(self.driver,jsstore)
            browser.excutejs(self.driver,jspos)
            browser.excutejs(self.driver,jscom)
            browser.delaytime(2,self.driver)

            #-仓库
            browser.peoplesel(self.driver,"edKType")

            #-经手人
            browser.peoplesel(self.driver,"edEType",1)

            #-购买单位
            browser.buycompanysel(self.driver,"edBType")

            #-部门
            browser.passpeople(self.driver,"edDept")

            #-门店
            browser.doubleclick(self.driver,"edStore")
            js="$(\"div:contains('mendiantest2')\").last().attr(\"id\",\"selmendian\")"
            browser.delaytime(1)
            browser.excutejs(self.driver,js)
            browser.findId(self.driver,"selmendian").click()

            #-收银台
            browser.doubleclick(self.driver,"edPos")
            js="$(\"div:contains('md2cashd2')\").last().attr(\"id\",\"possel\")"
            browser.delaytime(1)
            browser.excutejs(self.driver,js)
            browser.findId(self.driver,"possel").click()


            browser.exjscommin(self.driver,"保存")
            browser.accAlert(self.driver,1)

            #选择会员
            selmenid=pageid+browser.xmlRead(dom,"btnSelectVipMember",0)
            browser.delaytime(1)
            browser.menbersel(self.driver,selmenid)
            browser.delaytime(1)
            browser.exjscommin(self.driver,"退出")

            #选择套餐
            selpackid=pageid+browser.xmlRead(dom,"btnSelectPTypeSuit",0)
            browser.delaytime(1)
            browser.itempacksel(self.driver,selpackid)
            browser.delaytime(1)
            browser.exjscommin(self.driver,"退出")

            #选择商品
            selitid=pageid+browser.xmlRead(dom,"btnSelectPType",0)
            browser.delaytime(1)
            browser.cateitemsel(self.driver,selitid,1)


            #会员卡
            menidcard=pageid+browser.xmlRead(dom,"mencard",0)
            browser.findId(self.driver,menidcard).click()
            browser.exjscommin(self.driver,"取消")
            browser.findId(self.driver,menidcard).click()
            browser.exjscommin(self.driver,"确定")
            browser.exjscommin(self.driver,"关闭")
            browser.findId(self.driver,menidcard).click()
            js="$(\"input[id$=filter]\").attr(\"value\",\"vip2\")"
            browser.delaytime(1)
            browser.excutejs(self.driver,js)
            browser.exjscommin(self.driver,"确定")


            #提单
            loadid=pageid+browser.xmlRead(dom,"btnLoadBill",0)
            browser.delaytime(1)
            browser.findId(self.driver,loadid).click()
            browser.delaytime(1)
            browser.accAlert(self.driver,0)
            browser.delaytime(1,self.driver)
            browser.findId(self.driver,loadid).click()
            browser.delaytime(1)
            browser.inputid(self.driver,"edDateScope","最近一周")
            browser.exjscommin(self.driver,"查询")
            browser.accAlert(self.driver,1)
            browser.exjscommin(self.driver,"查看")
            browser.exjscommin(self.driver,"返回")
            browser.exjscommin(self.driver,"快速提单")


            #作废单据
            clbillid=pageid+browser.xmlRead(dom,"btnClearBill",0)
            browser.findId(self.driver,clbillid).click()
            browser.accAlert(self.driver,0)
            browser.findId(self.driver,clbillid).click()
            browser.accAlert(self.driver,1)

            #钱箱配置
            posid=pageid+browser.xmlRead(dom,"btnPosConfig",0)

            #小票配置
            priconid=pageid+browser.xmlRead(dom,"btnPrintConfig",0)



            #快捷键
            hotid=pageid+browser.xmlRead(dom,"btnHotkeyConfig",0)
            browser.findId(self.driver,hotid).click()
            browser.delaytime(2,self.driver)
            browser.exjscommin(self.driver,"关闭")

            #商品名字
            browser.findId(self.driver,selitid).click()
            browser.exjscommin(self.driver,"选中")

            #数量
            jsnum="$(\"div[class=GridBodyCellText]:contains('1')\").eq(1).attr(\"id\",\"numid\")"
            browser.delaytime(1)
            browser.excutejs(self.driver,jsnum)
            browser.doubleclick(self.driver,"numid")
            browser.exjscommin(self.driver,"取消")
            browser.doubleclick(self.driver,"numid")
            browser.delaytime(2,self.driver)
            js="$(\"input[id$=edDecimal]\").last().val('2')"
            browser.delaytime(1)
            browser.excutejs(self.driver,js)
            browser.exjscommin(self.driver,"确定")

            #单价
            jsprice="$(\"div[class=GridBodyCellText]:contains('29.5')\").first().attr(\"id\",\"pricid\")"
            browser.delaytime(1)
            browser.excutejs(self.driver,jsprice)
            browser.doubleclick(self.driver,"pricid")
            browser.exjscommin(self.driver,"取消")
            browser.doubleclick(self.driver,"pricid")
            js="$(\"input[id$=edDecimal]\").last().val('31.5')"
            browser.delaytime(1)
            browser.excutejs(self.driver,js)
            browser.exjscommin(self.driver,"确定")

            #折扣
            jsdis="$(\"div[class=GridBodyCellText]:contains('1')\").last().attr(\"id\",\"disid\")"
            browser.delaytime(1)
            browser.excutejs(self.driver,jsdis)
            browser.doubleclick(self.driver,"disid")
            browser.exjscommin(self.driver,"取消")
            browser.doubleclick(self.driver,"disid")
            js="$(\"input[id$=edDecimal]\").last().val('0.9')"
            browser.delaytime(1)
            browser.excutejs(self.driver,js)
            browser.exjscommin(self.driver,"确定")

            #经手人
            peoid=pageid+browser.xmlRead(dom,'edEType',0)
            browser.peoplesel(self.driver,peoid,1)

            #部门
            depid=pageid+browser.xmlRead(dom,'edDept',0)
            browser.passpeople(self.driver,depid)

            #购买单位
            companyid=pageid+browser.xmlRead(dom,'edBType',0)
            #print companyid
            browser.delaytime(1,self.driver)
            browser.buycompanysel(self.driver,companyid)

            browser.excutejs(self.driver,jsstore)
            browser.excutejs(self.driver,jspos)

            #门店
            browser.doubleclick(self.driver,"edStore")
            js="$(\"div:contains('mendiantest2')\").last().attr(\"id\",\"selmendian\")"
            browser.delaytime(1)
            browser.excutejs(self.driver,js)
            browser.findId(self.driver,"selmendian").click()

            #收银台
            browser.doubleclick(self.driver,"edPos")
            js="$(\"div:contains('md2cashd2')\").last().attr(\"id\",\"possel\")"
            browser.delaytime(1)
            browser.excutejs(self.driver,js)
            browser.findId(self.driver,"possel").click()


            #结算
            accend=pageid+commid["btnSave"]
            browser.findId(self.driver,accend).click()
            #-取消
            browser.exjscommin(self.driver,"取消")
            browser.findId(self.driver,accend).click()
            #-多账户选择
            browser.exjscommin(self.driver,"多账户选择")
            browser.exjscommin(self.driver,"取消")
            browser.exjscommin(self.driver,"多账户选择")
            browser.exjscommin(self.driver,"确定")

            #-实收金额
            js="$(\"input[id$=edReciveMoney]\").val('100')"
            browser.delaytime(1)
            browser.excutejs(self.driver,js)
            #-结算完成
            browser.exjscommin(self.driver,"结算完成")
            browser.findId(self.driver,selitid).click()
            browser.exjscommin(self.driver,"关闭")



        except:
            print traceback.format_exc()
            filename=browser.xmlRead(dom,'filename',0)
            #print filename+u"常用-单据草稿.png"
            #browser.getpicture(self.driver,filename+u"notedraft.png")
            browser.getpicture(self.driver,filename+u"批零-零售退货.png")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
