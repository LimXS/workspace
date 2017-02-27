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

class createsalereturnTest(unittest.TestCase):
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


    def assernote(self,num1,num2,note,noteok,flag):
        try:
            self.assertEqual(num1,num2,msg=note)
            print noteok
        except AssertionError,msg:
            print msg
            print flag
            print num1
            print num2

    def testcreatesaleReturn(self):
        u'''批零-销售退货单-新增'''
        dom = xml.dom.minidom.parse(r'C:\workspace\moc.pjgsw.nufeeb\src\data\salecreatedata')
        modulename=browser.xmlRead(self.driver,dom,"module",3)
        moduledetail=browser.xmlRead(self.driver,dom,'moduledetail',3)

        browser.openModule2(self.driver,modulename,moduledetail)
        time.sleep(1)

        #退货单位
        recompany=browser.xmlRead(self.driver,dom,"recompany",0)
        recompanysele=browser.xmlRead(self.driver,dom,"recompanysele",0)
        recompanyok=browser.xmlRead(self.driver,dom,"recompanyok",0)
        browser.setheader(self.driver,recompany,recompanysele,recompanyok)

        #经手人
        repeople=browser.xmlRead(self.driver,dom,"repeople",0)
        repeoselect=browser.xmlRead(self.driver,dom,"repeoselect",0)
        repeook=browser.xmlRead(self.driver,dom,"repeook",0)
        browser.setheader(self.driver,repeople,repeoselect,repeook)

        #部门
        redepart=browser.xmlRead(self.driver,dom,"redepart",0)
        redeselect=browser.xmlRead(self.driver,dom,"redeselect",0)
        redeseok=browser.xmlRead(self.driver,dom,"redeseok",0)
        browser.setheader(self.driver,redepart,redeselect,redeseok)

        #收货仓库
        recate=browser.xmlRead(self.driver,dom,"recate",0)
        recateselect=browser.xmlRead(self.driver,dom,"recateselect",0)
        recateok=browser.xmlRead(self.driver,dom,"recateok",0)
        browser.setheader(self.driver,recate,recateselect,recateok)

        #摘要
        resummary=browser.xmlRead(self.driver,dom,"resummary",0)
        browser.findXpath(self.driver,resummary).send_keys(u"我是摘要.....summary233333")

        #附加说明
        recomment=browser.xmlRead(self.driver,dom,"recomment",0)
        browser.findXpath(self.driver,recomment).send_keys(u"我是附加说明.....comment233333")

        #商品明细
        #商品名称
        reitem=browser.xmlRead(self.driver,dom,"reitem",0)
        reitemselect=browser.xmlRead(self.driver,dom,"reitemselect",0)
        reiteminput=browser.xmlRead(self.driver,dom,"reiteminput",0)
        reitemok=browser.xmlRead(self.driver,dom,"reitemok",0)

        browser.findXpath(self.driver,reitem).click()
        browser.findXpath(self.driver,reitemselect).click()
        time.sleep(2)
        browser.findXpath(self.driver,reiteminput).click()

        #名称和编号判断是否正确录入
        inputreitemname=browser.xmlRead(self.driver,dom,"inputreitemname",0)
        inputreitemcode=browser.xmlRead(self.driver,dom,"inputreitemcode",0)
        inputname=browser.findXpath(self.driver,inputreitemname).text
        inputcode=browser.findXpath(self.driver,inputreitemcode).text
        reitemcode=browser.xmlRead(self.driver,dom,"reitemcode",0)

        browser.findXpath(self.driver,reitemok).click()
        time.sleep(1)
        itemcode=browser.findXpath(self.driver,reitemcode).text
        reitemname=browser.findXpath(self.driver,reitem).text

        self.assernote(inputname,reitemname,u"商品名称不正确",u"商品名称正确(输入和显示)",u"商品名称")
        self.assernote(inputcode,itemcode,u"商品编号不正确",u"商品编号正确(输入和显示)",u"商品编号")




        #数量
        reitemnumbers=browser.xmlRead(self.driver,dom,"reitemnumbers",0)
        browser.findXpath(self.driver,reitemnumbers).send_keys("3")

        #折前单价
        reitemdpsigle=browser.xmlRead(self.driver,dom,"reitemdpsigle",0)
        reitdpsinput=browser.xmlRead(self.driver,dom,"reitdpsinput",0)
        browser.findXpath(self.driver,reitemdpsigle).click()
        browser.findXpath(self.driver,reitdpsinput).send_keys("15.25")

        #折扣
        rediscount=browser.xmlRead(self.driver,dom,"rediscount",0)
        redisinput=browser.xmlRead(self.driver,dom,"redisinput",0)
        browser.findXpath(self.driver,rediscount).click()
        browser.findXpath(self.driver,redisinput).send_keys("0.85")

        browser.findXpath(self.driver,recomment).click()

        #税率
        retax=browser.xmlRead(self.driver,dom,"retax",0)
        retaxinput=browser.xmlRead(self.driver,dom,"retaxinput",0)
        browser.findXpath(self.driver,retax).click()
        browser.findXpath(self.driver,retaxinput).send_keys("16.25")

        browser.findXpath(self.driver,recomment).click()

        #折前金额
        n=27
        reitxml=browser.xmlRead(self.driver,dom,"reiteminfo",0)
        reitdpmoneyxpath=reitxml+str(n)+"]"
        reitdpmoney=float(browser.findXpath(self.driver,reitdpmoneyxpath).text)
        dpmoney=float(15.25*3)
        self.assernote(dpmoney,reitdpmoney,u"折前金额不正确",u"折前金额正确",u"折前金额")

        #单价
        reitsiglexpath=reitxml+str(n+2)+"]"
        reitsigle=float(browser.findXpath(self.driver,reitsiglexpath).text)
        sigle=float(15.25*0.85)
        self.assernote(sigle,reitsigle,u"单价不正确",u"单价正确",u"单价")

        #金额
        reitmoneyxpath=reitxml+str(n+3)+"]"
        reitmoney=float(browser.findXpath(self.driver,reitmoneyxpath).text)
        money=float(dpmoney*0.85)
        money=round(money,2)
        self.assernote(money,reitmoney,u"金额不正确",u"金额正确",u"金额")

        #税额
        reittaxtotalxpath=reitxml+str(n+5)+"]"
        reittaxtotal=float(browser.findXpath(self.driver,reittaxtotalxpath).text)
        comtaxtotal=float(0.1625*money)
        comtaxtotal=round(comtaxtotal,2)
        self.assernote(reittaxtotal,comtaxtotal,u"税额不正确",u"税额正确",u"税额")

        #税后单价
        reittaxsiglexpath=reitxml+str(n+6)+"]"
        reittaxsigle=float(browser.findXpath(self.driver,reittaxsiglexpath).text)
        comtaxsigleprice=float(1.1625*sigle)
        comtaxsigleprice=round(comtaxsigleprice,4)
        self.assernote(reittaxsigle,comtaxsigleprice,u"税后单价不正确",u"税后单价正确",u"税后单价")

        #税后金额
        reittaxmoneyxpath=reitxml+str(n+7)+"]"
        reittaxmoney=float(browser.findXpath(self.driver,reittaxmoneyxpath).text)

        comtaxmoney=float(1.1625*money)
        comtaxmoney=round(comtaxmoney,2)
        self.assernote(reittaxmoney,comtaxmoney,u"税后金额不正确",u"税后金额正确",u"税后金额")


        #保存和退出单据
        try:
            saveandexit=browser.xmlRead(self.driver,dom,"saveandexit",2)
            browser.findXpath(self.driver,saveandexit).click()
            saveok=browser.xmlRead(self.driver,dom,"saveok",2)
            browser.findXpath(self.driver,saveok).click()
        except:
            print u"单据保存失败"
            print(traceback.format_exc())

    def testororderReturn(self):
        u'''批零-销售退货单-原单退货'''
        dom = xml.dom.minidom.parse(r'C:\workspace\moc.pjgsw.nufeeb\src\data\salecreatedata')
        modulename=browser.xmlRead(self.driver,dom,"module",3)
        moduledetail=browser.xmlRead(self.driver,dom,'moduledetail',3)

        browser.openModule2(self.driver,modulename,moduledetail)
        time.sleep(1)

        orreturn=browser.xmlRead(self.driver,dom,'orreturn',0)
        browser.findXpath(self.driver,orreturn).click()

        #order return id
        header={'cookie':self.cookiestr,"Content-Type": "application/json"}
        header2={'cookie':self.cookiestr,"Content-Type": "application/x-www-form-urlencoded"}

        oridurl="http://beefun.wsgjp.com/Beefun/Bill/BillSelector.gspx"
        oriddata={"__Params":"{\"vchtype\":11}"}
        oridtext=requests.post(url=oridurl,data=oriddata,headers=header2)
        orid=browser.getpageid(oridtext)

        #order lists
        orlisturl="http://beefun.wsgjp.com/Carpa.Web/Carpa.Web.Script.DataService.ajax/GetPagerData"
        orlistdata={"pagerId":orid,"queryParams":None,"orders":None,"filter":None,"first":0,"count":1000}
        orlisttext=requests.post(url=orlisturl,data=json.dumps(orlistdata),headers=header)
        #print orlisttext.text
        orlists=browser.datatrunjson(orlisttext)


        saleorderdata=browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\saleordercheckdata','r',1,'aaa')
        flagnum=saleorderdata[0].strip()
        print "checkdata no............"
        print flagnum

        order=''
        for temp in orlists["itemList"]["rows"]:
            #print "temp..............."
            #print temp
            #print temp[10][5:21]
            if temp[10][5:21]==flagnum:
                order=temp
                print u"原单退货中有该订单，测试成功..."
                break
        if len(order)==0:
            print u"原单退货没有有该订单，测试不通过..."
        else:
            print u"原单退货和原始单据录入................"
            #录单日期
            self.assernote(str(browser.handlestampdays(order[1],1)),str(saleorderdata[1].strip()),u"录单日期不正确(原单退货和原始单据录入)",u"录单日期正确",u"录单日期")
            #order[12]

            #购买单位
            self.assernote(str(order[13]),str(saleorderdata[2].strip()),u"购买单位不正确(原单退货和原始单据录入)",u"购买单位正确",u"购买单位")

            #经手人
            self.assernote(str(order[15]),str(saleorderdata[3].strip()),u"经手人不正确(原单退货和原始单据录入)",u"经手人正确",u"经手人")

            #仓库
            self.assernote(str(order[14]),str(saleorderdata[6].strip()),u"仓库不正确(原单退货和原始单据录入)",u"仓库正确",u"仓库")

            #金额
            self.assernote(float(order[11]),float(saleorderdata[20].strip()),u"金额不正确(原单退货和原始单据录入)",u"金额正确",u"金额")

            #过账时间

            #摘要
            self.assernote(str(order[9][4:]),str(saleorderdata[7].strip()),u"摘要不正确(原单退货和原始单据录入)",u"摘要正确",u"摘要")

            #page data
            pagedeurl="http://beefun.wsgjp.com/Beefun/Beefun.Bill.SaleBackBill.ajax/FromSaleBill"
            pagededa={"vchcode": order[0]}
            pagedetext=requests.post(url=pagedeurl,data=json.dumps(pagededa),headers=header)
            pagedetail=browser.datatrunjson(pagedetext)

            print u"退货页面和原始单据录入.........................."
            #退货单位
            self.assernote(str(pagedetail["bfullname"]),str(saleorderdata[2].strip()),u"退货单位不正确(退货页面和原始单据录入)",u"退货单位正确",u"退货单位")

            #经手人
            self.assernote(str(pagedetail["efullname"]),str(saleorderdata[3].strip()),u"经手人不正确(退货页面和原始单据录入)",u"经手人正确",u"经手人")

            #部门
            self.assernote(str(pagedetail["dfullname"]),str(saleorderdata[4].strip()),u"部门不正确(退货页面和原始单据录入)",u"部门正确",u"部门")

            #收货仓库
            self.assernote(str(pagedetail["kfullname"]),str(saleorderdata[6].strip()),u"收货仓库不正确(退货页面和原始单据录入)",u"收货仓库正确",u"收货仓库")

            #摘要
            self.assernote(str(pagedetail["summary"]),'',u"摘要不正确(退货页面和原始单据录入)",u"摘要正确",u"摘要")

            #附加说明
            self.assernote(str(pagedetail["comment"]),u"原销售单："+str(order[2]),u"附加说明不正确(退货页面和原始单据录入)",u"附加说明正确",u"附加说明")

            #商品信息
            #商品编号
            self.assernote(str(pagedetail["details"][0]["ptypecode"]),str(saleorderdata[9].strip()),u"商品编号不正确(退货页面和原始单据录入)",u"商品编号正确",u"商品编号")

            #商品名称
            self.assernote(str(pagedetail["details"][0]["pfullname"]),str(saleorderdata[10].strip()),u"商品名称不正确(退货页面和原始单据录入)",u"商品名称正确",u"商品名称")

            #数量
            self.assernote(float(pagedetail["details"][0]["qty"]),float(saleorderdata[11].strip()),u"数量不正确(退货页面和原始单据录入)",u"数量正确",u"数量")

            #折前单价
            self.assernote(float(pagedetail["details"][0]["dpprice"]),float(saleorderdata[12].strip()),u"折前单价不正确(退货页面和原始单据录入)",u"折前单价正确",u"折前单价")

            #折前金额
            self.assernote(float(pagedetail["details"][0]["dptotal"]),float(saleorderdata[13].strip()),u"折前金额不正确(退货页面和原始单据录入)",u"折前金额正确",u"折前金额")

            #折扣
            self.assernote(float(pagedetail["details"][0]["discount"]),float(saleorderdata[14].strip()),u"折扣不正确(退货页面和原始单据录入)",u"折扣正确",u"折扣")

            #单价
            self.assernote(float(pagedetail["details"][0]["tpprice"]),float(saleorderdata[15].strip()),u"单价不正确(退货页面和原始单据录入)",u"单价正确",u"单价")

            #金额
            self.assernote(float(pagedetail["details"][0]["tptotal"]),float(saleorderdata[16].strip()),u"金额不正确(退货页面和原始单据录入)",u"金额正确",u"金额")

            #税率
            self.assernote(float(pagedetail["details"][0]["tax"]),float(saleorderdata[17].strip()),u"税率不正确(退货页面和原始单据录入)",u"税率正确",u"税率")

            #税额
            self.assernote(float(pagedetail["details"][0]["taxtotal"]),float(saleorderdata[18].strip()),u"税额不正确(退货页面和原始单据录入)",u"税额正确",u"税额")

            #税后单价
            self.assernote(float(pagedetail["details"][0]["price"]),float(saleorderdata[19].strip()),u"税后单价不正确(退货页面和原始单据录入)",u"税后单价正确",u"税后单价")

            #税后金额
            self.assernote(float(pagedetail["details"][0]["total"]),float(saleorderdata[20].strip()),u"税后金额不正确(退货页面和原始单据录入)",u"税后金额正确",u"税后金额")

            #备注

            #选择并保存单据
            try:
                reorchoice=browser.xmlRead(self.driver,dom,"reorchoice",0)
                browser.findXpath(self.driver,reorchoice).click()
                saveandexit=browser.xmlRead(self.driver,dom,"saveandexit",2)
                browser.findXpath(self.driver,saveandexit).click()
                saveok=browser.xmlRead(self.driver,dom,"saveok",2)
                browser.findXpath(self.driver,saveok).click()
            except:
                print u"单据保存失败"
                print(traceback.format_exc())






if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()

