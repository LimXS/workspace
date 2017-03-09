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

class lsvipscoreschargeTest(unittest.TestCase):
    u'''报表-批发零售报表-会员积分变动记录'''

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
        #self.driver.close()
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


    def testLsvipscorescharge(self):
        u'''报表-批发零售报表-会员积分变动记录'''

        header={'cookie':self.cookiestr,"Content-Type": "application/json"}
        header2={'cookie':self.cookiestr,"Content-Type": "application/x-www-form-urlencoded"}

        stamp=browser.gettimestamp(1)

        #报表页面
        dom = xml.dom.minidom.parse(r'C:\workspace\moc.pjgsw.nufeeb\src\salereports\salereportsxpath')

        module1=browser.xmlRead(self.driver,dom,"module",2)
        module2=browser.xmlRead(self.driver,dom,'moduledetail',2)
        module3=browser.xmlRead(self.driver,dom,'moduledetail2',2)
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
        reurlid="http://beefun.wsgjp.com/Beefun/VipMember/VipMemberIntegralRecodList.gspx"
        retext=browser.handleorderRead(self.driver,reurlid,header3)
        #print retext
        repageid=browser.getpageid(retext,1)
        print repageid

        #report list
        reurl="http://beefun.wsgjp.com/Carpa.Web/Carpa.Web.Script.DataService.ajax/GetPagerData"
        data={"pagerId":repageid,"queryParams":None,"orders":None,"filter":None,"first":0,"count":100000}
        repadetail=browser.pagedetail(reurl,data,header3)
        print repadetail

        usescore=0
        minmoney=0
        givescore=0
        changescore=0
        k=0
        for redetail in repadetail["itemList"]:
            k=k+1
            print u"报表第"+str(k)+u"行数据:"+str(redetail["number"])
            #原始单据
            if str(redetail["number"])!="false":
                Vchtype=redetail["vchtypeid"]
                Vchcode=redetail["vchcode"]
                lsurl="http://beefun.wsgjp.com/Beefun/Bill/SaleBill.gspx?Vchtype="+str(Vchtype)+"&Vchcode="+str(Vchcode)+"&Mode=Read"
                ortext=requests.get(lsurl,headers = header)
                orheader=browser.getnotehead(ortext)
                orfoot=browser.getnotefoot(ortext)
            else:
                givescore+=float(redetail["addintegraltotal"])
                changescore+=float(redetail["changeintegraltotal"])
                continue

            vipinfo=browser.vipinfo(header)
            vippeople=[]
            for vip in vipinfo["itemList"]["rows"]:
                if vip[0]==orfoot[75]:
                    vippeople=vip
                    #卡号
                    self.assernote(str(redetail["cardnumber"]),str(vippeople[7]),u"卡号不相同（会员积分变动记录和其原始单据）","report note vip card ok",redetail["number"])

                    #卡类型
                    self.assernote(str(redetail["cardtypename"]),str(vippeople[5]),u"卡类型不相同（会员积分变动记录和其原始单据）","report note vip card type ok",redetail["number"])

                    #会员名
                    self.assernote(str(redetail["holdername"]),str(vippeople[8]),u"会员名不相同（会员积分变动记录和其原始单据）","report note vip name ok",redetail["number"])

                    #电话
                    self.assernote(str(redetail["holdertel"]),str(vippeople[10]),u"电话不相同（会员积分变动记录和其原始单据）","report note vip phone ok",redetail["number"])

                    break
            if len(vippeople)==0:
                print u"会员管理无此会员，请核实...."


            #单据类型
            if redetail["number"][:2]=="LS":
                notypr=u"销售单"
                comment=u"零售会员卡积分消费"
            elif redetail["number"][:2]=="LT":
                notypr=u"销售退货单"
                comment=u"零售退货会员卡积分扣除"
            else:
                notypr=u"初始赠送"
                comment=u"创建会员赠送积分"
            self.assernote(str(redetail["vchtypestr"]),notypr,u"单据类型不相同（会员积分变动记录和其原始单据）","report note type ok",redetail["number"])

            #单据编号
            self.assernote(str(redetail["number"]),str(orheader[11]),u"单据编号不相同（会员积分变动记录和其原始单据）","report note number ok",redetail["number"])

            #经手人
            self.assernote(str(redetail["fullname"]),str(orheader[39]),u"经手人不相同（会员积分变动记录和其原始单据）","report note handlepeople ok",redetail["number"])

            #使用积分
            usescore+=float(redetail["integraltotal"])
            orusescore=float(orfoot[9])
            self.assernote(str(redetail["integraltotal"]),str("%.1f"%orusescore),u"使用积分不相同（会员积分变动记录和其原始单据）","report use score ok",redetail["number"])

            #抵扣金额
            minmoney+=float(redetail["deductiontotal"])
            orminmont=float(orfoot[10])
            self.assernote(str(redetail["deductiontotal"]),str("%.1f"%orminmont),u"抵扣金额不相同（会员积分变动记录和其原始单据）","report min money ok",redetail["number"])

            #赠送积分
            givescore+=float(redetail["addintegraltotal"])
            if redetail["number"][:2]=="LT":
                score=-float(orfoot[12])
            else:
                score=float(orfoot[12])
            self.assernote(str(redetail["addintegraltotal"]),str(score),u"赠送积分不相同（会员积分变动记录和其原始单据）","report give money ok",redetail["number"])

            #积分变动
            changescore+=float(redetail["changeintegraltotal"])
            self.assernote(str(redetail["changeintegraltotal"]),str(float(redetail["addintegraltotal"])-float(redetail["integraltotal"])),u"积分变动不相同（会员积分变动记录和其原始单据）","report score change ok",redetail["number"])

            #变动日期
            #self.assernote(str(redetail["createtime"]),str(orheader[43]),u"变动日期不相同（会员积分变动记录和其原始单据）","report change date ok",redetail["number"])

            #备注
            self.assernote(str(redetail["comment"]),str(comment),u"备注不相同（会员积分变动记录和其原始单据）","report comment ok",redetail["number"])


        print u"报表页面统计sum.............."
        #report sum
        resum=browser.reportsumdata(repageid,header3)
        #print resum

        #使用积分
        float(resum["integraltotal"]["value"])
        self.assernote(str(resum["integraltotal"]["value"]),str(usescore),u"使用积分不相同（会员积分变动记录和其页面统计）","report sum use score ok",u"使用积分")

        #抵扣金额
        float(resum["deductiontotal"]["value"])
        self.assernote(str(resum["deductiontotal"]["value"]),str(minmoney),u"抵扣金额不相同（会员积分变动记录和其页面统计）","report sum min money ok",u"抵扣金额")

        #赠送积分
        float(resum["addintegraltotal"]["value"])
        self.assernote(str(resum["addintegraltotal"]["value"]),str(givescore),u"赠送积分不相同（会员积分变动记录和其页面统计）","report sum give score ok",u"赠送积分")

        #积分变动
        float(resum["changeintegraltotal"]["value"])
        self.assernote(str(resum["changeintegraltotal"]["value"]),str(changescore),u"积分变动不相同（会员积分变动记录和其页面统计）","report sum change score ok",u"积分变动")





if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()