#*-* coding:UTF-8 *-*
import time
import re
import datetime
import unittest
import  xml.dom.minidom
import traceback

from common import browserClass
browser=browserClass.browser()

class companyrepaTest(unittest.TestCase):
    u'''财务-往来单位应收应付'''

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


    def test_companyrePa(self):
        u'''财务-往来单位应收应付'''
        header={'cookie':self.cookiestr,"Content-Type": "application/json"}
        dom = xml.dom.minidom.parse(r'C:\workspace\proxynufeeb.button\finance\financelocation')
        comdom=xml.dom.minidom.parse(r'C:\workspace\proxynufeeb.button\data\commonlocation')
        module=browser.xmlRead(dom,'module',0)
        moduledetail=browser.xmlRead(dom,'moduledetail',2)

        browser.openModule2(self.driver,module,moduledetail)

        #页面id
        pageurl=browser.xmlRead(dom,"comurl",0)
        pageid=browser.getalertid(pageurl,header)
        #print pageid

        commid=browser.getallcommonid(comdom)

        try:
            #进入下级
            nextid=pageid+browser.xmlRead(dom,"btnNext",0)
            browser.findId(self.driver,nextid).click()

            #返回上级
            returnid=pageid+browser.xmlRead(dom,"btnReturn",0)
            browser.findId(self.driver,returnid).click()

            #筛选
            browser.selectbycon(self.driver,"单位名称")

            #刷新
            browser.refreshbutton(self.driver)

            #查询条件
            conid=pageid+browser.xmlRead(dom,"btnSearch",0)
            browser.conditonsel(self.driver,conid)

            #应收应付明细
            detid=pageid+browser.xmlRead(dom,"btnRecDetail",0)
            browser.findId(self.driver,detid).click()
            browser.exjscommin(self.driver,"关闭")
            browser.findId(self.driver,detid).click()
            browser.exjscommin(self.driver,"确定")
            browser.exjscommin(self.driver,"查看单据")
            browser.exjscommin(self.driver,"退出")
            browser.pagechoice(self.driver)
            browser.exjscommin(self.driver,"退出")

            #往来对账
            checkaccid=pageid+browser.xmlRead(dom,"btnCurrentAccount",0)
            browser.checkacccom(self.driver,checkaccid)

            #调整应收应付
            changerepayid=pageid+commid["btnMore"]
            conlist=["应收增加","应收减少","应付增加","应付减少"]
            for a in conlist:
                browser.findId(self.driver,changerepayid).click()
                browser.classmen(self.driver,a)
                browser.exjscommin(self.driver,"退出")


            #列表
            listid=pageid+browser.xmlRead(dom,"btnViewList",0)

            browser.findId(self.driver,listid).click()
            browser.delaytime(1)
            browser.exjscommin(self.driver,"关闭")
            browser.findId(self.driver,listid).click()
            browser.delaytime(3,self.driver)
            browser.exjscommin(self.driver,"确定")
            browser.pagechoice(self.driver)
            browser.exjscommin(self.driver,"单位筛选")
            browser.exjscommin(self.driver,"放弃")
            browser.exjscommin(self.driver,"单位筛选")
            js="$(\"input[id$=usercode]\").last().val('s');$(\"input[id$=fullname]\").last().val('e')"
            browser.delaytime(1)
            browser.excutejs(self.driver,js)
            browser.exjscommin(self.driver,"确定")
            browser.exjscommin(self.driver,"退出")



            #退出
            browser.exjscommin(self.driver,"退出")
            browser.openModule2(self.driver,module,moduledetail)
             #翻页
            browser.pagechoice(self.driver)
            browser.exjscommin(self.driver,"退出")
            browser.openModule2(self.driver,module,moduledetail)



        except:
            print traceback.format_exc()
            filename=browser.xmlRead(dom,'filename',0)
            #print filename+u"常用-单据草稿.png"
            #browser.getpicture(self.driver,filename+u"notedraft.png")
            browser.getpicture(self.driver,filename+u"财务-往来单位应收应付.png")



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
