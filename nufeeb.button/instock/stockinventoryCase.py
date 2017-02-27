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

class stockinvTest(unittest.TestCase):
    u'''库存-库存盘点'''

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

    def teststockInv(self):
        u'''库存-库存盘点.'''
        header={'cookie':self.cookiestr,"Content-Type": "application/json"}
        comdom=xml.dom.minidom.parse(r'C:\workspace\nufeeb.button\data\commonlocation')
        dom = xml.dom.minidom.parse(r'C:\workspace\nufeeb.button\instock\instocklocation')

        modulename=browser.xmlRead(dom,"module",0)
        moduledetail=browser.xmlRead(dom,'moduledetail',9)

        browser.openModule2(self.driver,modulename,moduledetail)

        #页面id
        pageurl=browser.xmlRead(dom,"invurl",0)
        pageid=browser.getalertid(pageurl,header)
        #print pageid

        #commid,id
        commid=browser.getallcommonid(comdom)


        try:
            #excel导入
            exinputid=pageid+browser.xmlRead(dom,"btnInPut",0)
            browser.delaytime(1)
            browser.findId(self.driver,exinputid).click()
            browser.delaytime(1,self.driver)

            #-盘点仓库
            js="$(\"input[id$=edKType]\").last().attr(\"id\",\"catedblid\")"
            browser.delaytime(1)
            browser.excutejs(self.driver,js)
            browser.passpeoplesel(self.driver,"catedblid")
            browser.exjscommin(self.driver,"开始导入")
            browser.delaytime(1)
            browser.accAlert(self.driver,1)
            browser.exjscommin(self.driver,"关闭")

            #盘点机导入
            machipid=pageid+browser.xmlRead(dom,"btnInPutTxt",0)
            browser.findId(self.driver,machipid).click()
            browser.delaytime(1,self.driver)

            js="$(\"input[id$=edKType]\").last().attr(\"id\",\"catedblid2\")"
            browser.delaytime(1)
            browser.excutejs(self.driver,js)
            browser.passpeoplesel(self.driver,"catedblid2")
            browser.exjscommin(self.driver,"开始导入")
            browser.accAlert(self.driver,1)
            #print "2"
            browser.exjscommin(self.driver,"关闭")

            #查看盘点历史
            js="$(\"div:contains('查看盘点历史')\").last().attr(\"id\",\"hisid\")"
            browser.delaytime(1)
            browser.excutejs(self.driver,js)
            browser.findId(self.driver,"hisid").click()
            browser.delaytime(5,self.driver)
            browser.exjscommin(self.driver,"退出")

            #开始新盘点
            newinvid=pageid+browser.xmlRead(dom,"btnNew",0)
            browser.findId(self.driver,newinvid).click()
            browser.delaytime(1)
            #-仓库选择框
            browser.exjscommin(self.driver,"关闭")
            browser.delaytime(2,self.driver)
            browser.findId(self.driver,newinvid).click()
            browser.delaytime(5,self.driver)
            browser.exjscommin(self.driver,"选中")
            #--选择盘点商品
            browser.exjscommin(self.driver,"关闭")
            browser.findId(self.driver,newinvid).click()
            browser.exjscommin(self.driver,"选中")
            js="$(\"input[id$=edTarget]\").attr(\"id\",\"classid\")"
            browser.delaytime(1)
            browser.excutejs(self.driver,js)
            browser.doubleclick(self.driver,"classid")
            browser.exjscommin(self.driver,"关闭")
            browser.doubleclick(self.driver,"classid")
            browser.exjscommin(self.driver,"选中")
            browser.exjscommin(self.driver,"确定")
            browser.exjscommin(self.driver,"退出")

            browser.findId(self.driver,newinvid).click()
            browser.delaytime(5,self.driver)
            browser.exjscommin(self.driver,"选中")
            browser.delaytime(5,self.driver)
            browser.exjscommin(self.driver,"确定")
            browser.delaytime(5,self.driver)

            #翻页
            browser.pagechoice(self.driver)
            #库存盘点
            #-选择商品
            browser.exjscommin(self.driver,"选择商品")
            browser.exjscommin(self.driver,"关闭")
            browser.exjscommin(self.driver,"选择商品")
            browser.exjscommin(self.driver,"确定")

            #数量
            js="$(\"input[id$=grid_checkqty]\").attr(\"value\",\"1000\")"
            browser.excutejs(self.driver,js)

            #-导出excel
            browser.exjscommin(self.driver,"导出excel")
            #-保存|退出
            browser.exjscommin(self.driver,"保存")
            #print "3"
            browser.accAlert(self.driver,1)
            browser.delaytime(2,self.driver)

            #继续盘点
            js="$(\"div:contains('继续盘点')\").last().attr(\"id\",\"conid\")"
            browser.delaytime(1)
            browser.excutejs(self.driver,js)
            browser.delaytime(1)
            browser.findId(self.driver,"conid").click()
            #print "countions inven"

            #-完成盘点
            browser.exjscommin(self.driver,"完成盘点")
            browser.exjscommin(self.driver,"关闭")
            browser.exjscommin(self.driver,"完成盘点")
            browser.exjscommin(self.driver,"确定")
            #print "4"
            browser.accAlert(self.driver,1)
            browser.delaytime(1)
            browser.exjscommin(self.driver,"退出")
            browser.delaytime(2,self.driver)

            #-打印

            #完成盘点
            browser.exjscommin(self.driver,"开始新盘点")
            browser.exjscommin(self.driver,"选中")
            browser.exjscommin(self.driver,"确定")
            browser.exjscommin(self.driver,"选择商品")
            browser.exjscommin(self.driver,"确定")
            js="$(\"input[id$=grid_checkqty]\").attr(\"value\",\"1000000\")"
            browser.delaytime(1)
            browser.excutejs(self.driver,js)
            browser.exjscommin(self.driver,"保存")
            browser.delaytime(1)
            browser.accAlert(self.driver,1)
            browser.delaytime(1)

            invokid=pageid+browser.xmlRead(dom,"btnBuildDraft",0)
            browser.delaytime(1)
            browser.findId(self.driver,invokid).click()
            browser.delaytime(1)
            browser.exjscommin(self.driver,"关闭")
            browser.findId(self.driver,invokid).click()
            browser.exjscommin(self.driver,"确定")
            browser.delaytime(1)
            browser.accAlert(self.driver,1)
            browser.delaytime(1)

            #删除记录
            delinvid=pageid+browser.xmlRead(dom,"btnDelNew",0)
            browser.delaytime(1)
            browser.findId(self.driver,delinvid).click()
            browser.delaytime(2)

            browser.accAlert(self.driver,0)
            browser.delaytime(2)
            browser.findId(self.driver,delinvid).click()
            browser.delaytime(2)
            browser.accAlert(self.driver,1)

            #仓库选择
            cateid=pageid+browser.xmlRead(dom,'edKType',0)
            browser.delaytime(1)
            browser.peoplesel(self.driver,cateid)

            #盘点人
            peoid=pageid+browser.xmlRead(dom,'edEType',0)
            browser.delaytime(1)
            browser.peoplesel(self.driver,peoid,1)

            #查询
            browser.exjscommin(self.driver,"查询")

            #退出
            browser.exjscommin(self.driver,"退出")
            browser.openModule2(self.driver,modulename,moduledetail)

        except:
            print traceback.format_exc()
            filename=browser.xmlRead(dom,'filename',0)
            browser.delaytime(1)
            browser.getpicture(self.driver,filename+u"库存-库存盘点.png")



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
