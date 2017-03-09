#*-* coding:UTF-8 *-*
import unittest
import  xml.dom.minidom
import traceback
from common import browserClass
browser=browserClass.browser()

class endmanageTest(unittest.TestCase):
    u'''财务-期末管理-年结存信息表.'''

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


    def test_endManage(self):
        u'''财务-期末管理-年结存信息表'''
        dom = xml.dom.minidom.parse(r'C:\workspace\nufeeb.button\finance\financelocation')
        module=browser.xmlRead(dom,'module',0)
        moduledetail=browser.xmlRead(dom,'moduledetail',10)
        moduledd=browser.xmlRead(dom,'moduledd',10)

        browser.openModule3(self.driver,module,moduledetail,moduledd)


        try:

            browser.accAlert(self.driver,1)
            browser.exjscommin(self.driver,"查看历史账套")
            browser.exjscommin(self.driver,"修改账套名称")
            browser.exjscommin(self.driver,"关闭")
            browser.openModule3(self.driver,module,moduledetail,moduledd)

        except:
            print traceback.format_exc()
            filename=browser.xmlRead(dom,'filename',0)
            #print filename+u"常用-单据草稿.png"
            #browser.getpicture(self.driver,filename+u"notedraft.png")
            browser.getpicture(self.driver,filename+u"财务-期末管理-年结存信息表.png")



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
