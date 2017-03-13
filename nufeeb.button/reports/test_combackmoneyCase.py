#*-* coding:UTF-8 *-*
import unittest
import  xml.dom.minidom
import traceback
import reportsClass
browser=reportsClass.instockclass()

class combackmoneyTest(unittest.TestCase):
    u'''报表-往来单位业务分析-往来单位回款统计'''

    def setUp(self):
        self.driver=browser.startBrowser('chrome')
        browser.set_up(self.driver)
        browser.delaytime(1)
        pass


    def tearDown(self):
        print "test over"
        self.driver.close()
        pass


    def test_comBackmoney(self):
        u'''报表-往来单位业务分析-往来单位回款统计'''
        dom = xml.dom.minidom.parse(r'C:\workspace\nufeeb.button\reports\reportslocation.xml')
        module=browser.xmlRead(dom,'module',0)
        moduledetail=browser.xmlRead(dom,'moduledetail',4)
        moduledd=browser.xmlRead(dom,'comadd',3)

        browser.openModule3(self.driver,module,moduledetail,moduledd)

        try:
            browser.exjscommin(self.driver,"关闭")
            browser.openModule3(self.driver,module,moduledetail,moduledd)
            browser.exjscommin(self.driver,"确定")

            browser.elementcontains(self.driver,"div","网店客户","companyid")
            browser.findId(self.driver,"companyid").click()

            #回款详情
            browser.exjscommin(self.driver,"回款详情")
            browser.exjscommin(self.driver,"明细账本")
            browser.exjscommin(self.driver,"关闭")
            browser.exjscommin(self.driver,"明细账本")
            browser.exjscommin(self.driver,"确定")
            browser.exjscommin(self.driver,"查看凭证")
            browser.exjscommin(self.driver,"退出")
            browser.pagechoice(self.driver)
            browser.exjscommin(self.driver,"退出")
            browser.exjscommin(self.driver,"退出")

            #回款明细账本
            browser.exjscommin(self.driver,"回款明细账本")
            browser.exjscommin(self.driver,"关闭")
            browser.exjscommin(self.driver,"回款明细账本")
            browser.exjscommin(self.driver,"确定")
            browser.delaytime(2)
            browser.know(self.driver)
            browser.exjscommin(self.driver,"查看凭证")
            browser.exjscommin(self.driver,"退出")
            browser.pagechoice(self.driver)
            browser.exjscommin(self.driver,"退出")

            #翻页
            browser.pagechoice(self.driver)

            #筛选
            browser.selectbycon(self.driver,"单位名称","2")

            #刷新
            browser.refreshbutton(self.driver)

            #条件查询
            browser.exjscommin(self.driver,"条件查询")
            browser.exjscommin(self.driver,"关闭")
            browser.exjscommin(self.driver,"条件查询")
            browser.exjscommin(self.driver,"确定")

            browser.exjscommin(self.driver,"退出")
            browser.openModule3(self.driver,module,moduledetail,moduledd)


        except:
            print traceback.format_exc()
            filename=browser.xmlRead(dom,'filename',0)
            #print filename+u"常用-单据草稿.png"
            #browser.getpicture(self.driver,filename+u"notedraft.png")
            browser.getpicture(self.driver,filename+u"报表-往来单位业务分析-往来单位回款统计.png")



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()