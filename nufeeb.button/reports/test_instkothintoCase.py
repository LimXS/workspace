#*-* coding:UTF-8 *-*
import unittest
import  xml.dom.minidom
import traceback
import reportsClass
browser=reportsClass.instockclass()

class inskothintoTest(unittest.TestCase):
    u'''报表-库存报表-其他入库单统计'''

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


    def test_invskothinto(self):
        u'''报表-库存报表-其他入库单统计'''
        header={'cookie':self.cookiestr,"Content-Type": "application/json"}
        dom = xml.dom.minidom.parse(r'C:\workspace\nufeeb.button\reports\reportslocation.xml')
        module=browser.xmlRead(dom,'module',0)
        moduledetail=browser.xmlRead(dom,'moduledetail',2)
        moduledd=browser.xmlRead(dom,'invadd',5)

        browser.openModule3(self.driver,module,moduledetail,moduledd)

        try:
            browser.weeklylast(self.driver)

            #明细账本
            browser.detailacc(self.driver)

            #筛选
            browser.selectbycon(self.driver,"商品名称","cx")

            #刷新
            browser.refreshbutton(self.driver)

            js="$(\"input[id$=edEType]\").last().attr(\"id\",\"peoid\");$(\"input[id$=edKType]\").last().attr(\"id\",\"cateid\");$(\"input[id$=edBType]\").last().attr(\"id\",\"comid\")"
            browser.delaytime(1)
            browser.excutejs(self.driver,js)

            #仓库
            browser.passpeoplesel(self.driver,"cateid")

            #经手人
            browser.passpeoplesel(self.driver,"peoid")

            #往来单位
            browser.viewcombaseinfo(self.driver,"comid")

            #查询
            browser.exjscommin(self.driver,"查 询")


            browser.exjscommin(self.driver,"退出")
            browser.openModule3(self.driver,module,moduledetail,moduledd)


        except:
            print traceback.format_exc()
            filename=browser.xmlRead(dom,'filename',0)
            #print filename+u"常用-单据草稿.png"
            #browser.getpicture(self.driver,filename+u"notedraft.png")
            browser.getpicture(self.driver,filename+u"报表-库存报表-其他入库单统计.png")



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()