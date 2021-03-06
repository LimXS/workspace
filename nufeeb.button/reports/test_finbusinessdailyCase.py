#*-* coding:UTF-8 *-*
import unittest
import  xml.dom.minidom
import traceback
import reportsClass
browser=reportsClass.instockclass()

class finbusinessdailyTest(unittest.TestCase):
    u'''报表-财务报表-经营日报'''

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


    def test_finbusinessDaily(self):
        u'''报表-财务报表-经营日报'''
        dom = xml.dom.minidom.parse(r'C:\workspace\nufeeb.button\reports\reportslocation.xml')
        module=browser.xmlRead(dom,'module',0)
        moduledetail=browser.xmlRead(dom,'moduledetail',3)
        moduledd=browser.xmlRead(dom,'finadd',1)

        browser.openModule3(self.driver,module,moduledetail,moduledd)

        #页面id
        #pageurl=browser.xmlRead(dom,"fixcapsaleurl",0)
        #pageid=browser.getalertid(pageurl,header)

        try:
            browser.exjscommin(self.driver,"关闭")
            browser.openModule3(self.driver,module,moduledetail,moduledd)
            browser.exjscommin(self.driver,"确定")

            #刷新
            browser.refreshbutton(self.driver)

            #选中日期
            js="$(\"div[style*=comboButton]\").last().attr(\"id\",\"dateid\")"
            browser.delaytime(1)
            browser.excutejs(self.driver,js)
            browser.findId(self.driver,"dateid").click()
            browser.know(self.driver)
            browser.exjscommin(self.driver,"今天")
            browser.findId(self.driver,"dateid").click()
            browser.know(self.driver)
            #browser.delaytime(1)
            #browser.accAlert(self.driver,1)


            js="$(\"td:contains('14')\").last().attr(\"id\",\"dateselid\")"
            browser.delaytime(1)
            browser.excutejs(self.driver,js)

            browser.findId(self.driver,"dateselid").click()

            browser.closexx(self.driver)
            browser.openModule3(self.driver,module,moduledetail,moduledd)


        except:
            print traceback.format_exc()
            filename=browser.xmlRead(dom,'filename',0)
            #print filename+u"常用-单据草稿.png"
            #browser.getpicture(self.driver,filename+u"notedraft.png")
            browser.getpicture(self.driver,filename+u"报表-财务报表-经营日报.png")



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()