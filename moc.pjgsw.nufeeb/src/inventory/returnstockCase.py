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

class returnstockTest(unittest.TestCase):
    u'''进货退货单'''

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


    def testReturnstock(self):
        u'''进货退货单'''
        dom = xml.dom.minidom.parse(r'C:\workspace\moc.pjgsw.nufeeb\src\data\basedata')

        module='moudle'
        modulename=browser.xmlRead(self.driver,dom,module,3)
        moduledetail=browser.xmlRead(self.driver,dom,'page',3)

        browser.openModule2(self.driver,modulename,moduledetail)

        #编号
        time.sleep(2)
        returnid=browser.xmlRead(self.driver,dom,'returnid',0)
        js="var code=document.getElementById('"+returnid+"').value;"+returnid+".setAttribute('value',code);"
        self.driver.execute_script(js)
        id=browser.findId(self.driver,returnid).get_attribute("value")
        #print id
        browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\returndata','w',0,id)
        browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\returndata','a+',0,'\n')


        #录单日期
        time.sleep(2)
        returnoetime=browser.xmlRead(self.driver,dom,'returnoetime',0)
        js="var code=document.getElementById('"+returnoetime+"').value;"+returnoetime+".setAttribute('value',code);"
        self.driver.execute_script(js)
        ordertime=browser.findId(self.driver,returnoetime).get_attribute("value")
        browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\returndata','a+',0,ordertime)
        browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\returndata','a+',0,'\n')

        #收货单位
        try:
            xpath=browser.xmlRead(self.driver,dom,'recompanyxpath',0)
            browser.findXpath(self.driver,xpath).click()
            #self.driver.implicitly_wait(10)
            comsec=browser.xmlRead(self.driver,dom,'recompanysec',0)
            browser.findXpath(self.driver,comsec).click()

            choice=browser.xmlRead(self.driver,dom,'reselectcom',0)
            browser.findXpath(self.driver,choice).click()
            print u"设置退货供货单位成功"
        except:
            print u"设置退货供货单位失败"
            print(traceback.format_exc())
            #js='document.getElementById("$eb57a3e$edBType").style.color="blue";'
            #self.driver.execute_script(js)

        companypath=browser.xmlRead(self.driver,dom,'recompany',0)
        time.sleep(2)
        js="var code=document.getElementById('"+companypath+"').value;"+companypath+".setAttribute('value',code);"
        self.driver.execute_script(js)
        company=browser.findId(self.driver,companypath).get_attribute("value")
        #print company
        try:
            browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\returndata','a+',0,company)
            browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\returndata','a+',0,'\n')
        except:
            print u"设置退货供货单位returndata失败"
            print(traceback.format_exc())


        #经手人
        try:
            handle=browser.xmlRead(self.driver,dom,'repeople',0)
            browser.findXpath(self.driver,handle).click()

            peoplesec=browser.xmlRead(self.driver,dom,'repeoplesec',0)
            browser.findXpath(self.driver,peoplesec).click()

            choicepeople=browser.xmlRead(self.driver,dom,'repeopleselect',0)
            browser.findXpath(self.driver,choicepeople).click()
            print u"设置退货经手人成功"
        except:
            print u"设置退货经手人失败"
            print(traceback.format_exc())
        time.sleep(2)
        people=browser.xmlRead(self.driver,dom,'repeopletext',0)
        js="var code=document.getElementById('"+people+"').value;"+people+".setAttribute('value',code);"
        self.driver.execute_script(js)
        people=browser.findId(self.driver,people).get_attribute("value")
        #print people
        try:
            browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\returndata','a+',0,people)
            browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\returndata','a+',0,'\n')
        except:
            print u"设置退货经手人returndata失败"
            print(traceback.format_exc())


        #部门
        try:
            redepart=browser.xmlRead(self.driver,dom,'redepart',0)
            browser.findXpath(self.driver,redepart).click()

            redepartsec=browser.xmlRead(self.driver,dom,'redepartsec',0)
            browser.findXpath(self.driver,redepartsec).click()

            redepartselect=browser.xmlRead(self.driver,dom,'redepartselect',0)
            browser.findXpath(self.driver,redepartselect).click()
            print u"设置退货经手人成功"
        except:
            print u"设置退货经手人失败"
            print(traceback.format_exc())
        time.sleep(2)
        redeparttext=browser.xmlRead(self.driver,dom,'redeparttext',0)
        js="var code=document.getElementById('"+redeparttext+"').value;"+redeparttext+".setAttribute('value',code);"
        self.driver.execute_script(js)
        redeparttext=browser.findId(self.driver,redeparttext).get_attribute("value")

        try:
            browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\returndata','a+',0,redeparttext)
            browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\returndata','a+',0,'\n')
        except:
            print u"设置退货部门returndata失败"
            print(traceback.format_exc())



        try:
            #收货仓库
            repertory=browser.xmlRead(self.driver,dom,'reaccre',0)
            browser.findXpath(self.driver,repertory).click()

            repertorysec=browser.xmlRead(self.driver,dom,'reaccresec',0)
            browser.findXpath(self.driver,repertorysec).click()

            choicerepertory=browser.xmlRead(self.driver,dom,'reaccreselect',0)
            browser.findXpath(self.driver,choicerepertory).click()
            print u"设置退货收货仓库成功"
        except:
            print u"设置退货收货仓库失败"
            print(traceback.format_exc())

        time.sleep(2)
        whichre=browser.xmlRead(self.driver,dom,'reaccretext',0)
        js="var code=document.getElementById('"+whichre+"').value;"+whichre+".setAttribute('value',code);"
        self.driver.execute_script(js)
        whichre=browser.findId(self.driver,whichre).get_attribute("value")
        #print whichre
        try:
            browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\returndata','a+',0,whichre)
            browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\returndata','a+',0,'\n')
        except:
            print u"设置退货收货仓库returndata失败"
            print(traceback.format_exc())

        #摘要
        try:
            sumnote=u'我是退货摘要abcde.233333333333333'
            resummary=browser.xmlRead(self.driver,dom,'resummary',0)
            browser.findId(self.driver,resummary).send_keys(sumnote)
            print u"设置退货摘要成功"
        except:
            print u"设置退货摘要失败"
            print(traceback.format_exc())

        time.sleep(2)
        js="var code=document.getElementById('"+resummary+"').value;"+resummary+".setAttribute('value',code);"
        self.driver.execute_script(js)
        summarynote=browser.findId(self.driver,resummary).get_attribute("value")
        #print summarynote
        if summarynote!=sumnote:
            print u"输入退货摘要和显示的摘要不一致"
        try:
            browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\returndata','a+',0,summarynote)
            browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\returndata','a+',0,'\n')
        except:
            print u"写入退货摘要returndata失败"
            print(traceback.format_exc())


        #附加说明
        try:
            comnote=u'我是退货附加说明abcde.233333333333333'
            recomment=browser.xmlRead(self.driver,dom,'recomment',0)
            browser.findId(self.driver,recomment).send_keys(comnote)
            print u"设置退货附加说明成功"
        except:
            print u"设置退货附加说明失败"
            print(traceback.format_exc())
        time.sleep(2)
        js="var code=document.getElementById('"+recomment+"').value;"+recomment+".setAttribute('value',code);"
        self.driver.execute_script(js)
        commentnote=browser.findId(self.driver,recomment).get_attribute("value")
        #print commentnote
        if commentnote!=comnote:
            print u"输入退货附加说明和显示的摘要不一致"
        try:
            browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\returndata','a+',0,commentnote)
            browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\returndata','a+',0,'\n')
        except:
            print u"写入退货附加说明returndata失败"
            print(traceback.format_exc())

        try:
            reitemxpath=browser.xmlRead(self.driver,dom,'reitemxpath',0)
            browser.findXpath(self.driver,reitemxpath).click()

            reitemselect=browser.xmlRead(self.driver,dom,'reitemselect',0)
            browser.findXpath(self.driver,reitemselect).click()
            time.sleep(2)

            reitemwhich=browser.xmlRead(self.driver,dom,'reitemwhich',0)
            browser.findXpath(self.driver,reitemwhich).click()

            reitemok=browser.xmlRead(self.driver,dom,'reitemok',0)
            browser.findXpath(self.driver,reitemok).click()
            print u"设置退货单据名字成功"

        except:
            print u"录入退货单据名字失败"
            print(traceback.format_exc())

        try:
            reitemtext=browser.xmlRead(self.driver,dom,'reitemtext',0)
            reitemtext=browser.findXpath(self.driver,reitemtext).text
            print reitemtext
            browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\returndata','a+',0,reitemtext)
            browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\returndata','a+',0,'\n')
        except:
            print u"录入退货单据名字returndata失败"
            print(traceback.format_exc())
        time.sleep(2)

        #数量

        #折扣
        rediscount=browser.xmlRead(self.driver,dom,'rediscount',0)
        redissend=browser.xmlRead(self.driver,dom,'redissend',0)
        browser.findXpath(self.driver,rediscount).click()
        browser.findXpath(self.driver,redissend).send_keys("0.75")

        #税率
        retax=browser.xmlRead(self.driver,dom,'retax',0)
        retaxsend=browser.xmlRead(self.driver,dom,'retaxsend',0)
        browser.findXpath(self.driver,retax).click()
        browser.findXpath(self.driver,retaxsend).send_keys("12.75")

        browser.findId(self.driver,recomment).click()

        #折前单价
        redpsigle=browser.xmlRead(self.driver,dom,'redpsigle',0)
        dpsigle=float(browser.findXpath(self.driver,redpsigle).text)


        #折前金额
        redpmoney=browser.xmlRead(self.driver,dom,'redpmoney',0)
        dpmoney=float(browser.findXpath(self.driver,redpmoney).text)

        #单价
        resigle=browser.xmlRead(self.driver,dom,'resigle',0)
        sigle=float(browser.findXpath(self.driver,resigle).text)
        pagetemp=dpsigle*0.75
        self.assernote(sigle,pagetemp,u"单价不相同",u"单价正确",u"单价")


        #金额
        remoney=browser.xmlRead(self.driver,dom,'remoney',0)
        money=float(browser.findXpath(self.driver,remoney).text)
        pagetemp=dpmoney*0.75
        pagetemp=round(pagetemp,2)
        self.assernote(money,pagetemp,u"金额不相同",u"金额正确",u"金额")


        #税额
        retaxtotal=browser.xmlRead(self.driver,dom,'retaxtotal',0)
        taxtotal=float(browser.findXpath(self.driver,retaxtotal).text)
        pagetemp=money*0.1275
        taxtotal=str("%.2f"%taxtotal)
        pagetemp=str("%.2f"%pagetemp)
        self.assernote(taxtotal,pagetemp,u"税额不相同",u"税额正确",u"税额")

        #税后单价
        retaxsigle=browser.xmlRead(self.driver,dom,'retaxsigle',0)
        taxsigle=float(browser.findXpath(self.driver,retaxsigle).text)

        pagetemp=float(sigle)*1.1275
        pagetemp=str(pagetemp)+'1'
        pagetemp=round(float(pagetemp),4)

        taxsigle=str("%.4f"%taxsigle)
        pagetemp=str("%.4f"%pagetemp)
        self.assernote(taxsigle,pagetemp,u"税后单价不相同",u"税后单价正确",u"税后单价")

        #税后金额
        retaxmoney=browser.xmlRead(self.driver,dom,'retaxmoney',0)
        taxmoney=float(browser.findXpath(self.driver,retaxmoney).text)
        pagetemp=float(money)*1.1275
        pagetemp=round(pagetemp,4)

        taxmoney=str("%.2f"%taxmoney)
        pagetemp=str("%.2f"%pagetemp)
        self.assernote(taxmoney,pagetemp,u"税后金额不相同",u"税后金额正确",u"税后金额")


        #进行提交
        try:
           resaveorexitxpath=browser.xmlRead(self.driver,dom,"resaveorexitxpath",0)
           time.sleep(1)
           browser.findXpath(self.driver,resaveorexitxpath).click()
        except:
            print u"保存或退出单据报错"
            print(traceback.format_exc())

        #进行保存
        try:
            resave=browser.xmlRead(self.driver,dom,"resave",0)
            time.sleep(2)
            browser.findXpath(self.driver,resave).click()
        except:
            print u"保存单据报错"
            print(traceback.format_exc())


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()