#*-* coding:UTF-8 *-*
import unittest
import  xml.dom.minidom
import traceback
import reportsClass
browser=reportsClass.instockclass()

class finbusinessTest(unittest.TestCase):
    u'''报表-财务报表-经营报告'''

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


    def test_finBusiness(self):
        u'''报表-财务报表-经营报告'''
        dom = xml.dom.minidom.parse(r'C:\workspace\proxynufeeb.button\reports\reportslocation.xml')
        module=browser.xmlRead(dom,'module',0)
        moduledetail=browser.xmlRead(dom,'moduledetail',3)
        moduledd=browser.xmlRead(dom,'finadd',0)

        browser.openModule3(self.driver,module,moduledetail,moduledd)

        #页面id
        #pageurl=browser.xmlRead(dom,"fixcapsaleurl",0)
        #pageid=browser.getalertid(pageurl,header)

        try:
            stations=["inStockTotalDays","outStockTotalDays","payTotalDays","arTotalDays","moneytotalDays","othermoneyDays"]
            #进货/销售/付款/收款/费用其他
            for classfiy in stations:
                js="$(\"input[id$="+classfiy+"]\").last().attr(\"id\",\""+classfiy+"\")"
                browser.delaytime(1)
                browser.excutejs(self.driver,js)
                browser.doubleclick(self.driver,classfiy)
                tempid=browser.getrandnumber(1)
                js="$(\"div:contains('最近10天')\").last().attr(\"id\",\"abc"+str(tempid[0])+"\")"
                browser.delaytime(1)
                browser.excutejs(self.driver,js)
                browser.findId(self.driver,"abc"+str(tempid[0])).click()


            #月销售
            browser.inputid(self.driver,"saleAnalyse","销售额日趋势图")


            #客户应收款
            browser.inputid(self.driver,"saleHot","供应商应付前5名")


            #本月进货情况
            js="$(\"input[id$=monthinstock]\").last().click();"
            browser.delaytime(1)
            browser.excutejs(self.driver,js)


            #本月销售情况
            js="$(\"input[id$=monthsale]\").last().click();"
            browser.delaytime(1)
            browser.excutejs(self.driver,js)

            #本月库存情况
            js="$(\"input[id$=monthstock]\").last().click();"
            browser.delaytime(1)
            browser.excutejs(self.driver,js)

            #关闭
            browser.closexx(self.driver)
            browser.openModule3(self.driver,module,moduledetail,moduledd)




        except:
            print traceback.format_exc()
            filename=browser.xmlRead(dom,'filename',0)
            #print filename+u"常用-单据草稿.png"
            #browser.getpicture(self.driver,filename+u"notedraft.png")
            browser.getpicture(self.driver,filename+u"报表-财务报表-经营报告.png")



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()