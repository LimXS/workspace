#*-* coding:UTF-8 *-*
import time
import re
import datetime
import unittest
import  xml.dom.minidom
import traceback
import requests
import json
import  urllib
from common import browserClass
browser=browserClass.browser()

class stockstateTest(unittest.TestCase):
    u'''常用-库存状况'''

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



    def teststockState(self):
        u'''常用-库存状况'''
        stamp=browser.gettimestamp()
        header={'cookie':self.cookiestr,"Content-Type": "application/json"}
        dom = xml.dom.minidom.parse(r'C:\workspace\nufeeb.button\frequentlyused\frelocation')
        modulename=browser.xmlRead(dom,"module",0)
        moduledetail=browser.xmlRead(dom,'moduledetail',2)



        try:
            browser.openModule2(self.driver,modulename,moduledetail)
            time.sleep(1)
            browser.exjscommin(self.driver,"退出")
            browser.openModule2(self.driver,modulename,moduledetail)
            cookies=browser.cookieSave(self.driver)
            header3={'cookie':cookies,"Content-Type": "application/json"}
            header4={'cookie':cookies,"Content-Type": "application/x-www-form-urlencoded"}

            #可销售库存占用分析id
            stockname="%C8%AB%B2%BF%B2%D6%BF%E2"
            pid="869585272784951"
            saleayaurl="http://beefun.wsgjp.com/Beefun/Report/SaleStockDetailList.gspx?ptypeid="+pid+"&ktypeids=&stockname="+stockname
            saletext=browser.requestget(saleayaurl,header)
            #print saletext
            saleid=browser.getdraftalterid(saletext,1)
            saleid=saleid[:10]
            #print saleid

            #页面id
            pageurl=browser.xmlRead(dom,"stockurl",0)
            pageid=browser.halfid(pageurl,header)
            #print pageid

            button=browser.xmlRead(dom,"button",0)
            btnExit=browser.xmlRead(dom,"selclose",0)
            printnote=browser.xmlRead(dom,"printnote",0)
            basetype=browser.xmlRead(dom,"basetype",0)
            selbtn=browser.xmlRead(dom,"selbtn",0)
            selbtnall=browser.xmlRead(dom,"selbtnall",0)

            pnext=browser.xmlRead(dom,'typenext',0)
            topnext=browser.xmlRead(dom,'typetopnext',0)
            before=browser.xmlRead(dom,'typebe',0)
            topebefore=browser.xmlRead(dom,'typetopbe',0)

            #未分类

            #快速查询

            #显示停用商品

            #显示可销售库存

            #过滤

            #刷新
            refresh=basetype+pageid+button+str(6)+browser.xmlRead(dom,"refresh",0)
            #print refresh
            browser.findXpath(self.driver,refresh).click()

            #明细账本 ok print
            '''
            #browser.delaytime(3,self.driver)
            browser.elementcontains(self.driver,"div","a1x","selid")
            browser.findId(self.driver,"selid").click()
            '''
            browser.exjscommin(self.driver,"明细账本")
            browser.exjscommin(self.driver,"关闭")
            browser.exjscommin(self.driver,"明细账本")
            browser.exjscommin(self.driver,"确定")
            browser.pagechoice(self.driver)
            browser.exjscommin(self.driver,"查看单据")
            browser.delaytime(2)
            browser.know(self.driver)
            browser.exjscommin(self.driver,"退出")
            browser.exjscommin(self.driver,"退出")
            browser.openModule2(self.driver,modulename,moduledetail)

            #打印
            #browser.findId(self.driver,itdeprint).click()

            print u"明细账本OK........."

            #选择仓库
            selcate=pageid+button+str(7)
            browser.findId(self.driver,selcate).click()
            browser.delaytime(1,self.driver)
            cateurl=browser.xmlRead(dom,"cateurl",0)
            catetext=browser.requestget(cateurl,header3)
            cateid=browser.getdraftalterid(catetext,1)
            cateid=cateid[:10]

            #选择
            cateselok=cateid+selbtn
            browser.delaytime(1)
            browser.findId(self.driver,cateselok).click()
            browser.delaytime(1)
            browser.findId(self.driver,selcate).click()
            browser.delaytime(3,self.driver)
            #全部
            cateselall=cateid+selbtnall
            browser.findId(self.driver,cateselall).click()
            browser.delaytime(1)
            browser.findId(self.driver,selcate).click()
            #关闭
            cateselclose=cateid+btnExit
            browser.findId(self.driver,cateselclose).click()

            print u"选择仓库OK........."



            #列表
            browser.delaytime(1)
            browser.delaytime(3,self.driver)
            browser.exjscommin(self.driver,"列表")
            browser.exjscommin(self.driver,"关闭")
            browser.exjscommin(self.driver,"列表")
            browser.exjscommin(self.driver,"选择")



            browser.selectbycon(self.driver,"商品编号","a1x")
            browser.exjscommin(self.driver,"明细账本")
            browser.exjscommin(self.driver,"关闭")
            browser.exjscommin(self.driver,"明细账本")
            browser.exjscommin(self.driver,"确定")
            browser.pagechoice(self.driver)
            browser.exjscommin(self.driver,"查看单据")
            browser.exjscommin(self.driver,"退出")
            browser.exjscommin(self.driver,"退出")
            browser.exjscommin(self.driver,"退出")

            browser.exjscommin(self.driver,"列表")
            browser.exjscommin(self.driver,"选择")
            browser.pagechoice(self.driver)
            browser.exjscommin(self.driver,"退出")



            #打印
            #browser.findId(self.driver,itdeaccprint).click()

            browser.openModule2(self.driver,modulename,moduledetail)


            print u"列表OK........."

            #商品分布 ok print
            browser.exjscommin(self.driver,"商品分布")
            browser.exjscommin(self.driver,"退出")

            #打印
            #browser.findId(self.driver,selspread).click()

            #browser.findId(self.driver,spreadprint).click()
            #browser.openModule2(self.driver,modulename,moduledetail)

            print u"商品分布OK........."


            #辅助数量ok
            browser.exjscommin(self.driver,"辅助数量")
            browser.exjscommin(self.driver,"关闭")
            browser.exjscommin(self.driver,"辅助数量")
            browser.exjscommin(self.driver,"确定")



            print u"辅助数量OK........."

            #序列号ok
            stockseno=browser.xmlRead(dom,"stockseno",0)
            serialno=pageid+stockseno
            browser.findId(self.driver,serialno).click()
            browser.accAlert(self.driver,1)

            #期初库存
            browser.exjscommin(self.driver,"期初库存")
            browser.pagechoice(self.driver)

            browser.exjscommin(self.driver,"选择仓库")
            browser.exjscommin(self.driver,"关闭")
            browser.exjscommin(self.driver,"选择仓库")
            browser.exjscommin(self.driver,"选中")
            browser.exjscommin(self.driver,"选择仓库")
            browser.exjscommin(self.driver,"全部")

            browser.exjscommin(self.driver,"商品分布")
            browser.exjscommin(self.driver,"退出")

            browser.exjscommin(self.driver,"辅助数量")
            browser.exjscommin(self.driver,"关闭")
            browser.exjscommin(self.driver,"辅助数量")
            browser.exjscommin(self.driver,"确定")

            browser.exjscommin(self.driver,"期初调整明细")
            browser.exjscommin(self.driver,"关闭")
            browser.exjscommin(self.driver,"期初调整明细")
            browser.exjscommin(self.driver,"确定")
            browser.exjscommin(self.driver,"退出")

            browser.refreshbutton(self.driver)

            js="$(\"div[class=GridBodyCellText]:contains('Series')\").last().attr(\"id\",\"seitemid\")"
            browser.delaytime(1)
            browser.excutejs(self.driver,js)
            browser.findId(self.driver,"seitemid").click()

            browser.exjscommin(self.driver,"序列号")
            browser.exjscommin(self.driver,"关闭")
            browser.exjscommin(self.driver,"序列号")
            browser.exjscommin(self.driver,"选中")

            browser.exjscommin(self.driver,"退出")
            browser.exjscommin(self.driver,"退出")

            browser.openModule2(self.driver,modulename,moduledetail)

            #打印
            print u"期初库存OK........."



            #库存调整ok print
            selcateajust=pageid+button+str(5)
            browser.findId(self.driver,selcateajust).click()
            cateajusturl="http://beefun.wsgjp.com/Beefun/Bill/StockAdjustBill.gspx"
            cateajusttext=browser.requestget(cateajusturl,header3)
            caahid=browser.getstockid(cateajusttext)
            caahid=caahid[:10]
            #print caahid
            browser.accAlert(self.driver,0)
            browser.findId(self.driver,selcateajust).click()
            browser.accAlert(self.driver,1)
            browser.exjscommin(self.driver,"退出")
            browser.delaytime(2)

            #库存调整单

            #browser.findId(self.driver,caajprint).click()

            print u"库存调整OK........."

            #可销售库存占用分析ok
            browser.exjscommin(self.driver,"可销售库存占用分析")
            js="$(\"font[color=blue]\").last().attr(\"id\",\"viewid\")"
            browser.delaytime(1)
            browser.excutejs(self.driver,js)
            browser.findId(self.driver,"viewid").click()
            browser.exjscommin(self.driver,"退出")
            browser.openModule2(self.driver,modulename,moduledetail)

            print u"可销售库存占用分析OK........."

            #序列号
            js="$(\"div[class=GridBodyCellText]:contains('Series')\").last().attr(\"id\",\"seitemid\")"
            browser.delaytime(1)
            browser.excutejs(self.driver,js)
            browser.findId(self.driver,"seitemid").click()

            browser.findId(self.driver,serialno).click()
            browser.exjscommin(self.driver,"关闭")
            browser.findId(self.driver,serialno).click()
            browser.exjscommin(self.driver,"选中")
            browser.pagechoice(self.driver)
            browser.exjscommin(self.driver,"添加")
            browser.exjscommin(self.driver,"关闭")
            browser.exjscommin(self.driver,"删除")

            browser.exjscommin(self.driver,"退出")

            browser.openModule2(self.driver,modulename,moduledetail)


            #返回上级

            #打印
            pageprint=pageid+printnote
            #browser.findId(self.driver,pageprint).click()

            #退出
            pageexit=pageid+btnExit
            browser.pagechoice(self.driver,1)
            browser.findId(self.driver,pageexit).click()
            browser.openModule2(self.driver,modulename,moduledetail)

            #翻页
            browser.pagewhich(self.driver,basetype,pageid,pnext,topebefore,before,topnext)
        except:
            print traceback.format_exc()
            filename=browser.xmlRead(dom,'filename',0)
            #print filename+u"常用-单据草稿.png"
            #browser.getpicture(self.driver,filename+u"notedraft.png")
            browser.getpicture(self.driver,filename+u"常用-库存状况.png")



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
