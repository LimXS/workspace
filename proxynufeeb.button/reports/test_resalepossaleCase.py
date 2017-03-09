#*-* coding:UTF-8 *-*
import unittest
import  xml.dom.minidom
import traceback
from common import browserClass
browser=browserClass.browser()

class resalepossaleTest(unittest.TestCase):
    u'''报表-批发零售报表-收银台销售流水'''

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


    def test_resaleposSale(self):
        u'''报表-批发零售报表-收银台销售流水'''
        header={'cookie':self.cookiestr,"Content-Type": "application/json"}
        dom = xml.dom.minidom.parse(r'C:\workspace\proxynufeeb.button\reports\reportslocation.xml')
        module=browser.xmlRead(dom,'module',0)
        moduledetail=browser.xmlRead(dom,'moduledetail',1)
        moduledd=browser.xmlRead(dom,'saleadd',13)

        browser.openModule3(self.driver,module,moduledetail,moduledd)

        #页面id
        #pageurl=browser.xmlRead(dom,"fixcapsaleurl",0)
        #pageid=browser.getalertid(pageurl,header)

        try:
            #筛选
            browser.selectbycon(self.driver,"零售单号",u"中文测试饕餮壹贰123！@#￥%……&*（）()； abcl ；2abc")

            #退出
            browser.exjscommin(self.driver,"退出")
            browser.openModule3(self.driver,module,moduledetail,moduledd)

        except:
            print traceback.format_exc()
            filename=browser.xmlRead(dom,'filename',0)
            #print filename+u"常用-单据草稿.png"
            #browser.getpicture(self.driver,filename+u"notedraft.png")
            browser.getpicture(self.driver,filename+u"报表-批发零售报表-收银台销售流水.png")



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
