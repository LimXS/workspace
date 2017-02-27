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

class saleorderTest(unittest.TestCase):
    u'''报表-批发零售报表-销售订单统计统计'''

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

    def testsaleOrder(self):
        u'''报表-批发零售报表-销售订单统计统计'''

        header={'cookie':self.cookiestr,"Content-Type": "application/json"}
        header2={'cookie':self.cookiestr,"Content-Type": "application/x-www-form-urlencoded"}


        print "销售订单管理......................................................................................."
        #销售订单管理页面id
        manidurl="http://beefun.wsgjp.com/Beefun/Carrier/OrderManager.gspx?vchtype=saleorder"
        manidtext=requests.get(manidurl,headers=header)
        #print manidtext.text
        manid=browser.getpageid(manidtext)
        #print manid

        #订单管理列表数据
        manurllists="http://beefun.wsgjp.com/Carpa.Web/Carpa.Web.Script.DataService.ajax/GetPagerData"
        urldata={"pagerId":manid,"queryParams":{"vchType":8,"xTypeid":"","isComplete":"0","isAudit":-1,"isExport":"-1","dlytype":-1},"orders":None,"filter":None,"first":0,"count":100000}
        manlits=requests.post(url=manurllists,headers=header,data=json.dumps(urldata))
        #print manlits.text
        manlisdic=browser.datatrunjson(manlits)
        #print manlisdic
        #print len(manlisdic["itemList"])


        #每一个订单的商品明细

        print  "销售订单商品明细..........................."
        n=0
        mannonums=0
        manoknums=0
        manrenums=0
        mannomoney=0
        manokmoney=0
        manremoney=0

        mandpmoney=0
        manmoney=0
        manaftermoeny=0

        for listdata in manlisdic["itemList"]:
            #print listdata
            n=n+1
            print "第"+str(n)+"行销售订单商品明细..............................."
            #订单编号
            number=listdata["number"]

            #获取每个订单详细数据并进行统计
            toqty=float(listdata["toqty"])
            untoqty=float(listdata["untoqty"])
            repairqty=float(listdata["repairqty"])
            repairtotal=listdata["repairtotal"]
            tototal=listdata["tototal"]
            untototal=listdata["untototal"]
            vchcode=listdata["vchcode"]
            comment=listdata["comment"]
            vchtype=listdata["vchtype"]
            summary=listdata["summary"]
            btypeid=listdata["btypeid"]
            etypeid=listdata["etypeid"]
            ktypeid=listdata["ktypeid"]
            ename=listdata["ename"]
            #仓库名称
            kfullname=listdata["kfullname"]
            #单位名称
            bname=listdata["bname"]
            total=listdata["total"]
            tptotal=listdata["tptotal"]
            dptotal=listdata["dptotal"]

            mannonums=mannonums+float(listdata["untoqty"])
            manoknums=manoknums+float(listdata["toqty"])
            manrenums=manrenums+float(listdata["repairqty"])
            mannomoney=mannomoney+float(listdata["untototal"])
            manokmoney=manokmoney+float(listdata["tototal"])
            manremoney=manremoney+float(listdata["repairtotal"])

            mandpmoney=mandpmoney+float(listdata["dptotal"])
            manmoney=manmoney+float(listdata["total"])
            manaftermoeny=manaftermoeny+float(listdata["tptotal"])


            manurldetail="http://beefun.wsgjp.com/Beefun/Beefun.Carrier.OrderManager.ajax/GetDetailsByorderid"
            mandetaildata={"hashdata":{"toqty":toqty,"untoqty":untoqty,"repairqty":repairqty,"repairtotal":repairtotal,"tototal":tototal,"untototal":untototal,"isdelivered":0,"checked":0,"vchcode":vchcode,"vchtype":vchtype,"date":"\/Date(1466092800000)\/","number":number,"todate":"\/Date(1466092800000)\/","comment":comment,"summary":summary,"btypeid":btypeid,"bpartypeid":"00000","etypeid":etypeid,"ktypeid":ktypeid,"auditover":False,"ename":ename,"kfullname":kfullname,"bname":bname,"artotal":0,"aptotal":0,"r_warnup":0,"orderover1":0,"createtypename":"本地创建","createtype":0,"reccnt":0,"total":total,"tptotal":tptotal,"dptotal":dptotal,"default_audited":0,"default_auditorid":None,"default_audittime":None,"default_auditremark":"","finance_audited":0,"finance_auditorid":0,"finance_audittime":None,"finance_auditremark":"","isexport":0,"earnest":0,"finance_auditorname":"","business_auditorname":"","receiverpeople":None,"receivercellphone":None,"receivertelephone":None,"receiverzipcode":None,"province":None,"city":None,"district":None,"receiveraddress":None,"isneedinvoice":None}}
            mandetail=requests.post(url=manurldetail,data=json.dumps(mandetaildata),headers=header)
            mandetaildic=browser.datatrunjson(mandetail)
            #print mandetaildic
            #print len(mandetaildic)

            print "第"+str(n)+"行销售订单原始单据..............................."
            Vchcode=listdata["vchcode"]
            orurl="http://beefun.wsgjp.com/Beefun/Bill/SaleOrderBill.gspx?Vchcode="+Vchcode+"&Mode=Read"
            ordata=requests.get(url=orurl,headers=header)

            #原始单据头
            orheader=browser.getfewernoethead(ordata)

            #原始单据数据
            notedatalists=browser.salenotedata(ordata)

            #原始单据的每一行商品
            m=0
            mandetonums=0
            mandetomoney=0

            mandetononums=0
            mandetooknums=0
            mandetorenums=0

            mandetonomoney=0
            mandetookmoney=0
            mandetoremoney=0

            bemoney=0
            listaxmoney=0
            for notelisdata in notedatalists:

                ordalis="{\"vchcode"+notelisdata[:-3]
                ordalisdic=browser.datatrunjson2(ordalis)
                print u"原始单据第"+str(m+1)+u"行商品:"+str(ordalisdic["pfullname"])
                #mandetaildic
                #商品编号
                ormancode=ordalisdic["ptypecode"]
                mandecode=mandetaildic[m]["ptypecode"]
                self.assernote(mandecode,ormancode,u"商品编号不相同（销售订单管理商品明细和原始单据明细）","manage detail item code ok",ordalisdic["pfullname"])

                #商品名称
                orname=ordalisdic["pfullname"]
                mandename=mandetaildic[m]["pfullname"]
                self.assernote(mandename,orname,u"商品名称不相同（销售订单管理商品明细和原始单据明细）","manage detail item name ok",ordalisdic["pfullname"])

                #数量
                ormannums=float(ordalisdic["qty"])
                mandenums=float(mandetaildic[m]["qty"])
                self.assernote(mandenums,ormannums,u"数量不相同（销售订单管理商品明细和原始单据明细）","manage detail item numbers ok",ordalisdic["pfullname"])

                mandetonums=mandetonums+mandenums

                #单价
                ormanprice=float(ordalisdic["price"])
                mandeprice=float(mandetaildic[m]["price"])

                self.assernote(mandeprice,ormanprice,u"单价不相同（销售订单管理商品明细和原始单据明细）","manage detail item sigle price ok",ordalisdic["pfullname"])

                #金额
                ormanmoney=float(ordalisdic["total"])
                mandemoney=float(mandetaildic[m]["total"])
                self.assernote(mandemoney,ormanmoney,u"金额不相同（销售订单管理商品明细和原始单据明细）","manage detail item money ok",ordalisdic["pfullname"])

                mandetomoney=mandetomoney+mandemoney

                #税后金额
                #print "ordalisdic......................................"
                listaxmoney=float(ordalisdic["total"])+listaxmoney



                #未完成数量
                ormannonums=float(ordalisdic["qty"])-float(ordalisdic["toqty"])
                mandenonums=float(mandetaildic[m]["untoqty"])
                self.assernote(mandenonums,ormannonums,u"未完成数量不相同（销售订单管理商品明细和原始单据明细）","manage detail no numbers ok",ordalisdic["pfullname"])

                mandetononums=mandetononums+mandenonums

                #完成数量
                ormanoknums=float(ordalisdic["toqty"])
                mandeoknums=float(mandetaildic[m]["toqty"])
                self.assernote(mandeoknums,ormanoknums,u"完成数量不相同（销售订单管理商品明细和原始单据明细）","manage detail ok numbers ok",ordalisdic["pfullname"])

                mandetooknums=mandetooknums+mandeoknums

                #补订数量
                manderenums=float(mandetaildic[m]["repairqty"])
                mandetorenums=mandetorenums+manderenums

                #未完成金额
                #print "ordalisdic..................................."
                #print ordalisdic
                ormannomoney=(float(ordalisdic["qty"])-float(ordalisdic["toqty"]))*float(ordalisdic["tpprice"])
                mandenomoney=float(mandetaildic[m]["untototal"])

                ormannomoney=str("%.4f"%ormannomoney)
                mandenomoney=str("%.4f"%mandenomoney)
                self.assernote(mandenomoney,ormannomoney,u"未完成金额不相同（销售订单管理商品明细和原始单据明细）","manage detail no money ok",ordalisdic["pfullname"])

                mandetonomoney=float(mandetonomoney)+float(mandenomoney)

                #完成金额
                ormanokmoney=float(ordalisdic["tpprice"])*float(ordalisdic["toqty"])
                #ormanokmoney=float(ordalisdic["price"])
                mandeokmoney=float(mandetaildic[m]["tototal"])

                self.assernote(mandeokmoney,ormanokmoney,u"完成金额不相同（销售订单管理商品明细和原始单据明细）","manage detail ok money ok",ordalisdic["pfullname"])

                mandetookmoney=mandetookmoney+mandeokmoney

                #补订金额
                manderemoney=float(mandetaildic[m]["repairtotal"])
                mandetoremoney=mandetoremoney+manderemoney

                #备注
                ormancomm=ordalisdic["comment"]
                mandebeizhu=mandetaildic[m]["comment"]
                self.assernote(mandebeizhu,ormancomm,u"备注不相同（销售订单管理商品明细和原始单据明细）","manage detail comment ok",ordalisdic["pfullname"])

                #折前金额
                bemoney=bemoney+float(mandetaildic[m]["dptotal"])

                m=m+1

            #原始单据商品合计和订单管理列表数据
            print u"原始单据商品合计和订单管理列表数据..........................."
            #金额
            mandetomoney=str("%.4f"%mandetomoney)
            total=str("%.4f"%total)
            self.assernote(mandetomoney,total,u"金额不相同（销售订单管理商品明细和销售订单管理lists数据）","manage lists money ok",number)

            #未完成数量
            self.assernote(mandetononums,untoqty,u"未完成数量不相同（销售订单管理商品明细和销售订单管理lists数据）","manage lists no qty ok",number)

            #完成数量
            self.assernote(mandetooknums,toqty,u"完成数量不相同（销售订单管理商品明细和销售订单管理lists数据）","manage lists ok qty ok",number)

            #补订数量
            self.assernote(mandetorenums,repairqty,u"补订数量不相同（销售订单管理商品明细和销售订单管理lists数据）","manage lists re qty ok",number)

            #未完成金额
            mandetonomoney=str("%.4f"%mandetonomoney)
            untototal=str("%.4f"%untototal)
            self.assernote(mandetonomoney,untototal,u"未完成金额不相同（销售订单管理商品明细和销售订单管理lists数据）","manage lists no money ok",number)

            #完成金额
            mandetookmoney=str("%.4f"%mandetookmoney)
            tototal=str("%.4f"%tototal)
            self.assernote(mandetookmoney,tototal,u"完成金额不相同（销售订单管理商品明细和销售订单管理lists数据）","manage lists ok money ok",number)

            #补订金额
            self.assernote(mandetoremoney,repairtotal,u"补订金额不相同（销售订单管理商品明细和销售订单管理lists数据）","manage lists re money ok",number)


            print u"销售订单管理数据和其原始单据..................................."
            #日期
            mdate=browser.handlestampdays(listdata["date"],1)
            ordate=browser.handlestampdays(orheader[1][9:-1],1)
            self.assernote(mdate,ordate,u"日期不相同（销售订单管理数据和其原始单据）","manage date ok",number)

            #订单编号
            ornumber=orheader[2]
            self.assernote(number,ornumber,u"订单编号不相同（销售订单管理数据和其原始单据）","manage number ok",number)

            #往来单位
            orcompany=orheader[32]
            self.assernote(bname,orcompany,u"往来单位不相同（销售订单管理数据和其原始单据）","manage company ok",number)

            #仓库名称
            orcate=orheader[34]
            self.assernote(kfullname,orcate,u"仓库名称不相同（销售订单管理数据和其原始单据）","manage cate name ok",number)

            #经手人
            orpasspeople=orheader[33]
            self.assernote(ename,orpasspeople,u"经手人不相同（销售订单管理数据和其原始单据）","manage pass people ok",number)

            #交货日期
            mtodate=browser.handlestampdays(listdata["todate"],1)
            ortodate=browser.handlestampdays(orheader[15][9:-1],1)
            self.assernote(mtodate,ortodate,u"交货日期不相同（销售订单管理数据和其原始单据）","manage give date ok",number)


            #折前金额
            #print "orheader............................."
            #print orheader
            ormoney=float(bemoney)
            totalmoney=float(listdata["dptotal"])
            ormoney=str("%.4f"%ormoney)
            totalmoney=str("%.4f"%totalmoney)
            self.assernote(totalmoney,ormoney,u"折前金额不相同（销售订单管理数据和其原始单据）","manage dp money ok",number)

            #金额
            #listdata["tptotal"]

            #税后金额
            #print "listdata........................................"
            self.assernote(float(listdata["total"]),listaxmoney,u"税后金额不相同（销售订单管理数据和其原始单据）","manage tax money ok",number)

            #已收定金金额

            #附加说明
            orcomm=orheader[5]
            self.assernote(comment,orcomm,u"附加说明不相同（销售订单管理数据和其原始单据）","manage comment ok",number)


            #是否完成

            #业务审核人
            #制单人
            orpeople=orheader[35]
            mangepeople=listdata["finance_auditorname"]
            #self.assernote(mangepeople,orpeople,u"业务审核人不相同（销售订单管理数据和其原始单据）","manage check people ok",number)

            #审核时间
            #mfintime=browser.handlestampdaysevery(listdata["finance_audittime"])


            #审核说明

            #创建类型

        print "销售订单管理列表统计..............................................."
        #订单管理列表统计
        manurlsum="http://beefun.wsgjp.com/Carpa.Web/Carpa.Web.Script.DataService.ajax/GetPagerSummary"
        manurlsumdata={"pagerId":manid}
        manlitssum=requests.post(url=manurlsum,headers=header,data=json.dumps(manurlsumdata))
        manlisum=browser.datatrunjson(manlitssum)
        #print manlitssum.text

        #折前金额
        mandpmoney=float(mandpmoney)
        mantodpmoney=float(manlisum["dptotal"]["value"])
        mandpmoney=str("%.4f"%mandpmoney)
        mantodpmoney=str("%.4f"%mantodpmoney)
        self.assernote(mandpmoney,mantodpmoney,u"折前金额不相同（销售订单管理数据和其统计）","manage dpmoney ok",u"折前金额")

        #金额
        manmoney=float(manmoney)
        mantomoney=float(manlisum["total"]["value"])
        manmoney=str("%.4f"%manmoney)
        mantomoney=str("%.4f"%mantomoney)

        self.assernote(manmoney,mantomoney,u"金额不相同（销售订单管理数据和其统计）","manage money ok",u"金额")

        #税后金额
        manaftermoeny=float(manaftermoeny)
        mantoaftermoeny=float(manlisum["tptotal"]["value"])
        manaftermoeny=str("%.4f"%manaftermoeny)
        mantoaftermoeny=str("%.4f"%mantoaftermoeny)

        self.assernote(manaftermoeny,mantoaftermoeny,u"税后金额不相同（销售订单管理数据和其统计）","manage tax after money ok",u"税后金额")

        #未完成数量
        mannonums=float(mannonums)
        mantononums=float(manlisum["untoqty"]["value"])
        mannonums=str("%.4f"%mannonums)
        mantononums=str("%.4f"%mantononums)

        self.assernote(mannonums,mantononums,u"未完成数量不相同（销售订单管理数据和其统计）","manage un numbers ok",u"未完成数量")

        #完成数量
        manoknums=float(manoknums)
        mantooknums=float(manlisum["toqty"]["value"])
        manoknums=str("%.4f"%manoknums)
        mantooknums=str("%.4f"%mantooknums)
        self.assernote(manoknums,mantooknums,u"完成数量不相同（销售订单管理数据和其统计）","manage ok numbers ok",u"完成数量")


        #补订数量
        manrenums=float(manrenums)
        mantorenums=float(manlisum["repairqty"]["value"])
        manrenums=str("%.4f"%manrenums)
        mantorenums=str("%.4f"%mantorenums)
        self.assernote(manrenums,mantorenums,u"补订数量不相同（销售订单管理数据和其统计）","manage re numbers ok",u"补订数量")

        #为未完成金额
        mannomoney=float(mannomoney)
        mantonomoney=float(manlisum["untototal"]["value"])
        mannomoney=str("%.4f"%mannomoney)
        mantonomoney=str("%.4f"%mantonomoney)
        self.assernote(mannomoney,mantonomoney,u"未完成金额不相同（销售订单管理数据和其统计）","manage un money ok",u"未完成金额")


        #完成金额
        manokmoney=float(manokmoney)
        mantookmoney=float(manlisum["tototal"]["value"])
        manokmoney=str("%.4f"%manokmoney)
        mantookmoney=str("%.4f"%mantookmoney)
        self.assernote(manokmoney,mantookmoney,u"完成金额不相同（销售订单管理数据和其统计）","manage ok money ok",u"完成金额")

        #补订金额
        manremoney=float(manremoney)
        mantoremoney=float(manlisum["repairtotal"]["value"])
        manremoney=str("%.4f"%manremoney)
        mantoremoney=str("%.4f"%mantoremoney)
        self.assernote(manremoney,mantoremoney,u"补订金额不相同（销售订单管理数据和其统计）","manage re money ok",u"补订金额")




        print "报表.................."
        #销售订单统计
        #页面id
        stamp=browser.gettimestamp()
        reidurl="http://beefun.wsgjp.com/Beefun/Report/PTypeSaleOrderStatistic.gspx?vchtype=saleorder"
        reidda="{\"startDate\":\""+stamp[3]+"\",\"endDate\":\""+stamp[2]+"\",\"index\":0,\"btypeid\":0}"
        reiddata={"__Params":reidda}
        reidtext=requests.post(url=reidurl,data=reiddata,headers=header2)
        reid=browser.getpageid(reidtext)
        #print reid

        #销售订单报表list
        print "lists data..................................."
        reurl="http://beefun.wsgjp.com/Carpa.Web/Carpa.Web.Script.DataService.ajax/GetPagerData"
        redata={"pagerId":reid,"queryParams":{"startdate":stamp[3],"enddate":stamp[2],"startDate":stamp[3],"endDate":stamp[2],"btypeid":0,"isCompleteFlag":"0","isStockOrderBillAudited":True,"financeAuditedEnabled":False},"orders":None,"filter":None,"first":0,"count":100000}
        relist=requests.post(url=reurl,headers=header,data=json.dumps(redata))
        relistdic=browser.datatrunjson(relist)
        #print relistdic

        j=0
        retoordernum=0
        retorenum=0
        retocomtonum=0
        retostopnum=0
        retonocomnum=0

        retomoney=0
        retoremoney=0
        retocommoney=0
        retostopmoney=0
        retonocommoney=0
        for relisdata in relistdic["itemList"]["rows"]:
            j=j+1
            print u"销售订单报表明细第"+str(j)+u"行:"+str(relisdata[9])

            #销售订单报表list detail
            #print "lists data detail..................................."
            redeurl="http://beefun.wsgjp.com/Beefun/Report/PTypeSaleOrderStatisticDetails.gspx?vchtype=saleorder"
            urldeda="{\"startdate\":\""+stamp[3]+"\",\"enddate\":\""+stamp[2]+"\",\"startDate\":\""+stamp[3]+"\",\"endDate\":\""+stamp[2]+"\",\"typeid\":\""+str(relisdata[14])+"\",\"fullname\":\"\",\"isCompleteFlag\":\"0\",\"btypeid\":0}"
            urldedata={"__Params":urldeda}
            redetext=requests.post(url=redeurl,data=urldedata,headers=header2)
            #print redetext.text
            itemnums=0
            reitemnums=0
            overitemnums=0
            noitemnums=0
            stopitemnums=0

            itemmoney=0
            reitemmoney=0
            overitemmoney=0
            noitemmoney=0
            stopitemmoney=0
            print "销售订单报表list和其明细........................"
            redetaillist=browser.reportgetdata(redetext)
            for redetaildata in redetaillist:
                detaildata=browser.getdetaildata(redetaildata)
                #print detaildata
                itemnums=itemnums+float(detaildata[12])
                reitemnums=reitemnums+float(detaildata[15])
                overitemnums=overitemnums+float(detaildata[16])
                stopitemnums=stopitemnums+float(detaildata[17])
                noitemnums=noitemnums+float(detaildata[18])

                itemmoney=itemmoney+float(detaildata[19])
                reitemmoney=reitemmoney+float(detaildata[20])
                overitemmoney=overitemmoney+float(detaildata[21])
                stopitemmoney=stopitemmoney+float(detaildata[22])
                noitemmoney=noitemmoney+float(detaildata[23])



                #商品编号
                self.assernote(str(relisdata[8]),str(detaildata[0]),u"商品编号不相同（销售订单报表和其明细）","report item code ok",relisdata[9])

                #商品名称
                self.assernote(str(relisdata[9]),str(detaildata[1]),u"商品名称不相同（销售订单报表和其明细）","report item name ok",relisdata[9])


            #订货数量
            itemnums=str("%.4f"%itemnums)
            renums=float(relisdata[18])
            renums=str("%.4f"%renums)
            self.assernote(renums,itemnums,u"订货数量不相同（销售订单报表和其明细）","report itemnums ok",relisdata[9])

            retoordernum=retoordernum+float(relisdata[18])


            #补订数量
            reitemnums=str("%.4f"%reitemnums)
            rereinums=float(relisdata[19])
            rereinums=str("%.4f"%rereinums)
            self.assernote(rereinums,reitemnums,u"补订数量不相同（销售订单报表和其明细）","report reitemnums ok",relisdata[9])

            retorenum=retorenum+float(relisdata[19])


            #完成数量
            overitemnums=str("%.4f"%overitemnums)
            reoverinums=float(relisdata[20])
            reoverinums=str("%.4f"%reoverinums)
            self.assernote(reoverinums,overitemnums,u"完成数量不相同（销售订单报表和其明细）","report over item nums ok",relisdata[9])

            retocomtonum=retocomtonum+float(relisdata[20])


            #终止完成数量
            stopitemnums=str("%.4f"%stopitemnums)
            restopnums=float(relisdata[21])
            restopnums=str("%.4f"%restopnums)
            self.assernote(restopnums,stopitemnums,u"终止完成数量不相同（销售订单报表和其明细）","report stop nums ok",relisdata[9])

            retostopnum=retostopnum+float(relisdata[21])


            #未完成数量
            noitemnums=str("%.4f"%noitemnums)
            renonums=float(relisdata[22])
            renonums=str("%.4f"%renonums)
            self.assernote(renonums,noitemnums,u"未完成数量不相同（销售订单报表和其明细）","report no nums ok",relisdata[9])

            retonocomnum=retonocomnum+float(relisdata[22])

            #订货金额
            itemmoney=str("%.4f"%itemmoney)
            remoney=float(relisdata[23])
            remoney=str("%.4f"%remoney)
            self.assernote(remoney,itemmoney,u"订货金额不相同（销售订单报表和其明细）","report money ok",relisdata[9])

            retomoney=retomoney+float(relisdata[23])


            #补订金额
            reitemmoney=str("%.4f"%reitemmoney)
            reremoney=float(relisdata[24])
            reremoney=str("%.4f"%reremoney)
            self.assernote(reremoney,reitemmoney,u"补订金额不相同（销售订单报表和其明细）","report re money ok",relisdata[9])

            retoremoney=retoremoney+float(relisdata[24])


            #完成金额
            overitemmoney=str("%.4f"%overitemmoney)
            reovermoney=float(relisdata[25])
            reovermoney=str("%.4f"%reovermoney)
            self.assernote(reovermoney,overitemmoney,u"完成金额不相同（销售订单报表和其明细）","report over money ok",relisdata[9])

            retocommoney=retocommoney+float(relisdata[25])

            #终止完成金额
            stopitemmoney=str("%.4f"%stopitemmoney)
            restopmoney=float(relisdata[26])
            restopmoney=str("%.4f"%restopmoney)
            self.assernote(restopmoney,stopitemmoney,u"终止完成金额不相同（销售订单报表和其明细）","report stop nums ok",relisdata[9])

            retostopmoney=retostopmoney+float(relisdata[26])

            #未完成金额
            noitemmoney=str("%.4f"%noitemmoney)
            renomoeny=float(relisdata[27])
            renomoeny=str("%.4f"%renomoeny)
            self.assernote(renomoeny,noitemmoney,u"未完成金额不相同（销售订单报表和其明细）","report no money ok",relisdata[9])

            retonocommoney=retonocommoney+float(relisdata[27])

            #订货售价
            itemsigle=float(relisdata[23])/float(relisdata[18])
            itemsigle=str("%.4f"%itemsigle)
            resigle=float(relisdata[28])
            resigle=str("%.4f"%resigle)
            self.assernote(resigle,itemsigle,u"订货售价不相同（销售订单报表和其页面）","report item sigle ok",relisdata[9])


            #赠品

        #销售订单报表list total
        print "lists data sum..................................."
        reurlsum="http://beefun.wsgjp.com/Carpa.Web/Carpa.Web.Script.DataService.ajax/GetPagerSummary"
        resumdata={"pagerId":reid}
        relistsum=requests.post(url=reurlsum,headers=header,data=json.dumps(resumdata))
        relistsumdic=browser.datatrunjson(relistsum)
        #print relistsumdic

        #页面统计
        print u"销售订单报表和其页面统计数据......................................"
        #订货数量
        #print "relistsumdic................."
        #print relistsumdic
        qty=float(relistsumdic["qty"]["value"])
        qty=str("%.4f"%qty)
        retoordernum=str("%.4f"%retoordernum)
        self.assernote(qty,retoordernum,u"订货数量不相同（销售订单报表和其页面统计）","report total numbers ok","订货数量")



        #补订数量
        repairqty=float(relistsumdic["repairqty"]["value"])
        repairqty=str("%.4f"%repairqty)
        retorenum=str("%.4f"%retorenum)
        self.assernote(repairqty,retorenum,u"补订数量不相同（销售订单报表和其页面统计）","report total repair numbers ok","补订数量")

        #完成数量
        completeqty=float(relistsumdic["completeqty"]["value"])
        completeqty=str("%.4f"%completeqty)
        retocomtonum=str("%.4f"%retocomtonum)
        self.assernote(completeqty,retocomtonum,u"完成数量不相同（销售订单报表和其页面统计）","report total ok numbers ok","完成数量")

        #终止完成数量
        forcecompletetotal=float(relistsumdic["forcecompletetotal"]["value"])
        forcecompletetotal=str("%.4f"%forcecompletetotal)
        retostopnum=str("%.4f"%retostopnum)
        self.assernote(forcecompletetotal,retostopnum,u"终止完成数量不相同（销售订单报表和其页面统计）","report total stop numbers ok","终止完成数量")

        #未完成数量
        nocompleteqty=float(relistsumdic["nocompleteqty"]["value"])
        nocompleteqty=str("%.4f"%nocompleteqty)
        retonocomnum=str("%.4f"%retonocomnum)
        self.assernote(nocompleteqty,retonocomnum,u"未完成数量不相同（销售订单报表和其页面统计）","report total no numbers ok","未完成数量")

        #订货金额
        ordertotal=relistsumdic["ordertotal"]["value"]
        ordertotal=str("%.4f"%ordertotal)
        retomoney=str("%.4f"%retomoney)
        self.assernote(ordertotal,retomoney,u"订货金额不相同（销售订单报表和其页面统计）","report total order money ok","订货金额")

        #补订金额
        repairtotal=relistsumdic["repairtotal"]["value"]
        repairtotal=str("%.4f"%repairtotal)
        retoremoney=str("%.4f"%retoremoney)
        self.assernote(repairtotal,retoremoney,u"补订金额不相同（销售订单报表和其页面统计）","report total repair money ok","补订金额")

        #完成金额
        completetotal=relistsumdic["completetotal"]["value"]
        completetotal=str("%.4f"%completetotal)
        retocommoney=str("%.4f"%retocommoney)
        self.assernote(completetotal,retocommoney,u"完成金额不相同（销售订单报表和其页面统计）","report total complete money ok","完成金额")

        #终止完成金额
        forcecompletetotal=relistsumdic["forcecompletetotal"]["value"]
        forcecompletetotal=str("%.4f"%forcecompletetotal)
        retostopmoney=str("%.4f"%retostopmoney)
        self.assernote(forcecompletetotal,retostopmoney,u"终止完成金额不相同（销售订单报表和其页面统计）","report total stop money ok","终止完成金额")

        #未完成金额
        nocompletetotal=relistsumdic["nocompletetotal"]["value"]
        nocompletetotal=str("%.4f"%nocompletetotal)
        retonocommoney=str("%.4f"%retonocommoney)

        self.assernote(nocompletetotal,retonocommoney,u"未完成金额不相同（销售订单报表和其页面统计）","report total no money ok","未完成金额")

        #总条数
        itount=float(len(relistdic["itemList"]["rows"]))
        relto=float(browser.totallist(reidtext))
        self.assernote(itount,relto,u"总条数不相同（销售订单报表和其页面统计）","report total lists ok","总条数")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
