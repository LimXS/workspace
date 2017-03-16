#*-* coding:UTF-8 *-*
import unittest
import  xml.dom.minidom
import traceback
import reportsClass
browser=reportsClass.instockclass()

class resalebenefitTest(unittest.TestCase):
    u'''报表-批发零售报表-销售毛利统计'''

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


    def test_resaleBenefit(self):
        u'''报表-批发零售报表-销售毛利统计'''
        header={'cookie':self.cookiestr,"Content-Type": "application/json"}
        dom = xml.dom.minidom.parse(r'C:\workspace\nufeeb.button\reports\reportslocation.xml')
        module=browser.xmlRead(dom,'module',0)
        moduledetail=browser.xmlRead(dom,'moduledetail',1)
        moduledd=browser.xmlRead(dom,'saleadd',3)

        browser.openModule3(self.driver,module,moduledetail,moduledd)

        #页面id
        #pageurl=browser.xmlRead(dom,"fixcapsaleurl",0)
        #pageid=browser.getalertid(pageurl,header)

        try:
            browser.exjscommin(self.driver,"关闭")
            browser.openModule3(self.driver,module,moduledetail,moduledd)
            browser.exjscommin(self.driver,"确定")

            #查看单据
            browser.exjscommin(self.driver,"查看单据")
            browser.delaytime(2)
            browser.know(self.driver)
            browser.exjscommin(self.driver,"退出")

            #成本明细
            browser.exjscommin(self.driver,"成本明细")
            browser.selectbycon(self.driver,"商品编号")
            browser.exjscommin(self.driver,"退出")

            #翻页
            browser.pagechoice(self.driver)

            #查询条件
            browser.selothersavecon(self.driver)
            browser.selcomcaitpeo(self.driver)

            #筛选
            browser.selectbycon(self.driver,"单据编号","XS")

            #刷新
            browser.refreshbutton(self.driver)

            #退出
            browser.exjscommin(self.driver,"退出")
            browser.openModule3(self.driver,module,moduledetail,moduledd)

        except:
            print traceback.format_exc()
            filename=browser.xmlRead(dom,'filename',0)
            #print filename+u"常用-单据草稿.png"
            #browser.getpicture(self.driver,filename+u"notedraft.png")
            browser.getpicture(self.driver,filename+u"报表-批发零售报表-销售毛利统计.png")



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
