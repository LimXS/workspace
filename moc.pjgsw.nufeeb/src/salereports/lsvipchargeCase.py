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

class lsvipchargeTest(unittest.TestCase):
    u'''报表-批发零售报表-会员储值变动记录'''

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


    def testLsvipcharge(self):
        u'''报表-批发零售报表-会员储值变动记录'''

        header={'cookie':self.cookiestr,"Content-Type": "application/json"}
        header2={'cookie':self.cookiestr,"Content-Type": "application/x-www-form-urlencoded"}

        stamp=browser.gettimestamp(1)
        #print stamp
        #单据中心
        #pagedic=browser.notecentel(header)
        #print pagedic
        #print pagedic["itemList"]
        #print pagedic["itemList"][0]["number"]


        #报表页面
        dom = xml.dom.minidom.parse(r'C:\workspace\moc.pjgsw.nufeeb\src\salereports\salereportsxpath')

        module1=browser.xmlRead(self.driver,dom,"module",1)
        module2=browser.xmlRead(self.driver,dom,'moduledetail',1)
        module3=browser.xmlRead(self.driver,dom,'moduledetail2',1)
        #browser.openModule3(self.driver,module1,module2,module3)
        browser.findXpath(self.driver,module1).click()
        browser.findXpath(self.driver,module2).click()
        browser.findXpath(self.driver,module3).click()

        time.sleep(2)
        cookie2 = [item["name"] + "=" + item["value"] for item in self.driver.get_cookies()]
        #print cookie
        cookiestr2 = ';'.join(item for item in cookie2)
        header3={'cookie':cookiestr2,"Content-Type": "application/json"}
        header4={'cookie':cookiestr2,"Content-Type": "application/x-www-form-urlencoded"}

        #页面Id
        reurlid="http://beefun.wsgjp.com/Beefun/VipMember/VipMemberRechargeList.gspx"
        retext=browser.handleorderRead(self.driver,reurlid,header3)
        #print retext
        repageid=browser.getpageid(retext,1)
        #print repageid

        #report list
        reurl="http://beefun.wsgjp.com/Carpa.Web/Carpa.Web.Script.DataService.ajax/GetPagerData"
        data={"pagerId":repageid,"queryParams":{"CardNumber":"","Name":"","VipMemberId":0,"Tel":"","BeginTime":stamp[3],"EndTime":stamp[2],"ViewRed":0},"orders":None,"filter":None,"first":0,"count":100000}
        repadetail=browser.pagedetail(reurl,data,header3)
        #print repadetail

        cchargemoney=0.0
        cgivemoney=0.0
        cusmoney=0.0
        cchangemoney=0.0
        k=0
        for redetail in repadetail["itemList"]["rows"]:
            k=k+1
            print u"报表第"+str(k)+u"行数据:"+str(redetail[5])
            #原始单据头
            Vchtype=redetail[6]
            Vchcode=redetail[3]
            lsurl="http://beefun.wsgjp.com/Beefun/Bill/SaleBill.gspx?Vchtype="+str(Vchtype)+"&Vchcode="+str(Vchcode)+"&Mode=Read"
            ortext=requests.get(lsurl,headers = header)
            #单据头
            if redetail[5][:2]=="SK":
                orheadertext=re.findall("\"details\":(.*?)fc_total",ortext.text)
                #print orheadertext
                orheader=orheadertext[0].replace("\"","")
                orheader=re.findall(":(.*?),",orheader)
            else:
                orheader=browser.getnotehead(ortext)

            #科目详情
            suburl="http://beefun.wsgjp.com/Beefun/Beefun.Bill.SaleBackBill.ajax/LoadDlyaString"
            vcode=redetail[3]
            subdata=browser.subjectdetail2(suburl,vcode,header3)

            #print redetail

            vipinfo=browser.vipinfo(header)
            vippeople=[]
            for vip in vipinfo["itemList"]["rows"]:
                if vip[0]==redetail[11]:
                    vippeople=vip
                    #卡号
                    self.assernote(str(redetail[0]),str(vippeople[7]),u"卡号不相同（会员储值变动记录和其原始单据）","report note vip card ok",redetail[5])

                    #卡类型
                    self.assernote(str(redetail[1]),str(vippeople[5]),u"卡类型不相同（会员储值变动记录和其原始单据）","report note vip card type ok",redetail[5])

                    #会员名
                    self.assernote(str(redetail[8]),str(vippeople[8]),u"会员名不相同（会员储值变动记录和其原始单据）","report note vip name ok",redetail[5])

                    #电话
                    self.assernote(str(redetail[9]),str(vippeople[10]),u"电话不相同（会员储值变动记录和其原始单据）","report note vip phone ok",redetail[5])

                    break
            if len(vippeople)==0:
                print u"会员管理无此会员，请核实...."

            #单据类型
            #redetail[7]
            if redetail[5][:2]=="SK":
                ortype=u"充值"
            elif redetail[5][:2]=="LT":
                ortype=u"销售退货单"
            else:
                ortype=u"销售单"
            self.assernote(str(redetail[7]),str(ortype),u"单据类型相同（会员储值变动记录和其原始单据）","report or type ok",redetail[5])


            #单据编号
            self.assernote(str(redetail[5]),str(orheader[11]),u"单据编号相同（会员储值变动记录和其原始单据）","report or number ok",redetail[5])

            #经手人
            if redetail[4]=='':
                handpeople="null"
            else:
                handpeople=redetail[4]
            self.assernote(str(handpeople),str(orheader[39]),u"经手人不相同（会员储值变动记录和其原始单据）","report or handpeople ok",redetail[5])

            if redetail[5][:2]=="SK":
                orchargemoney=float(subdata[1])
                orgivemoney=float(subdata[2])
                orusemoney=0.0
                orchangemoney=float(subdata[3])

                chargemoney=float(redetail[12])
            elif redetail[5][:2]=="LT":
                orchargemoney=float(subdata[6])
                orgivemoney=0.0
                orusemoney=0.0
                orchangemoney=float(subdata[6])

                chargemoney=float(redetail[12])
            else:
                orchargemoney=0.0
                orgivemoney=0.0
                if len(subdata)<7:
                    orusemoney=-float(subdata[5])
                    orchangemoney=float(subdata[5])
                else:
                    orusemoney=-float(subdata[6])
                    orchangemoney=float(subdata[6])

                chargemoney=float(redetail[13])

             #充值金额
            cchargemoney+=chargemoney
            self.assernote(str(chargemoney),str(orchargemoney),u"充值金额不相同（会员储值变动记录和其原始单据）","report or charge money ok",redetail[5])

            #赠送金额
            cgivemoney+=float(redetail[13])
            self.assernote(str(redetail[13]),str(orgivemoney),u"赠送金额不相同（会员储值变动记录和其原始单据）","report or give money ok",redetail[5])

            #使用金额
            if redetail[22]=="false":
                usemoney=0.0
            else:
                usemoney=float(redetail[22])
            cusmoney+=usemoney

            self.assernote(str(usemoney),str(orusemoney),u"使用金额不相同（会员储值变动记录和其原始单据）","report or use money ok",redetail[5])

            #变动金额
            cchangemoney+=float(redetail[15])
            self.assernote(str(redetail[15]),str(orchangemoney),u"变动金额不相同（会员储值变动记录和其原始单据）","report or change money ok",redetail[5])

            #变动账户
            #redetail[20]
            if redetail[5][:2]=="SK":
                skurl="http://beefun.wsgjp.com/Beefun/Bill/GatheringBill.gspx?Vchtype="+str(Vchtype)+"&Vchcode="+str(Vchcode)+"&Mode=Read"
                orsktext=requests.get(skurl,headers = header)
                orfullname=re.findall("\"fullname\":\"(.*?)\"",orsktext.text)
                orfullname=orfullname[0]
            else:
                orfullname=""
            if redetail[20]=="false":
                fullname=""
            else:
                fullname=redetail[20]
            self.assernote(str(fullname),str(orfullname),u"变动账户不相同（会员储值变动记录和其原始单据）","report or change account ok",redetail[5])



            #变动单位
            self.assernote(str(redetail[19]),str(orheader[38]),u"变动单位不相同（会员储值变动记录和其原始单据）","report or change company ok",redetail[5])

            #录单日期
            #self.assernote(str(redetail[16]),str(orheader[43]),u"录单日期不相同（会员储值变动记录和其原始单据）","report or date ok",u"录单日期")

            #备注
            if orheader[13]=="":
                if redetail[5][:2]=="SK":
                    orbeizhu=""
                elif redetail[5][:2]=="LT":
                    orbeizhu=u"零售退货会员卡储值退款"
                else:
                    orbeizhu=u"零售会员卡储值消费"
            else:
                orbeizhu=orheader[13]
            self.assernote(str(redetail[14]),str(orbeizhu),u"备注不相同（会员储值变动记录和其原始单据）","report or beizhu ok",redetail[5])

        #report sum
        print u"报表页面统计sum.............."
        resum=browser.reportsumdata(repageid,header3)
        #print resum

        #充值金额
        self.assernote(str(resum["artotal"]["value"]),str(cchargemoney),u"充值金额不相同（会员储值变动记录和其页面统计）","report sum charge money ok",u"充值金额")

        #赠送金额
        #resum["favorabletotal"]["value"]
        self.assernote(str(resum["favorabletotal"]["value"]),str(cgivemoney),u"赠送金额不相同（会员储值变动记录和其页面统计）","report sum give money ok",u"赠送金额")

        #使用金额
        #resum["aptotal"]["value"]
        self.assernote(str(resum["aptotal"]["value"]),str(cusmoney),u"使用金额不相同（会员储值变动记录和其页面统计）","report sum use money ok",u"使用金额")

        #变动金额
        #resum["balancetotal"]["value"]
        self.assernote(str(resum["balancetotal"]["value"]),str(cchangemoney),u"变动金额不相同（会员储值变动记录和其页面统计）","report sum change money ok",u"变动金额")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()