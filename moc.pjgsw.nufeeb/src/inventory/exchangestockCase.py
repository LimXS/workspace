#*-* coding:UTF-8 *-*
import time
import unittest
import  xml.dom.minidom
import traceback
import requests
import re
import json
from common import browserClass
browser=browserClass.browser()

class exchangestockTest(unittest.TestCase):
    u'''进货换货单'''
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


    def testExchangestock(self):
        u'''进货换货单'''
        dom = xml.dom.minidom.parse(r'C:\workspace\moc.pjgsw.nufeeb\src\data\basedata')

        module='moudle'
        modulename=browser.xmlRead(self.driver,dom,module,4)
        moduledetail=browser.xmlRead(self.driver,dom,'page',4)

        browser.openModule2(self.driver,modulename,moduledetail)

        #编号
        time.sleep(2)
        exid=browser.xmlRead(self.driver,dom,'exid',0)
        js="var code=document.getElementById('"+exid+"').value;"+exid+".setAttribute('value',code);"
        self.driver.execute_script(js)
        exid=browser.findId(self.driver,exid).get_attribute("value")
        #print id
        browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\exchangedata','w',0,exid)
        browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\exchangedata','a+',0,'\n')


        #录单日期
        time.sleep(2)
        exdate=browser.xmlRead(self.driver,dom,'exdate',0)
        js="var code=document.getElementById('"+exdate+"').value;"+exdate+".setAttribute('value',code);"
        self.driver.execute_script(js)
        exdate=browser.findId(self.driver,exdate).get_attribute("value")
        browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\exchangedata','a+',0,exdate)
        browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\exchangedata','a+',0,'\n')

        #供货单位
        try:
            excompanyxpath=browser.xmlRead(self.driver,dom,'excompanyxpath',0)
            browser.findXpath(self.driver,excompanyxpath).click()
            #self.driver.implicitly_wait(10)
            excompanysec=browser.xmlRead(self.driver,dom,'excompanysec',0)
            browser.findXpath(self.driver,excompanysec).click()

            exselectcom=browser.xmlRead(self.driver,dom,'exselectcom',0)
            browser.findXpath(self.driver,exselectcom).click()
            print u"设置换货供货单位成功"
        except:
            print u"设置换货供货单位失败"
            print(traceback.format_exc())
            #js='document.getElementById("$eb57a3e$edBType").style.color="blue";'
            #self.driver.execute_script(js)

        excompany=browser.xmlRead(self.driver,dom,'excompany',0)
        time.sleep(2)
        js="var code=document.getElementById('"+excompany+"').value;"+excompany+".setAttribute('value',code);"
        self.driver.execute_script(js)
        excompany=browser.findId(self.driver,excompany).get_attribute("value")
        #print company
        try:
            browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\exchangedata','a+',0,excompany)
            browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\exchangedata','a+',0,'\n')
        except:
            print u"设置换货供货单位exchangedata失败"
            print(traceback.format_exc())


        #经手人
        try:
            time.sleep(1)
            expeople=browser.xmlRead(self.driver,dom,'expeople',0)
            browser.findXpath(self.driver,expeople).click()

            expeoplesec=browser.xmlRead(self.driver,dom,'expeoplesec',0)
            browser.findXpath(self.driver,expeoplesec).click()

            expeopleselect=browser.xmlRead(self.driver,dom,'expeopleselect',0)
            browser.findXpath(self.driver,expeopleselect).click()
            print u"设置换货经手人成功"
        except:
            print u"设置换货经手人失败"
            print(traceback.format_exc())
        time.sleep(2)
        expeopletext=browser.xmlRead(self.driver,dom,'expeopletext',0)
        js="var code=document.getElementById('"+expeopletext+"').value;"+expeopletext+".setAttribute('value',code);"
        self.driver.execute_script(js)
        expeopletext=browser.findId(self.driver,expeopletext).get_attribute("value")
        #print people
        try:
            browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\exchangedata','a+',0,expeopletext)
            browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\exchangedata','a+',0,'\n')
        except:
            print u"设置换货经手人exchangedata失败"
            print(traceback.format_exc())


        #部门
        try:
            exdepart=browser.xmlRead(self.driver,dom,'exdepart',0)
            browser.findXpath(self.driver,exdepart).click()

            exdepartsec=browser.xmlRead(self.driver,dom,'exdepartsec',0)
            browser.findXpath(self.driver,exdepartsec).click()

            exdepartselect=browser.xmlRead(self.driver,dom,'exdepartselect',0)
            browser.findXpath(self.driver,exdepartselect).click()
            print u"设置退货经手人成功"
        except:
            print u"设置退货经手人失败"
            print(traceback.format_exc())
        time.sleep(2)
        exdeparttext=browser.xmlRead(self.driver,dom,'exdeparttext',0)
        js="var code=document.getElementById('"+exdeparttext+"').value;"+exdeparttext+".setAttribute('value',code);"
        self.driver.execute_script(js)
        exdeparttext=browser.findId(self.driver,exdeparttext).get_attribute("value")

        try:
            browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\exchangedata','a+',0,exdeparttext)
            browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\exchangedata','a+',0,'\n')
        except:
            print u"设置换货货部门exchangedata失败"
            print(traceback.format_exc())



        try:
            #换出仓库
            exout=browser.xmlRead(self.driver,dom,'exout',0)
            browser.findXpath(self.driver,exout).click()

            exoutsec=browser.xmlRead(self.driver,dom,'exoutsec',0)
            browser.findXpath(self.driver,exoutsec).click()

            exoutselect=browser.xmlRead(self.driver,dom,'exoutselect',0)
            browser.findXpath(self.driver,exoutselect).click()
            print u"设置换货换出仓库成功"
        except:
            print u"设置换货换出仓库失败"
            print(traceback.format_exc())

        time.sleep(2)
        exouttext=browser.xmlRead(self.driver,dom,'exouttext',0)
        js="var code=document.getElementById('"+exouttext+"').value;"+exouttext+".setAttribute('value',code);"
        self.driver.execute_script(js)
        exouttext=browser.findId(self.driver,exouttext).get_attribute("value")
        #print whichre
        try:
            browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\exchangedata','a+',0,exouttext)
            browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\exchangedata','a+',0,'\n')
        except:
            print u"设置换货换出仓库exchangedata失败"
            print(traceback.format_exc())

        #换货类型
        time.sleep(2)
        extype=browser.xmlRead(self.driver,dom,'extype',0)
        js="var code=document.getElementById('"+extype+"').value;"+extype+".setAttribute('value',code);"
        self.driver.execute_script(js)
        extype=browser.findId(self.driver,extype).get_attribute("value")
        #print whichre
        try:
            browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\exchangedata','a+',0,extype)
            browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\exchangedata','a+',0,'\n')
        except:
            print u"设置换货换货类型失败"
            print(traceback.format_exc())


        try:
            #换入仓库
            exin=browser.xmlRead(self.driver,dom,'exin',0)
            browser.findXpath(self.driver,exin).click()

            exinsec=browser.xmlRead(self.driver,dom,'exinsec',0)
            browser.findXpath(self.driver,exinsec).click()

            exinselect=browser.xmlRead(self.driver,dom,'exinselect',0)
            browser.findXpath(self.driver,exinselect).click()
            print u"设置换货换入仓库成功"
        except:
            print u"设置换货换入仓库失败"
            print(traceback.format_exc())

        time.sleep(2)
        exintext=browser.xmlRead(self.driver,dom,'exintext',0)
        js="var code=document.getElementById('"+exintext+"').value;"+exintext+".setAttribute('value',code);"
        self.driver.execute_script(js)
        exintext=browser.findId(self.driver,exintext).get_attribute("value")
        #print whichre
        try:
            browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\exchangedata','a+',0,exintext)
            browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\exchangedata','a+',0,'\n')
        except:
            print u"设置换货换入仓库exchangedata失败"
            print(traceback.format_exc())


        #摘要
        try:
            sumnote=u'我是换货摘要abcde.233333333333333'
            exsummary=browser.xmlRead(self.driver,dom,'exsummary',0)
            browser.findId(self.driver,exsummary).send_keys(sumnote)
            print u"设置换货摘要成功"
        except:
            print u"设置换货摘要失败"
            print(traceback.format_exc())

        time.sleep(2)
        js="var code=document.getElementById('"+exsummary+"').value;"+exsummary+".setAttribute('value',code);"
        self.driver.execute_script(js)
        summarynote=browser.findId(self.driver,exsummary).get_attribute("value")
        #print summarynote
        if summarynote!=sumnote:
            print u"输入换货摘要和显示的摘要不一致"
        try:
            browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\exchangedata','a+',0,summarynote)
            browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\exchangedata','a+',0,'\n')
        except:
            print u"写入退货摘要exchangedata失败"
            print(traceback.format_exc())


        #附加说明
        try:
            comnote=u'我是换货附加说明abcde.233333333333333'
            excomment=browser.xmlRead(self.driver,dom,'excomment',0)
            browser.findId(self.driver,excomment).send_keys(comnote)
            print u"设置换货附加说明成功"
        except:
            print u"设置换货附加说明失败"
            print(traceback.format_exc())
        time.sleep(2)
        js="var code=document.getElementById('"+excomment+"').value;"+excomment+".setAttribute('value',code);"
        self.driver.execute_script(js)
        commentnote=browser.findId(self.driver,excomment).get_attribute("value")
        #print commentnote
        if commentnote!=comnote:
            print u"输入换货附加说明和显示的摘要不一致"
        try:
            browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\exchangedata','a+',0,commentnote)
            browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\exchangedata','a+',0,'\n')
        except:
            print u"写入换货附加说明exchangedata失败"
            print(traceback.format_exc())

        #换货out商品名字
        try:

            exitemxpath=browser.xmlRead(self.driver,dom,'exitemxpath',0)
            time.sleep(2)
            browser.findXpath(self.driver,exitemxpath).click()

            exitemselect=browser.xmlRead(self.driver,dom,'exitemselect',0)
            browser.findXpath(self.driver,exitemselect).click()

            '''
            reitemwhich=browser.xmlRead(self.driver,dom,'reitemwhich',0)
            browser.findXpath(self.driver,reitemwhich).click()
           '''
            exitemok=browser.xmlRead(self.driver,dom,'exitemok',0)
            browser.findXpath(self.driver,exitemok).click()
            print u"设置换货单据out名字成功"

        except:
            print u"录入换货单据out名字失败"
            print(traceback.format_exc())

        try:
            exitemxpath=browser.xmlRead(self.driver,dom,'exitemxpath',0)
            exitemxpath=browser.findXpath(self.driver,exitemxpath).text
            print exitemxpath
            browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\exchangedata','a+',0,exitemxpath)
            browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\exchangedata','a+',0,'\n')
        except:
            print u"录入退货单据名字失败"
            print(traceback.format_exc())
        time.sleep(2)

        #折扣
        exoutdiscount=browser.xmlRead(self.driver,dom,'exoutdiscount',0)
        browser.findXpath(self.driver,exoutdiscount).click()
        exoutdissend=browser.xmlRead(self.driver,dom,'exoutdissend',0)
        browser.findXpath(self.driver,exoutdissend).send_keys("0.85")

        #税率
        exouttax=browser.xmlRead(self.driver,dom,'exouttax',0)
        browser.findXpath(self.driver,exouttax).click()
        exouttaxsend=browser.xmlRead(self.driver,dom,'exouttaxsend',0)
        browser.findXpath(self.driver,exouttaxsend).send_keys("13.75")

        browser.findId(self.driver,excomment).click()

        #折前单价
        reoutdpsigle=browser.xmlRead(self.driver,dom,'outdpsigle',0)
        outdpsigle=float(browser.findXpath(self.driver,reoutdpsigle).text)

        #折前金额
        reoutdpmoney=browser.xmlRead(self.driver,dom,'outdpmoney',0)
        outdpmoney=float(browser.findXpath(self.driver,reoutdpmoney).text)

        #单价
        reoutsigle=browser.xmlRead(self.driver,dom,'outsigle',0)
        outsigle=float(browser.findXpath(self.driver,reoutsigle).text)
        pagetemp=outdpsigle*0.85
        self.assernote(str(outsigle),str(pagetemp),u"换出单价不相同",u"换出单价正确",u"换出单价")

        #金额
        reoutmoney=browser.xmlRead(self.driver,dom,'outmoney',0)
        outmoney=float(browser.findXpath(self.driver,reoutmoney).text)
        pagetemp=outdpmoney*0.85
        outmoney=str("%.2f"%outmoney)
        pagetemp=str("%.2f"%pagetemp)
        self.assernote(outmoney,pagetemp,u"换出金额不相同",u"换出金额正确",u"换出金额")

        #税额
        reouttaxtotal=browser.xmlRead(self.driver,dom,'outtaxtotal',0)
        outtaxtotal=float(browser.findXpath(self.driver,reouttaxtotal).text)
        pagetemp=float(outmoney)*0.1375
        outtaxtotal=str("%.2f"%outtaxtotal)
        pagetemp=str("%.2f"%pagetemp)
        self.assernote(outtaxtotal,pagetemp,u"换出税额不相同",u"换出税额正确",u"换出税额")

        #税后单价
        reouttaxsigle=browser.xmlRead(self.driver,dom,'outtaxsigle',0)
        outtaxsigle=float(browser.findXpath(self.driver,reouttaxsigle).text)
        pagetemp=float(outsigle)*1.1375
        pagetemp=str(pagetemp)+'1'
        pagetemp=round(float(pagetemp),4)

        outtaxsigle=str("%.4f"%outtaxsigle)
        pagetemp=str("%.4f"%pagetemp)
        self.assernote(outtaxsigle,pagetemp,u"换出税后单价不相同",u"换出税后单价正确",u"换出税后单价")

        #税后金额
        reouttaxmoney=browser.xmlRead(self.driver,dom,'outtaxmoney',0)
        outtaxmoney=float(browser.findXpath(self.driver,reouttaxmoney).text)
        pagetemp=float(outmoney)*1.1375
        pagetemp=round(pagetemp,4)

        outtaxmoney=str("%.2f"%outtaxmoney)
        pagetemp=str("%.2f"%pagetemp)
        self.assernote(outtaxmoney,pagetemp,u"换出税后金额不相同",u"换出税后金额正确",u"换出税后金额")


        #换货in商品名字
        try:
            exiteminxpath=browser.xmlRead(self.driver,dom,'exiteminxpath',0)
            time.sleep(2)
            browser.findXpath(self.driver,exiteminxpath).click()

            exiteminselect=browser.xmlRead(self.driver,dom,'exiteminselect',0)
            browser.findXpath(self.driver,exiteminselect).click()


            exitemwhitchok=browser.xmlRead(self.driver,dom,'exitemwhitchok',0)
            browser.findXpath(self.driver,exitemwhitchok).click()

            exiteminok=browser.xmlRead(self.driver,dom,'exiteminok',0)
            browser.findXpath(self.driver,exiteminok).click()
            print u"设置换货单据in名字成功"

        except:
            print u"录入换货单据in名字失败"
            print(traceback.format_exc())

        try:
            exiteminxpath=browser.xmlRead(self.driver,dom,'exiteminxpath',0)
            exiteminxpath=browser.findXpath(self.driver,exiteminxpath).text
            print exiteminxpath
            browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\exchangedata','a+',0,exiteminxpath)
            browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\exchangedata','a+',0,'\n')
        except:
            print u"录入退货单据in名字失败"
            print(traceback.format_exc())
        time.sleep(2)

        #设置金额
        try:
            exiteminprice=browser.xmlRead(self.driver,dom,'exiteminprice',0)
            browser.findXpath(self.driver,exiteminprice).click()

            exprice=browser.xmlRead(self.driver,dom,'exprice',0)
            time.sleep(2)
            browser.findXpath(self.driver,exprice).send_keys("18")

            print u"设置换货单据in price成功"

        except:
            print u"录入换货单据in price失败"
            print(traceback.format_exc())

        try:
            time.sleep(1)
            browser.findId(self.driver,excomment).click()
            exiteminprice=browser.xmlRead(self.driver,dom,'exiteminprice',0)
            exiteminprice=browser.findXpath(self.driver,exiteminprice).text
            #print exiteminxpath
            browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\exchangedata','a+',0,exiteminprice)
            browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\exchangedata','a+',0,'\n')
        except:
            print u"录入退货单据inprice失败"
            print(traceback.format_exc())
        time.sleep(2)

        #折扣
        exindiscount=browser.xmlRead(self.driver,dom,'exindiscount',0)
        browser.findXpath(self.driver,exindiscount).click()
        exindissend=browser.xmlRead(self.driver,dom,'exindissend',0)
        browser.findXpath(self.driver,exindissend).send_keys("0.75")

        #税率
        exintax=browser.xmlRead(self.driver,dom,'exintax',0)
        browser.findXpath(self.driver,exintax).click()
        exintaxsend=browser.xmlRead(self.driver,dom,'exintaxsend',0)
        browser.findXpath(self.driver,exintaxsend).send_keys("12.75")

        browser.findId(self.driver,excomment).click()

        #折前单价
        reindpsigle=browser.xmlRead(self.driver,dom,'indpsigle',0)
        indpsigle=float(browser.findXpath(self.driver,reindpsigle).text)

        #折前金额
        reindpmoney=browser.xmlRead(self.driver,dom,'indpmoney',0)
        indpmoney=float(browser.findXpath(self.driver,reindpmoney).text)

        #单价
        reinsigle=browser.xmlRead(self.driver,dom,'insigle',0)
        insigle=float(browser.findXpath(self.driver,reinsigle).text)
        pagetemp=indpsigle*0.75
        self.assernote(insigle,pagetemp,u"换入单价不相同",u"换入单价正确",u"换入单价")

        #金额
        reinmoney=browser.xmlRead(self.driver,dom,'inmoney',0)
        inmoney=float(browser.findXpath(self.driver,reinmoney).text)
        pagetemp=indpmoney*0.75
        self.assernote(inmoney,pagetemp,u"换入金额不相同",u"换入金额正确",u"换入金额")

        #税额
        reintaxtotal=browser.xmlRead(self.driver,dom,'intaxtotal',0)
        intaxtotal=float(browser.findXpath(self.driver,reintaxtotal).text)
        pagetemp=inmoney*0.1275
        intaxtotal=str("%.2f"%intaxtotal)
        pagetemp=str("%.2f"%pagetemp)
        self.assernote(intaxtotal,pagetemp,u"换入税额不相同",u"换入税额正确",u"换入税额")

        #税后单价
        reintaxsigle=browser.xmlRead(self.driver,dom,'intaxsigle',0)
        intaxsigle=float(browser.findXpath(self.driver,reintaxsigle).text)
        pagetemp=float(insigle)*1.1275
        pagetemp=str(pagetemp)+'1'
        pagetemp=round(float(pagetemp),4)

        intaxsigle=str("%.4f"%intaxsigle)
        pagetemp=str("%.4f"%pagetemp)
        self.assernote(intaxsigle,pagetemp,u"换入税后单价不相同",u"换入税后单价正确",u"换入税后单价")

        #税后金额
        reintaxmoney=browser.xmlRead(self.driver,dom,'intaxmoney',0)
        intaxmoney=float(browser.findXpath(self.driver,reintaxmoney).text)
        pagetemp=float(inmoney)*1.1275
        pagetemp=round(pagetemp,4)

        intaxmoney=str("%.2f"%intaxmoney)
        pagetemp=str("%.2f"%pagetemp)
        self.assernote(intaxmoney,pagetemp,u"换入税后金额不相同",u"换入税后金额正确",u"换入税后金额")

        #保存
        try:
            exitensave=browser.xmlRead(self.driver,dom,'exitensave',0)
            browser.findXpath(self.driver,exitensave).click()

            exitenlastsave=browser.xmlRead(self.driver,dom,'exitenlastsave',0)
            browser.findXpath(self.driver,exitenlastsave).click()
            print u"保存退货单据成功"
        except:
            print u"保存退货单据失败"
            print(traceback.format_exc())



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
