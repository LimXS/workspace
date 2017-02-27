#*-* coding:UTF-8 *-*
import unittest
import  xml.dom.minidom
import traceback
import reportsClass
browser=reportsClass.instockclass()

class depmkpeogetTest(unittest.TestCase):
    u'''报表-部门职员业务分析-制单人收付款统计'''

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
        #self.driver.close()
        pass


    def test_depMkpeoget(self):
        u'''报表-部门职员业务分析-制单人收付款统计'''
        dom = xml.dom.minidom.parse(r'C:\workspace\nufeeb.button\reports\reportslocation.xml')
        module=browser.xmlRead(dom,'module',0)
        moduledetail=browser.xmlRead(dom,'moduledetail',5)
        moduledd=browser.xmlRead(dom,'depadd',5)

        browser.openModule3(self.driver,module,moduledetail,moduledd)

        try:
            browser.exjscommin(self.driver,"关闭")
            browser.openModule3(self.driver,module,moduledetail,moduledd)
            browser.exjscommin(self.driver,"确定")

            #查询条件
            browser.exjscommin(self.driver,"查询条件")
            browser.exjscommin(self.driver,"关闭")
            browser.exjscommin(self.driver,"查询条件")
            browser.exjscommin(self.driver,"确定")
            browser.exjscommin(self.driver,"查询条件")
            browser.lableclick(self.driver,"listType_radio1")
            browser.exjscommin(self.driver,"确定")
            browser.refreshbutton(self.driver)
            browser.exjscommin(self.driver,"退出")

            #我的查询
            browser.exjscommin(self.driver,"我的查询")
            browser.exjscommin(self.driver,"取消")
            browser.exjscommin(self.driver,"我的查询")
            browser.exjscommin(self.driver,"新增")
            browser.exjscommin(self.driver,"取消")
            browser.exjscommin(self.driver,"新增")
            newselcon="sel_"+str(browser.getrandnumber())
            changesel="change_"+str(browser.getrandnumber())
            browser.elementvalue(self.driver,"input","txtname",newselcon)
            browser.exjscommin(self.driver,"确定")

            browser.exjscommin(self.driver,"更名")
            browser.exjscommin(self.driver,"取消")
            browser.exjscommin(self.driver,"更名")
            browser.elementvalue(self.driver,"input","txtname",changesel)
            browser.exjscommin(self.driver,"确定")

            browser.exjscommin(self.driver,"自动分组")

            browser.exjscommin(self.driver,"删除")
            browser.accAlert(self.driver,1)
            browser.exjscommin(self.driver,"删除")
            browser.accAlert(self.driver,1)

            browser.inputid(self.driver,"xx","现金",1)
            js="$(\"input[type=checkbox]\").eq(5).click()"
            browser.delaytime(1)
            browser.excutejs(self.driver,js)
            browser.exjscommin(self.driver,"确定")

            #刷新
            browser.refreshbutton(self.driver)

            browser.exjscommin(self.driver,"退出")
            browser.openModule3(self.driver,module,moduledetail,moduledd)


        except:
            print traceback.format_exc()
            filename=browser.xmlRead(dom,'filename',0)
            browser.delaytime(1)
            browser.getpicture(self.driver,filename+u"报表-部门职员业务分析-制单人收付款统计.png")



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()