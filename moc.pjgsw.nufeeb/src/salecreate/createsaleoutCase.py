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

class createsaleoutTest(unittest.TestCase):
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


    def assernote(self,num1,num2,note,noteok,flag):
        try:
            self.assertEqual(num1,num2,msg=note)
            print noteok
        except AssertionError,msg:
            print msg
            print flag
            print num1
            print num2

    def stockstatus(self):
        '''常用-库存状况'''
        #计算成本
        #主仓库
        pass
        #在途仓库

    def testcreatesaleOut(self):
        u'''批零-销售出库单(调用销售订单)'''
        dom = xml.dom.minidom.parse(r'C:\workspace\moc.pjgsw.nufeeb\src\data\salecreatedata')
        modulename=browser.xmlRead(self.driver,dom,"module",2)
        moduledetail=browser.xmlRead(self.driver,dom,'moduledetail',2)

        browser.openModule2(self.driver,modulename,moduledetail)

        time.sleep(1)

        saleorderdata=browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\saleordercheckdata','r',1,'aaa')
        flagnum=saleorderdata[0].strip()

        saleorderxpath=browser.xmlRead(self.driver,dom,'saleorderxpath',0)
        browser.findXpath(self.driver,saleorderxpath).click()

        #选择单据
        header={'cookie':self.cookiestr,"Content-Type": "application/json"}
        header2={'cookie':self.cookiestr,"Content-Type": "application/x-www-form-urlencoded"}
        #note page id
        noteidrul="http://beefun.wsgjp.com/Beefun/Bill/OrderSelector.gspx"
        noteidda="{\"btypeid\":null,\"isBtypeEnable\":true,\"bfullname\":null,\"isKtypeEnable\":true,\"vchtype\":\"saleorder\",\"wholeSale\":false,\"isShowSameNumber\":true}"
        noteiddata={"__Params":noteidda}
        noteidtext=requests.post(url=noteidrul,data=noteiddata,headers=header2)
        #print noteidtext.text
        noteid=browser.getpageid(noteidtext)

        #note page detail
        nodeurl="http://beefun.wsgjp.com/Carpa.Web/Carpa.Web.Script.DataService.ajax/GetPagerData"
        nodedata={"pagerId":noteid,"queryParams":None,"orders":None,"filter":None,"first":0,"count":1000}
        nodetailtext=requests.post(url=nodeurl,data=json.dumps(nodedata),headers=header)
        #print nodetailtext.text
        noitdetail=browser.datatrunjson(nodetailtext)

        ordetail=''
        for ordedata in noitdetail["itemList"]["rows"]:
            if ordedata[3]==flagnum:
                ordetail=ordedata
                print u"销售订单管理审核通过至销售出库单"
                break


        if len(ordetail)==0:
            print u"销售订单管理审核至销售出库单无此单据，测试不通过"
        else:
            #note item detail
            noitdeurl="http://beefun.wsgjp.com/Beefun/Beefun.Bill.OrderSelector.ajax/GetOrderDetails"
            noitdedata={"querydata":{"ordercode":ordetail[0],"ktypeid":ordetail[15],"btypeid":ordetail[6],"vchtype":8,"wmsOrder":False,"ischecked":True,"ptypeid":0}}
            noitemdetailtext=requests.post(url=noitdeurl,data=json.dumps(noitdedata),headers=header)
            #print noitemdetailtext.text
            noitemdetail=browser.datatrunjson(noitemdetailtext)

            #录单日期
            inputdate=saleorderdata[1].strip()
            orinputdate=ordetail[4]
            self.assernote(str(inputdate),str(orinputdate.strip()),u"录单日期不正确（原始订单和销售出库单选择单据页面）",u"录单日期正确",u"录单日期")

            #往来单位
            company=saleorderdata[2].strip()
            orcom=ordetail[5].strip()
            self.assernote(str(company),str(orcom),u"往来单位不正确（原始订单和销售出库单选择单据页面）",u"往来单位正确",u"往来单位")

            #交货日期
            givedate=saleorderdata[5].strip()
            orgivedate=ordetail[7].strip()
            self.assernote(str(givedate),str(orgivedate),u"交货日期不正确（原始订单和销售出库单选择单据页面）",u"交货日期正确",u"交货日期")

            #经手人
            passpeople=saleorderdata[3].strip()
            orpeople=ordetail[10].strip()
            self.assernote(str(passpeople),str(orpeople),u"经手人不正确（原始订单和销售出库单选择单据页面）",u"经手人正确",u"经手人")

            #仓库
            cate=saleorderdata[6].strip()
            orcate=ordetail[16]
            self.assernote(str(cate),str(orcate),u"仓库不正确（原始订单和销售出库单选择单据页面）",u"仓库正确",u"仓库")

            #部门
            department=saleorderdata[4].strip()
            ordepart=ordetail[17]
            self.assernote(str(department),str(ordepart),u"部门不正确（原始订单和销售出库单选择单据页面）",u"部门正确",u"部门")

            #附加说明
            comment=saleorderdata[8].strip()
            orcomment=ordetail[13]
            self.assernote(str(comment),str(orcomment),u"附加说明不正确（原始订单和销售出库单选择单据页面）",u"附加说明正确",u"附加说明")

            #摘要
            summary=saleorderdata[7].strip()
            orsummery=ordetail[14]
            self.assernote(str(summary),str(orsummery),u"摘要不正确（原始订单和销售出库单选择单据页面）",u"摘要正确",u"摘要")

            choiceorder=browser.xmlRead(self.driver,dom,'choiceorder',0)
            time.sleep(2)
            browser.findXpath(self.driver,choiceorder).click()


            #print "checkdata no............"
            #print flagnum
            #销售出库单
            '''
            #录单日期
            inputdate
            noitemdetail

            #购买单位
            company

            #经手人
            #self.assernote(str(passpeople),str(noitemdetail[0]["pname"]),u"经手人不正确（原始订单和销售出库单页面）",u"经手人正确",u"经手人")



            #发货仓库
            cate

            #摘要
            summary
            #附加说明
            comment
            '''

            #商品信息
            #商品编号
            itemcode=saleorderdata[9].strip()
            self.assernote(str(itemcode),str(noitemdetail[0]["ptypecode"]),u"商品编号不正确（原始订单和销售出库单页面）",u"商品编号正确",u"商品编号")

            #商品名称
            itemname=saleorderdata[10].strip()
            self.assernote(str(itemname),str(noitemdetail[0]["pfullname"]),u"商品名称不正确（原始订单和销售出库单页面）",u"商品名称正确",u"商品名称")

             #数量
            itemnumbers=float(saleorderdata[11].strip())
            self.assernote(str(itemnumbers),str(noitemdetail[0]["qty"]),u"商品数量不正确（原始订单和销售出库单页面）",u"商品数量正确",u"商品数量")

            #折前单价
            dpsigle=float(saleorderdata[12].strip())
            self.assernote(str("%.4f"%dpsigle),str("%.4f"%noitemdetail[0]["dpprice"]),u"折前单价不正确（原始订单和销售出库单页面）",u"折前单价正确",u"折前单价")

            #折前金额
            dpmoney=float(saleorderdata[13].strip())
            self.assernote(str("%.4f"%dpmoney),str("%.4f"%noitemdetail[0]["dptotal"]),u"折前金额不正确（原始订单和销售出库单页面）",u"折前金额正确",u"折前金额")

            #折扣
            discount=float(saleorderdata[14].strip())
            self.assernote(str(discount),str("%.2f"%noitemdetail[0]["discount"]),u"折扣不正确（原始订单和销售出库单页面）",u"折扣正确",u"折扣")

            #单价
            sigle=float(saleorderdata[15].strip())
            self.assernote(str("%.4f"%sigle),str("%.4f"%noitemdetail[0]["tpprice"]),u"单价不正确（原始订单和销售出库单页面）",u"单价正确",u"单价")

            #金额
            money=float(saleorderdata[16].strip())
            self.assernote(str("%.4f"%money),str("%.4f"%noitemdetail[0]["tptotal"]),u"金额不正确（原始订单和销售出库单页面）",u"金额正确",u"金额")

            #税率
            tax=float(saleorderdata[17].strip())
            self.assernote(str(tax),str("%.2f"%noitemdetail[0]["tax"]),u"税率不正确（原始订单和销售出库单页面）",u"税率正确",u"税率")

            #税额
            taxtotal=float(saleorderdata[18].strip())
            self.assernote(str("%.4f"%taxtotal),str("%.4f"%noitemdetail[0]["taxtotal"]),u"税额不正确（原始订单和销售出库单页面）",u"税额正确",u"税额")

            #税后单价
            taxsigle=float(saleorderdata[19].strip())
            self.assernote(str("%.4f"%taxsigle),str("%.4f"%noitemdetail[0]["price"]),u"税后单价不正确（原始订单和销售出库单页面）",u"税后单价正确",u"税后单价")

            #税后金额
            taxmoney=float(saleorderdata[20].strip())
            self.assernote(str("%.4f"%taxmoney),str("%.4f"%noitemdetail[0]["total"]),u"税后金额不正确（原始订单和销售出库单页面）",u"税后金额正确",u"税后金额")

            #备注
            #money=float(saleorderdata[16])

            #保存前库存状况
            catedata=browser.catestatus(header,flag=0)

            #保存和退出单据
            try:
                saveandexit=browser.xmlRead(self.driver,dom,"saveandexit",1)
                browser.findXpath(self.driver,saveandexit).click()
                saveok=browser.xmlRead(self.driver,dom,"saveok",1)
                browser.findXpath(self.driver,saveok).click()
            except:
                print u"单据保存失败"
                print(traceback.format_exc())

            #保存后科目详情


    def testcreateornewsaleOut(self):
        u'''批零-销售出库单(新建原始单据)'''
        dom = xml.dom.minidom.parse(r'C:\workspace\moc.pjgsw.nufeeb\src\data\salecreatedata')
        modulename=browser.xmlRead(self.driver,dom,"module",2)
        moduledetail=browser.xmlRead(self.driver,dom,'moduledetail',2)

        browser.openModule2(self.driver,modulename,moduledetail)

        #购买单位
        outcompany=browser.xmlRead(self.driver,dom,"outcompany",0)
        outcomsele=browser.xmlRead(self.driver,dom,"outcomsele",0)
        outcomok=browser.xmlRead(self.driver,dom,"outcomok",0)
        browser.setheader(self.driver,outcompany,outcomsele,outcomok)

        #经手人
        outpeople=browser.xmlRead(self.driver,dom,"outpeople",0)
        outselepeo=browser.xmlRead(self.driver,dom,"outselepeo",0)
        outpeook=browser.xmlRead(self.driver,dom,"outpeook",0)
        browser.setheader(self.driver,outpeople,outselepeo,outpeook)

        #部门
        outdepart=browser.xmlRead(self.driver,dom,"outdepart",0)
        outdeselect=browser.xmlRead(self.driver,dom,"outdeselect",0)
        outdeseok=browser.xmlRead(self.driver,dom,"outdeseok",0)
        browser.setheader(self.driver,outdepart,outdeselect,outdeseok)

        #发货仓库
        outcate=browser.xmlRead(self.driver,dom,"outcate",0)
        outcaselect=browser.xmlRead(self.driver,dom,"outcaselect",0)
        outcateok=browser.xmlRead(self.driver,dom,"outcateok",0)
        browser.setheader(self.driver,outcate,outcaselect,outcateok)

        #摘要
        outsummary=browser.xmlRead(self.driver,dom,"outsummary",0)
        browser.findXpath(self.driver,outsummary).send_keys(u"销售出库单我是摘要.....summary233333")

        #附加说明
        outcomment=browser.xmlRead(self.driver,dom,"outcomment",0)
        browser.findXpath(self.driver,outcomment).send_keys(u"销售出库单我是附加说明.....comment233333")


        #商品信息
        #商品名称
        outitem=browser.xmlRead(self.driver,dom,"outitem",0)
        outitemselect=browser.xmlRead(self.driver,dom,"outitemselect",0)
        outiteminput=browser.xmlRead(self.driver,dom,"outiteminput",0)
        outitemok=browser.xmlRead(self.driver,dom,"outitemok",0)

        browser.findXpath(self.driver,outitem).click()
        browser.findXpath(self.driver,outitemselect).click()
        time.sleep(2)
        browser.findXpath(self.driver,outiteminput).click()
        browser.findXpath(self.driver,outitemok).click()


        #数量
        outitemnum=browser.xmlRead(self.driver,dom,"outitemnum",0)
        browser.findXpath(self.driver,outitemnum).send_keys("3")

        #折前单价
        time.sleep(1)
        outitemdprice=browser.xmlRead(self.driver,dom,"outitemdprice",0)
        outitemdpinput=browser.xmlRead(self.driver,dom,"outitemdpinput",0)
        browser.findXpath(self.driver,outitemdprice).click()
        browser.findXpath(self.driver,outitemdpinput).send_keys("15.25")

        #折扣
        outitemdiscount=browser.xmlRead(self.driver,dom,"outitemdiscount",0)
        outitemdisinput=browser.xmlRead(self.driver,dom,"outitemdisinput",0)
        browser.findXpath(self.driver,outitemdiscount).click()
        browser.findXpath(self.driver,outitemdisinput).send_keys("0.85")

        browser.findXpath(self.driver,outcomment).click()

        #税率
        outitemtax=browser.xmlRead(self.driver,dom,"outitemtax",0)
        outitemtaxinput=browser.xmlRead(self.driver,dom,"outitemtaxinput",0)
        browser.findXpath(self.driver,outitemtax).click()
        browser.findXpath(self.driver,outitemtaxinput).send_keys("15.85")

        browser.findXpath(self.driver,outcomment).click()


        outiteminfo=browser.xmlRead(self.driver,dom,"outiteminfo",0)
        n=28

        #商品编号
        #折前金额
        dpmoney=float(browser.findXpath(self.driver,outiteminfo+str(n)+"]").text)
        cdpmoney=float(15.25*3)
        self.assernote(dpmoney,cdpmoney,u"折前金额不正确",u"折前金额正确",u"折前金额")


        #单价
        price=float(browser.findXpath(self.driver,outiteminfo+str(n+2)+"]").text)
        cprice=float(15.25*0.85)
        self.assernote(price,cprice,u"单价不正确",u"单价正确",u"单价")

        #金额
        money=float(browser.findXpath(self.driver,outiteminfo+str(n+3)+"]").text)
        cmoney=float(dpmoney*0.85)
        cmoney=round(cmoney,2)
        self.assernote(money,cmoney,u"金额不正确",u"金额正确",u"金额")

        #税额
        taxtotal=float(browser.findXpath(self.driver,outiteminfo+str(n+5)+"]").text)
        ctaxtotal=float(money*0.1585)
        ctaxtotal=round(ctaxtotal,2)
        self.assernote(taxtotal,ctaxtotal,u"税额不正确",u"税额正确",u"税额")

        #税后单价
        taxprice=float(browser.findXpath(self.driver,outiteminfo+str(n+6)+"]").text)
        ctaxprice=float(price*1.1585)
        ctaxprice=round(ctaxprice,4)
        self.assernote(taxprice,ctaxprice,u"税后单价不正确",u"税后单价正确",u"税后单价")

        #税后金额
        taxmoney=float(browser.findXpath(self.driver,outiteminfo+str(n+7)+"]").text)
        ctaxmoney=float(money*1.1585)
        ctaxmoney=round(ctaxmoney,2)
        self.assernote(taxmoney,ctaxmoney,u"税后金额不正确",u"税后金额正确",u"税后金额")

        #保存前库存状况
        header={'cookie':self.cookiestr,"Content-Type": "application/json"}
        catedata=browser.catestatus(header,flag=0)
        #for item in catedata[0]["itemList"]:
        #    if item[""]==

        #保存和退出单据
        try:
            saveandexit=browser.xmlRead(self.driver,dom,"saveandexit",1)
            browser.findXpath(self.driver,saveandexit).click()
            saveok=browser.xmlRead(self.driver,dom,"saveok",1)
            browser.findXpath(self.driver,saveok).click()
        except:
            print u"单据保存失败"
            print(traceback.format_exc())

        #保存后科目详情

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()

