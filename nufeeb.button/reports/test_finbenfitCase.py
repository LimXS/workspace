#*-* coding:UTF-8 *-*
import unittest
import  xml.dom.minidom
import traceback
import reportsClass
browser=reportsClass.instockclass()

class finbenfitTest(unittest.TestCase):
    u'''报表-财务报表-利润表'''

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


    def test_finBenfit(self):
        u'''报表-财务报表-利润表'''
        dom = xml.dom.minidom.parse(r'C:\workspace\nufeeb.button\reports\reportslocation.xml')
        module=browser.xmlRead(dom,'module',0)
        moduledetail=browser.xmlRead(dom,'moduledetail',3)
        moduledd=browser.xmlRead(dom,'finadd',2)

        browser.openModule3(self.driver,module,moduledetail,moduledd)

        #页面id
        #pageurl=browser.xmlRead(dom,"fixcapsaleurl",0)
        #pageid=browser.getalertid(pageurl,header)

        try:
            #展示级数
            browser.inputid(self.driver,"leveal","3")

            #明细账本
            browser.exjscommin(self.driver,"明细账本")
            browser.accAlert(self.driver,1)
            browser.exjscommin(self.driver,"关闭")

            browser.elementcontains(self.driver,"div","销售收入","saleid")
            browser.findId(self.driver,"saleid").click()

            browser.exjscommin(self.driver,"明细账本")
            browser.exjscommin(self.driver,"关闭")
            browser.exjscommin(self.driver,"明细账本")
            browser.exjscommin(self.driver,"确定")
            browser.delaytime(2)
            browser.know(self.driver)
            browser.exjscommin(self.driver,"查看凭证")
            browser.exjscommin(self.driver,"退出")
            browser.delaytime(2)
            browser.know(self.driver)
            browser.pagechoice(self.driver)
            browser.inputid(self.driver,"edOrder","按单据时间排序")
            browser.inputid(self.driver,"edRedwordFilter","不显示红冲单据")
            browser.exjscommin(self.driver,"退出")

            #每月比较
            browser.exjscommin(self.driver,"每月比较")
            browser.exjscommin(self.driver,"关闭")
            browser.exjscommin(self.driver,"每月比较")
            browser.exjscommin(self.driver,"调整结束日期")
            browser.exjscommin(self.driver,"追加一年会计月")
            browser.accAlert(self.driver,0)
            js="$(\"div:contains('结存')\").attr(\"flagesel\",\"0000\");$(\"div:contains('已结存')\").attr(\"flagesel\",\"1111\");$(\"div[flagesel=0000]\").first().attr(\"id\",\"overokid\")"
            browser.delaytime(1)
            browser.excutejs(self.driver,js)
            browser.findId(self.driver,"overokid").click()
            browser.delaytime(1)
            browser.accAlert(self.driver,1)
            browser.exjscommin(self.driver,"确定")

            #翻页
            browser.pagechoice(self.driver)

            #刷新
            browser.refreshbutton(self.driver)




            browser.exjscommin(self.driver,"退出")
            browser.openModule3(self.driver,module,moduledetail,moduledd)


        except:
            print traceback.format_exc()
            filename=browser.xmlRead(dom,'filename',0)
            #print filename+u"常用-单据草稿.png"
            #browser.getpicture(self.driver,filename+u"notedraft.png")
            browser.getpicture(self.driver,filename+u"报表-财务报表-利润表.png")



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()