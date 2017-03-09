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

class gatherstockTest(unittest.TestCase):
    u'''库存-汇总备货'''

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

    def testgatherStock(self):
        u'''库存-汇总备货.'''
        header={'cookie':self.cookiestr,"Content-Type": "application/json"}
        dom = xml.dom.minidom.parse(r'C:\workspace\nufeeb.button\instock\instocklocation')

        modulename=browser.xmlRead(dom,"module",0)
        moduledetail=browser.xmlRead(dom,'moduledetail',8)

        browser.openModule2(self.driver,modulename,moduledetail)

        #页面id
        pageurl=browser.xmlRead(dom,"gatherurl",0)
        pageid=browser.getalertid(pageurl,header)
        #print pageid

        try:

            #时间
            starttime=pageid+browser.xmlRead(dom,"startime",0)
            browser.findId(self.driver,starttime).clear()
            browser.delaytime(1)
            browser.findId(self.driver,starttime).send_keys("2017-01-01 00:00:00")
            endtime=pageid+browser.xmlRead(dom,"endtime",0)
            browser.findId(self.driver,endtime).clear()
            browser.findId(self.driver,endtime).send_keys("2017-01-20 23:59:59")
            browser.know(self.driver)
            browser.exjscommin(self.driver,"今天")

            #库存状态
            catestate=pageid+browser.xmlRead(dom,"c_hasgoodsqty",0)
            #print catestate
            browser.delaytime(1)
            browser.delaytime(1)
            browser.doubleclick(self.driver,catestate)
            js="$(\"div:contains('全部')\").last().attr(\"id\",\"allid\")"
            browser.delaytime(1)
            browser.excutejs(self.driver,js)
            browser.findId(self.driver,"allid").click()



            #查询
            browser.exjscommin(self.driver,"查询")

            #数量
            qtyid=pageid+browser.xmlRead(dom,"needqty",0)
            browser.findId(self.driver,qtyid).send_keys("2")

            #配置剩余库存
            jslast="$(\"td[nowrap=true]:contains('配置剩余库存')\").click()"
            browser.excutejs(self.driver,jslast)
            browser.exjscommin(self.driver,"取消")
            browser.excutejs(self.driver,jslast)
            browser.exjscommin(self.driver,"确定")

            #生成单据
            jsbill="$(\"td[nowrap=true]:contains('生成单据')\").click()"
            browser.excutejs(self.driver,jsbill)

            #-生成进货订单
            browser.findId(self.driver,qtyid).send_keys("2")
            js="$(\"td[class=MenuCaption]:contains('进货订单')\").click()"
            browser.excutejs(self.driver,js)
            browser.exjscommin(self.driver,"确")

            #-进货入库单草稿
            #browser.findId(self.driver,qtyid).send_keys("2")
            browser.excutejs(self.driver,jsbill)
            js="$(\"td[class=MenuCaption]:contains('进货入库单草稿')\").click()"
            browser.excutejs(self.driver,js)
            browser.exjscommin(self.driver,"确")

            #-调拨单草稿
            #browser.findId(self.driver,qtyid).send_keys("2")
            browser.excutejs(self.driver,jsbill)
            js="$(\"td[class=MenuCaption]:contains('调拨单草稿')\").click()"
            browser.excutejs(self.driver,js)
            browser.exjscommin(self.driver,"确")

            #保存退出
            browser.exjscommin(self.driver,"退出")
            browser.openModule2(self.driver,modulename,moduledetail)

        except:
            print traceback.format_exc()
            filename=browser.xmlRead(dom,'filename',0)
            #print filename+u"常用-单据草稿.png"
            #browser.getpicture(self.driver,filename+u"notedraft.png")
            browser.getpicture(self.driver,filename+u"库存-汇总备货.png")



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
