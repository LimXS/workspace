#*-* coding:UTF-8 *-*
import time
import re
import datetime
import unittest
import  xml.dom.minidom
import traceback
import requests
import json
from common import browserClass
import instockClass
browser=instockClass.instockclass()

class alarmupTest(unittest.TestCase):
    u'''库存-库存报警-库存上限报警表'''

    def setUp(self):
        self.driver=browser.startBrowser('chrome')
        browser.set_up(self.driver)
        cookie = [item["name"] + "=" + item["value"] for item in self.driver.get_cookies()]
        #print cookie
        self.cookiestr = ';'.join(item for item in cookie)

        time.sleep(2)
        pass


    def tearDown(self):
        print "test over"
        self.driver.close()
        pass

    def testalarmUp(self):
        u'''库存-库存报警-库存上限报警表.'''

        dom = xml.dom.minidom.parse(r'C:\workspace\nufeeb.button\instock\instocklocation')

        modulename=browser.xmlRead(dom,"module",0)
        moduledetail=browser.xmlRead(dom,'moduledetail',10)
        moduledd=browser.xmlRead(dom,'moduledd',2)

        browser.openModule3(self.driver,modulename,moduledetail,moduledd)


        try:
            browser.exjscommin(self.driver,"关闭")
            browser.openModule3(self.driver,modulename,moduledetail,moduledd)
            browser.exjscommin(self.driver,"选中")

            #商品分类
            jsclass="$(\"input[id$=classtypeid]\").attr(\"id\",\"classid\")"
            browser.delaytime(1)
            browser.excutejs(self.driver,jsclass)
            browser.doubleclick(self.driver,"classid")
            browser.exjscommin(self.driver,"关闭")
            browser.doubleclick(self.driver,"classid")
            browser.exjscommin(self.driver,"选中")

            #查询
            browser.exjscommin(self.driver,"查询")
            browser.exjscommin(self.driver,"退出")

            browser.openModule3(self.driver,modulename,moduledetail,moduledd)
            browser.exjscommin(self.driver,"全部")

            #删除一行
            browser.exjscommin(self.driver,"删除一行")
            browser.exjscommin(self.driver,"查询")

            #修改数量
            browser.exjscommin(self.driver,"修改数量")
            browser.exjscommin(self.driver,"关闭")
            browser.exjscommin(self.driver,"修改数量")
            jsnum="$(\"input[id$=ednumber]\").attr(\"value\",\"2\")"
            browser.delaytime(1)
            browser.excutejs(self.driver,jsnum)
            browser.exjscommin(self.driver,"确定")

            jszai="$(\"div[class=GridBodyCellText]:contains('x')\").first().attr(\"id\",\"tempid\")"
            browser.delaytime(1)
            browser.excutejs(self.driver,jszai)
            browser.doubleclick(self.driver,"tempid")
            browser.delaytime(1)
            browser.excutejs(self.driver,jsnum)
            browser.exjscommin(self.driver,"确定")


            #商品分布
            browser.exjscommin(self.driver,"商品分布")
            browser.exjscommin(self.driver,"退出")

            #自动生成草稿单据
            browser.exjscommin(self.driver,"自动生成草稿单据")
            browser.exjscommin(self.driver,"退出")
            browser.exjscommin(self.driver,"自动生成草稿单据")
            browser.exjscommin(self.driver,"确定")
            browser.accAlert(self.driver,1)

            #退出
            browser.exjscommin(self.driver,"退出")
            browser.openModule3(self.driver,modulename,moduledetail,moduledd)




        except:
            print traceback.format_exc()
            filename=browser.xmlRead(dom,'filename',0)
            browser.getpicture(self.driver,filename+u"库存-库存报警-库存上限报警表.png")



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
