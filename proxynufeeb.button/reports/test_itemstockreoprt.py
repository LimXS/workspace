#*-* coding:UTF-8 *-*
import unittest
import  xml.dom.minidom
import traceback
from common import browserClass
import reportsClass
browser=reportsClass.instockclass()

class itemstockreoportTest(unittest.TestCase):
    u'''报表-进货报表-商品进货/退货统计'''

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


    def test_iteminstockReport(self):
        u'''报表-进货报表-商品进货/退货统计'''
        header={'cookie':self.cookiestr,"Content-Type": "application/json"}
        dom = xml.dom.minidom.parse(r'C:\workspace\proxynufeeb.button\reports\reportslocation.xml')
        module=browser.xmlRead(dom,'module',0)
        moduledetail=browser.xmlRead(dom,'moduledetail',0)
        moduledd=browser.xmlRead(dom,'moduledd',1)

        browser.openModule3(self.driver,module,moduledetail,moduledd)

        #页面id
        #pageurl=browser.xmlRead(dom,"fixcapsaleurl",0)
        #pageid=browser.getalertid(pageurl,header)




        try:
            browser.exjscommin(self.driver,"关闭")
            browser.openModule3(self.driver,module,moduledetail,moduledd)
            browser.exjscommin(self.driver,"确定")

            #明细账本
            browser.exjscommin(self.driver,"明细账本")
            browser.pagechoice(self.driver)
            browser.exjscommin(self.driver,"查看单据")
            browser.exjscommin(self.driver,"退出")
            browser.exjscommin(self.driver,"退出")

            #列表
            browser.exjscommin(self.driver,"列表")
            browser.exjscommin(self.driver,"取消")
            browser.exjscommin(self.driver,"列表")
            browser.exjscommin(self.driver,"确定")
            browser.exjscommin(self.driver,"明细账本")
            browser.pagechoice(self.driver)
            browser.exjscommin(self.driver,"查看单据")
            browser.exjscommin(self.driver,"退出")
            browser.exjscommin(self.driver,"退出")
            browser.exjscommin(self.driver,"每月比较")
            browser.exjscommin(self.driver,"取消")
            browser.exjscommin(self.driver,"每月比较")
            browser.exjscommin(self.driver,"确定")
            browser.exjscommin(self.driver,"图形比较")
            browser.exjscommin(self.driver,"退出")
            browser.exjscommin(self.driver,"退出")
            browser.selectbycon(self.driver,"商品编号")
            browser.exjscommin(self.driver,"退出")


            #每月比较
            browser.exjscommin(self.driver,"每月比较")
            browser.exjscommin(self.driver,"取消")
            browser.exjscommin(self.driver,"每月比较")
            browser.exjscommin(self.driver,"确定")
            browser.exjscommin(self.driver,"图形比较")
            browser.exjscommin(self.driver,"退出")
            browser.exjscommin(self.driver,"退出")

            #价格分析
            browser.exjscommin(self.driver,"价格分析")
            browser.exjscommin(self.driver,"关闭")

            #查询条件
            browser.exjscommin(self.driver,"查询条件")
            browser.exjscommin(self.driver,"关闭")
            browser.exjscommin(self.driver,"查询条件")
            browser.exjscommin(self.driver,"另存为")
            browser.exjscommin(self.driver,"取消")
            browser.exjscommin(self.driver,"另存为")
            js="$(\"input[id$=txtconfigname]\").last().val('solution"+str(browser.getrandnumber())+"')"
            browser.delaytime(1)
            browser.excutejs(self.driver,js)
            browser.exjscommin(self.driver,"确定")
            browser.exjscommin(self.driver,"删除")

            js="$(\"input[id$=edEType]\").last().attr(\"id\",\"peoid\");$(\"input[id$=edKType]\").last().attr(\"id\",\"cateid\")"
            js2="$(\"input[id$=edPType]\").last().attr(\"id\",\"itemid\");$(\"input[id$=edBType]\").last().attr(\"id\",\"comid\")"
            browser.delaytime(1)
            browser.excutejs(self.driver,js)
            browser.excutejs(self.driver,js2)

            #-商品
            browser.selconitem(self.driver,"itemid")

            #-往来单位
            browser.selcompany(self.driver,"comid")

            #-内部职员
            browser.passpeoplesel(self.driver,"peoid")

            #-仓库
            browser.passpeoplesel(self.driver,"cateid")

            browser.exjscommin(self.driver,"确定")


            #筛选
            browser.selectbycon(self.driver,"商品编号",u"中文测试饕餮壹贰123！@#￥%……&*（）()； abc")

            #刷新
            browser.refreshbutton(self.driver)

            #退出
            browser.exjscommin(self.driver,"退出")
            browser.openModule3(self.driver,module,moduledetail,moduledd)




        except:
            print traceback.format_exc()
            filename=browser.xmlRead(dom,'filename',0)
            browser.delaytime(1)
            #print filename+u"常用-单据草稿.png"
            #browser.getpicture(self.driver,filename+u"notedraft.png")
            browser.getpicture(self.driver,filename+"报表-进货报表-商品进货退货统计.png")



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
