#*-* coding:UTF-8 *-*
import unittest
import  xml.dom.minidom
import traceback
import reportsClass
browser=reportsClass.instockclass()

class resaleitemsareTest(unittest.TestCase):
    u'''报表-批发零售报表-商品销售/退货分析'''

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


    def test_resaleitemsaRe(self):
        u'''报表-批发零售报表-商品销售/退货分析'''
        dom = xml.dom.minidom.parse(r'C:\workspace\nufeeb.button\reports\reportslocation.xml')
        module=browser.xmlRead(dom,'module',0)
        moduledetail=browser.xmlRead(dom,'moduledetail',1)
        moduledd=browser.xmlRead(dom,'saleadd',2)

        browser.openModule3(self.driver,module,moduledetail,moduledd)

        #页面id
        #pageurl=browser.xmlRead(dom,"fixcapsaleurl",0)
        #pageid=browser.getalertid(pageurl,header)

        try:
            browser.exjscommin(self.driver,"关闭")
            browser.openModule3(self.driver,module,moduledetail,moduledd)
            browser.exjscommin(self.driver,"确定")

            #列表
            browser.exjscommin(self.driver,"列表")
            browser.exjscommin(self.driver,"取消")
            browser.exjscommin(self.driver,"列表")
            browser.exjscommin(self.driver,"确定")
            browser.selectbycon(self.driver,"商品编号")
            browser.exjscommin(self.driver,"退出")

            #刷新
            browser.refreshbutton(self.driver)

            #查询条件
            browser.selothersavecon(self.driver)
            browser.selcomcaitpeo(self.driver)

            #筛选
            browser.selectbycon(self.driver,"商品编号")

            #退出
            browser.exjscommin(self.driver,"退出")
            browser.openModule3(self.driver,module,moduledetail,moduledd)



        except:
            print traceback.format_exc()
            filename=browser.xmlRead(dom,'filename',0)
            browser.delaytime(1)
            browser.getpicture(self.driver,filename+"报表-批发零售报表-商品销售退货分析.png")
            #browser.getpicture(self.driver,filename+u"报表.png")



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
