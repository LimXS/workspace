#*-* coding:UTF-8 *-*
import unittest
import  xml.dom.minidom
import traceback
import reportsClass
browser=reportsClass.instockclass()

class deppeogetTest(unittest.TestCase):
    u'''报表-部门职员业务分析-职员应收应付'''

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


    def test_depPeoget(self):
        u'''报表-部门职员业务分析-职员应收应付'''
        dom = xml.dom.minidom.parse(r'C:\workspace\nufeeb.button\reports\reportslocation.xml')
        module=browser.xmlRead(dom,'module',0)
        moduledetail=browser.xmlRead(dom,'moduledetail',5)
        moduledd=browser.xmlRead(dom,'depadd',2)

        browser.openModule3(self.driver,module,moduledetail,moduledd)

        try:
            browser.exjscommin(self.driver,"关闭")
            browser.openModule3(self.driver,module,moduledetail,moduledd)
            browser.exjscommin(self.driver,"确定")

            #单位明细
            browser.exjscommin(self.driver,"单位明细")
            browser.exjscommin(self.driver,"取消")
            browser.exjscommin(self.driver,"单位明细")
            browser.exjscommin(self.driver,"确定")
            browser.pagechoice(self.driver)
            browser.exjscommin(self.driver,"关闭")
            browser.elementcontains(self.driver,"div","001","comdeid")
            browser.findId(self.driver,"comdeid").click()
            browser.exjscommin(self.driver,"单位明细")
            js="$(\"label[for$=listtype_radio1]\").click()"
            browser.delaytime(1)
            browser.excutejs(self.driver,js)
            browser.exjscommin(self.driver,"确定")
            browser.pagechoice(self.driver)
            browser.exjscommin(self.driver,"关闭")

            #应收应付详情
            browser.exjscommin(self.driver,"应收应付详情")
            browser.exjscommin(self.driver,"关闭")
            browser.exjscommin(self.driver,"应收应付详情")
            browser.exjscommin(self.driver,"确定")
            browser.pagechoice(self.driver)
            browser.exjscommin(self.driver,"退出")

            #筛选职员
            browser.exjscommin(self.driver,"筛选职员")
            browser.exjscommin(self.driver,"退出")
            browser.exjscommin(self.driver,"筛选职员")
            browser.elementvalue(self.driver,"input","edFullname","001")
            browser.exjscommin(self.driver,"确定")
            browser.exjscommin(self.driver,"筛选职员")
            browser.elementvalue(self.driver,"input","edUsercode","001")
            browser.exjscommin(self.driver,"确定")

            browser.exjscommin(self.driver,"退出")
            browser.openModule3(self.driver,module,moduledetail,moduledd)


        except:
            print traceback.format_exc()
            filename=browser.xmlRead(dom,'filename',0)
            browser.delaytime(1)
            browser.getpicture(self.driver,filename+u"报表-部门职员业务分析-职员应收应付.png")



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()