#*-* coding:UTF-8 *-*
import unittest
import  xml.dom.minidom
import traceback
import reportsClass
browser=reportsClass.instockclass()

class combusinessTest(unittest.TestCase):
    u'''报表-往来单位业务分析-往来单位业务统计'''

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


    def test_comBusiness(self):
        u'''报表-往来单位业务分析-往来单位业务统计'''
        dom = xml.dom.minidom.parse(r'C:\workspace\nufeeb.button\reports\reportslocation.xml')
        module=browser.xmlRead(dom,'module',0)
        moduledetail=browser.xmlRead(dom,'moduledetail',4)
        moduledd=browser.xmlRead(dom,'comadd',5)


        try:
            browser.openModule3(self.driver,module,moduledetail,moduledd)
            browser.exjscommin(self.driver,"关闭")
            browser.openModule3(self.driver,module,moduledetail,moduledd)
            browser.exjscommin(self.driver,"确定")

            #翻页
            browser.pagechoice(self.driver)

            #筛选单位
            browser.exjscommin(self.driver,"筛选单位")
            browser.exjscommin(self.driver,"关闭")
            browser.exjscommin(self.driver,"筛选单位")
            comlist=["edFullname","edName","edUsercode"]
            for i in comlist:
                browser.elementvalue(self.driver,"input",i,"2")
            browser.exjscommin(self.driver,"确定")


            #刷新
            browser.refreshbutton(self.driver)

            browser.exjscommin(self.driver,"退出")
            browser.openModule3(self.driver,module,moduledetail,moduledd)


        except:
            print traceback.format_exc()
            filename=browser.xmlRead(dom,'filename',0)
            #print filename+u"常用-单据草稿.png"
            #browser.getpicture(self.driver,filename+u"notedraft.png")
            browser.getpicture(self.driver,filename+u"报表-往来单位业务分析-往来单位业务统计.png")



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()