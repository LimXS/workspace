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

class saleincountTest(unittest.TestCase):
    u'''报表-批发零售报表-批零业务毛利统计'''

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



    def assernote(self,num1,num2,note,noteok,flag):
        try:
            self.assertEqual(num1,num2,msg=note)
            print noteok
        except AssertionError,msg:
            print msg
            print flag
            print num1
            print num2


    def testSaleincount(self):
        u'''报表-批发零售报表-批零业务毛利统计'''

        header={'cookie':self.cookiestr,"Content-Type": "application/json"}
        header2={'cookie':self.cookiestr,"Content-Type": "application/x-www-form-urlencoded"}

        stamp=browser.gettimestamp()

        #页面id
        incomeidurl="http://beefun.wsgjp.com/Beefun/Report/ProductsSaleCostQuery.gspx"
        incomidda="{\"btypeid\":null,\"bfullname\":\"全部单位\",\"etypeid\":null,\"efullname\":\"全部职员\",\"ktypeid\":null,\"kfullname\":\"全部仓库\",\"ptypeid\":null,\"pfullname\":\"全部商品\",\"begin\":\""+str(stamp[3])+"\",\"end\":\""+str(stamp[2])+"\",\"saveDate\":false}"
        indataid={"__Params":incomidda}
        inidtext=requests.post(url=incomeidurl,data=indataid,headers=header2)
        #pagetext=inidtext.text
        pageid=browser.getpageid(inidtext)
        #print pageid

        #报表页面统计
        incomsumurl="http://beefun.wsgjp.com/Carpa.Web/Carpa.Web.Script.DataService.ajax/GetPagerSummary"
        insumdata={"pagerId":pageid}
        incomsumtext=requests.post(url=incomsumurl,data=json.dumps(insumdata),headers=header)
        incomsum=browser.datatrunjson(incomsumtext)
        #print incomsum

        #报表明细数据
        incomeurl="http://beefun.wsgjp.com/Carpa.Web/Carpa.Web.Script.DataService.ajax/GetPagerData"
        incomedata={"pagerId":pageid,"queryParams":{"btypeid":None,"etypeid":None,"ktypeid":None,"ptypeid":None,"begin":stamp[3],"end":stamp[2],"redold":-1,"vchtype":0,"orderClause":"order by ndx.date"},"orders":None,"filter":None,"first":0,"count":100000}
        incometext=requests.post(url=incomeurl,data=json.dumps(incomedata),headers=header)
        incomelists=browser.datatrunjson(incometext)
        #print incomelists

        salemoney=0
        salecost=0
        salein=0
        saledis=0
        saletran=0
        n=0
        for data in incomelists["itemList"]["rows"]:
            n=n+1
            print "\n"
            print u"报表第"+str(n)+u"行数据："+str(data[3])
            #获取原始单据
            Vchtype=data[13]
            Vchcode=data[0]

            #进货、退货明细
            if data[3][:2]=='XS'or data[3][:2]=='XT':
                if data[3][:2]=='XS':
                    noteouturl="http://beefun.wsgjp.com.cn/Beefun/Bill/SaleBill.gspx?Vchtype="+str(Vchtype)+"&Vchcode="+str(Vchcode)+"&Mode=Read"
                    notedetail=requests.get(noteouturl,headers=header)
                elif data[3][:2]=='XT':
                    notebackurl="http://beefun.wsgjp.com.cn/Beefun/Bill/SaleBackBill.gspx?Vchtype="+str(Vchtype)+"&Vchcode="+str(Vchcode)+"&Mode=Read"
                    notedetail=requests.get(notebackurl,headers=header)

                else:
                    print u"不是XS也不是XT..............."

                #header
                orheader=browser.getnotehead2(notedetail)
                #print "orheader...."
                #print orheader


            elif data[3][:2]=='XH':
                noteexurl="http://beefun.wsgjp.com.cn/Beefun/Bill/SaleChangeBill.gspx?Vchtype="+str(Vchtype)+"&Vchcode="+str(Vchcode)+"&Mode=Read"
                notedetail=requests.get(noteexurl,headers=header)

                #header
                orheader=browser.getnotehead2(notedetail)
                #print "orheader...."
                #print orheader


            elif data[3][:2]=='LS':
                noteexurl="http://beefun.wsgjp.com/Beefun/Bill/SaleBill.gspx?Vchtype="+str(Vchtype)+"&Vchcode="+str(Vchcode)+"&Mode=Read"
                notedetail=requests.get(noteexurl,headers=header)
                orheader=browser.getnotehead2(notedetail)

            elif data[3][:2]=='LT':
                noteexurl="http://beefun.wsgjp.com/Beefun/Bill/SaleBackBill.gspx?Vchtype="+str(Vchtype)+"&Vchcode="+str(Vchcode)+"&Mode=Read"
                notedetail=requests.get(noteexurl,headers=header)
                orheader=browser.getnotehead2(notedetail)


            else:
                #print u"不是商品进货/退货模式的单据(报表)"
                #print number
                continue

            orde=notedetail.text

            #销售收入[3]、销售成本[2]、应交税金[4]、应付款合计[5]
            saledataurl="http://beefun.wsgjp.com/Beefun/Beefun.Bill.SaleBackBill.ajax/LoadDlyaString"
            saledata={"vchcode":orheader[24]}
            saletext=requests.post(url=saledataurl,data=json.dumps(saledata),headers=header)
            saletext=saletext.text.replace(u"：",":")
            saletext=saletext.replace("\"","\\r")
            #print "saletext........."
            #print saletext
            sale=re.findall(":(.*?)\\\\r",saletext)

            #日期

            ordata=browser.handlestampdays(str(data[2]),1)
            self.assernote(str(ordata),str(orheader[43][:10]),u"日期不相同（批零业务毛利统计报表和其原始单据）","report date ok",data[3])

            #单据编号
            #data[3]

            #单位名称
            self.assernote(data[9],orheader[38],u"单位名称不相同（批零业务毛利统计报表和其原始单据）","report company name ok",data[3])
            #print "sale....."
            #print sale
            #print data
            if data[3][:2]=='XH':
                money=str(float(sale[2].strip()))
                cost=str(float(sale[3].strip()))
            elif data[3][:2]=='LT':
                if len(sale)>4:
                    money=str(float(sale[4].strip()))
                else:
                    money=str(float(sale[2].strip()))
                cost=str(float(sale[3].strip()))

            elif data[3][:2]=='LS':
                if len(sale)==8:
                    money=str(float(sale[4].strip()))
                    cost=str(float(sale[3].strip()))
                else:
                    money=str(float(sale[4].strip()))
                    cost=str(float(sale[3].strip()))

            else:
                money=str(float(sale[3].strip()))
                cost=str(float(sale[2].strip()))
            #销售收入
            self.assernote(str(float(data[5])),money,u"销售收入不相同（批零业务毛利统计报表和其原始单据）","report sale money ok",data[3])
            salemoney += float(data[5])

            #销售成本
            self.assernote(str(float(data[6])),str(cost),u"销售成本不相同（批零业务毛利统计报表和其原始单据）","report sale cost ok",data[3])
            salecost += float(data[6])

            #销售毛利
            float(data[7])
            salein += float(data[7])
            self.assernote(str(float(data[7])),str(float(data[5])-float(data[6])),u"销售毛利不相同（批零业务毛利统计报表和其页面）","report sale income ok",data[3])

            #毛利率
            perincom=float(data[7])/float(data[5])*100
            perincom=round(perincom,2)
            self.assernote(str(float(data[8])),str(perincom),u"毛利率不相同（批零业务毛利统计报表和其页面）","report percent income ok",data[3])


            #整单优惠
            dismoeny=re.findall("\"preference\":(.*?),",orde)
            self.assernote(str(float(data[18])),str(float(dismoeny[0])),u"整单优惠不相同（批零业务毛利统计报表和其原始单据）","report discount money ok",data[3])

            saledis += float(data[18])

            #买家运费
            #float(data[19])
            freighttype=re.findall("\"freighttype\":(.*?),",orde)
            #self.assernote(str(float(data[19])),str(float(freighttype[0])),u"买家运费不相同（批零业务毛利统计报表和其原始单据）","report transports money ok",data[3])

            saletran+=float(data[19])

            #经手人
            self.assernote(data[10],orheader[39],u"经手人不相同（批零业务毛利统计报表和其原始单据）","report pass people ok",data[3])

            #部门
            if str(orheader[40])=="null":
                department=''
            else:
                department=orheader[40]
            self.assernote(data[11],department,u"部门不相同（批零业务毛利统计报表和其原始单据）","report department ok",data[3])

            #仓库
            if data[3][:2]=='XH':
                cate=orheader[4]
            else:
                cate=orheader[2]
            self.assernote(data[12],cate,u"仓库不相同（批零业务毛利统计报表和其原始单据）","report cate ok",data[3])

            #摘要
            self.assernote(data[4],orheader[12],u"摘要不相同（批零业务毛利统计报表和其原始单据）","report summary ok",data[3])

            #单据类型
            if data[3][:2]=='XS':
                notetype=u"销售出库单"
            elif data[3][:2]=='XT':
                notetype=u"销售退货"
            elif data[3][:2]=='XH':
                notetype=u"销售换货单"
            elif data[3][:2]=='LS':
                notetype=u"销售出库单"
            elif data[3][:2]=='LT':
                notetype=u"销售退货"
            else:
                notetype=u"无此单据类型"
            self.assernote(str(data[15]),notetype,u"单据类型不相同（批零业务毛利统计报表和其原始单据）","report note type ok",data[3])

        #页面统计sum
        print u"页面统计sum..........."
        #print incomsum
        #print float(salemoney),float(salecost),float(salein)
        #销售收入
        self.assernote(str(float(incomsum["total"]["value"])),str(float(salemoney)),u"销售收入不相同（批零业务毛利统计报表和其页面统计）","report sale money ok",u"批零业务毛利统计")

        #销售成本
        self.assernote(str(float(incomsum["costtotal"]["value"])),str(float(salecost)),u"销售成本不相同（批零业务毛利统计报表和其页面统计）","report sale cost ok",u"销售成本")

        #销售毛利
        self.assernote(str(float(incomsum["gain"]["value"])),str(float(salein)),u"销售毛利不相同（批零业务毛利统计报表和其页面统计）","report income ok",u"销售毛利")

        #整单优惠
        #float(incomsum["preference"]["value"])
        self.assernote(str(float(incomsum["preference"]["value"])),str(saledis),u"整单优惠不相同（批零业务毛利统计报表和其页面统计）","report sale discount ok",u"整单优惠")

        #买家运费
        tran=float(incomsum["buyerfreight"]["value"])+float(incomsum["salerfreight"]["value"])
        self.assernote(str(tran),str(saletran),u"买家运费不相同（批零业务毛利统计报表和其页面统计）","report sale pass money ok",u"买家运费")

        #总条数


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()