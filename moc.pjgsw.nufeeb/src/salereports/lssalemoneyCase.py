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

class lssalemoneyTest(unittest.TestCase):
    u'''报表-批发零售报表-批零业务毛利统计'''

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


    def testLssalemoney(self):
        u'''报表-批发零售报表-批零业务毛利统计'''

        header={'cookie':self.cookiestr,"Content-Type": "application/json"}
        header2={'cookie':self.cookiestr,"Content-Type": "application/x-www-form-urlencoded"}

        stamp=browser.gettimestamp()

        #单据中心
        pagedic=browser.notecentel(header)
        #print pagedic["itemList"]
        #print pagedic["itemList"][0]["number"]

        #报表取数
        #页面id
        urlid="http://beefun.wsgjp.com/Beefun/Bill/Retail/RetailTotalReport.gspx"
        pagedata=browser.pageidsum(urlid,header)
        pageid=pagedata[0]
        #print pageid


        #print
        #一周内页面数据up list
        #print "up lists"
        urldatauplist="http://beefun.wsgjp.com/Carpa.Web/Carpa.Web.Script.DataService.ajax/GetPagerData"
        pageuplistdata={"pagerId":pageid,"queryParams":{"begindate":stamp[3],"enddate":stamp[2],"beginhour":0,"endhour":24,"ktypeid":0,"kfullname":None,"etypeid":0,"efullname":None,"order":""},"orders":None,"filter":None,"first":0,"count":100000}
        #pagetext=requests.post(url=urldata,data=json.dumps(pagelistdata),headers=header)
        #pagelists=browser.datatrunjson(pagetext)
        pagelistsup=browser.pagedetail(urldatauplist,pageuplistdata,header)
        #print len(pagelistsup)
        #print pagelistsup["itemList"]["rows"][0]

        cupmoney=0
        cupvipcharge=0
        cupsocremin=0
        cupdismoney=0
        cuprecash=0
        cuprevipcharge=0
        cupredismoney=0
        cupsalemoney=0
        n=0
        for people in pagelistsup["itemList"]["rows"]:
            print u"第"+str(n+1)+u"行商品详情,经手人："+str(people[0])
            #一周内页面数据down list
            #print "down list.."
            urldata="http://beefun.wsgjp.com/Carpa.Web/Carpa.Web.Script.DataService.ajax/GetPagerData"
            #print people[1]
            pagelistdata={"pagerId":pageid[:-11]+"billDetail_pager1","queryParams":{"begindate":stamp[3],"enddate":stamp[2],"beginhour":0,"endhour":24,"ktypeid":0,"kfullname":None,"etypeid":people[1],"efullname":None,"order":""},"orders":None,"filter":None,"first":0,"count":100000}
            #pagetext=requests.post(url=urldata,data=json.dumps(pagelistdata),headers=header)
            #pagelists=browser.datatrunjson(pagetext)
            pagelists=browser.pagedetail(urldata,pagelistdata,header)
            #print pagelists["itemList"]["rows"]

            #sum down list detail
            m=0
            dsccash=0
            dsccard=0
            dscdismoney=0
            dscminmoney=0
            dscvipcate=0
            dscvipmin=0

            lsinmoney=0
            lsinvipcate=0
            lsremoney=0
            lsrevipcate=0
            for down in pagelists["itemList"]["rows"]:
                print u"第"+str(m+1)+u"单据："+str(down[0])
                #原始单据科目详情
                subject=[]
                for ordetail in pagedic["itemList"]:
                    if ordetail["number"]==down[0]:
                        vchcode=ordetail["vchcode"]
                        subject=browser.subjectdetail(vchcode,header)
                        break

                #现金金额
                dsccash+=down[1]
                self.assernote(str(down[1]),str(float(subject[1])),u"现金金额不相同（零售金额统计报表明细和原始单据）","reportdetail ornote down money ok",u"现金金额"+str(down[0]))

                #银行卡金额
                down[2]
                dsccard+=down[2]

                #优惠金额
                dscdismoney+=down[3]
                if down[0][:2]=="LS" and len(subject)>5:
                    ordismoney=abs(float(subject[5]))
                else:
                    ordismoney=0.0
                self.assernote(str(down[3]),str(ordismoney),u"优惠金额不相同（零售金额统计报表明细和原始单据）","reportdetail ornote discount money ok",u"优惠金额"+str(down[0]))

                #调减金额
                dscminmoney+=down[4]
                if down[0][:2]=="LT" and len(subject)>5:
                    orminmoney=abs(float(subject[5]))
                else:
                    orminmoney=0.0
                self.assernote(str(down[4]),str(orminmoney),u"调减金额不相同（零售金额统计报表明细和原始单据）","reportdetail ornote min money ok",u"调减金额"+str(down[0]))

                #会员储值
                dscvipcate+=down[6]
                if len(subject)>6:
                   orvipcate= -float(subject[6])
                else:
                    orvipcate=0.0
                self.assernote(str(down[6]),str(orvipcate),u"会员储值不相同（零售金额统计报表明细和原始单据）","reportdetail ornote vip cate ok",u"会员储值"+str(down[0]))

                #积分抵扣金额
                dscvipmin+=down[5]

                #零售销售总金额，零售退货总金额 现金 会员储值
                #print "down..."
                #print down
                if down[0][:2]=='LS':
                    lsinmoney+=down[1]
                    lsinvipcate+=down[6]
                elif down[0][:2]=='LT':
                    lsremoney+=down[1]
                    lsrevipcate+=down[6]

                m+=1

            #页面sumdown
            #print "sumdown......"
            urlsumdown="http://beefun.wsgjp.com/Carpa.Web/Carpa.Web.Script.DataService.ajax/GetPagerSummary"
            sumdatadown={"pagerId":pageid[:-11]+"billDetail_pager1"}
            sumtextdown=requests.post(url=urlsumdown,data=json.dumps(sumdatadown),headers=header)
            pagesumdown=browser.datatrunjson(sumtextdown)
            #print pagesumdown

            #现金金额
            self.assernote(str(pagesumdown["cashmoneydetail"]["value"]),str(dsccash),u"现金金额不相同（零售金额统计报表和其明细）","reportdetail sum down money ok",u"现金金额,经手人"+str(people[0]))

            #银行卡金额
            self.assernote(str(pagesumdown["bankcardcash"]["value"]),str(dsccard),u"银行卡金额不相同（零售金额统计报表和其明细）","reportdetail sum down bankcard money ok",u"银行卡金额,经手人"+str(people[0]))

            #优惠金额
            self.assernote(str(pagesumdown["preferencedetail"]["value"]),str(dscdismoney),u"优惠金额不相同（零售金额统计报表和其明细）","reportdetail sum down discount money ok",u"优惠金额,经手人"+str(people[0]))

            #调减金额
            self.assernote(str(pagesumdown["changetotaldetail"]["value"]),str(dscminmoney),u"调减金额不相同（零售金额统计报表和其明细）","reportdetail sum down min money ok",u"调减金额,经手人"+str(people[0]))

            #会员储值
            self.assernote(str(pagesumdown["vipmemberrecharge"]["value"]),str(dscvipcate),u"会员储值不相同（零售金额统计报表和其明细）","reportdetail sum down vip cate money ok",u"会员储值,经手人"+str(people[0]))

            #积分抵扣金额
            self.assernote(str(pagesumdown["vipmemberducrate"]["value"]),str(dscvipmin),u"积分抵扣金额不相同（零售金额统计报表和其明细）","reportdetail sum down vip scpres money ok",u"积分抵扣金额,经手人"+str(people[0]))


            #up detail
            print u"零售金额统计uplists...."

            #零售销售总金额
            #现金
            float(people[5])
            cupmoney+=float(people[5])
            self.assernote(str(float(people[5])),str(lsinmoney),u"现金不相同（零售金额统计报表up和其明细down sum）","reportdetail up money ok",u"零售销售现金"+str(people[0]))
            #print "people.........."
            #print people

            #会员储值
            float(people[3])
            cupvipcharge+=float(people[3])

            self.assernote(str(float(people[3])),str(lsinvipcate),u"会员储值不相同（零售金额统计报表up和其明细down sum）","reportdetail vip cate ok",u"零售销售会员储值"+str(people[0]))

            #积分抵扣总金额
            float(people[2])
            cupsocremin+=float(people[2])
            self.assernote(str(float(people[2])),str(pagesumdown["vipmemberducrate"]["value"]),u"积分抵扣总金额不相同（零售金额统计报表up和其明细down sum）","reportdetail vip min scores ok",u"积分抵扣总金额"+str(people[0]))

            #优惠总金额
            cupdismoney+=float(people[6])
            self.assernote(str(float(people[6])),str(pagesumdown["preferencedetail"]["value"]),u"优惠总金额不相同（零售金额统计报表up和其明细down sum）","reportdetail up discount money ok",u"优惠总金额"+str(people[0]))


            #零售退货总金额
            #现金
            float(people[7])
            cuprecash+=float(people[7])
            self.assernote(str(float(people[7])),str(abs(lsremoney)),u"现金不相同（零售金额统计报表up和其明细down sum）","reportdetail back money ok",u"零售退货现金"+str(people[0]))

            #会员储值
            float(people[4])
            cuprevipcharge+=float(people[4])
            self.assernote(str(float(people[4])),str(abs(lsrevipcate)),u"会员储值不相同（零售金额统计报表up和其明细down sum）","reportdetail vip back cate ok",u"零售退货会员储值"+str(people[0]))

            #调减总金额
            float(people[8])
            cupredismoney+=float(people[8])
            self.assernote(str(float(people[8])),str(pagesumdown["changetotaldetail"]["value"]),u"调减总金额不相同（零售金额统计报表up和其明细down sum）","reportdetail up min money ok",u"调减总金额"+str(people[0]))


            #零售总金额
            float(people[9])
            cupsalemoney+=float(people[9])
            self.assernote(str(float(people[9])),str(float(people[5])+float(people[3])-float(people[7])-float(people[4])),u"零售总金额不相同（零售金额统计报表up和其明细up detail）","reportdetail up sale money ok",u"零售总金额"+str(people[0]))

            n+=1



        #页面sumup
        print u"零售金额统计sumup........."
        urlsum="http://beefun.wsgjp.com/Carpa.Web/Carpa.Web.Script.DataService.ajax/GetPagerSummary"
        sumdata={"pagerId":pageid}
        sumtext=requests.post(url=urlsum,data=json.dumps(sumdata),headers=header)
        pagesum=browser.datatrunjson(sumtext)
        #print pagesum

        #零售销售总金额
        #现金
        self.assernote(str(pagesum["cashtotal"]["value"]),str(cupmoney),u"现金不相同（零售金额统计报表和其页面统计）","report sum up money ok",u"零售销售总金额")

        #会员储值
        self.assernote(str(pagesum["vipmemberrechargetotal"]["value"]),str(cupvipcharge),u"会员储值不相同（零售金额统计报表和其页面统计）","report sum up vip charge ok",u"零售销售总金额")

        #积分抵扣总金额
        self.assernote(str(pagesum["vipmemberducratetotal"]["value"]),str(cupsocremin),u"积分抵扣总金额不相同（零售金额统计报表和其页面统计）","report sum up vip min ok",u"积分抵扣总金额")

        #优惠总金额
        self.assernote(str(pagesum["preference"]["value"]),str(cupdismoney),u"优惠总金额不相同（零售金额统计报表和其页面统计）","report sum up discount total ok",u"优惠总金额")

        #零售退货总金额
        #现金
        self.assernote(str(pagesum["cashbacktotal"]["value"]),str(cuprecash),u"现金不相同（零售金额统计报表和其页面统计）","report sum back money ok",u"零售退货总金额")

        #会员储值
        self.assernote(str(pagesum["vipmeberrechargebacktotal"]["value"]),str(cuprevipcharge),u"会员储值不相同（零售金额统计报表和其页面统计）","report sum vip back charge ok",u"零售退货总金额")

        #调减总金额
        self.assernote(str(pagesum["changetotal"]["value"]),str(cupredismoney),u"调减总金额不相同（零售金额统计报表和其页面统计）","report sum back distotal ok",u"调减总金额")

        #零售总金额
        self.assernote(str(pagesum["counttotal"]["value"]),str(cupsalemoney),u"零售总金额不相同（零售金额统计报表和其页面统计）","report sum sale money ok",u"零售总金额")





if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()