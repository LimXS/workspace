#*-* coding:UTF-8 *-*
import unittest
import  xml.dom.minidom
import traceback
from common import browserClass
browser=browserClass.browser()

class instockorderreportTest(unittest.TestCase):
    u'''报表-进货报表-进货订单统计'''

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


    def test_instockorderReport(self):
        u'''报表-进货报表-进货订单统计'''
        header={'cookie':self.cookiestr,"Content-Type": "application/json"}
        dom = xml.dom.minidom.parse(r'C:\workspace\proxynufeeb.button\reports\reportslocation.xml')
        module=browser.xmlRead(dom,'module',0)
        moduledetail=browser.xmlRead(dom,'moduledetail',0)
        moduledd=browser.xmlRead(dom,'moduledd',0)

        browser.openModule3(self.driver,module,moduledetail,moduledd)

        #页面id
        #pageurl=browser.xmlRead(dom,"fixcapsaleurl",0)
        #pageid=browser.getalertid(pageurl,header)


        try:
            browser.exjscommin(self.driver,"关闭")
            browser.openModule3(self.driver,module,moduledetail,moduledd)
            browser.exjscommin(self.driver,"确定")

            #详情
            browser.exjscommin(self.driver,"详情")
            browser.exjscommin(self.driver,"取消")
            browser.exjscommin(self.driver,"详情")
            browser.exjscommin(self.driver,"确定")

            browser.selectbycon(self.driver,"商品编号",u"中文测试饕餮壹贰123！@#￥%……&*（）()； abc")
            browser.exjscommin(self.driver,"退出")

            #刷新
            browser.refreshbutton(self.driver)

            #筛选
            browser.selectbycon(self.driver,"商品编号")

            #查询条件
            browser.exjscommin(self.driver,"查询条件")
            browser.exjscommin(self.driver,"关闭")
            browser.exjscommin(self.driver,"查询条件")

            js="$(\"input[id$=edBType]\").last().attr(\"id\",\"conid\")"
            browser.delaytime(1)
            browser.excutejs(self.driver,js)
            conid="conid"
            browser.doubleclick(self.driver,conid)
            browser.pagechoice(self.driver)
            browser.exjscommin(self.driver,"关闭")
            browser.doubleclick(self.driver,conid)
            browser.exjscommin(self.driver,"进入下级")
            browser.exjscommin(self.driver,"查看单位基本信息")
            browser.exjscommin(self.driver,"关闭")
            browser.exjscommin(self.driver,"返回上级")


            browser.exjscommin(self.driver,"选择一类")
            browser.doubleclick(self.driver,conid)
            browser.exjscommin(self.driver,"选中")
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
            browser.getpicture(self.driver,filename+u"报表-进货报表-进货订单统计.png")



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
