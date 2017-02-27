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

class createsaleexchangeTest(unittest.TestCase):
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


    def assernote(self,num1,num2,note,noteok,flag):
        try:
            self.assertEqual(num1,num2,msg=note)
            print noteok
        except AssertionError,msg:
            print msg
            print flag
            print num1
            print num2

    def testcreatesaleExchange(self):
        u'''批零-销售换货单'''
        dom = xml.dom.minidom.parse(r'C:\workspace\moc.pjgsw.nufeeb\src\data\salecreatedata')
        modulename=browser.xmlRead(self.driver,dom,"module",4)
        moduledetail=browser.xmlRead(self.driver,dom,'moduledetail',4)

        browser.openModule2(self.driver,modulename,moduledetail)

        #往来单位
        excompany=browser.xmlRead(self.driver,dom,'excompany',0)
        excomsele=browser.xmlRead(self.driver,dom,'excomsele',0)
        excomok=browser.xmlRead(self.driver,dom,'excomok',0)
        browser.setheader(self.driver,excompany,excomsele,excomok)

        #经手人
        expeople=browser.xmlRead(self.driver,dom,'expeople',0)
        expeoselect=browser.xmlRead(self.driver,dom,'expeoselect',0)
        expeook=browser.xmlRead(self.driver,dom,'expeook',0)
        browser.setheader(self.driver,expeople,expeoselect,expeook)

        #部门
        exdepartment=browser.xmlRead(self.driver,dom,'exdepartment',0)
        exdeselect=browser.xmlRead(self.driver,dom,'exdeselect',0)
        exdeok=browser.xmlRead(self.driver,dom,'exdeok',0)
        browser.setheader(self.driver,exdepartment,exdeselect,exdeok)

        #换入仓库
        exincate=browser.xmlRead(self.driver,dom,'exincate',0)
        exincasele=browser.xmlRead(self.driver,dom,'exincasele',0)
        exincaok=browser.xmlRead(self.driver,dom,'exincaok',0)
        browser.setheader(self.driver,exincate,exincasele,exincaok)

        #换货类型

        #换出仓库
        exoutcate=browser.xmlRead(self.driver,dom,'exoutcate',0)
        exoutselec=browser.xmlRead(self.driver,dom,'exoutselec',0)
        exoutok=browser.xmlRead(self.driver,dom,'exoutok',0)
        browser.setheader(self.driver,exoutcate,exoutselec,exoutok)

        #摘要
        exsummary=browser.xmlRead(self.driver,dom,"exsummary",0)
        browser.findXpath(self.driver,exsummary).send_keys(u"我是摘要销售换货单23333333333................")

        #附加说明
        excomment=browser.xmlRead(self.driver,dom,"excomment",0)
        browser.findXpath(self.driver,excomment).send_keys(u"我是附加说明销售换货单23333333333................")

        #换入商品详情

        #商品名称
        exinitem=browser.xmlRead(self.driver,dom,"exinitem",0)
        exinitemselect=browser.xmlRead(self.driver,dom,"exinitemselect",0)
        exinitinput=browser.xmlRead(self.driver,dom,"exinitinput",0)
        exinitemok=browser.xmlRead(self.driver,dom,"exinitemok",0)

        browser.findXpath(self.driver,exinitem).click()
        browser.findXpath(self.driver,exinitemselect).click()
        time.sleep(1)
        browser.findXpath(self.driver,exinitinput).click()
        browser.findXpath(self.driver,exinitemok).click()

        #数量
        exinitemnum=browser.xmlRead(self.driver,dom,"exinitemnum",0)
        browser.findXpath(self.driver,exinitemnum).send_keys("3")

        #折前单价
        exinitdpprice=browser.xmlRead(self.driver,dom,"exinitdpprice",0)
        exinitdpinput=browser.xmlRead(self.driver,dom,"exinitdpinput",0)
        browser.findXpath(self.driver,exinitdpprice).click()
        browser.findXpath(self.driver,exinitdpinput).send_keys("15.25")

        #折扣
        exinitdiscount=browser.xmlRead(self.driver,dom,"exinitdiscount",0)
        exinitdisinput=browser.xmlRead(self.driver,dom,"exinitdisinput",0)
        browser.findXpath(self.driver,exinitdiscount).click()
        browser.findXpath(self.driver,exinitdisinput).send_keys("0.85")

        browser.findXpath(self.driver,excomment).click()

        #税率
        exinittax=browser.xmlRead(self.driver,dom,"exinittax",0)
        exinittaxinput=browser.xmlRead(self.driver,dom,"exinittaxinput",0)
        browser.findXpath(self.driver,exinittax).click()
        browser.findXpath(self.driver,exinittaxinput).send_keys("15.85")

        browser.findXpath(self.driver,excomment).click()

        print u"换入商品........................................."
        exiniteminfo=browser.xmlRead(self.driver,dom,"exiniteminfo",0)
        n=25

        #商品编号
        #折前金额
        indpmoney=float(browser.findXpath(self.driver,exiniteminfo+str(n)+"]").text)
        cindpmoney=float(15.25*3)
        self.assernote(indpmoney,cindpmoney,u"折前金额不正确(换货页面和原始单据录入，换入商品)",u"折前金额正确",u"折前金额")


        #单价
        inprice=float(browser.findXpath(self.driver,exiniteminfo+str(n+2)+"]").text)
        cinprice=float(15.25*0.85)
        self.assernote(inprice,cinprice,u"单价不正确(换货页面和原始单据录入，换入商品)",u"单价正确",u"单价")

        #金额
        inmoney=float(browser.findXpath(self.driver,exiniteminfo+str(n+3)+"]").text)
        cinmoney=float(indpmoney*0.85)
        cinmoney=round(cinmoney,2)
        self.assernote(inmoney,cinmoney,u"金额不正确(换货页面和原始单据录入，换入商品)",u"金额正确",u"金额")

        #税额
        intaxtotal=float(browser.findXpath(self.driver,exiniteminfo+str(n+5)+"]").text)
        cintaxtotal=float(inmoney*0.1585)
        cintaxtotal=round(cintaxtotal,2)
        self.assernote(intaxtotal,cintaxtotal,u"税额不正确(换货页面和原始单据录入，换入商品)",u"税额正确",u"税额")

        #税后单价
        intaxprice=float(browser.findXpath(self.driver,exiniteminfo+str(n+6)+"]").text)
        cintaxprice=float(inprice*1.1585)
        cintaxprice=round(cintaxprice,4)
        self.assernote(intaxprice,cintaxprice,u"税后单价不正确(换货页面和原始单据录入，换入商品)",u"税后单价正确",u"税后单价")

        #税后金额
        intaxmoney=float(browser.findXpath(self.driver,exiniteminfo+str(n+7)+"]").text)
        cintaxmoney=float(inmoney*1.1585)
        cintaxmoney=round(cintaxmoney,2)
        self.assernote(intaxmoney,cintaxmoney,u"税后金额不正确(换货页面和原始单据录入，换入商品)",u"税后金额正确",u"税后金额")


        #换出商品详情
        print u"换出商品........................................."
        #商品名称
        exoutitem=browser.xmlRead(self.driver,dom,"exoutitem",0)
        exoutitemselect=browser.xmlRead(self.driver,dom,"exoutitemselect",0)
        exoutitinput=browser.xmlRead(self.driver,dom,"exoutitinput",0)
        exoutitemok=browser.xmlRead(self.driver,dom,"exoutitemok",0)

        browser.findXpath(self.driver,exoutitem).click()
        browser.findXpath(self.driver,exoutitemselect).click()
        time.sleep(1)
        browser.findXpath(self.driver,exoutitinput).click()
        browser.findXpath(self.driver,exoutitemok).click()

        #数量
        exoutitemnum=browser.xmlRead(self.driver,dom,"exoutitemnum",0)
        browser.findXpath(self.driver,exoutitemnum).send_keys("3")

        #折前单价
        exoutitdpprice=browser.xmlRead(self.driver,dom,"exoutitdpprice",0)
        exoutitdpinput=browser.xmlRead(self.driver,dom,"exoutitdpinput",0)
        browser.findXpath(self.driver,exoutitdpprice).click()
        browser.findXpath(self.driver,exoutitdpinput).send_keys("16.25")

        #折扣
        exoutitdiscount=browser.xmlRead(self.driver,dom,"exoutitdiscount",0)
        exoutitdisinput=browser.xmlRead(self.driver,dom,"exoutitdisinput",0)
        browser.findXpath(self.driver,exoutitdiscount).click()
        browser.findXpath(self.driver,exoutitdisinput).send_keys("0.95")

        browser.findXpath(self.driver,excomment).click()

        #税率
        exoutittax=browser.xmlRead(self.driver,dom,"exoutittax",0)
        exoutittaxinput=browser.xmlRead(self.driver,dom,"exoutittaxinput",0)
        browser.findXpath(self.driver,exoutittax).click()
        browser.findXpath(self.driver,exoutittaxinput).send_keys("16.85")

        browser.findXpath(self.driver,excomment).click()

        exitemoutinfo=browser.xmlRead(self.driver,dom,"exitemoutinfo",0)

        #商品编号
        #折前金额
        outdpmoney=float(browser.findXpath(self.driver,exitemoutinfo+str(n)+"]").text)
        coutdpmoney=float(16.25*3)
        self.assernote(outdpmoney,coutdpmoney,u"折前金额不正确(换货页面和原始单据录入，换出商品)",u"折前金额正确",u"折前金额")

        #单价
        outprice=float(browser.findXpath(self.driver,exitemoutinfo+str(n+2)+"]").text)
        coutprice=float(16.25*0.95)
        self.assernote(outprice,coutprice,u"单价不正确(换货页面和原始单据录入，换出商品)",u"单价正确",u"单价")

        #金额
        outmoney=float(browser.findXpath(self.driver,exitemoutinfo+str(n+3)+"]").text)
        coutmoney=float(outdpmoney*0.95)
        coutmoney=round(coutmoney,2)
        self.assernote(outmoney,coutmoney,u"金额不正确(换货页面和原始单据录入，换出商品)",u"金额正确",u"金额")

        #税额
        outtaxtaotal=float(browser.findXpath(self.driver,exitemoutinfo+str(n+5)+"]").text)
        couttaxtaotal=float(outmoney*0.1685)
        couttaxtaotal=round(couttaxtaotal,2)
        self.assernote(outtaxtaotal,couttaxtaotal,u"税额不正确(换货页面和原始单据录入，换入商品)",u"税额正确",u"税额")

        #税后单价
        outtaxprice=float(browser.findXpath(self.driver,exitemoutinfo+str(n+6)+"]").text)
        couttaxprice=float(outprice*1.1685)
        couttaxprice=round(couttaxprice,4)
        self.assernote(outtaxprice,couttaxprice,u"税后单价不正确(换货页面和原始单据录入，换出商品)",u"税后单价正确",u"税后单价")

        #税后金额
        outtaxmoney=float(browser.findXpath(self.driver,exitemoutinfo+str(n+7)+"]").text)
        couttaxmoney=float(outmoney*1.1685)
        couttaxmoney=round(couttaxmoney,2)
        self.assernote(outtaxmoney,couttaxmoney,u"税后金额不正确(换货页面和原始单据录入，换出商品)",u"税后金额正确",u"税后金额")

        #保存单据
        try:
            saveandexit=browser.xmlRead(self.driver,dom,"saveandexit",3)
            browser.findXpath(self.driver,saveandexit).click()
            saveok=browser.xmlRead(self.driver,dom,"saveok",3)
            browser.findXpath(self.driver,saveok).click()
        except:
            print u"单据保存失败"
            print(traceback.format_exc())



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
