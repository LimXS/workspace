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

class lsstorecountTest(unittest.TestCase):
    u'''报表-批发零售报表-门店零售统计'''

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


    def testLsstorecount(self):
        u'''报表-批发零售报表-门店零售统计'''

        header={'cookie':self.cookiestr,"Content-Type": "application/json"}
        header2={'cookie':self.cookiestr,"Content-Type": "application/x-www-form-urlencoded"}

        stamp=browser.gettimestamp()
        #单据中心
        #pagedic=browser.notecentel(header)
        #print pagedic
        #print pagedic["itemList"]
        #报表页面
        dom = xml.dom.minidom.parse(r'C:\workspace\moc.pjgsw.nufeeb\src\salereports\salereportsxpath')

        module1=browser.xmlRead(self.driver,dom,"module",4)
        module2=browser.xmlRead(self.driver,dom,'moduledetail',4)
        module3=browser.xmlRead(self.driver,dom,'moduledetail2',4)
        #print module3
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
        reurlid="http://beefun.wsgjp.com/Beefun/Report/StoreRetailStatistics.gspx"
        retext=browser.handleorderRead(self.driver,reurlid,header3)
        #print retext
        repageid=browser.getpageid(retext,1)
        #print repageid

        #print stamp
        #report list
        reurl="http://beefun.wsgjp.com/Carpa.Web/Carpa.Web.Script.DataService.ajax/GetPagerData"
        data={"pagerId":repageid,"queryParams":{"mode":"storecode","key":"","begin":stamp[3],"end":stamp[2]},"orders":None,"filter":None,"first":0,"count":100000}
        repadetail=browser.pagedetail(reurl,data,header3)

        #print repadetail["itemList"]["rows"]
        #门店信息
        mdurlid="http://beefun.wsgjp.com/Beefun/BaseInfo/StoreList.gspx"
        mdidtext=browser.handleorderRead(self.driver,mdurlid,header3)
        mdid=browser.getpageid(mdidtext,1)
        #print mdid
        #门店list
        mendata={"pagerId":mdid,"queryParams":None,"orders":None,"filter":None,"first":0,"count":100000}
        menlists=browser.reportdetail(mendata,header3)
        print "menlists........"
        print menlists["itemList"]["rows"]

        mdname=""
        mdcode=""
        for relist in repadetail["itemList"]["rows"]:
            #report detail
            if relist[2]==0:
                continue
            #detailid
            deurlid="http://beefun.wsgjp.com/Beefun/Report/StoreRetailList.gspx"
            storeid=relist[2]
            reiddeda="{\"begin\":\""+stamp[3]+"\",\"end\":\""+stamp[2]+"\",\"storeid\":"+str(storeid)+"}"
            dadataid={"__Params":reiddeda}
            deidtext=browser.pagedetail(deurlid,dadataid,header4,2)
            #print deidtext
            deid=browser.getpageid(deidtext,1)

            #print deid
            #detail
            dedata={"pagerId":deid,"queryParams":None,"orders":None,"filter":None,"first":0,"count":100000}
            detaillists=browser.reportdetail(dedata,header3)
            #print detaillists["itemList"]["rows"]

            cdemoney=0
            cdedismoney=0
            salenumbers=0
            for dedetail in detaillists["itemList"]["rows"]:
                #原始单据
                number=dedetail[2]
                if number[:3]=='LS-':
                    #print
                    print u"单据号为："+str(number)
                    vchcode=dedetail[8]
                    vchtypeid=dedetail[3]
                    noteurl="http://beefun.wsgjp.com/Beefun/Bill/SaleBill.gspx?Vchtype="+str(vchtypeid)+"&Vchcode="+vchcode+"&Mode=Read"
                    notetext=requests.get(url=noteurl,headers=header)
                elif number[:3]=='LT-':
                    print u"单据号为："+str(number)
                    vchcode=dedetail[8]
                    vchtypeid=dedetail[3]
                    noteurl="http://beefun.wsgjp.com/Beefun/Bill/SaleBackBill.gspx?Vchtype="+str(vchtypeid)+"&Vchcode="+vchcode+"&Mode=Read"
                    notetext=requests.get(url=noteurl,headers=header)
                    #print notetext.text
                    #noteheader=browser.getnotehead2(notetext)
                else:
                    continue

                #原始单据头/尾
                noteheader=browser.getnotehead2(notetext)
                notefoot=browser.getnotefoot(notetext)
                #原始单据明细
                notedetail=browser.salenoteoutdata(notetext)

                #门店、收银台id
                idstore=""
                idpos=""
                if number[:2]=="LS":
                    idstore=notefoot[7]
                    idpos=notefoot[8]
                elif number[:2]=="LT":
                    idstore=notefoot[9]
                    idpos=notefoot[10]
                else:
                    print u"无此单据类型"
                whichdesk=""
                for mendetail in menlists["itemList"]["rows"]:
                    if mendetail[0]==idstore:
                        mdcode=mendetail[1]
                        mdname=mendetail[2]
                        deskurl="http://beefun.wsgjp.com/Beefun/BaseInfo/RetailCashierList.gspx?storeid="+str(idstore)
                        desktext=requests.get(url=deskurl,headers=header3)
                        deskdic=browser.reportgetdata(desktext)
                        #print "deskdic........"
                        #print deskdic
                        for desk in deskdic:
                            deskinfo=re.findall("(.*?),",desk)
                            #print "deskinfo....."
                            #print deskinfo
                            if deskinfo[0]==idpos:
                                whichdesk=deskinfo[2]
                                break
                        break

                desalenumbers=0
                for a in notedetail:
                    detail=browser.dbnotedetail(a)
                    #print "detail....."
                    #print detail
                    if number[:3]=='LT-':
                        desalenumbers-=float(detail[19])
                    else:
                        desalenumbers+=float(detail[19])
                #print noteheader
                #print len(noteheader)
                #print notefoot
                #print dedetail
                salenumbers+=desalenumbers

                #单据编号
                #print dedetail[2]
                self.assernote(str(dedetail[2]),str(noteheader[11]),u"单据编号不相同（门店零售单和其原始单据）","report note id ok",dedetail[2])

                #业务类型
                #dedetail[12]
                money=0.0
                alldis=0.0
                sexnum=0.0
                sexmoney=0.0
                sexgive=0.0
                daydate=browser.handlestampdays(noteheader[6][9:-1],1)
                if dedetail[2][:2]=="LT":
                    service=u"# 销售退货"
                    money=-float(noteheader[8])
                    alldis=-float(notefoot[15])
                    sexnum=0.0000
                    sexmoney=0.0000
                    sexgive=float(notefoot[8])

                elif dedetail[2][:2]=="LS":
                    service=u"# 销售"
                    money=float(noteheader[8])
                    alldis=float(notefoot[26])
                    sexnum=float(notefoot[9])
                    sexmoney=float(notefoot[10])
                    sexgive=float(notefoot[12])
                else:
                    service=u"不应该出现的类型"
                self.assernote(str(dedetail[13]),str(service),u"业务类型不相同（门店零售单和其页面数据）","report note id ok",dedetail[2])
                #日期
                self.assernote(str(dedetail[15]),str(daydate),u"日期不相同（门店零售单和其原始单据）","report day date ok",dedetail[2])

                #收银员
                self.assernote(str(dedetail[11]),str(noteheader[41]),u"收银员不相同（门店零售单和其原始单据）","report money people ok",dedetail[2])

                #营业员
                self.assernote(str(dedetail[12]),str(noteheader[39]),u"营业员不相同（门店零售单和其原始单据）","report business people ok",dedetail[2])

                #收银机
                self.assernote(str(dedetail[9]),str(whichdesk),u"收银机不相同（门店零售单和其原始单据）","report which desk ok",dedetail[2])

                #过账时间
                self.assernote(str(dedetail[16]),str(noteheader[43]),u"过账时间不相同（门店零售单和其原始单据）","report pass time ok",dedetail[2])

                #金额
                cdemoney+=dedetail[0]
                self.assernote(str(dedetail[0]),str(money),u"金额不相同（门店零售单和其原始单据）","report money ok",dedetail[2])

                #整单优惠
                cdedismoney+=dedetail[1]
                aldis=float(dedetail[1])
                self.assernote(str(dedetail[1]),str(alldis),u"整单优惠不相同（门店零售单和其原始单据）","report all discount ok",dedetail[2])

                #积分兑换数目
                self.assernote(str(dedetail[4]),str(sexnum),u"积分兑换数目不相同（门店零售单和其原始单据）","report scores exchange nums ok",dedetail[2])

                #积分兑换金额

                self.assernote(str(dedetail[5]),str(sexmoney),u"积分兑换金额不相同（门店零售单和其原始单据）","report scores exchange money ok",dedetail[2])

                #消费赠送积分数目
                self.assernote(str(dedetail[6]),str(sexgive),u"消费赠送积分数目不相同（门店零售单和其原始单据）","report give scores ok",dedetail[2])


            #detailsum
            print u"报表明细页面detail sum.............."
            detailsum=browser.reportsumdata(deid,header3)
            #print detailsum

            #金额
            self.assernote(str(detailsum["total"]["value"]),str(cdemoney),u"金额不相同（门店零售单和其页面统计）","report money ok",u"金额")

            #整单优惠
            self.assernote(str(detailsum["preference"]["value"]),str(cdedismoney),u"整单优惠不相同（门店零售单和其页面统计）","report all discount ok",u"整单优惠")


            #门店名称
            self.assernote(str(relist[0]),str(mdname),u"门店名称不相同（门店零售统计和门店零售单）","report mendian name ok",u"门店名称")

            #门店编号
            if relist[1]!="false":
                storeno=relist[1]
            else:
                storeno=""
            self.assernote(str(storeno),str(mdcode),u"门店编号不相同（门店零售统计和门店零售单）","report mendian code ok",u"门店编号")

            #零售数量
            self.assernote(str(relist[3]),str(salenumbers),u"零售数量不相同（门店零售统计和门店零售单）","report sale numbers ok",u"零售数量")

            #零售金额
            resalemoney=float(detailsum["total"]["value"])-float(detailsum["preference"]["value"])
            self.assernote(str(float(relist[4])-float(relist[7])),str(resalemoney),u"零售金额不相同（门店零售统计和门店零售单）","report sale money ok",u"零售金额")

            #成交笔数
            self.assernote(str(relist[6]),str(len(detaillists["itemList"]["rows"])),u"成交笔数不相同（门店零售统计和门店零售单）","report ok numbers order ok",u"成交笔数")





if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()