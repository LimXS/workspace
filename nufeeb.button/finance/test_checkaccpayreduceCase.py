#*-* coding:UTF-8 *-*
import unittest
import  xml.dom.minidom
import traceback
from common import browserClass
browser=browserClass.browser()

class checkaccpayreduceTest(unittest.TestCase):
    u'''财务-调账-应付款减少'''

    def setUp(self):
        self.driver=browser.startBrowser('chrome')
        browser.set_up(self.driver)
        cookie = [item["name"] + "=" + item["value"] for item in self.driver.get_cookies()]
        #print cookie
        self.cookiestr = ';'.join(item for item in cookie)

        browser.delaytime(1)
        pass


    def tearDown(self):
        print "test over"
        self.driver.close()
        pass


    def test_checkaccpayReduce(self):
        u'''财务-调账-应付款减少'''
        header={'cookie':self.cookiestr,"Content-Type": "application/json"}
        dom = xml.dom.minidom.parse(r'C:\workspace\nufeeb.button\finance\financelocation')
        dom2 = xml.dom.minidom.parse(r'C:\workspace\nufeeb.button\saleretail\salelocation')
        comdom=xml.dom.minidom.parse(r'C:\workspace\nufeeb.button\data\commonlocation')
        module=browser.xmlRead(dom,'module',0)
        moduledetail=browser.xmlRead(dom,'moduledetail',8)
        moduledd=browser.xmlRead(dom,'moduledd',1)

        browser.openModule3(self.driver,module,moduledetail,moduledd)

        #页面id
        pageurl=browser.xmlRead(dom,"checkaccpayreduceurl",0)
        pageid=browser.getalertid(pageurl,header)
        #print pageid

        commid=browser.getallcommonid(comdom)



        try:
            #记录该往来收入的科目名称
            itnaid=commid["basetype"]+pageid+browser.xmlRead(dom2,"partitna",0)+str(3)+"]"
            #print itnaid
            browser.findXpath(self.driver,itnaid).click()
            itemid=pageid+commid["grid_fullname"]
            browser.doubleclick(self.driver,itemid)
            browser.exjscommin(self.driver,"关闭")
            browser.doubleclick(self.driver,itemid)
            browser.delaytime(2)
            browser.exjscommin(self.driver,"选中")

            #增加金额
            js="$(\"input[id$=grid_total]\").val('200')"
            browser.delaytime(1)
            browser.excutejs(self.driver,js)

            #往来单位
            companyid=pageid+browser.xmlRead(dom2,'edBType',0)
            browser.nebecompany2(self.driver,companyid)

            #经手人
            peoid=pageid+browser.xmlRead(dom2,'edEType',0)
            browser.passpeoplesel(self.driver,peoid)

            #部门
            depid=pageid+browser.xmlRead(dom2,'edDept',0)
            browser.passpeople(self.driver,depid)

            #摘要
            summid=pageid+browser.xmlRead(dom2,'edSummary',0)
            browser.findId(self.driver,summid).send_keys(u"中文蘩軆饕餮！@#￥%……&*（）？； 。.finance check account pay reduce summary")

            #附加说明
            commentid=pageid+browser.xmlRead(dom2,'edComment',0)
            browser.findId(self.driver,commentid).send_keys(u"finance account pay reduce commentid中文蘩軆饕餮！@#￥%……&*（）？； 。.")

            #录单配置
            conbillid=pageid+browser.xmlRead(dom2,"btnBillConfig",0)
            browser.conbill(self.driver,conbillid)
            browser.delaytime(2,self.driver)
            browser.accAlert(self.driver,1)

            #保存退出
            saexid=pageid+commid["selclose"]
            browser.savedraftexit(self.driver,saexid,itnaid,itemid,1)
            browser.openModule3(self.driver,module,moduledetail,moduledd)

        except:
            print traceback.format_exc()
            filename=browser.xmlRead(dom,'filename',0)
            #print filename+u"常用-单据草稿.png"
            #browser.getpicture(self.driver,filename+u"notedraft.png")
            browser.getpicture(self.driver,filename+u"财务-调账-应付款减少.png")



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
