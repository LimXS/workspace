#*-* coding:UTF-8 *-*
import unittest
import  xml.dom.minidom
import traceback
import reportsClass
browser=reportsClass.instockclass()

class comsalereturnTest(unittest.TestCase):
    u'''报表-往来单位业务分析-单位销售/退货统计'''

    def setUp(self):
        self.driver=browser.startBrowser('chrome')
        browser.set_up(self.driver)
        browser.delaytime(1)
        pass


    def tearDown(self):
        print "test over"
        self.driver.close()
        pass


    def test_comiSalereturn(self):
        u'''报表-往来单位业务分析-单位销售/退货统计'''
        dom = xml.dom.minidom.parse(r'C:\workspace\nufeeb.button\reports\reportslocation.xml')
        module=browser.xmlRead(dom,'module',0)
        moduledetail=browser.xmlRead(dom,'moduledetail',4)
        moduledd=browser.xmlRead(dom,'comadd',2)

        browser.openModule3(self.driver,module,moduledetail,moduledd)

        try:
            browser.exjscommin(self.driver,"关闭")
            browser.openModule3(self.driver,module,moduledetail,moduledd)
            browser.exjscommin(self.driver,"确定")

            #明细账本
            browser.exjscommin(self.driver,"明细账本")
            browser.exjscommin(self.driver,"查看单据")
            browser.exjscommin(self.driver,"退出")
            browser.pagechoice(self.driver)
            browser.inputid(self.driver,"filterRed","不显示红冲数据")
            browser.selectbycon(self.driver,"单据编号","LS")
            browser.exjscommin(self.driver,"退出")

            #列表
            browser.exjscommin(self.driver,"列表")
            browser.exjscommin(self.driver,"取消")
            browser.exjscommin(self.driver,"列表")
            browser.exjscommin(self.driver,"确定")
            browser.exjscommin(self.driver,"明细账本")
            browser.exjscommin(self.driver,"查看单据")
            browser.exjscommin(self.driver,"退出")
            browser.pagechoice(self.driver)
            browser.inputid(self.driver,"filterRed","不显示红冲数据")
            browser.selectbycon(self.driver,"单据编号","LS")
            browser.exjscommin(self.driver,"退出")
            browser.exjscommin(self.driver,"退出")

            #过滤
            browser.inputid(self.driver,"edZeroShowType","全部显示")

            #翻页
            browser.pagechoice(self.driver)

            #查询条件
            browser.selothersavecon(self.driver)
            browser.selcomcaitpeo(self.driver)

            #筛选
            browser.selectbycon(self.driver,"单位名称","2")

            #刷新
            browser.refreshbutton(self.driver)

            browser.exjscommin(self.driver,"退出")
            browser.openModule3(self.driver,module,moduledetail,moduledd)


        except:
            print traceback.format_exc()
            filename=browser.xmlRead(dom,'filename',0)
            #print filename+u"常用-单据草稿.png"
            #browser.getpicture(self.driver,filename+u"notedraft.png")
            browser.getpicture(self.driver,filename+"报表-往来单位业务分析-单位销售退货统计.png")



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()