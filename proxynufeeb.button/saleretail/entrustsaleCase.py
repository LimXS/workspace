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

class entrustsaleTest(unittest.TestCase):
    u'''批零-委托代销-委托发货单'''

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

    def testentrustSale(self):
        u'''批零-委托代销-委托发货单'''
        header={'cookie':self.cookiestr,"Content-Type": "application/json"}
        comdom=xml.dom.minidom.parse(r'C:\workspace\proxynufeeb.button\data\commonlocation')
        dom = xml.dom.minidom.parse(r'C:\workspace\proxynufeeb.button\saleretail\salelocation')

        modulename=browser.xmlRead(dom,"module",0)
        moduledetail=browser.xmlRead(dom,'moduledetail',6)
        moduledd=browser.xmlRead(dom,'moduledd',0)

        browser.openModule3(self.driver,modulename,moduledetail,moduledd)

        cookies=browser.cookieSave(self.driver)
        header3={'cookie':cookies,"Content-Type": "application/json"}
        header4={'cookie':cookies,"Content-Type": "application/x-www-form-urlencoded"}

        #页面id
        pageurl=browser.xmlRead(dom,"ensalurl",0)
        pageid=browser.getalertid(pageurl,header)
        #print pageid

        #commid,id
        commid=browser.getallcommonid(comdom)
        #id=browser.getcommonid(dom)

        try:
            #发货仓库
            cateid=pageid+browser.xmlRead(dom,'edKType',0)
            browser.delaytime(1)
            browser.peoplesel(self.driver,cateid)

            #收货单位
            companyid=pageid+browser.xmlRead(dom,'edBType',0)
            #print companyid
            browser.delaytime(1)
            browser.buycompanysel(self.driver,companyid)

            #经手人
            peoid=pageid+browser.xmlRead(dom,'edEType',0)
            browser.delaytime(1)
            browser.peoplesel(self.driver,peoid,1)

            #部门
            depid=pageid+browser.xmlRead(dom,'edDept',0)
            browser.delaytime(1)
            browser.passpeople(self.driver,depid)



            #摘要
            summid=pageid+browser.xmlRead(dom,'edSummary',0)
            browser.findId(self.driver,summid).send_keys(u"中文测试饕餮壹贰123！@#￥%……&*（）()； abcentrust sale summary")

            #附加说明
            commentid=pageid+browser.xmlRead(dom,'edComment',0)
            browser.findId(self.driver,commentid).send_keys(u"中文测试饕餮壹贰123！@#￥%……&*（）()； abcentrust sale commentid")

            #商品名字
            itnaid=commid["basetype"]+pageid+browser.xmlRead(dom,"partitna",0)+str(3)+"]"
            browser.delaytime(1)
            #print itnaid
            browser.findXpath(self.driver,itnaid).click()
            itemid=pageid+commid["grid_pfullname"]
            browser.cateitemsel(self.driver,itemid)

            #单位
            js="$(\"div:contains('个')\").last().attr(\"id\",\"itunid\")"
            browser.delaytime(1)
            browser.excutejs(self.driver,js)
            browser.delaytime(1)
            browser.itemunit(self.driver,"itunid")

            #数量
            itemgrid=browser.xmlRead(dom,"partitna",0)
            qtyid=pageid+commid["grid_assqty"]
            browser.delaytime(1)
            itqty=commid["basetype"]+pageid+itemgrid+str(13)+"]"
            browser.findXpath(self.driver,itqty).click()

            browser.itemnums(self.driver,qtyid)

            #折前单价
            dpprice=commid["basetype"]+pageid+itemgrid+str(14)+"]"
            browser.delaytime(1)
            browser.findXpath(self.driver,dpprice).click()

            dppriceid=pageid+browser.xmlRead(dom,'grid_assprice',0)
            browser.delaytime(1)
            browser.itemunit(self.driver,dppriceid)

            #打印

            #保存退出
            saexid=pageid+commid["selclose"]
            browser.savedraftexit(self.driver,saexid,itnaid,itemid)
            browser.openModule3(self.driver,modulename,moduledetail,moduledd)


        except:
            print traceback.format_exc()
            filename=browser.xmlRead(dom,'filename',0)
            #print filename+u"常用-单据草稿.png"
            #browser.getpicture(self.driver,filename+u"notedraft.png")
            browser.getpicture(self.driver,filename+u"批零-委托代销-委托发货单.png")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
