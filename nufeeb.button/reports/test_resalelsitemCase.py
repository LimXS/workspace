#*-* coding:UTF-8 *-*
import unittest
import  xml.dom.minidom
import traceback
import reportsClass
browser=reportsClass.instockclass()

class resalelsitemTest(unittest.TestCase):
    u'''报表-批发零售报表-零售商品统计'''

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


    def test_resalelsItem(self):
        u'''报表-批发零售报表-零售商品统计'''
        header={'cookie':self.cookiestr,"Content-Type": "application/json"}
        dom = xml.dom.minidom.parse(r'C:\workspace\nufeeb.button\reports\reportslocation.xml')
        module=browser.xmlRead(dom,'module',0)
        moduledetail=browser.xmlRead(dom,'moduledetail',1)
        moduledd=browser.xmlRead(dom,'saleadd',9)

        browser.openModule3(self.driver,module,moduledetail,moduledd)

        #页面id
        #pageurl=browser.xmlRead(dom,"fixcapsaleurl",0)
        #pageid=browser.getalertid(pageurl,header)

        try:
            js="$(\"input[id$=edEType]\").last().attr(\"id\",\"peoid\");$(\"input[id$=edKType]\").last().attr(\"id\",\"cateid\");$(\"input[id$=edDateScope]\").last().attr(\"id\",\"dateid\")"
            browser.delaytime(1)
            browser.excutejs(self.driver,js)

            #仓库
            browser.passpeoplesel(self.driver,"cateid")

            #经手人
            browser.passpeoplesel(self.driver,"peoid")

            #汇总日期
            browser.doubleclick(self.driver,"dateid")
            js="$(\"div:contains('最近三天')\").last().attr(\"id\",\"seldateid\")"
            browser.delaytime(1)
            browser.excutejs(self.driver,js)
            browser.findId(self.driver,"seldateid").click()

            #查询
            browser.exjscommin(self.driver,"查 询")

            #筛选
            browser.selectbycon(self.driver,"商品编号","a1x")

            #退出
            browser.exjscommin(self.driver,"退出")
            browser.openModule3(self.driver,module,moduledetail,moduledd)


        except:
            print traceback.format_exc()
            filename=browser.xmlRead(dom,'filename',0)
            #print filename+u"常用-单据草稿.png"
            #browser.getpicture(self.driver,filename+u"notedraft.png")
            browser.getpicture(self.driver,filename+u"报表-批发零售报表-零售商品统计.png")



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
