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

class saleordermanTest(unittest.TestCase):
    u'''批零-销售订单管理'''

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

    def testnewsaleorderMan(self):
        u'''批零-销售订单管理.'''
        header={'cookie':self.cookiestr,"Content-Type": "application/json"}
        comdom=xml.dom.minidom.parse(r'C:\workspace\proxynufeeb.button\data\commonlocation')
        dom = xml.dom.minidom.parse(r'C:\workspace\proxynufeeb.button\saleretail\salelocation')

        modulename=browser.xmlRead(dom,"module",0)
        moduledetail=browser.xmlRead(dom,'moduledetail',1)

        browser.openModule2(self.driver,modulename,moduledetail)

        #页面id
        pageurl=browser.xmlRead(dom,"salemanurl",0)
        pageid=browser.getalertid(pageurl,header)
        #print pageid

        #commid,id
        commid=browser.getallcommonid(comdom)


        try:
            #审核
            browser.delaytime(1)
            js="$(\"div[class=GridBodyCellText]:contains('网店客户')\").first().attr(\"id\",\"checkid\")"
            browser.delaytime(1)
            browser.excutejs(self.driver,js)
            browser.findId(self.driver,"checkid").click()
            jscheck="$(\"button:contains('审核')\").first().click()"
            browser.delaytime(1)
            browser.excutejs(self.driver,jscheck)
            browser.exjscommin(self.driver,"关闭")
            browser.excutejs(self.driver,jscheck)
            browser.exjscommin(self.driver,"审核通过")

            #更多
            browser.exjscommin(self.driver,"更多")
            #-修改发货信息
            jschageinfo="$(\"td[class=MenuCaption]:contains('修改发货信息')\").click()"
            browser.excutejs(self.driver,jschageinfo)
            #--关闭
            browser.exjscommin(self.driver,"关闭")
            browser.exjscommin(self.driver,"更多")
            browser.excutejs(self.driver,jschageinfo)
            #--快捷选择
            js="$(\"input[id$=edDeliveryInfo]\").last().attr(\"id\",\"quickseid\")"
            time.sleep(1)
            browser.excutejs(self.driver,js)
            browser.doubleclick(self.driver,"quickseid")

            #print "into..."

            #---修改
            browser.exjscommin(self.driver,"修改")
            browser.exjscommin(self.driver,"保存并关闭")
            browser.exjscommin(self.driver,"修改")
            browser.exjscommin(self.driver,"关闭")

            #---新增
            browser.exjscommin(self.driver,"新增")
            js1="$(\"input[id$=edReceiverPeople]\").last().attr(\"value\",\"repeople\")"
            browser.delaytime(1)
            browser.excutejs(self.driver,js1)
            js2="$(\"input[id$=edReceiverTelephone]\").last().attr(\"value\",\"12345678901\")"
            browser.delaytime(1)
            browser.excutejs(self.driver,js2)
            js2="$(\"input[id$=edReceiverAddress]\").last().attr(\"value\",\"address\")"
            browser.delaytime(1)
            browser.excutejs(self.driver,js2)

            js1="$(\"input[id$=edProvince]\").last().attr(\"id\",\"proid\")"
            js2="$(\"div:contains(\'山西省\')\").last().attr(\"id\",\"shanxiid\")"
            browser.delaytime(1)
            browser.excutejs(self.driver,js1)
            browser.delaytime(1)
            browser.delaytime(3,self.driver)
            browser.doubleclick(self.driver,"proid")
            #time.sleep(1)
            browser.excutejs(self.driver,js2)
            browser.findId(self.driver,"shanxiid").click()

            js1="$(\"input[id$=edCity]\").last().attr(\"id\",\"cityid\")"
            js2="$(\"div:contains(\'太原市\')\").last().attr(\"id\",\"taiyuanid\")"
            browser.delaytime(1)
            browser.excutejs(self.driver,js1)
            browser.doubleclick(self.driver,"cityid")
            browser.excutejs(self.driver,js2)
            browser.findId(self.driver,"taiyuanid").click()


            browser.exjscommin(self.driver,"保存并关闭")
            browser.exjscommin(self.driver,"新增")
            browser.exjscommin(self.driver,"关闭")

            #---删除
            browser.exjscommin(self.driver,"删除")
            browser.delaytime(2,self.driver)
            browser.accAlert(self.driver,0)
            browser.exjscommin(self.driver,"删除")
            browser.delaytime(2,self.driver)
            browser.accAlert(self.driver,1)

            #---选中
            browser.exjscommin(self.driver,"选中")
            browser.exjscommin(self.driver,"确定")


            #-复制为销售订单
            browser.exjscommin(self.driver,"更多")
            jscpsaleorder="$(\"td[class=MenuCaption]:contains('复制为销售订单')\").click()"
            browser.excutejs(self.driver,jscpsaleorder)
            browser.delaytime(2,self.driver)
            browser.accAlert(self.driver,0)

            browser.exjscommin(self.driver,"更多")
            browser.excutejs(self.driver,jscpsaleorder)
            browser.delaytime(1)
            browser.accAlert(self.driver,1)

            browser.openModule2(self.driver,modulename,moduledetail)

            #-复制为进货订单
            browser.exjscommin(self.driver,"更多")
            jscpstockorder="$(\"td[class=MenuCaption]:contains('复制为进货订单')\").click()"
            browser.excutejs(self.driver,jscpstockorder)
            browser.delaytime(2,self.driver)
            browser.accAlert(self.driver,0)

            browser.exjscommin(self.driver,"更多")
            browser.excutejs(self.driver,jscpstockorder)
            browser.delaytime(2,self.driver)
            browser.accAlert(self.driver,1)

            browser.openModule2(self.driver,modulename,moduledetail)

            #-订单审核配置
            browser.exjscommin(self.driver,"更多")
            jsorcon="$(\"td[class=MenuCaption]:contains('订单审核配置')\").click()"
            browser.excutejs(self.driver,jsorcon)
            browser.exjscommin(self.driver,"退出")

            browser.exjscommin(self.driver,"更多")
            browser.excutejs(self.driver,jsorcon)
            browser.exjscommin(self.driver,"保存")
            browser.delaytime(2,self.driver)
            browser.accAlert(self.driver,1)

            #-删除
            browser.exjscommin(self.driver,"更多")
            jsdel="$(\"td[class=MenuCaption]:contains('删除')\").click()"
            browser.excutejs(self.driver,jsdel)
            browser.delaytime(2,self.driver)
            browser.accAlert(self.driver,0)

            browser.exjscommin(self.driver,"更多")
            browser.excutejs(self.driver,jsdel)
            browser.delaytime(2,self.driver)
            browser.accAlert(self.driver,1)

            #-提交发货
            browser.exjscommin(self.driver,"更多")
            jssubend="$(\"td[class=MenuCaption]:contains('提交发货')\").click()"
            browser.excutejs(self.driver,jssubend)
            browser.delaytime(1,self.driver)
            browser.exjscommin(self.driver,"确定")

            #-终止并完成
            browser.exjscommin(self.driver,"更多")
            jsendok="$(\"td[class=MenuCaption]:contains('终止并完成')\").click()"
            browser.excutejs(self.driver,jsendok)
            browser.delaytime(2,self.driver)
            browser.accAlert(self.driver,0)

            browser.exjscommin(self.driver,"更多")
            browser.excutejs(self.driver,jsendok)
            browser.delaytime(2,self.driver)
            browser.accAlert(self.driver,1)

            #-打印

            #退出
            browser.exjscommin(self.driver,"退出")
            browser.openModule2(self.driver,modulename,moduledetail)

            #仓库选择框
            catexpath=commid["basetype"]+pageid+browser.xmlRead(dom,"partitna",0)+str(10)+"]"
            browser.findXpath(self.driver,catexpath).click()
            cateid=pageid+commid["grid_kfullname"]

            browser.peoplesel(self.driver,cateid)

            #经手人
            peoxpath=commid["basetype"]+pageid+browser.xmlRead(dom,"partitna",0)+str(11)+"]"
            browser.findXpath(self.driver,peoxpath).click()
            peoid=pageid+commid["grid_ename"]
            browser.delaytime(1)
            browser.peoplesel(self.driver,peoid,1)

            #翻页
            browser.pagechoice(self.driver)

            #刷新
            js="$(\"span:contains('刷新')\").last().click()"
            browser.delaytime(1)
            browser.excutejs(self.driver,js)

            #发货订单
            js="$(\"div[class=TabTopCaptionText]\").last().attr(\"id\",\"seorid\")"
            browser.delaytime(1)
            browser.excutejs(self.driver,js)
            browser.findId(self.driver,"seorid")

            #商品明细
            js="$(\"div[class=TabTopCaptionText]\").eq(2).attr(\"id\",\"itdeid\")"
            browser.delaytime(1)
            browser.excutejs(self.driver,js)
            browser.findId(self.driver,"itdeid")



            #修改
            browser.exjscommin(self.driver,"修改")
            browser.openModule2(self.driver,modulename,moduledetail)

            #执行情况
            browser.exjscommin(self.driver,"执行情况")
            browser.openModule2(self.driver,modulename,moduledetail)

            #查询条件
            browser.exjscommin(self.driver,"查询条件")
            browser.exjscommin(self.driver,"关闭")
            browser.exjscommin(self.driver,"查询条件")
            browser.exjscommin(self.driver,"确定")

        except:
            print traceback.format_exc()
            filename=browser.xmlRead(dom,'filename',0)
            #print filename+u"常用-单据草稿.png"
            #browser.getpicture(self.driver,filename+u"notedraft.png")
            browser.getpicture(self.driver,filename+u"批零-销售订单管理.png")



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
