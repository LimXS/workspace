#*-* coding:UTF-8 *-*
import unittest
import  xml.dom.minidom
import traceback
import reportsClass
browser=reportsClass.instockclass()

class cominstockTest(unittest.TestCase):
    u'''报表-往来单位业务分析-单位进货统计'''

    def setUp(self):
        self.driver=browser.startBrowser('chrome')
        browser.set_up(self.driver)
        browser.delaytime(1)
        pass


    def tearDown(self):
        print "test over"
        self.driver.close()
        pass


    def test_comiInstock(self):
        u'''报表-往来单位业务分析-单位进货统计'''
        dom = xml.dom.minidom.parse(r'C:\workspace\proxynufeeb.button\reports\reportslocation.xml')
        module=browser.xmlRead(dom,'module',0)
        moduledetail=browser.xmlRead(dom,'moduledetail',4)
        moduledd=browser.xmlRead(dom,'comadd',0)

        browser.openModule3(self.driver,module,moduledetail,moduledd)

        try:
            browser.exjscommin(self.driver,"关闭")
            browser.openModule3(self.driver,module,moduledetail,moduledd)
            browser.exjscommin(self.driver,"确定")

            #列表
            browser.exjscommin(self.driver,"列表",1)
            browser.exjscommin(self.driver,"取消")
            browser.exjscommin(self.driver,"列表",1)
            browser.exjscommin(self.driver,"确定")
            browser.exjscommin(self.driver,"明细账本")
            browser.exjscommin(self.driver,"查看单据")
            browser.exjscommin(self.driver,"退出")
            browser.pagechoice(self.driver)
            browser.inputid(self.driver,"filterRed","不显示红冲数据")
            browser.selectbycon(self.driver,"单据编号",u"中文测试饕餮壹贰123！@#￥%……&*（）()； abc")
            browser.exjscommin(self.driver,"退出")
            browser.exjscommin(self.driver,"退出")

            #明细账本
            browser.exjscommin(self.driver,"明细账本")
            browser.exjscommin(self.driver,"查看单据")
            browser.exjscommin(self.driver,"退出")
            browser.pagechoice(self.driver)
            browser.inputid(self.driver,"filterRed","不显示红冲数据")
            browser.selectbycon(self.driver,"单据编号",u"中文测试饕餮壹贰123！@#￥%……&*（）()； abc")
            browser.exjscommin(self.driver,"退出")

            #筛选
            browser.selectbycon(self.driver,"单位名称","22")

            #刷新
            browser.refreshbutton(self.driver)

            #查询条件
            browser.selothersavecon(self.driver)
            browser.selcomcaitpeo(self.driver)

            browser.exjscommin(self.driver,"退出")
            browser.openModule3(self.driver,module,moduledetail,moduledd)


        except:
            print traceback.format_exc()
            filename=browser.xmlRead(dom,'filename',0)
            browser.delaytime(1)
            browser.getpicture(self.driver,filename+u"报表-往来单位业务分析-单位进货统计.png")



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()