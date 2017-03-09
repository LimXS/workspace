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

class notecentralTest(unittest.TestCase):
    u'''常用-单据中心'''

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


    def testnoteCentral(self):
        u'''常用-单据中心'''
        #零售出库单要在第一个
        header={'cookie':self.cookiestr,"Content-Type": "application/json"}
        dom = xml.dom.minidom.parse(r'C:\workspace\proxynufeeb.button\frequentlyused\frelocation')
        module=browser.xmlRead(dom,'module',0)
        moduledetail=browser.xmlRead(dom,'moduledetail',1)

        browser.openModule2(self.driver,module,moduledetail)
        cookies=browser.cookieSave(self.driver)
        header3={'cookie':cookies,"Content-Type": "application/json"}
        header4={'cookie':cookies,"Content-Type": "application/x-www-form-urlencoded"}

        #页面id
        pageurl="http://dba.wsgjp.com.cn/Beefun/Assistant/BusinessHistory.gspx"
        pageid=browser.halfid(pageurl,header)
        #print pageid

        refrdragt=browser.xmlRead(dom,'refrdragt',0)
        basetype=browser.xmlRead(dom,'basetype',0)
        selexit=browser.xmlRead(dom,'selclose',0)
        selok=browser.xmlRead(dom,'selbtn',0)
        btnexit=browser.xmlRead(dom,'btnexit',0)
        btnok=browser.xmlRead(dom,'btnok',0)

        pnext=browser.xmlRead(dom,'typenext',0)
        topnext=browser.xmlRead(dom,'typetopnext',0)
        before=browser.xmlRead(dom,'typebe',0)
        topebefore=browser.xmlRead(dom,'typetopbe',0)

        try:
            #刷新
            refresh=basetype+pageid+refrdragt
            #print refresh
            browser.findXpath(self.driver,refresh).click()

            #查看单据
            time.sleep(1)
            cenview=pageid+browser.xmlRead(dom,'cenview',0)
            #print cenview
            browser.findId(self.driver,cenview).click()

            browser.openModule2(self.driver,module,moduledetail)

            #网店商品明细
            cenidetail=pageid+browser.xmlRead(dom,'cenidetail',0)
            browser.delaytime(2,self.driver)
            browser.findId(self.driver,cenidetail).click()
            browser.delaytime(2,self.driver)
            browser.accAlert(self.driver,1)


            #红冲单据
            cenred=pageid+browser.xmlRead(dom,'cenidetail',0)
            browser.delaytime(2,self.driver)
            browser.findId(self.driver,cenred).click()
            browser.delaytime(2,self.driver)
            browser.accAlert(self.driver,0)
            #browser.findId(self.driver,cenred).click()
            #browser.accAlert(self.driver,1)
            #browser.accAlert(self.driver,1)

            #复制为草稿
            cencopy=pageid+browser.xmlRead(dom,'cencopy',0)
            browser.findId(self.driver,cencopy).click()

            browser.exjscommin(self.driver,"退出")
            browser.findId(self.driver,cencopy).click()
            browser.exjscommin(self.driver,"选中")
            browser.delaytime(2,self.driver)
            browser.accAlert(self.driver,1)
            #print "exit"

            #单据中心数据
            notedic=browser.notecentel(header3)
            etypeid=notedic["itemList"][0]["etypeid"]
            efullname=notedic["itemList"][0]["efullname"]


            #修改摘要/物流单号

            cenupsumm=pageid+browser.xmlRead(dom,'cenupsumm',0)
            browser.findId(self.driver,cenupsumm).click()


            #确定
            browser.exjscommin(self.driver,"确定")
            browser.findId(self.driver,cenupsumm).click()
            #关闭
            browser.exjscommin(self.driver,"关闭")


            #修改经手人
            cenupppeo=pageid+browser.xmlRead(dom,'cenupppeo',0)
            browser.findId(self.driver,cenupppeo).click()

            ppeourl="http://dba.wsgjp.com.cn/Beefun/Assistant/BusinessHistoryUpdateEmployee.gspx"
            da="{\"etypeid\":\""+str(etypeid)+"\",\"efullname\":\""+str(efullname)+"\"}"
            data={"__Params":da}
            ppeotext=browser.requestpost(ppeourl,data,header4)
            #print ppeotext
            ppeoid=browser.getdraftalterid(ppeotext)
            ppeoid=ppeoid+"$"
            #print ppeoid

            seloppeo=browser.xmlRead(dom,'seloppeo',0)
            selbtn=browser.xmlRead(dom,'seloppeo',0)

            browser.doubleclick(self.driver,ppeoid+seloppeo)
            #选中
            peourl="http://dba.wsgjp.com.cn/Beefun/Selector/ETypeSelector.gspx?SelectClass=False&&HideStoppedItem=True&Add=False&Mode=Money"
            speoid=browser.halfid(peourl,header3)
            #print speoid
            #time.sleep(1)
            peoselbtn=browser.xmlRead(dom,'selbtn',0)
            browser.findId(self.driver,speoid+peoselbtn).click()

            browser.doubleclick(self.driver,ppeoid+seloppeo)

            #关闭
            time.sleep(1)
            browser.findId(self.driver,speoid+selexit).click()

            #退出
            browser.findId(self.driver,ppeoid+btnexit).click()

            #确定
            browser.findId(self.driver,cenupppeo).click()
            browser.findId(self.driver,ppeoid+btnok).click()


            #航天金穗
            js="$(\"div[class=GridBodyCellText]:contains('XS-')\").first().attr(\"id\",\"htid\")"
            time.sleep(1)
            browser.excutejs(self.driver,js)
            time.sleep(1)
            browser.findId(self.driver,"htid").click()
            time.sleep(1)
            cenflygold=pageid+browser.xmlRead(dom,'cenflygold',0)
            browser.delaytime(2,self.driver)
            browser.findId(self.driver,cenflygold).click()
            time.sleep(1)
            browser.accAlert(self.driver,1)

            #翻页
            browser.pagechoice(self.driver)

            #退出
            time.sleep(1)
            browser.findId(self.driver,pageid+selexit).click()
            time.sleep(1)
            browser.openModule2(self.driver,module,moduledetail)
            '''
            #翻页
            #下一页
            denext=basetype+pageid+pnext
            time.sleep(1)
            print denext
            browser.findXpath(self.driver,denext).click()
            #第一页
            detopbe=basetype+pageid+topebefore
            browser.findXpath(self.driver,detopbe).click()
            #上一页
            debe=basetype+pageid+before
            browser.findXpath(self.driver,debe).click()
            #最后一页
            detopnext=basetype+pageid+topnext
            browser.findXpath(self.driver,detopnext).click()
            '''

        except:
            print traceback.format_exc()
            filename=browser.xmlRead(dom,'filename',0)
            #print filename+u"常用-单据草稿.png"
            #browser.getpicture(self.driver,filename+u"notedraft.png")
            browser.getpicture(self.driver,filename+u"常用-单据中心.png")



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
