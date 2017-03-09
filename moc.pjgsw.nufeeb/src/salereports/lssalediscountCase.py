#*-* coding:UTF-8 *-*
import time
import unittest
import  xml.dom.minidom
import traceback
import requests
import re
import json
from common import browserClass
browser=browserClass.browser()

class lssalediscountTest(unittest.TestCase):
    u'''报表-批发零售报表-销售优惠统计'''

    def setUp(self):
        self.driver=browser.startBrowser('chrome')
        browser.set_up(self.driver)
        '''
        dom = xml.dom.minidom.parse(r'C:\workspace\moc.pjgsw.nufeeb\src\data\report')

        module1=browser.xmlRead(self.driver,dom,"module",1)
        module2=browser.xmlRead(self.driver,dom,'module',2)

        browser.openModule2(self.driver,module1,module2)
       '''
        cookie = [item["name"] + "=" + item["value"] for item in self.driver.get_cookies()]
        #print cookie
        self.cookiestr = ';'.join(item for item in cookie)
        time.sleep(2)
        pass


    def tearDown(self):
        print "test over"
        self.driver.close()
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


    def testLssalediscount(self):
        u'''报表-批发零售报表-销售优惠统计'''

        header={'cookie':self.cookiestr,"Content-Type": "application/json"}
        header2={'cookie':self.cookiestr,"Content-Type": "application/x-www-form-urlencoded"}

        stamp=browser.gettimestamp()

        #单据中心
        #pagedic=browser.notecentel(header)
        #print pagedic
        #print pagedic["itemList"]
        #print pagedic["itemList"][0]["number"]


        #报表页面
        dom = xml.dom.minidom.parse(r'C:\workspace\moc.pjgsw.nufeeb\src\salereports\salereportsxpath')

        module1=browser.xmlRead(self.driver,dom,"module",0)
        module2=browser.xmlRead(self.driver,dom,'moduledetail',0)
        module3=browser.xmlRead(self.driver,dom,'moduledetail2',0)
        browser.openModule3(self.driver,module1,module2,module3)
        comfirm=browser.xmlRead(self.driver,dom,'comfirm',0)
        browser.findXpath(self.driver,comfirm).click()
        time.sleep(2)
        cookie2 = [item["name"] + "=" + item["value"] for item in self.driver.get_cookies()]
        #print cookie
        cookiestr2 = ';'.join(item for item in cookie2)
        header3={'cookie':cookiestr2,"Content-Type": "application/json"}
        header4={'cookie':cookiestr2,"Content-Type": "application/x-www-form-urlencoded"}

        #页面Id
        urlid="http://beefun.wsgjp.com/Beefun/Report/SalePreferentialQuery.gspx"
        ida="{\"btypeid\":null,\"bfullname\":\"\",\"etypeid\":null,\"efullname\":\"\",\"preferentialtype\":0,\"begin\":\""+str(stamp[3])+"\",\"end\":\""+str(stamp[2])+"\",\"saveDate\":false,\"page\":0}"
        idata={"__Params":ida}
        pagetext=requests.post(url=urlid,data=idata,headers=header4)
        #print pagetext.text
        pageid=browser.getpageid(pagetext)
        #print pageid

        #页面Lists detail
        #print stamp
        urldetail="http://beefun.wsgjp.com/Carpa.Web/Carpa.Web.Script.DataService.ajax/GetPagerData"
        detaildata={"pagerId":pageid,"queryParams":{"begin":stamp[3],"end":stamp[2],"etypeid":None,"btypeid":None,"filter":0,"page":0},"orders":None,"filter":None,"first":0,"count":100000}
        detailtext=requests.post(url=urldetail,data=json.dumps(detaildata),headers=header3)
        #print detailtext.text
        detailists=browser.datatrunjson(detailtext)

        monatax=0
        distotal=0
        dismoney=0
        for detail in detailists["itemList"]["rows"]:
            #单位优惠明细账本
            #print detail
            #id
            detialurl="http://beefun.wsgjp.com/Beefun/Report/SalePreferentialDetailQuery.gspx"
            deda="{\"vchcode\":\""+detail[0]+"\",\"id\":\""+detail[1]+"\",\"total\":585.94,\"preferentialtotal\":0,\"afterpreferentialtotal\":585.94,\"usercode\":\""+detail[5]+"\",\"fullname\":\""+detail[6]+"\",\"page\":0,\"begin\":\"2016-08-19\",\"end\":\"2016-08-25\",\"btypeid\":null,\"etypeid\":null}"
            dedata={"__Params":deda}
            dedetailtext=requests.post(url=detialurl,headers=header4,data=dedata)
            #print dedetailtext.text
            detailid=browser.getpageid(dedetailtext)
            #print detailid

            #detaillists
            redetailurl="http://beefun.wsgjp.com/Carpa.Web/Carpa.Web.Script.DataService.ajax/GetPagerData"
            rededata={"pagerId":detailid,"queryParams":None,"orders":None,"filter":None,"first":0,"count":100000}
            rededetailtext=requests.post(url=redetailurl,data=json.dumps(rededata),headers=header3)
            redelists=browser.datatrunjson(rededetailtext)
            #print "redelists............"
            #print redelists
            n=0
            redetaxamoney=0
            rededistotal=0
            rededismoney=0
            for redetail in redelists["itemList"]["rows"]:
                n+=1
                #原始单据信息
                Vchtype=redetail[6]
                Vchcode=redetail[5]
                lsurl="http://beefun.wsgjp.com/Beefun/Bill/SaleBill.gspx?Vchtype="+str(Vchtype)+"&Vchcode="+str(Vchcode)+"&Mode=Read"
                ortext=requests.get(lsurl,headers = header)
                #单据头
                orheader=browser.getnotehead(ortext)
                #单据优惠、金额等
                ordata=re.findall("dataBind(.*?)settleaccounts",ortext.text)

                print u"单位优惠明细账本第"+str(n)+u"行数据："+str(redetail[2])
                #print redetail
                #日期
                #ordate=browser.handlestampdays(float(orheader[6][9:-1]),1)
                self.assernote(str(redetail[0]),str(orheader[6][9:-1]),u"日期不相同（单位优惠明细账本和其原始单据）","reportdetail date ok",u"日期")

                #单据编号
                self.assernote(str(redetail[2]),str(orheader[11]),u"单据编号不相同（单位优惠明细账本和其原始单据）","reportdetail number ok",u"单据编号")

                #摘要
                self.assernote(str(redetail[4]),str(orheader[12]),u"摘要不相同（单位优惠明细账本和其原始单据）","reportdetail summary ok",u"摘要")

                #单位名称
                self.assernote(str(redetail[7]),str(orheader[38]),u"单位名称不相同（单位优惠明细账本和其原始单据）","reportdetail company ok",u"单位名称")
                self.assernote(str(redetail[7]),str(detail[6]),u"单位名称不相同（单位优惠明细账本和单位销售优惠统计）","report company ok",u"单位名称")

                #价税合计
                redetaxamoney+=float(redetail[12])
                if redetail[2][:2]=="LT" or redetail[2][:2]=="XT":
                    ortaxmon=-float(orheader[8])
                else:
                    ortaxmon=float(orheader[8])
                self.assernote(str(redetail[12]),str(ortaxmon),u"价税合计不相同（单位优惠明细账本和其原始单据）","reportdetail taxmoney ok",u"价税合计")

                #优惠金额
                ordistotal=re.findall("\"preference\":(.*?),\"jtotal\"",ortext.text)
                rededistotal+=float(redetail[13])
                redistot=float(redetail[13])
                ordistot=float(ordistotal[0])
                self.assernote(str("%.2f"%redistot),str("%.2f"%ordistot),u"优惠金额不相同（单位优惠明细账本和其原始单据）","reportdetail distotal ok",u"优惠金额")

                #优惠后金额
                rededismoney+=float(redetail[14])
                redismon=float(redetail[14])
                ordismon=ortaxmon-float(ordistotal[0])
                self.assernote(str("%.2f"%redismon),str("%.2f"%ordismon),u"优惠后金额不相同（单位优惠明细账本和其原始单据）","reportdetail discount money ok",u"优惠后金额")


            #detailsum
            redetailsum=browser.funpagesum(detailid,header3)
            #print "redetailsum......"
            #print redetailsum

            #价税合计
            self.assernote(str(redetailsum["total"]["value"]),str(redetaxamoney),u"价税合计不相同（单位优惠明细账本和其页面统计）","reportdetail sum taxafter money ok",u"价税合计")

            #优惠金额
            self.assernote(str(redetailsum["preferentialtotal"]["value"]),str(rededistotal),u"优惠金额不相同（单位优惠明细账本和其页面统计）","reportdetail sum discount total ok",u"优惠金额")

            #优惠后金额
            self.assernote(str(redetailsum["afterpreferentialtotal"]["value"]),str(rededismoney),u"优惠后金额不相同（单位优惠明细账本和其页面统计）","reportdetail sum discount money ok",u"优惠后金额")

            #单位编号
            detail[5]

            #价税合计
            monatax+=float(detail[2])
            self.assernote(str(detail[2]),str(redetailsum["total"]["value"]),u"价税合计不相同（单位销售优惠统计和单位优惠明细账本统计）","report taxafter money ok",u"价税合计")

            #优惠金额
            distotal+=float(detail[3])
            self.assernote(str(detail[3]),str(redetailsum["preferentialtotal"]["value"]),u"优惠金额不相同（单位销售优惠统计和单位优惠明细账本统计）","report discount total ok",u"优惠金额")

            #优惠后金额
            dismoney+=float(detail[4])
            self.assernote(str(detail[4]),str(redetailsum["afterpreferentialtotal"]["value"]),u"优惠后金额不相同（单位销售优惠统计和单位优惠明细账本统计）","report discount money ok",u"优惠后金额")

        #页面统计sum
        pagesum=browser.funpagesum(pageid,header3)
        print pagesum

        #价税合计
        self.assernote(str(pagesum["total"]["value"]),str(monatax),u"价税合计不相同（单位销售优惠统计和其页面统计）","report sum taxafter money ok",u"价税合计")

        #优惠金额

        self.assernote(str(pagesum["preferentialtotal"]["value"]),str(distotal),u"优惠金额不相同（单位销售优惠统计和其页面统计）","report sum discount total ok",u"优惠金额")

        #优惠后金额
        self.assernote(str(pagesum["afterpreferentialtotal"]["value"]),str(dismoney),u"优惠后金额不相同（单位销售优惠统计和其页面统计）","report sum discount money ok",u"优惠后金额")




if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()