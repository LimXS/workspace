#*-* coding:UTF-8 *-*
import unittest
import  xml.dom.minidom
import traceback
import reportsClass
browser=reportsClass.instockclass()

class finbossTest(unittest.TestCase):
    u'''报表-财务报表-老板表'''

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


    def test_finBoss(self):
        u'''报表-财务报表-老板表'''
        dom = xml.dom.minidom.parse(r'C:\workspace\nufeeb.button\reports\reportslocation.xml')
        module=browser.xmlRead(dom,'module',0)
        moduledetail=browser.xmlRead(dom,'moduledetail',3)
        moduledd=browser.xmlRead(dom,'finadd',4)

        browser.openModule3(self.driver,module,moduledetail,moduledd)

        try:
            browser.exjscommin(self.driver,"关闭")
            browser.openModule3(self.driver,module,moduledetail,moduledd)
            browser.exjscommin(self.driver,"确定")
            browser.delaytime(5)

            #明细账本
            browser.exjscommin(self.driver,"明细账本")
            browser.delaytime(1)
            browser.accAlert(self.driver,1)
            browser.exjscommin(self.driver,"退出")

            browser.elementcontains(self.driver,"div","固定资产__甲","cashid")
            browser.findId(self.driver,"cashid").click()
            browser.exjscommin(self.driver,"明细账本")
            browser.exjscommin(self.driver,"查看凭证")
            browser.exjscommin(self.driver,"退出")
            browser.pagechoice(self.driver)
            browser.inputid(self.driver,"edOrder","按单据时间排序")
            browser.inputid(self.driver,"edRedwordFilter","不显示红冲单据")
            browser.exjscommin(self.driver,"退出")

            #翻页
            browser.pagechoice(self.driver)

            #刷新
            browser.refreshbutton(self.driver)
            browser.delaytime(1)

            #级数
            browser.inputid(self.driver,"leveal","3")

            #查询条件
            browser.exjscommin(self.driver,"查询条件")
            browser.exjscommin(self.driver,"关闭")
            browser.exjscommin(self.driver,"查询条件")
            browser.exjscommin(self.driver,"确定")

            browser.exjscommin(self.driver,"退出")
            browser.openModule3(self.driver,module,moduledetail,moduledd)


        except:
            print traceback.format_exc()
            filename=browser.xmlRead(dom,'filename',0)
            browser.delaytime(1)
            browser.getpicture(self.driver,filename+u"报表-财务报表-老板表.png")



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()