#*-* coding:UTF-8 *-*
import unittest
import  xml.dom.minidom
import traceback
import reportsClass
browser=reportsClass.instockclass()

class deppeocostgridTest(unittest.TestCase):
    u'''报表-部门职员业务分析-职员费用分布'''

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


    def test_depPeocostGrid(self):
        u'''报表-部门职员业务分析-职员费用分布'''
        dom = xml.dom.minidom.parse(r'C:\workspace\proxynufeeb.button\reports\reportslocation.xml')
        module=browser.xmlRead(dom,'module',0)
        moduledetail=browser.xmlRead(dom,'moduledetail',5)
        moduledd=browser.xmlRead(dom,'depadd',3)

        browser.openModule3(self.driver,module,moduledetail,moduledd)

        try:
            browser.exjscommin(self.driver,"关闭")
            browser.openModule3(self.driver,module,moduledetail,moduledd)
            browser.exjscommin(self.driver,"确定")

            #刷新
            browser.refreshbutton(self.driver)

            browser.exjscommin(self.driver,"退出")
            browser.openModule3(self.driver,module,moduledetail,moduledd)


        except:
            print traceback.format_exc()
            filename=browser.xmlRead(dom,'filename',0)
            browser.delaytime(1)
            browser.getpicture(self.driver,filename+u"报表-部门职员业务分析-职员费用分布.png")



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()