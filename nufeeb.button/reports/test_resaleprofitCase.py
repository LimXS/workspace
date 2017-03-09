#*-* coding:UTF-8 *-*
import unittest
import  xml.dom.minidom
import traceback
from common import browserClass
browser=browserClass.browser()

class resaleprofitTest(unittest.TestCase):
    u'''报表-批发零售报表-销售优惠表'''

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


    def test_resaleProfit(self):
        u'''报表-批发零售报表-销售优惠表'''
        header={'cookie':self.cookiestr,"Content-Type": "application/json"}
        dom = xml.dom.minidom.parse(r'C:\workspace\nufeeb.button\reports\reportslocation.xml')
        module=browser.xmlRead(dom,'module',0)
        moduledetail=browser.xmlRead(dom,'moduledetail',1)
        moduledd=browser.xmlRead(dom,'saleadd',7)

        browser.openModule3(self.driver,module,moduledetail,moduledd)

        #页面id
        #pageurl=browser.xmlRead(dom,"fixcapsaleurl",0)
        #pageid=browser.getalertid(pageurl,header)

        try:
            browser.exjscommin(self.driver,"关闭")
            browser.openModule3(self.driver,module,moduledetail,moduledd)
            browser.exjscommin(self.driver,"确定")

            #明细账本
            browser.exjscommin(self.driver,"明细账本")
            browser.exjscommin(self.driver,"查看单据")
            browser.exjscommin(self.driver,"退出")
            browser.selectbycon(self.driver,"单据编号","XS")
            browser.exjscommin(self.driver,"退出")

            #查询条件
            browser.exjscommin(self.driver,"查询条件")
            browser.exjscommin(self.driver,"关闭")
            browser.exjscommin(self.driver,"查询条件")
            js="$(\"input[id$=edEType]\").last().attr(\"id\",\"peoid\");$(\"input[id$=edBType]\").last().attr(\"id\",\"comid\")"
            browser.delaytime(1)
            browser.excutejs(self.driver,js)
            browser.doubleclick(self.driver,"peoid")
            browser.exjscommin(self.driver,"关闭")
            browser.doubleclick(self.driver,"peoid")
            browser.exjscommin(self.driver,"选中")
            browser.doubleclick(self.driver,"comid")
            browser.exjscommin(self.driver,"确定")


            #刷新
            browser.refreshbutton(self.driver)

            #筛选
            browser.selectbycon(self.driver,"单位编号","10")

            #退出
            browser.exjscommin(self.driver,"退出")
            browser.openModule3(self.driver,module,moduledetail,moduledd)

        except:
            print traceback.format_exc()
            filename=browser.xmlRead(dom,'filename',0)
            browser.delaytime(1)
            browser.getpicture(self.driver,filename+u"报表-批发零售报表-销售优惠表.png")



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
