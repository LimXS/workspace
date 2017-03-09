#*-* coding:UTF-8 *-*
import unittest
import  xml.dom.minidom
import traceback
from common import browserClass
browser=browserClass.browser()

class resalestorelsTest(unittest.TestCase):
    u'''报表-批发零售报表-门店零售流水'''

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

    def test_resalestoreLs(self):
        u'''报表-批发零售报表-门店零售流水'''
        header={'cookie':self.cookiestr,"Content-Type": "application/json"}
        dom = xml.dom.minidom.parse(r'C:\workspace\nufeeb.button\reports\reportslocation.xml')
        module=browser.xmlRead(dom,'module',0)
        moduledetail=browser.xmlRead(dom,'moduledetail',1)
        moduledd=browser.xmlRead(dom,'saleadd',12)

        browser.openModule3(self.driver,module,moduledetail,moduledd)

        #页面id
        #pageurl=browser.xmlRead(dom,"fixcapsaleurl",0)
        #pageid=browser.getalertid(pageurl,header)

        try:
            closejs="$(\"div[style*=closeButton]\").last().click()"
            #订单详情
            browser.exjscommin(self.driver,"订单详情")
            browser.pagechoice(self.driver)
            browser.exjscommin(self.driver,"订单明细")
            browser.exjscommin(self.driver,"退出")
            browser.selectbycon(self.driver,"单据编号","LS")
            browser.excutejs(self.driver,closejs)


            #检索
            js="$(\"input[id$=filterKey\").last().val('3');$(\"img[src*=find]\").last().click()"
            browser.delaytime(1)
            browser.excutejs(self.driver,js)

            #退出
            browser.excutejs(self.driver,closejs)
            browser.openModule3(self.driver,module,moduledetail,moduledd)


        except:
            print traceback.format_exc()
            filename=browser.xmlRead(dom,'filename',0)
            #print filename+u"常用-单据草稿.png"
            #browser.getpicture(self.driver,filename+u"notedraft.png")
            browser.getpicture(self.driver,filename+u"报表-批发零售报表-门店零售流水.png")



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
