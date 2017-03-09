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

class lscashsalelogTest(unittest.TestCase):
    u'''报表-批发零售报表-收银台销售流水'''

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


    def testLscashsalelog(self):
        u'''报表-批发零售报表-收银台销售流水'''

        header={'cookie':self.cookiestr,"Content-Type": "application/json"}
        header2={'cookie':self.cookiestr,"Content-Type": "application/x-www-form-urlencoded"}

        #单据中心
        pagedic=browser.notecentel(header)
        #print pagedic
        #print pagedic["itemList"]
        #print pagedic["itemList"][0]["number"]

        stamp=browser.gettimestamp()

        #报表页面
        dom = xml.dom.minidom.parse(r'C:\workspace\moc.pjgsw.nufeeb\src\salereports\salereportsxpath')

        module1=browser.xmlRead(self.driver,dom,"module",3)
        module2=browser.xmlRead(self.driver,dom,'moduledetail',3)
        module3=browser.xmlRead(self.driver,dom,'moduledetail2',3)
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
        reurlid="http://beefun.wsgjp.com/Beefun/Report/PosOrderList.gspx"
        retext=browser.handleorderRead(self.driver,reurlid,header3)
        #print retext
        repageid=browser.getpageid(retext,1)
        #print repageid

        #report list
        reurl="http://beefun.wsgjp.com/Carpa.Web/Carpa.Web.Script.DataService.ajax/GetPagerData"
        data={"pagerId":repageid,"queryParams":{"vchtype":0,"begin":stamp[3],"end":stamp[2],"storeid":0,"posid":0,"vipcardnumber":"","posetypeid":0,"efullname":None,"etypeid":0,"ptypeid":0,"fullname":None},"orders":None,"filter":None,"first":0,"count":100000}
        #browser.pagedetail(reurl,data,header3)
        #data={"pagerId":repageid,"queryParams":None,"orders":[{"dataField":"saledate","ascending":False}],"filter":None,"first":0,"count":100000}
        repadetail=browser.pagedetail(reurl,data,header3)
        #print repadetail["itemList"]["rows"]
        #print repadetail["itemList"]["rows"][4]
        #print len(repadetail["itemList"]["rows"][7])

        dismoney=0
        qty=0
        m=0
        flagnum=""
        for detail in repadetail["itemList"]["rows"]:
            m=m+1
            print u"单据第"+str(m)+u"行："+detail[32]
            #print detail
            itemqty=0
            itemmoney=0

            itemcode=""
            itemdpsigle=0
            itemdiscount=0
            itemdissigle=0
            notedis=0
            noetalldis=0
            cashpeople=""
            businesspeo=""
            vipcard=""
            itemtime=""
            #原始单据
            for orlist in pagedic["itemList"]:
                if flagnum!=orlist["number"]:
                    citemdpmoney=0
                    citemmoney=0
                    flagnum=orlist["number"]
                if orlist["number"]==detail[32]:
                    Vchcode=orlist["vchcode"]
                    Vchtype=orlist["vchtypeid"]
                    #print "orlist number..."
                    #print orlist["number"]
                    break
                else:
                    continue
            if detail[32][:2]=='XS'or detail[32][:2]=='XT':
                if detail[32][:2]=='XS':
                    noteouturl="http://beefun.wsgjp.com.cn/Beefun/Bill/SaleBill.gspx?Vchtype="+str(Vchtype)+"&Vchcode="+str(Vchcode)+"&Mode=Read"
                    notedetail=requests.get(noteouturl,headers=header)
                elif detail[32][:2]=='XT':
                    notebackurl="http://beefun.wsgjp.com.cn/Beefun/Bill/SaleBackBill.gspx?Vchtype="+str(Vchtype)+"&Vchcode="+str(Vchcode)+"&Mode=Read"
                    notedetail=requests.get(notebackurl,headers=header)

                else:
                    print u"不是XS也不是XT..............."

                #header
                orheader=browser.getnotehead2(notedetail)

                ordetail=browser.salenoteoutdata(notedetail)
                orfoot=[]
                #print len(ordetail)
                for ortemp in ordetail:
                    temp=browser.dbnotedetail(ortemp)
                    if temp[74]==detail[39]:
                        #print "temp......"
                        #print temp
                        itemcode=temp[78]
                        itemdpsigle=temp[11]
                        itemdiscount=temp[9]
                        itemdissigle=temp[20]
                        notedis=re.findall("\"preference\":(.*?),",notedetail.text)
                        notedis=float(notedis[0])
                        noetalldis=0.0
                        cashpeople=orheader[41]
                        businesspeo=orheader[39]
                        vipcard=""
                        itemtime=temp[44][9:-1]
                        if detail[32][:2]=='XS':
                            itemqty=float(temp[19])
                            itemmoney=float(temp[21])

                        elif detail[32][:2]=='XT':
                            itemqty=-float(temp[19])
                            itemmoney=-float(temp[21])
                            #cashpeople=orheader[41]
                            #businesspeo=orheader[39]

                        else:
                            print u"不是XS也不是XT..............."
                        break

            elif detail[32][:2]=='LS' or detail[32][:2]=='LT':
                if detail[32][:2]=='LS':
                    noteexurl="http://beefun.wsgjp.com/Beefun/Bill/SaleBill.gspx?Vchtype="+str(Vchtype)+"&Vchcode="+str(Vchcode)+"&Mode=Read"
                    notedetail=requests.get(noteexurl,headers=header)

                elif detail[32][:2]=='LT':
                    noteexurl="http://beefun.wsgjp.com/Beefun/Bill/SaleBackBill.gspx?Vchtype="+str(Vchtype)+"&Vchcode="+str(Vchcode)+"&Mode=Read"
                    notedetail=requests.get(noteexurl,headers=header)
                orheader=browser.getnotehead2(notedetail)
                ordetail=browser.salenoteoutdata(notedetail)
                orfoot=browser.getnotefoot(notedetail)
                for ortemp in ordetail:
                    temp=browser.dbnotedetail(ortemp)
                    #print temp[74]
                    #print temp[78]
                    if temp[74]==detail[39]:
                        #print "temp......"
                        #print temp
                        itemcode=temp[78]
                        itemdpsigle=temp[11]
                        itemdiscount=temp[9]
                        itemdissigle=temp[13]
                        itemtime=temp[44][9:-1]
                        notedis=re.findall("\"preference\":(.*?),",notedetail.text)
                        notedis=float(notedis[0])

                        cashpeople=orheader[41]
                        businesspeo=orheader[39]


                        #print "orfoot...."
                        #print orfoot
                        #print len(orfoot)
                        #print orheader
                        if orfoot!="":
                            vipinfo=browser.vipinfo(header)
                            #print vipinfo["itemList"]["rows"]
                            for vip in vipinfo["itemList"]["rows"]:
                                #print "vip...."
                                #print vip
                                #print vip[14]
                                if len(orfoot)>53:
                                    if vip[0]==orfoot[75]:
                                        vipcard=vip[7]
                                        noetalldis=vip[14]

                                else:
                                    if vip[0]==orfoot[51]:
                                        vipcard=vip[7]
                                        noetalldis=vip[14]

                        else:
                            vipcard=""
                        if detail[32][:2]=='LS':
                            itemqty=float(temp[19])
                            itemmoney=float(temp[12])

                        elif detail[32][:2]=='LT':
                            itemqty=-float(temp[19])
                            itemmoney=-float(temp[12])
                        break

                else:
                    #print u"不是商品进货/退货模式的单据(单据中心)"
                    #print number
                    continue

            #业务类型
            if detail[32][:2]=="LS"or detail[32][:2]=="XS":
                worktype=u"销售出库单"
            else:
                worktype=u"销售退货"
            self.assernote(str(detail[58]),str(worktype),u"业务类型不相同（收银台销售流水和其页面统计）","report work type ok",detail[32])

            #零售单号
            #detail[32]

            #销售时间
            #print "detail........"
            #print detail
            self.assernote(str(detail[11]),str(itemtime),u"销售时间不相同（收银台销售流水和其页面统计）","report sale time ok",detail[32])

            #商品编号xs52
            self.assernote(str(detail[42]),str(itemcode),u"商品编号不相同（收银台销售流水和其页面统计）","report item code ok",detail[32])

            #商品名称
            #detail[38]

            #数量
            qty+=float(detail[0])
            self.assernote(str(detail[0]),str(itemqty),u"数量不相同（收银台销售流水和其页面统计）","report item qty ok",detail[32])

            #零售价
            self.assernote(str("%.4f"%float(detail[8])),str(itemdpsigle),u"零售价不相同（收银台销售流水和其页面统计）","report dpsigle ok",detail[32])

            #折扣
            self.assernote(str("%.2f"%float(detail[6])),str(itemdiscount),u"折扣不相同（收银台销售流水和其页面统计）","report discount ok",detail[32])

            #折扣单价
            self.assernote(str("%.4f"%float(detail[5])),str(itemdissigle),u"折扣单价不相同（收银台销售流水和其页面统计）","report discount sigle ok",detail[32])

            #折后金额xt8 xs1
            dismoney+=float(detail[1])
            self.assernote(str(detail[1]),str(itemmoney),u"折后金额不相同（收银台销售流水和其页面统计）","report discount money ok",detail[32])

            #整单优惠
            self.assernote(str(detail[30]),str(notedis),u"整单优惠不相同（收银台销售流水和其页面统计）","report discount all moeny ok",detail[32])

            #整单折扣
            #print "detail....."
            #print detail
            self.assernote(str(detail[31]),str(float(noetalldis)),u"整单折扣不相同（收银台销售流水和其页面统计）","report discount all ok",detail[32])

            #收银员
            self.assernote(str(detail[60]),str(cashpeople),u"收银员不相同（收银台销售流水和其页面统计）","report cashpeople  ok",detail[32])

            #营业员
            self.assernote(str(detail[61]),str(businesspeo),u"营业员不相同（收银台销售流水和其页面统计）","report business people  ok",detail[32])

            #门店
            #print detail
            detail[35]
            #收银台
            detail[37]
            #会员卡号
            detail[56]

            vipinfo=browser.vipinfo(header)
            for vip in vipinfo["itemList"]["rows"]:
                if len(orfoot)>76:
                    if vip[0]==orfoot[75]:
                        #卡号
                        vipcard=vip[7]

            if detail[56]=="false":
                pvipcard=""
            else:
                pvipcard=detail[56]
            self.assernote(str(pvipcard),str(vipcard),u"会员卡号不相同（收银台销售流水和其页面统计）","report vip card ok",detail[32])

        print u"报表页面统计sum.............."
        #report sum
        resum=browser.reportsumdata(repageid,header3)
        #print resum

        #数量
        self.assernote(str(resum["qty"]["value"]),str(qty),u"数量不相同（收银台销售流水和其页面统计）","report sum qty ok",u"数量")

        #折后金额
        self.assernote(str(resum["total"]["value"]),str(dismoney),u"折后金额不相同（收银台销售流水和其页面统计）","report sum discount money ok",u"折后金额")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()