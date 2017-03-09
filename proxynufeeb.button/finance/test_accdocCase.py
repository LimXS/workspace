#*-* coding:UTF-8 *-*
import time
import unittest
import  xml.dom.minidom
import traceback

from common import browserClass
browser=browserClass.browser()

class accdocTest(unittest.TestCase):
    u'''财务-会计凭证'''

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


    def test_accDoc(self):
        u'''财务-会计凭证'''
        header={'cookie':self.cookiestr,"Content-Type": "application/json"}
        dom = xml.dom.minidom.parse(r'C:\workspace\proxynufeeb.button\finance\financelocation')
        dom2 = xml.dom.minidom.parse(r'C:\workspace\proxynufeeb.button\saleretail\salelocation')
        comdom=xml.dom.minidom.parse(r'C:\workspace\proxynufeeb.button\data\commonlocation')
        module=browser.xmlRead(dom,'module',0)
        moduledetail=browser.xmlRead(dom,'moduledetail',1)

        browser.openModule2(self.driver,module,moduledetail)

        #页面id
        pageurl=browser.xmlRead(dom,"accdocurl",0)
        pageid=browser.getalertid(pageurl,header)
        pageid=pageid[:9]
        #print pageid

        commid=browser.getallcommonid(comdom)



        try:
            #总账科目编号
            itnaid=commid["basetype"]+pageid+browser.xmlRead(dom2,"partitna",0)+str(3)+"]"
            browser.findXpath(self.driver,itnaid).click()
            itemid=pageid+browser.xmlRead(dom,"accnum",0)
            browser.subselect(self.driver,itemid)

            #借方
            js="$(\"input[id$=grid_debit]\").val('200')"
            browser.delaytime(1)
            browser.excutejs(self.driver,js)

            #贷方
            itnaid2=commid["basetype"]+pageid+browser.xmlRead(dom,"partitna",0)+str(3)+"]"
            browser.findXpath(self.driver,itnaid2).click()
            browser.doubleclick(self.driver,itemid)
            browser.exjscommin(self.driver,"选中")
            browser.exjscommin(self.driver,"选中")
            browser.exjscommin(self.driver,"选中")
            dit=commid["basetype"]+pageid+browser.xmlRead(dom,"partitna",0)+str(7)+"]"
            browser.findXpath(self.driver,dit).click()
            js="$(\"input[id$=grid_credit]\").val('200')"
            browser.delaytime(1)
            browser.excutejs(self.driver,js)


            #经手人
            peoid=pageid+browser.xmlRead(dom2,'edEType',0)
            browser.passpeoplesel(self.driver,peoid)

            #部门
            depid=pageid+browser.xmlRead(dom2,'edDept',0)
            browser.passpeople(self.driver,depid)

            #摘要
            summid=pageid+browser.xmlRead(dom2,'edSummary',0)
            browser.findId(self.driver,summid).send_keys(u"finance acc note summary中文测试饕餮壹贰！@#￥%^ &*（）12；")

            #附加说明
            commentid=pageid+browser.xmlRead(dom2,'edComment',0)
            browser.findId(self.driver,commentid).send_keys(u"中文测试饕餮壹贰！@#￥%^ &*（）12；finance acc note commentid")

            #录单配置
            conbillid=pageid+browser.xmlRead(dom2,"btnBillConfig",0)
            browser.conbill(self.driver,conbillid)
            browser.delaytime(2,self.driver)
            browser.accAlert(self.driver,1)


            #保存退出
            saexid=pageid+commid["selclose"]
            browser.savedraftexit(self.driver,saexid,itnaid,itemid,10)
            browser.openModule2(self.driver,module,moduledetail)

        except:
            print traceback.format_exc()
            filename=browser.xmlRead(dom,'filename',0)
            #print filename+u"常用-单据草稿.png"
            #browser.getpicture(self.driver,filename+u"notedraft.png")
            browser.getpicture(self.driver,filename+u"财务-会计凭证.png")



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
