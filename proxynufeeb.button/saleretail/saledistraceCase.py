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

class saledistraceTest(unittest.TestCase):
    u'''批零-价格折扣跟踪'''

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


    def testsaledisTrace(self):
        u'''批零-价格折扣跟踪'''
        header={'cookie':self.cookiestr,"Content-Type": "application/json"}
        comdom=xml.dom.minidom.parse(r'C:\workspace\proxynufeeb.button\data\commonlocation')
        dom = xml.dom.minidom.parse(r'C:\workspace\proxynufeeb.button\saleretail\salelocation')

        modulename=browser.xmlRead(dom,"module",0)
        moduledetail=browser.xmlRead(dom,'moduledetail',11)


        browser.openModule2(self.driver,modulename,moduledetail)


        #commid,id
        commid=browser.getallcommonid(comdom)
        #id=browser.getcommonid(dom)

        try:
            browser.exjscommin(self.driver,"关闭")
            browser.openModule2(self.driver,modulename,moduledetail)
            browser.exjscommin(self.driver,"确定")



            js="$(\"button:contains('新增')\").attr(\"id\",\"addbutton\")"
            jsdel="$(\"button:contains('删除')\").attr(\"id\",\"delbutton\")"
            browser.delaytime(1)
            browser.excutejs(self.driver,js)
            browser.excutejs(self.driver,jsdel)

            #新增
            browser.findId(self.driver,"addbutton").click()
            browser.exjscommin(self.driver,"查看单位基本信息")
            browser.exjscommin(self.driver,"关闭")
            browser.pagechoice(self.driver)
            browser.exjscommin(self.driver,"关闭")
            browser.findId(self.driver,"addbutton").click()
            browser.exjscommin(self.driver,"选中")
            browser.pagechoice(self.driver)
            browser.exjscommin(self.driver,"选中")

            #修改
            browser.exjscommin(self.driver,"修改")
            browser.exjscommin(self.driver,"退出")
            browser.exjscommin(self.driver,"修改")
            js="$(\"input[id$=edSaleDiscount]\").val('0.99')"
            browser.delaytime(1)
            browser.excutejs(self.driver,js)
            browser.exjscommin(self.driver,"确定")

            #删除
            browser.findId(self.driver,"addbutton").click()
            browser.exjscommin(self.driver,"选中")
            browser.exjscommin(self.driver,"选中")
            browser.delaytime(1)

            del1="$(\"td[class=MenuCaption]:contains(删除指定商品)\").click()"
            del2="$(\"td[class=MenuCaption]:contains(删除指定单位)\").click()"
            del3="$(\"td[class=MenuCaption]:contains(删除已选择)\").click()"
            del4="$(\"td[class=MenuCaption]:contains(删除全部)\").click()"
            browser.delaytime(1)

            #-删除指定商品
            browser.findId(self.driver,"delbutton").click()
            browser.delaytime(1)
            browser.excutejs(self.driver,del1)
            browser.exjscommin(self.driver,"选中")
            browser.accAlert(self.driver,1)

            #-删除指定单位
            browser.findId(self.driver,"addbutton").click()
            browser.exjscommin(self.driver,"选中")
            browser.exjscommin(self.driver,"选中")
            browser.delaytime(2)

            browser.findId(self.driver,"delbutton").click()
            browser.delaytime(1)
            browser.excutejs(self.driver,del2)
            browser.exjscommin(self.driver,"选中")
            browser.accAlert(self.driver,1)

            #-删除已选择
            browser.findId(self.driver,"addbutton").click()
            browser.exjscommin(self.driver,"选中")
            browser.exjscommin(self.driver,"选中")
            browser.delaytime(2,self.driver)

            check="$(\"input[type=checkbox]\").eq(3).click()"
            browser.delaytime(1)
            browser.excutejs(self.driver,check)
            browser.delaytime(1)

            browser.findId(self.driver,"delbutton").click()
            browser.delaytime(1)
            browser.excutejs(self.driver,del3)
            browser.accAlert(self.driver,1)

            #删除全部
            browser.findId(self.driver,"addbutton").click()
            browser.exjscommin(self.driver,"选中")
            browser.exjscommin(self.driver,"选中")
            browser.delaytime(1)

            browser.findId(self.driver,"delbutton").click()
            browser.delaytime(1)
            browser.excutejs(self.driver,del4)
            browser.accAlert(self.driver,1)

            for a in range(0,2):
                browser.findId(self.driver,"addbutton").click()
                browser.exjscommin(self.driver,"选中")
                browser.exjscommin(self.driver,"选中")
                browser.delaytime(1)


            #清除标记
            jscheckone="$(\"input[type=checkbox]\").eq(3).click()"
            browser.delaytime(1)
            browser.excutejs(self.driver,jscheckone)
            browser.exjscommin(self.driver,"清除标记")

            #批量修改
            jschecktwo="$(\"input[type=checkbox]\").eq(4).click()"
            jscheckone="$(\"input[type=checkbox]\").eq(3).click()"
            browser.delaytime(1)
            browser.excutejs(self.driver,jschecktwo)
            browser.excutejs(self.driver,jscheckone)
            browser.exjscommin(self.driver,"批量修改")
            browser.exjscommin(self.driver,"取消")
            browser.exjscommin(self.driver,"批量修改")
            addprice="$(\"input[id$=txtSaleprice]\").val(12)"
            pricejs="$(\"input[id$=edSaleprice]\").attr(\"id\",\"salepriceid\")"
            jssel="$(\"div:contains('零售价')\").last().attr(\"id\",\"selitempr\")"
            browser.delaytime(1)
            browser.excutejs(self.driver,pricejs)
            browser.doubleclick(self.driver,"salepriceid")
            browser.excutejs(self.driver,jssel)
            browser.delaytime(1)
            browser.findId(self.driver,"selitempr").click()
            browser.excutejs(self.driver,addprice)
            browser.exjscommin(self.driver,"确定")


            #查询
            browser.exjscommin(self.driver,"查询")
            browser.exjscommin(self.driver,"关闭")
            browser.exjscommin(self.driver,"查询")
            js="$(\"input[id$=edPType]\").attr(\"id\",\"itemsel\")"
            js2="$(\"input[id$=edBType]\").attr(\"id\",\"comsel\")"
            browser.delaytime(1)
            browser.excutejs(self.driver,js)
            browser.excutejs(self.driver,js2)
            browser.doubleclick(self.driver,"itemsel")
            browser.pagechoice(self.driver)
            browser.exjscommin(self.driver,"关闭")
            browser.doubleclick(self.driver,"itemsel")
            browser.exjscommin(self.driver,"全部")
            browser.doubleclick(self.driver,"itemsel")
            browser.exjscommin(self.driver,"选中")
            browser.doubleclick(self.driver,"itemsel")
            browser.exjscommin(self.driver,"选择一类")

            browser.doubleclick(self.driver,"itemsel")
            browser.exjscommin(self.driver,"选择一类")
            browser.doubleclick(self.driver,"itemsel")
            browser.pagechoice(self.driver)
            browser.exjscommin(self.driver,"查看单位基本信息")
            browser.exjscommin(self.driver,"关闭")
            browser.exjscommin(self.driver,"全部")
            browser.doubleclick(self.driver,"itemsel")
            browser.exjscommin(self.driver,"选中")

            browser.exjscommin(self.driver,"确定")

            #退出
            browser.exjscommin(self.driver,"退出")
            browser.openModule2(self.driver,modulename,moduledetail)



        except:
            print traceback.format_exc()
            filename=browser.xmlRead(dom,'filename',0)
            #print filename+u"常用-单据草稿.png"
            #browser.getpicture(self.driver,filename+u"notedraft.png")
            browser.getpicture(self.driver,filename+u"批零-价格折扣跟踪.png")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
