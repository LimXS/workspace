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

class itemreturnTest(unittest.TestCase):
    u'''报表-批发零售报表-商品销售/退货分析'''

    def setUp(self):
        self.driver=browser.startBrowser('chrome')
        browser.set_up(self.driver)

        dom = xml.dom.minidom.parse(r'C:\workspace\moc.pjgsw.nufeeb\src\data\report')

        module1=browser.xmlRead(self.driver,dom,"module",1)
        module2=browser.xmlRead(self.driver,dom,'module',2)

        browser.openModule2(self.driver,module1,module2)


        cookie = [item["name"] + "=" + item["value"] for item in self.driver.get_cookies()]
        #print cookie
        self.cookiestr = ';'.join(item for item in cookie)

        time.sleep(2)
        pass

    def assernote(self,num1,num2,note,noteok,flag):
        try:
            self.assertEqual(num1,num2,msg=note)
            print noteok
        except AssertionError,msg:
            print msg
            print flag
            print num1
            print num2

    def tearDown(self):
        print "test over"
        self.driver.close()
        pass

    def testitemReturn(self):
        u'''报表-批发零售报表-商品销售/退货分析'''

        header={'cookie':self.cookiestr,"Content-Type": "application/json"}
        header2={'cookie':self.cookiestr,"Content-Type": "application/x-www-form-urlencoded"}

        stamp=browser.gettimestamp()
        #print stamp
        #页面id
        itemreidurl="http://beefun.wsgjp.com/Beefun/Report/ProductsSaleAndOut.gspx"
        itredata="{\"mode\":\"psale\",\"reporttype\":4,\"StartDate\":\"\/Date("+str(stamp[1]*1000)+")\/\",\"EndDate\":\"\/Date("+str(stamp[0]*1000)+")\/\",\"dlytype\":[0,1,2,3],\"pTypeid\":null,\"eTypeid\":null,\"kTypeid\":null,\"bTypeid\":null,\"brandid\":null,\"saveDate\":false,\"bId\":null,\"bfullname\":\"\",\"eId\":null,\"efullname\":\"\",\"kId\":null,\"kfullname\":\"\",\"pId\":null,\"pfullname\":\"\",\"brandname\":\"\",\"startDate\":\""+str(stamp[3])+"\",\"endDate\":\""+str(stamp[2])+"\",\"filter\":0,\"leveal\":1,\"querytype\":1}"
        itreform={"__Params":itredata}
        itemretext=requests.post(url=itemreidurl,data=itreform,headers=header2)
        #print itemretext.text
        itemreid=browser.getpageid(itemretext)
        #print itemreid

        #获取页面数据
        itemrelistsurl="http://beefun.wsgjp.com/Carpa.Web/Carpa.Web.Script.DataService.ajax/GetPagerData"
        itemrelidata={"pagerId":itemreid,"queryParams":{"mode":"psale","pTypeid":None,"bTypeid":None,"eTypeid":None,"kTypeid":None,"brandid":None,"dlytype":[0,1,2,3],"StartDate":stamp[3],"EndDate":stamp[2],"filter":0,"leveal":1,"querytype":1,"reporttype":4,"pfullname":"","bfullname":"","efullname":"","kfullname":"","brandname":""},"orders":None,"filter":None,"first":0,"count":100000}
        itemrelitext=requests.post(url=itemrelistsurl,data=json.dumps(itemrelidata),headers=header)
        #print itemrelitext.text
        itemrelist=browser.datatrunjson(itemrelitext)
        #print itemrelist

        #获取页面统计数据
        itemresumurl="http://beefun.wsgjp.com/Carpa.Web/Carpa.Web.Script.DataService.ajax/GetPagerSummary"
        itemresumdata={"pagerId":itemreid}
        itemresumtext=requests.post(url=itemresumurl,data=json.dumps(itemresumdata),headers=header)
        #print itemresumtext.text
        itemresum=browser.datatrunjson(itemresumtext)
        #print itemresum

        #商品销售退货分析
        csalenum=0
        cmoney=0
        coutnum=0
        coutmoney=0
        crenum=0
        cremoney=0

        checkdata=browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\salereports\analysischeck','r',1,'aaa')
        n=0
        m=0
        for item in itemrelist["itemList"]["rows"]:
            #print item
            #print len(item)
            m+=1
            print u"报表第"+str(m)+u"行数据："+str(item[5])
            #商品编号
            self.assernote(str(item[0]),str(checkdata[n+5].strip()),u"商品编号不相同（商品销售统计页面）","report item code ok",u"商品编号验证")

            #商品名称
            self.assernote(str(item[5]),str(checkdata[n+6].strip()),u"商品名称不相同（商品销售统计页面）","report item name ok",u"商品名称验证")

            #销售数量
            salenum=item[18]
            csalenum=csalenum+float(item[18])

            self.assernote(str(salenum),str(float(checkdata[n+1].strip())-float(checkdata[n].strip())),u"销售数量不相同（商品销售统计页面）","report sale number ok",u"销售数量验证")

            #金额
            money=item[15]
            cmoney=cmoney+float(item[15])

            self.assernote(str(money),str(float(checkdata[n+2].strip())),u"金额不相同（商品销售统计页面）","report money ok",u"金额验证")


            #销售出库数量
            outnum=item[21]
            coutnum=coutnum+float(item[21])

            self.assernote(str(outnum),str(float(checkdata[n+1].strip())),u"销售出库数量不相同（商品销售统计页面）","report out number ok",u"销售出库数量验证")

            #销售出库金额
            outmoney=item[22]
            coutmoney=coutmoney+float(item[22])
            checkoutmoney=float(checkdata[n+3].strip())
            checkoutmoney=round(checkoutmoney,2)
            self.assernote(str(outmoney),str(checkoutmoney),u"销售出库金额不相同（商品销售统计页面）","report out money ok",u"销售出库金额验证")

            #销售退货数量
            renum=item[25]
            crenum=crenum+float(item[25])

            self.assernote(str(renum),str(float(checkdata[n].strip())),u"销售退货数量不相同（商品销售统计页面）","report re number ok",u"销售退货数量验证")


            #销售退货金额
            remoney=item[26]
            cremoney=cremoney+float(item[26])
            checkremoney=float(checkdata[n+4].strip())
            checkremoney=round(checkremoney,2)
            self.assernote(str(remoney),str(checkremoney),u"销售退货金额不相同（商品销售统计页面）","report re money ok",u"销售退货金额验证")

            n=n+7

            #退货率
            repercent=item[28]
            if float(item[21])==0.0:
                citrepercent=0.0
            else:
                citrepercent=float(item[25])/float(item[21])*100
                citrepercent=round(citrepercent,2)
            self.assernote(str(repercent),str(citrepercent),u"退货率不相同（商品销售统计页面）","report re precent ok",item[5])


        #商品销售/退货分析页面统计sum数据
        print u"商品销售/退货分析页面统计sum数据核对......................."

        #销售数量
        salenum=float(itemresum["qty"]["value"])
        self.assernote(str(salenum),str(csalenum),u"销售数量不相同（商品销售统计页面）","report sale numbers sum ok",u"统计销售数量")

        #金额
        money=float(itemresum["tptotal"]["value"])
        self.assernote(str(money),str(cmoney),u"金额不相同（商品销售统计页面）","report money sum ok",u"统计金额")

        #销售出库数量
        outnum=float(itemresum["outqty"]["value"])
        self.assernote(str(outnum),str(coutnum),u"销售出库数量不相同（商品销售统计页面）","report sale out numbers sum ok",u"统计销售出库数量")

        #销售出库金额
        outmoney=float(itemresum["outtotal"]["value"])
        self.assernote(str(outmoney),str(coutmoney),u"销售出库金额不相同（商品销售统计页面）","report sale out money sum ok",u"统计销售出库金额")

        #销售退货数量
        salerenum=float(itemresum["backqty"]["value"])
        self.assernote(str(salerenum),str(crenum),u"销售退货数量不相同（商品销售统计页面）","report sale return number sum ok",u"统计销售退货数量")

        #销售退货金额
        saleremoney=float(itemresum["backtotal"]["value"])
        self.assernote(str(saleremoney),str(cremoney),u"销售退货金额不相同（商品销售统计页面）","report sale return money sum ok",u"统计销售退货金额")






if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
