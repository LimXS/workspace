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

class createnewsaleorderTest(unittest.TestCase):
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


    def assernote(self,num1,num2,note,noteok,flag):
        try:
            self.assertEqual(num1,num2,msg=note)
            print noteok
        except AssertionError,msg:
            print msg
            print flag
            print num1
            print num2

    def testcreatenewsaleOrder(self):
        u'''批零-新增销售订单'''
        dom = xml.dom.minidom.parse(r'C:\workspace\moc.pjgsw.nufeeb\src\data\salecreatedata')
        modulename=browser.xmlRead(self.driver,dom,"module",0)
        moduledetail=browser.xmlRead(self.driver,dom,'moduledetail',0)

        browser.openModule2(self.driver,modulename,moduledetail)

        #编号
        time.sleep(2)
        idlocation=browser.xmlRead(self.driver,dom,'idlocation',0)
        js="var code=document.getElementById('"+idlocation+"').value;"+idlocation+".setAttribute('value',code);"
        self.driver.execute_script(js)
        id=browser.findId(self.driver,idlocation).get_attribute("value")
        #print id
        browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\saleordercheckdata','w',0,id)
        browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\saleordercheckdata','a+',0,'\n')


        #录单日期
        time.sleep(2)
        inputdate=browser.xmlRead(self.driver,dom,'inputdate',0)
        js="var code=document.getElementById('"+inputdate+"').value;"+inputdate+".setAttribute('value',code);"
        self.driver.execute_script(js)
        inputdate=browser.findId(self.driver,inputdate).get_attribute("value")
        browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\saleordercheckdata','a+',0,inputdate)
        browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\saleordercheckdata','a+',0,'\n')

        try:
            #购买单位
            buycompany=browser.xmlRead(self.driver,dom,"buycompany",0)
            buycomsele=browser.xmlRead(self.driver,dom,"buycomsele",0)
            buycomseok=browser.xmlRead(self.driver,dom,"buycomseok",0)


            browser.findXpath(self.driver,buycompany).click()
            browser.findXpath(self.driver,buycomsele).click()
            browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\saleordercheckdata','a+',0,browser.findXpath(self.driver,buycomsele).text)
            browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\saleordercheckdata','a+',0,'\n')
            browser.findXpath(self.driver,buycomseok).click()

            #经手人
            people=browser.xmlRead(self.driver,dom,"people",0)
            peoplesele=browser.xmlRead(self.driver,dom,"peoplesele",0)
            peopleseok=browser.xmlRead(self.driver,dom,"peopleseok",0)

            time.sleep(1)

            browser.findXpath(self.driver,people).click()
            browser.findXpath(self.driver,peoplesele).click()
            browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\saleordercheckdata','a+',0,browser.findXpath(self.driver,peoplesele).text)
            browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\saleordercheckdata','a+',0,'\n')

            #部门
            department=browser.xmlRead(self.driver,dom,"department",0)
            browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\saleordercheckdata','a+',0,browser.findXpath(self.driver,department).text)
            browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\saleordercheckdata','a+',0,'\n')
            browser.findXpath(self.driver,peopleseok).click()

            #交货日期

            givedateid=browser.xmlRead(self.driver,dom,'givedateid',0)
            js="var code=document.getElementById('"+givedateid+"').value;"+givedateid+".setAttribute('value',code);"
            self.driver.execute_script(js)
            givedateid=browser.findId(self.driver,givedateid).get_attribute("value")
            browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\saleordercheckdata','a+',0,givedateid)
            browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\saleordercheckdata','a+',0,'\n')

            #发货仓库
            cate=browser.xmlRead(self.driver,dom,"cate",0)
            catesel=browser.xmlRead(self.driver,dom,"catesel",0)
            cateseok=browser.xmlRead(self.driver,dom,"cateseok",0)

            #browser.setheader(self.driver,cate,catesel,cateseok)
            browser.findXpath(self.driver,cate).click()
            browser.findXpath(self.driver,catesel).click()
            browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\saleordercheckdata','a+',0,browser.findXpath(self.driver,catesel).text)
            browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\saleordercheckdata','a+',0,'\n')
            browser.findXpath(self.driver,cateseok).click()

            #摘要
            summary=browser.xmlRead(self.driver,dom,"summary",0)
            browser.findXpath(self.driver,summary).send_keys(u"我是摘要新增销售订单23333333333................")

            browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\saleordercheckdata','a+',0,u"我是摘要新增销售订单23333333333................")
            browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\saleordercheckdata','a+',0,'\n')

            #附加说明
            comment=browser.xmlRead(self.driver,dom,"comment",0)
            browser.findXpath(self.driver,comment).send_keys(u"我是附加说明新增销售订单23333333333................")

            browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\saleordercheckdata','a+',0,u"我是附加说明新增销售订单23333333333................")
            browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\saleordercheckdata','a+',0,'\n')


        except:
            print u"单据头设置失败"
            print(traceback.format_exc())


        try:
            #商品名称
            itemname=browser.xmlRead(self.driver,dom,"itemname",0)
            itemselect=browser.xmlRead(self.driver,dom,"itemselect",0)
            iteminput=browser.xmlRead(self.driver,dom,"iteminput",0)
            itemok=browser.xmlRead(self.driver,dom,"itemok",0)
            time.sleep(1)

            browser.openModule3(self.driver,itemname,itemselect,iteminput)

            #编号和名称进行写入
            itemcodetext=browser.xmlRead(self.driver,dom,"itemcodetext",0)
            itemnametext=browser.xmlRead(self.driver,dom,"itemnametext",0)
            browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\saleordercheckdata','a+',0,browser.findXpath(self.driver,itemcodetext).text)
            browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\saleordercheckdata','a+',0,'\n')
            browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\saleordercheckdata','a+',0,browser.findXpath(self.driver,itemnametext).text)
            browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\saleordercheckdata','a+',0,'\n')

            browser.findXpath(self.driver,itemok).click()

            #数量
            itemnum=browser.xmlRead(self.driver,dom,"itemnum",0)
            browser.findXpath(self.driver,itemnum).send_keys("13")
            browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\saleordercheckdata','a+',0,"13")
            browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\saleordercheckdata','a+',0,'\n')

            #折前单价
            time.sleep(1)
            itemprice=browser.xmlRead(self.driver,dom,"itemprice",0)
            browser.findXpath(self.driver,itemprice).click()
            itempriceinput=browser.xmlRead(self.driver,dom,"itempriceinput",0)
            browser.findXpath(self.driver,itempriceinput).send_keys("23")

            browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\saleordercheckdata','a+',0,"23")
            browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\saleordercheckdata','a+',0,'\n')

            browser.findXpath(self.driver,comment).click()

            k=28

            #折前金额
            dpmoney=browser.xmlRead(self.driver,dom,"iteminfo",0)+str(k)+"]"
            dpmoney=float(browser.findXpath(self.driver,dpmoney).text)
            browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\saleordercheckdata','a+',0,str(dpmoney))
            browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\saleordercheckdata','a+',0,'\n')

            comdpmoney=float(23*13)
            self.assernote(dpmoney,comdpmoney,u"折前金额不正确",u"折前金额正确",u"折前金额")


            #折扣
            itemdiscount=browser.xmlRead(self.driver,dom,"itemdiscount",0)
            browser.findXpath(self.driver,itemdiscount).click()
            itemdiscountinput=browser.xmlRead(self.driver,dom,"itemdiscountinput",0)
            browser.findXpath(self.driver,itemdiscountinput).send_keys("0.85")

            browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\saleordercheckdata','a+',0,"0.85")
            browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\saleordercheckdata','a+',0,'\n')

            browser.findXpath(self.driver,comment).click()

            #单价
            sigleprice=browser.xmlRead(self.driver,dom,"iteminfo",0)+str(k+2)+"]"
            sigleprice=float(browser.findXpath(self.driver,sigleprice).text)
            browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\saleordercheckdata','a+',0,str(sigleprice))
            browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\saleordercheckdata','a+',0,'\n')

            comsigle=float(0.85*23)
            self.assernote(comsigle,sigleprice,u"单价不正确",u"单价正确",u"单价")

            #金额
            money=browser.xmlRead(self.driver,dom,"iteminfo",0)+str(k+3)+"]"
            money=float(browser.findXpath(self.driver,money).text)
            browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\saleordercheckdata','a+',0,str(money))
            browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\saleordercheckdata','a+',0,'\n')

            commoney=float(0.85*dpmoney)
            self.assernote(money,commoney,u"金额不正确",u"金额正确",u"金额")

            #税率
            itemtax=browser.xmlRead(self.driver,dom,"itemtax",0)
            browser.findXpath(self.driver,itemtax).click()
            itemtaxinput=browser.xmlRead(self.driver,dom,"itemtaxinput",0)
            browser.findXpath(self.driver,itemtaxinput).send_keys("16.25")
            browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\saleordercheckdata','a+',0,"16.25")
            browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\saleordercheckdata','a+',0,'\n')

            browser.findXpath(self.driver,comment).click()

            #税额
            taxtotal=browser.xmlRead(self.driver,dom,"iteminfo",0)+str(k+5)+"]"
            taxtotal=float(browser.findXpath(self.driver,taxtotal).text)
            browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\saleordercheckdata','a+',0,str(taxtotal))
            browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\saleordercheckdata','a+',0,'\n')

            comtaxtotal=float(0.1625*money)
            comtaxtotal=round(comtaxtotal,2)
            self.assernote(taxtotal,comtaxtotal,u"税额不正确",u"税额正确",u"税额")

            #税后单价
            taxsigleprice=browser.xmlRead(self.driver,dom,"iteminfo",0)+str(k+6)+"]"
            taxsigleprice=float(browser.findXpath(self.driver,taxsigleprice).text)
            browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\saleordercheckdata','a+',0,str(taxsigleprice))
            browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\saleordercheckdata','a+',0,'\n')

            comtaxsigleprice=float(1.1625*sigleprice)
            comtaxsigleprice=round(comtaxsigleprice,4)
            self.assernote(taxsigleprice,comtaxsigleprice,u"税后单价不正确",u"税后单价正确",u"税后单价")



            #税后金额
            taxmoney=browser.xmlRead(self.driver,dom,"iteminfo",0)+str(k+7)+"]"
            taxmoney=float(browser.findXpath(self.driver,taxmoney).text)
            browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\saleordercheckdata','a+',0,str(taxmoney))
            browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\saleordercheckdata','a+',0,'\n')

            comtaxmoney=float(1.1625*money)
            comtaxmoney=round(comtaxmoney,2)
            self.assernote(taxmoney,comtaxmoney,u"税后金额不正确",u"税后金额正确",u"税后金额")

        except:
            print u"单据明细商品信息设置失败"
            print(traceback.format_exc())

        #保存单据
        try:
            saveandexit=browser.xmlRead(self.driver,dom,"saveandexit",0)
            browser.findXpath(self.driver,saveandexit).click()
            saveok=browser.xmlRead(self.driver,dom,"saveok",0)
            browser.findXpath(self.driver,saveok).click()
        except:
            print u"单据保存失败"
            print(traceback.format_exc())

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
