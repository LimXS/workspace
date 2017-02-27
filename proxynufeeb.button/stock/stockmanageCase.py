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

class stockmanageTest(unittest.TestCase):
    u'''进货-进货订单管理'''

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

    def teststockmanage(self):
        u'''进货-进货订单管理.'''
        header={'cookie':self.cookiestr,"Content-Type": "application/json"}
        comdom=xml.dom.minidom.parse(r'C:\workspace\proxynufeeb.button\data\commonlocation')
        dom = xml.dom.minidom.parse(r'C:\workspace\proxynufeeb.button\stock\stocklocation')

        modulename=browser.xmlRead(dom,"module",0)
        moduledetail=browser.xmlRead(dom,'moduledetail',1)

        browser.openModule2(self.driver,modulename,moduledetail)
        cookies=browser.cookieSave(self.driver)
        header3={'cookie':cookies,"Content-Type": "application/json"}
        header4={'cookie':cookies,"Content-Type": "application/x-www-form-urlencoded"}

        #页面id
        pageurl=browser.xmlRead(dom,"manageurl",0)
        pageid=browser.getalertid(pageurl,header)
        #print pageid

        btypeidtext=browser.requestget(pageurl,header)
        btypeid=re.findall("\"btypeid\":\"(.*?)\",",btypeidtext)
        #print btypeid
        btypeid=btypeid[0]


        #commid,id
        commid=browser.getallcommonid(comdom)


        try:
            #刷新
            btnrefresh=commid["basetype"]+pageid+browser.xmlRead(dom,"btnrefresh",0)
            browser.findXpath(self.driver,btnrefresh).click()

            #查询条件
            selcon=pageid+browser.xmlRead(dom,"btnOrderQuery",0)
            browser.findId(self.driver,selcon).click()
            conurl="http://dba.wsgjp.com.cn/Beefun/Carrier/OrderQueryCondition.gspx"
            conid=browser.getalertid(conurl,header3)
            #print conid

            #-关闭
            conclose=conid+commid["btnexit"]
            browser.findId(self.driver,conclose).click()
            browser.findId(self.driver,selcon).click()

            #-确定
            conok=conid+commid["button"]+str(1)
            browser.findId(self.driver,conok).click()

            #修改
            change=pageid+browser.xmlRead(dom,"btnModify",0)
            browser.findId(self.driver,change).click()
            browser.openModule2(self.driver,modulename,moduledetail)

            #审核
            check=pageid+browser.xmlRead(dom,"check",0)

            checkurl="http://dba.wsgjp.com.cn/Beefun/Report/OrderAudit.gspx?isshowgrid=false&audittype=1&ctype=0&vchtype=stockorder&btypeid="+btypeid
            checkid=browser.getalertid(checkurl,header)
            #print checkid

            #-审核通过
            checkok=checkid+browser.xmlRead(dom,"btnAuditPass",0)
            #print checkok

            js="$(\"div[class=GridBodyCellText]:contains('网店客户')\").first().attr(\"id\",\"checkid\")"
            browser.delaytime(1)
            browser.excutejs(self.driver,js)
            browser.findId(self.driver,"checkid").click()
            browser.exjscommin(self.driver,"审核")
            browser.exjscommin(self.driver,"审核通过")

            #-关闭
            checkclose=checkid+commid["btnexit"]
            #print checkclose
            browser.delaytime(1)
            browser.findId(self.driver,check).click()
            browser.findId(self.driver,checkclose).click()
            time.sleep(1)
            browser.findId(self.driver,check).click()

            browser.delaytime(1)
            browser.delaytime(3,self.driver)
            browser.findId(self.driver,checkok).click()


            #执行情况
            exinfo=pageid+browser.xmlRead(dom,"btnExecInfo",0)
            browser.findId(self.driver,exinfo).click()
            browser.openModule2(self.driver,modulename,moduledetail)

            #更多
            btnMore=pageid+browser.xmlRead(dom,"btnMore",0)

            #更多-复制为进货订单
            morecpinstock=commid["basetype"]+pageid+browser.xmlRead(dom,"btnCopyBuyOrder",0)+browser.xmlRead(dom,"moredetail",0)
            for a in range(2):
                #print morecpinstock
                browser.findId(self.driver,btnMore).click()
                browser.findXpath(self.driver,morecpinstock).click()
                browser.accAlert(self.driver,0)
            browser.findId(self.driver,btnMore).click()
            browser.findXpath(self.driver,morecpinstock).click()
            browser.accAlert(self.driver,1)
            time.sleep(1)
            browser.openModule2(self.driver,modulename,moduledetail)

            #更多-删除
            moredel=commid["basetype"]+pageid+browser.xmlRead(dom,"btnDel",0)+browser.xmlRead(dom,"moredetail",0)
            #print moredel
            browser.findId(self.driver,btnMore).click()
            browser.findXpath(self.driver,moredel).click()
            browser.accAlert(self.driver,0)
            browser.findId(self.driver,btnMore).click()
            browser.findXpath(self.driver,moredel).click()
            browser.accAlert(self.driver,1)
            time.sleep(1)

            #更多-复制为销售订单
            morecpsale=commid["basetype"]+pageid+browser.xmlRead(dom,"btnCopyOrder",0)+browser.xmlRead(dom,"moredetail",0)
            #print morecpsale
            browser.findId(self.driver,btnMore).click()
            browser.findXpath(self.driver,morecpsale).click()
            browser.accAlert(self.driver,0)
            browser.findId(self.driver,btnMore).click()
            browser.findXpath(self.driver,morecpsale).click()
            browser.accAlert(self.driver,1)
            time.sleep(1)
            browser.openModule2(self.driver,modulename,moduledetail)

            #更多-终止并完成
            moreforce=commid["basetype"]+pageid+browser.xmlRead(dom,"btnForceOver",0)+browser.xmlRead(dom,"moredetail",0)
            #print moreforce
            browser.findId(self.driver,btnMore).click()
            browser.findXpath(self.driver,moreforce).click()
            browser.accAlert(self.driver,0)
            browser.findId(self.driver,btnMore).click()
            browser.findXpath(self.driver,moreforce).click()
            browser.accAlert(self.driver,1)
            time.sleep(1)
            browser.openModule2(self.driver,modulename,moduledetail)



            #更多-订单审核配置
            moreset=commid["basetype"]+pageid+browser.xmlRead(dom,"btnOrderConfig",0)+browser.xmlRead(dom,"moredetail",0)
            #print moreset
            browser.findId(self.driver,btnMore).click()
            browser.findXpath(self.driver,moreset).click()
            jsclose="$(\"button:contains('退出')\").eq(5).click()"
            time.sleep(1)
            browser.excutejs(self.driver,jsclose)
            browser.findId(self.driver,btnMore).click()
            browser.findXpath(self.driver,moreset).click()
            jssave="$(\"button:contains('保存')\").eq(3).click()"
            time.sleep(1)
            browser.excutejs(self.driver,jssave)
            browser.accAlert(self.driver,1)

            itemgrid=browser.xmlRead(dom,"itemgrid",0)

            #仓库选择框
            catesel=commid["basetype"]+pageid+itemgrid+str(10)+"]"
            browser.findXpath(self.driver,catesel).click()
            browser.doubleclick(self.driver,pageid+browser.xmlRead(dom,"grid_kfullname",0))

            #-添加,-关闭
            browser.catesel(self.driver)

            #选中
            browser.doubleclick(self.driver,pageid+browser.xmlRead(dom,"grid_kfullname",0))
            js="$(\"button:contains('选中')\").click()"
            time.sleep(1)
            browser.excutejs(self.driver,js)


            #经手人选择框
            peosel=commid["basetype"]+pageid+itemgrid+str(11)+"]"
            browser.delaytime(1)
            browser.findXpath(self.driver,peosel).click()
            browser.doubleclick(self.driver,pageid+browser.xmlRead(dom,"grid_ename",0))

            #-添加，-关闭
            js="$(\"input[class=ButtonEdit]\").last().attr(\"id\",\"tempid\");"
            browser.catesel(self.driver,js,"tempid")

            #-选中
            browser.findXpath(self.driver,peosel).click()
            browser.doubleclick(self.driver,pageid+browser.xmlRead(dom,"grid_ename",0))

            js="$(\"button:contains('选中')\").click()"
            time.sleep(1)
            browser.excutejs(self.driver,js)

            #更多-打印
            #moredel=commid["basetype"]+pageid+browser.xmlRead(dom,"btnDel",0)+browser.xmlRead(dom,"moredetail",0)
            #退出
            pageexit=pageid+commid["selclose"]
            browser.findId(self.driver,pageexit).click()
            browser.openModule2(self.driver,modulename,moduledetail)

        except:
            print traceback.format_exc()
            filename=browser.xmlRead(dom,'filename',0)
            browser.delaytime(1)
            browser.getpicture(self.driver,filename+u"进货-进货订单管理.png")



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
