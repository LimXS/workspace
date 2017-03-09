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

class alarmsetTest(unittest.TestCase):
    u'''库存-库存报警-库存报警设置'''

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

    def testalarmSet(self):
        u'''库存-库存报警-库存报警设置.'''
        header={'cookie':self.cookiestr,"Content-Type": "application/json"}
        comdom=xml.dom.minidom.parse(r'C:\workspace\proxynufeeb.button\data\commonlocation')
        dom = xml.dom.minidom.parse(r'C:\workspace\proxynufeeb.button\instock\instocklocation')

        modulename=browser.xmlRead(dom,"module",0)
        moduledetail=browser.xmlRead(dom,'moduledetail',10)
        moduledd=browser.xmlRead(dom,'moduledd',1)

        browser.openModule3(self.driver,modulename,moduledetail,moduledd)
        cookies=browser.cookieSave(self.driver)


        #页面id
        #pageurl=browser.xmlRead(dom,"chprurl",0)
        #pageid=browser.getalertid(pageurl,header)
        #print pageid

        #commid,id
        commid=browser.getallcommonid(comdom)


        try:
            browser.exjscommin(self.driver,"关闭")
            browser.openModule3(self.driver,modulename,moduledetail,moduledd)
            #-商品分类框
            jsit="$(\"input[id$=edTarget]\").attr(\"id\",\"itid\")"
            browser.delaytime(1)
            browser.excutejs(self.driver,jsit)
            browser.doubleclick(self.driver,"itid")
            browser.exjscommin(self.driver,"关闭")
            browser.doubleclick(self.driver,"itid")
            browser.exjscommin(self.driver,"选中")

            browser.exjscommin(self.driver,"确定")
            browser.exjscommin(self.driver,"退出")

            browser.openModule3(self.driver,modulename,moduledetail,moduledd)
            browser.exjscommin(self.driver,"确定")

            #商品上下限报警量设置【全部库存】
            #翻页
            browser.pagechoice(self.driver)
            #查询条件
            browser.exjscommin(self.driver,"查询条件")
            browser.exjscommin(self.driver,"确定")

            #设置合计仓库上下限
            browser.exjscommin(self.driver,"设置合计仓库上下限")
            browser.exjscommin(self.driver,"退出")
            browser.exjscommin(self.driver,"设置合计仓库上下限")
            jsup="$(\"input[id$=warnup]\").val(\"500\")"
            jsdown="$(\"input[id$=warndown]\").attr(\"value\",\"200\")"
            browser.delaytime(1)
            browser.excutejs(self.driver,jsup)
            browser.excutejs(self.driver,jsdown)
            browser.exjscommin(self.driver,"确定")

            #设置每个仓库上下限
            browser.exjscommin(self.driver,"设置每个仓库上下限")
            browser.exjscommin(self.driver,"退出")
            browser.exjscommin(self.driver,"设置每个仓库上下限")
            browser.exjscommin(self.driver,"设置上下限量")
            browser.exjscommin(self.driver,"退出")
            browser.exjscommin(self.driver,"设置上下限量")
            jsup="$(\"input[id$=warnup]\").val(\"300\")"
            jsdown="$(\"input[id$=warndown]\").attr(\"value\",\"100\")"
            browser.delaytime(1)
            browser.excutejs(self.driver,jsup)
            browser.excutejs(self.driver,jsdown)
            browser.exjscommin(self.driver,"确定")
            jszai="$(\"div[class=GridBodyCellText]:contains('在途仓库')\").attr(\"id\",\"tempid\")"
            browser.delaytime(1)
            browser.excutejs(self.driver,jszai)
            browser.findId(self.driver,"tempid").click()
            browser.doubleclick(self.driver,"tempid")
            browser.exjscommin(self.driver,"确定")
            browser.delaytime(2,self.driver)
            browser.exjscommin(self.driver,"设置为所有仓库合计值")
            browser.accAlert(self.driver,0)
            browser.exjscommin(self.driver,"设置为所有仓库合计值")
            browser.accAlert(self.driver,1)
            browser.exjscommin(self.driver,"退出")

            #退出
            browser.exjscommin(self.driver,"退出")
            browser.openModule3(self.driver,modulename,moduledetail,moduledd)
            browser.exjscommin(self.driver,"确定")




        except:
            print traceback.format_exc()
            filename=browser.xmlRead(dom,'filename',0)
            browser.getpicture(self.driver,filename+u"库存-库存报警-库存报警设置.png")



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
