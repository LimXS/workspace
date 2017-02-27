#*-* coding:UTF-8 *-*
import unittest
import  xml.dom.minidom
import traceback
from reports import reportsClass
browser=reportsClass.instockclass()

class resalepackageTest(unittest.TestCase):
    u'''报表-批发零售报表-套餐销售统计'''

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


    def test_resalePackage(self):
        u'''报表-批发零售报表-套餐销售统计'''
        header={'cookie':self.cookiestr,"Content-Type": "application/json"}
        dom = xml.dom.minidom.parse(r'C:\workspace\proxynufeeb.button\reports\reportslocation.xml')
        module=browser.xmlRead(dom,'module',0)
        moduledetail=browser.xmlRead(dom,'moduledetail',1)
        moduledd=browser.xmlRead(dom,'saleadd',14)

        browser.openModule3(self.driver,module,moduledetail,moduledd)

        #页面id
        #pageurl=browser.xmlRead(dom,"fixcapsaleurl",0)
        #pageid=browser.getalertid(pageurl,header)

        try:
            browser.exjscommin(self.driver,"关闭")
            browser.openModule3(self.driver,module,moduledetail,moduledd)
            browser.exjscommin(self.driver,"确定")

            #套餐销售明细
            browser.exjscommin(self.driver,"套餐销售明细")
            browser.pagechoice(self.driver)
            browser.selectbycon(self.driver,"单据编号","XS")
            browser.refreshbutton(self.driver)
            browser.selpackage(self.driver)
            browser.delaytime(2)
            browser.exjscommin(self.driver,"退出")
            browser.exjscommin(self.driver,"退出")
            #print "ok1"

            #查询条件
            browser.selpackage(self.driver)
            browser.exjscommin(self.driver,"退出")

            #筛选
            browser.selectbycon(self.driver,"套餐编号",u"中文测试饕餮壹贰123！@#￥%……&*（）()； abc")

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
            browser.getpicture(self.driver,filename+u"报表-批发零售报表-套餐销售统计.png")



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
