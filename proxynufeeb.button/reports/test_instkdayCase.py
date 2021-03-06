#*-* coding:UTF-8 *-*
import unittest
import  xml.dom.minidom
import traceback
import reportsClass
browser=reportsClass.instockclass()

class inskdayTest(unittest.TestCase):
    u'''报表-库存报表-进销存日报表'''

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


    def test_invskdaily(self):
        u'''报表-库存报表-进销存日报表'''
        header={'cookie':self.cookiestr,"Content-Type": "application/json"}
        dom = xml.dom.minidom.parse(r'C:\workspace\proxynufeeb.button\reports\reportslocation.xml')
        module=browser.xmlRead(dom,'module',0)
        moduledetail=browser.xmlRead(dom,'moduledetail',2)
        moduledd=browser.xmlRead(dom,'invadd',0)

        browser.openModule3(self.driver,module,moduledetail,moduledd)

        #页面id
        #pageurl=browser.xmlRead(dom,"fixcapsaleurl",0)
        #pageid=browser.getalertid(pageurl,header)

        try:
            browser.exjscommin(self.driver,"关闭")
            browser.openModule3(self.driver,module,moduledetail,moduledd)
            browser.exjscommin(self.driver,"确定")

            #翻页
            browser.pagechoice(self.driver)

            #刷新
            browser.refreshbutton(self.driver)

            #筛选
            browser.selectbycon(self.driver,"商品名称",u"中文测试饕餮壹贰123！@#￥%……&*（）()； abc")

            #查询条件
            browser.selothersavecon(self.driver)
            js="$(\"input[id$=edKType]\").last().attr(\"id\",\"cateid\")"
            browser.delaytime(1)
            browser.excutejs(self.driver,js)
            browser.doubleclick(self.driver,"cateid")
            browser.exjscommin(self.driver,"关闭")
            browser.doubleclick(self.driver,"cateid")
            browser.exjscommin(self.driver,"选中")
            browser.exjscommin(self.driver,"确定")

            #退出
            browser.exjscommin(self.driver,"退出")
            browser.openModule3(self.driver,module,moduledetail,moduledd)



        except:
            print traceback.format_exc()
            filename=browser.xmlRead(dom,'filename',0)
            #print filename+u"常用-单据草稿.png"
            #browser.getpicture(self.driver,filename+u"notedraft.png")
            browser.getpicture(self.driver,filename+u"报表-库存报表-进销存日报表.png")



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()