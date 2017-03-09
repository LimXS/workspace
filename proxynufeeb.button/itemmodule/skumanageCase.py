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
browser=browserClass.browser()

class skumanageTest(unittest.TestCase):
    u'''商品-SKU管理'''

    def setUp(self):
        self.driver=browser.startBrowser('chrome')
        browser.set_up(self.driver)
        cookie = [item["name"] + "=" + item["value"] for item in self.driver.get_cookies()]
        #print cookie
        self.cookiestr = ';'.join(item for item in cookie)

        browser.delaytime(2)
        pass


    def tearDown(self):
        print "test over"
        self.driver.close()
        pass



    def testskuManage(self):
        u'''商品-SKU管理'''
        header={'cookie':self.cookiestr,"Content-Type": "application/json"}
        dom = xml.dom.minidom.parse(r'C:\workspace\proxynufeeb.button\itemmodule\itemlocation')
        modulename=browser.xmlRead(dom,"module",0)
        moduledetail=browser.xmlRead(dom,'moduledetail',1)

        browser.openModule2(self.driver,modulename,moduledetail)
        browser.delaytime(1)
        cookies=browser.cookieSave(self.driver)
        header3={'cookie':cookies,"Content-Type": "application/json"}
        header4={'cookie':cookies,"Content-Type": "application/x-www-form-urlencoded"}

        #页面id
        pageurl=browser.xmlRead(dom,"skuurl",0)
        pageid=browser.halfid(pageurl,header)
        #print pageid

        #commid
        commid=browser.getcommonid(dom)

        try:
            skuexit=pageid+commid["btnClose"]

            #商品选择
            skuitemsel=browser.xmlRead(dom,"skuitemsel",0)
            itemsel=pageid+skuitemsel
            browser.findId(self.driver,itemsel).click()

            #print itselaltid
            #翻页
            browser.pagechoice(self.driver)
            #关闭
            browser.exjscommin(self.driver,"关闭")

            #选中
            browser.findId(self.driver,itemsel).click()
            browser.exjscommin(self.driver,"选中",1)
            #选中关闭
            browser.exjscommin(self.driver,"选中并关闭")

            #全部选中
            browser.exjscommin(self.driver,"全部选中")
            browser.exjscommin(self.driver,"全部取消")

            #条码打印设置
            prcodeset=browser.xmlRead(dom,"prcodeset",0)
            #browser.findId(self.driver,pageid+prcodeset).click()

            #条码打印
            selitem=browser.xmlRead(dom,"selitem",0)
            browser.findXpath(self.driver,commid["basetype"]+pageid+selitem).click()
            #codeprint=browser.xmlRead(dom,"codeprint",0)
            browser.exjscommin(self.driver,"条码打印")

            #关闭
            browser.exjscommin(self.driver,"关闭")

            #确认
            #browser.exjscommin(self.driver,"条码打印")
            #browser.exjscommin(self.driver,"确定")


            #导入商品条码
            btnImport=browser.xmlRead(dom,"btnImport",0)
            browser.delaytime(1)
            #print pageid+btnImport
            browser.findId(self.driver,pageid+btnImport).click()

            js1="$(\"div[class=TabTopCaptionText]:contains('导入过程')\").attr(\"id\",\"improid\")"
            js2="$(\"div[class=TabTopCaptionText]:contains('设置字段对应')\").attr(\"id\",\"setid\")"
            browser.delaytime(1)
            browser.excutejs(self.driver,js1)
            browser.excutejs(self.driver,js2)
            browser.findId(self.driver,"improid").click()
            browser.findId(self.driver,"setid").click()
            js="$(\"input[id$=grid_exfield_exfield]\").attr(\"id\",\"selqote\")"
            browser.delaytime(1)
            browser.excutejs(self.driver,js)
            browser.doubleclick(self.driver,"selqote")
            browser.exjscommin(self.driver,"关闭")
            browser.doubleclick(self.driver,"selqote")
            browser.exjscommin(self.driver,"选中")
            browser.exjscommin(self.driver,"导入")
            browser.accAlert(self.driver,1)
            browser.exjscommin(self.driver,"关闭")


            #淘宝商品补码
            #browser.findId(self.driver,itemselall).click()

            btnUpload=browser.xmlRead(dom,"btnUpload",0)
            #print pageid+btnUpload
            browser.findId(self.driver,pageid+btnUpload).click()
            browser.accAlert(self.driver,0)
            browser.findId(self.driver,pageid+btnUpload).click()
            browser.accAlert(self.driver,1)
            browser.delaytime(1)
            browser.accAlert(self.driver,1)

            #SKU编号规则设置
            browser.exjscommin(self.driver,"SKU编号规则设置")
            browser.exjscommin(self.driver,"下移")
            browser.exjscommin(self.driver,"上移")
            browser.exjscommin(self.driver,"全部生成")
            browser.accAlert(self.driver,1)
            browser.exjscommin(self.driver,"选中生成")
            browser.accAlert(self.driver,1)
            js="$(\"div:contains('生成过程')\").last().attr(\"id\",\"picmanid\")"
            browser.delaytime(1)
            browser.excutejs(self.driver,js)
            browser.findId(self.driver,"picmanid").click()
            js="$(\"div:contains('编辑规则')\").last().attr(\"id\",\"editid\")"
            browser.delaytime(1)
            browser.excutejs(self.driver,js)
            browser.findId(self.driver,"editid").click()


            browser.exjscommin(self.driver,"关闭")

            #退出
            #print ruleclose
            browser.exjscommin(self.driver,"退出")
            browser.openModule2(self.driver,modulename,moduledetail)

            #翻页
            browser.pagechoice(self.driver)

            #查询
            js="$(\"input[id$=pusercodetxt]\").val('a1');"
            browser.delaytime(1)
            browser.excutejs(self.driver,js)
            browser.exjscommin(self.driver,"查询")
            browser.exjscommin(self.driver,"退出")

            browser.openModule2(self.driver,modulename,moduledetail)
        except:
            print traceback.format_exc()
            filename=browser.xmlRead(dom,'filename',0)
            #print filename+u"常用-单据草稿.png"
            #browser.getpicture(self.driver,filename+u"notedraft.png")
            browser.getpicture(self.driver,filename+u"商品-SKU管理.png")



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
