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

class stockfewerTest(unittest.TestCase):
    u'''报表-库存报表-报损单统计'''

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


    def teststockFewer(self):
        u'''报表-库存报表-报损单统计'''
        #单据中心数据
        header={'cookie':self.cookiestr,"Content-Type": "application/json"}
        pagedic=browser.notecentel(header)
        print u"单据中心................................."
        notelisttotal=[]
        #总条数
        itemcount=str(pagedic["itemCount"])
        pagelisttotal=str(len(pagedic["itemList"]))
        self.assernote(pagelisttotal,itemcount,u"总条数不相同（单据中心和和它页面）","note total list  ok","单据中心总条数")

        notetotalmoney=0.00
        for j in range(len(pagedic["itemList"])):
            #原始单据明细
            number=pagedic["itemList"][j]["number"]
            if number[:2]=='BS':
                print u"单据号为："+str(number)+u"进行对比............................."
                Vchcode=pagedic["itemList"][j]["vchcode"]
                Vchtype=pagedic["itemList"][j]["vchtypeid"]
                noteurl="http://beefun.wsgjp.com/Beefun/Bill/StockLossBill.gspx?Vchtype="+str(Vchtype)+"&Vchcode="+str(Vchcode)+"&Mode=Read"

                notedetail=requests.get(noteurl,headers=header)
                #单据头
                notefew=browser.getfewernoethead(notedetail)

                #单据明细
                ordetailnum=re.findall("details(.*?)form.add_close",notedetail.text)
                ordetailnum=re.findall("vchcode(.*?)retailprice",ordetailnum[0])
                for a in ordetailnum:
                    notelisttotal.append(number)


                #日期
                pagedate=pagedic["itemList"][j]["date"]
                ordedate=notefew[14][9:-1]
                ordedate=browser.handlestamp(ordedate)
                self.assernote(pagedate,ordedate,u"日期不相同（单据中心和其原始单据）","note date ok",notefew[3])


                #单据编号
                pagenumber=pagedic["itemList"][j]["number"]
                ordenumber=notefew[3]
                self.assernote(pagenumber,ordenumber,u"单据编号不相同（单据中心和其原始单据）","note number ok",notefew[3])

                #单据类型
                pagetype=pagedic["itemList"][j]["vchtype"]
                ordetype=re.findall("\<title\>(.*?)\</title\>",notedetail.text)
                self.assernote(pagetype,str(ordetype[0]),u"单据类型不相同（单据中心和其原始单据）","note type ok",notefew[3])

                #单据金额
                totalmon=float(pagedic["itemList"][j]["total"])
                totalmon=str("%.4f"%totalmon)
                ordedate=float(notefew[12])
                ordedate=str("%.4f"%ordedate)
                self.assernote(totalmon,ordedate,u"单据金额不相同（单据中心和其原始单据）","note money ok",notefew[3])

                notetotalmoney=notetotalmoney+float(pagedic["itemList"][j]["total"])

                #摘要
                summary=pagedic["itemList"][j]["summary"]
                ordedate=notefew[17]
                self.assernote(summary,ordedate,u"摘要不相同（单据中心和其原始单据）","note summary ok",notefew[3])

                #print pagedic["itemList"][j]
                #print notefew
                #经手人
                efullname=pagedic["itemList"][j]["efullname"]
                ordepassname=notefew[68]
                self.assernote(efullname,ordepassname,u"经手人不相同（单据中心和其原始单据）","note pass people ok",notefew[3])

                #制单人
                inputfullname=pagedic["itemList"][j]["inputfullname"]
                ordemakepeople=notefew[71]
                self.assernote(inputfullname,ordemakepeople,u"制单人不相同（单据中心和其原始单据）","note make people ok",notefew[3])


                #往来单位
                btypename=pagedic["itemList"][j]["btypename"]
                self.assernote(btypename,None,u"往来单位不相同（单据中心和其原始单据）","note company ok",notefew[3])


                #仓库
                kfullname=pagedic["itemList"][j]["kfullname"]
                ordecate=notefew[69]
                self.assernote(kfullname,ordecate,u"仓库不相同（单据中心和其原始单据）","note cate ok",notefew[3])

                #过账人
                postfullname=pagedic["itemList"][j]["postfullname"]
                #ordedate=notefew

                #业务类型
                btypeid=str(pagedic["itemList"][j]["btypeid"])
                ordebtype=str(notefew[4])

                self.assernote(btypeid,ordebtype,u"业务类型不相同（单据中心和其原始单据）","note btypeid ok",notefew[3])


                #附加说明
                comment=pagedic["itemList"][j]["comment"]
                ordecomment=notefew[18]
                self.assernote(comment,ordecomment,u"附加说明不相同（单据中心和其原始单据）","note comment ok",notefew[3])

                #物流单号
                #freightbillno=pagedic["itemList"][j]["freightbillno"]

                #过账时间
                overtime=pagedic["itemList"][j]["overtime"]
                ordeovdate=notefew[81]
                self.assernote(overtime,ordeovdate,u"过账时间不相同（单据中心和其原始单据）","note overtime ok",notefew[3])

        #单据中心数据总条数
        notenumbertot=len(notelisttotal)


        #单据中心报损单总金额
        '''
        notesumurl="http://beefun.wsgjp.com.cn/Carpa.Web/Carpa.Web.Script.DataService.ajax/GetPagerSummary"
        noteid={"pagerId": "$c3e1bf43$grid_pager1"}
        notesum=requests.post(url=notesumurl,headers=header,data=json.dumps(noteid))
        notesumdata=json.loads(notesum.text)
        notesummoney=float(notesumdata["total"]["value"])
        notesummoney=str("%.4f"%notesummoney)
        notetotalmoney=str("%.4f"%notetotalmoney)

        self.assernote(notesummoney,notetotalmoney,u"单据中心报损单总金额不相同（单据中心和本页面统计）","note total fewer money  ok","单据中心和本页面统计总金额")

        '''

        print u"报损单统计................................................"

        #报损单统计
        today = datetime.date.today()
        overday=today+datetime.timedelta(days=-6)
        bsheader={'cookie':self.cookiestr,"Content-Type": "application/x-www-form-urlencoded"}
        bsurl="http://beefun.wsgjp.com.cn/Beefun/Report/LossOrderQuery.gspx?mode=1"
        bs="{\"etypetypeid\":null,\"btypetypeid\":null,\"ktypetypeid\":null,\"departtypeid\":null,\"eId\":null,\"efullname\":\"全部职员\",\"kId\":null,\"kfullname\":\"全部仓库\",\"deptid\":null,\"deptname\":\"全部部门\",\"StartDate\":\""+str(overday)+"\",\"EndDate\":\""+str(str(today))+"\",\"saveDate\":false,\"bfullname\":\"全部单位\",\"mode\":\"1\"}"
        bsdata={"__Params":bs}
        bspage=requests.post(url=bsurl,data=bsdata,headers=bsheader)
        #报损报表每一行数据
        bspagelist=browser.reportgetdata(bspage)

        id=re.findall("PagerBottom\" id=\"(.*?)\"",bspage.text)
        id=id[0]
        #print "bspagelist........."
        #print bspagelist
        #print len(bspagelist)

        #报损报表每一行数据的明细
        bsnum=0.0000
        bsmoney=0.0000
        reporttotalmoney=0.00
        reporttotalnum=0.00
        a=0
        detailtotal=0.00
        for m in bspagelist:
            #每一种商品
            a=a+1
            evitem=re.findall("(.*?),",m)
            print u"报损单第"+str(a)+u"行数据:"+str(evitem[2])
            print evitem[0]
            time.sleep(2)
            #报损明细
            bsdetailurl="http://beefun.wsgjp.com/Beefun/Report/LossOrderQueryDetails.gspx?mode=1"
            bsdet2="{\"etypetypeid\":null,\"btypetypeid\":null,\"ktypetypeid\":null,\"departtypeid\":null,\"eId\":null,\"efullname\":\"全部职员\",\"kId\":null,\"kfullname\":\"全部仓库\",\"deptid\":null,\"deptname\":\"全部部门\",\"StartDate\":\""+str(overday)+"\",\"EndDate\":\""+str(str(today))+"\",\"saveDate\":false,\"bfullname\":\"全部单位\",\"mode\":\"1\",\"pfullname\":\"""\",\"sonnum\":0,\"ptypetypeid\":\""+str(evitem[0])+"\",\"isnullflag\":1}"
            bsdedata={"__Params":bsdet2}
            bsdetail=requests.post(url=bsdetailurl,data=bsdedata,headers=bsheader)

            ddetail=bsdetail
            bsdetaillist=browser.reportgetdata(bsdetail)

            detailtotal=detailtotal+int(len(bsdetaillist))

            #print "bsdetaillist............"
            #print bsdetaillist
            #print len(bsdetaillist)
            denumbers=0.000
            demoneys=0.0000
            b=0
            print u"报损单明细和原始单据..............................."
            for n in bsdetaillist:
                b=b+1
                bsddetail=re.findall("(.*?),",n+",")

                print u"报损单明细第"+str(b)+u"行数据:"+str(bsddetail[4])
                try:
                    notelisttotal.remove(str(bsddetail[4]))
                except:
                    print(traceback.format_exc())
                    print u"单据中心无此单据编号"
                    print str(bsddetail[4])

                #报损单原始单据
                ordetrul="http://beefun.wsgjp.com.cn/Beefun/Bill/StockLossBill.gspx?Vchtype="+bsddetail[1]+"&Vchcode="+bsddetail[0]+"&Mode=Read"
                ordetail=requests.get(ordetrul,headers=header)

                #原始单据头
                ordeheader=re.findall("\{\"vchcode\"(.*?)\"details\":",ordetail.text)
                ordeheader=ordeheader[0].replace("\"","")
                ordeheader=re.findall(":(.*?),",ordeheader)

                #明细账本和原始单据
                #日期
                timeStamp=bsddetail[2][9:-1]
                dateArray = datetime.datetime.utcfromtimestamp(float(timeStamp)/1000)
                threeDayAgo = dateArray + datetime.timedelta(days = 1)
                bstime = threeDayAgo.strftime("%Y-%m-%d")

                ortime=ordeheader[16][9:-1]
                dateArray = datetime.datetime.utcfromtimestamp(float(ortime)/1000)
                ortime = dateArray.strftime("%Y-%m-%d")

                self.assernote(bstime,ortime,u"日期不相同（明细账本和其原始单据）","reportdetail date ok",bsddetail[4])

                #单据编号
                bsnumber=bsddetail[4]
                ornumber=ordeheader[3]
                self.assernote(bsnumber,ornumber,u"单据编号不相同（明细账本和其原始单据）","reportdetail number ok",bsddetail[4])

                #摘要
                desummary=bsddetail[5]
                orsummary=ordeheader[17]
                self.assernote(desummary,orsummary,u"摘要不相同（明细账本和其原始单据）","reportdetail summary ok",bsddetail[4])


                #仓库名称
                #print ordeheader
                bscate=bsddetail[12]
                orcate=ordeheader[69]
                self.assernote(bscate,orcate,u"仓库名称不相同（明细账本和其原始单据）","reportdetail cate name ok",bsddetail[4])

                #商品名称
                dename=bsddetail[6]
                evname=evitem[2]
                self.assernote(dename,evname,u"商品名称不相同（报损单和其明细账本）","report item name ok",bsddetail[4])

                #单据里面具体数据
                ordata=re.findall("\"details\":(.*?)form\.add_close",ordetail.text)
                ordata=re.findall("vchcode(.*?)retailprice",ordata[0])
                for k in ordata:
                    ordatasigle=k.replace("\"","")
                    ordatasigle=re.findall(":(.*?),",ordatasigle)

                    if ordatasigle[36]==dename:
                        break
                #商品编号
                evnumber=evitem[1]
                siglcode=ordatasigle[40]
                self.assernote(evnumber,siglcode,u"商品编号不相同（报损单和其原始单据）","report item code ok",bsddetail[4])



                #明细报损数量
                sinum=float(ordatasigle[11])
                denums=float(bsddetail[13])

                sinum=str("%.4f"%sinum)
                nums=str("%.4f"%denums)

                denumbers=denumbers+denums

                self.assernote(sinum,nums,u"报损数量不相同（报损单明细和其原始单据）","reportdetail fewer number ok",bsddetail[4])


                #明细报损金额
                demoney=float(bsddetail[15])
                sigmoney=float(ordatasigle[13])

                sigmoney=str("%.4f"%sigmoney)
                money=str("%.4f"%demoney)

                demoneys=demoney+demoneys

                self.assernote(sigmoney,money,u"报损金额不相同（报损单明细和其原始单据）","reportdetail fewer money ok",bsddetail[4])


            #报损单和其明细账本
            #报表页面明细合计页面数据
            #页面统计数据
            detailid=re.findall("PagerBottom\" id=\"(.*?)\"",bsdetail.text)
            detailid=detailid[0]
            detailsumda={"pagerId":detailid}
            detailsumurl="http://beefun.wsgjp.com/Carpa.Web/Carpa.Web.Script.DataService.ajax/GetPagerSummary"
            desum=requests.post(url=detailsumurl,headers=header,data=json.dumps(detailsumda))
            dedata=json.loads(desum.text)
            #print "dedata..........................."
            #print dedata
            #print detailid

            print u"报损单和其明细账本..............................."
            #报溢数量
            evnum=float(evitem[10])
            evnum=str("%.4f"%evnum)
            denumbers=str("%.4f"%denumbers)

            retonum=float(dedata["qty"]["value"])
            retonum=str("%.4f"%retonum)

            self.assernote(evnum,denumbers,u"报损数量不相同（报损单和其明细账本）","report more number ok",evitem[2])
            self.assernote(denumbers,retonum,u"报损金额不相同（明细账本和页面统计）","reportdetail total money ok",evitem[2])
            reporttotalnum=reporttotalnum+float(evnum)

            #报损金额
            evmoney=float(evitem[12])
            evmoney=str("%.4f"%evmoney)
            demoneys=str("%.4f"%demoneys)

            retomoney=float(dedata["total"]["value"])
            retomoney=str("%.4f"%retomoney)
            self.assernote(evmoney,demoneys,u"报损金额不相同（报损单和其明细账本）","report more money ok",evitem[2])
            self.assernote(demoneys,retomoney,u"报损金额不相同（明细账本和页面统计）","reportdetail total money ok",evitem[2])
            reporttotalmoney=reporttotalmoney+float(evmoney)

            #单据总条数
            delistnum=float(len(bsdetaillist))
            numlis=re.findall("itemCount\":(.*?),",ddetail.text)
            retollist=float(numlis[0])
            self.assernote(delistnum,retollist,u"单据条数不相同（明细数据和明细统计）","reportdetail lists numbers ok",evitem[2])

            #time.sleep(2)
        #报名页面和它页面的统计
        #数量
        print u"报表页面和它页面的统计..............................."
        sumurl="http://beefun.wsgjp.com/Carpa.Web/Carpa.Web.Script.DataService.ajax/GetPagerSummary"
        sumda={"pagerId":id}
        resum=requests.post(url=sumurl,headers=header,data=json.dumps(sumda))
        sumdata=json.loads(resum.text)

        totnum=float(sumdata["qty"]["value"])
        totnum=str("%.4f"%totnum)
        reporttotalnum=str("%.4f"%reporttotalnum)

        self.assernote(totnum,reporttotalnum,u"数量不相同（报表页面和它页面的统计）","reportself number ok",u"报损单统计")

        #金额
        totmoney=float(sumdata["total"]["value"])
        totmoney=str("%.4f"%totmoney)

        reporttotalmoney=str("%.4f"%reporttotalmoney)

        self.assernote(totmoney,reporttotalmoney,u"金额不相同（报表页面和它页面的统计）","reportself money ok",u"报损单统计")

        #总条数
        pagelist=float(len(bspagelist))
        totlist=re.findall("itemCount\":(.*?),",bspage.text)
        totlist=float(totlist[0])


        self.assernote(pagelist,totlist,u"总条数不相同（报表页面和它页面的统计）","report totlelist ok",u"报损单统计")


        print u"单据中心和报损单统计数据...................."
        #单据中心和报损单统计数据
        if len(notelisttotal)!=0:
            print u"单据中心统计到报损单统计报表有多余或者遗漏"
            print u"单据中心数据总条数："+str(notenumbertot)
            print u"报损单统计数据总条数："+str(int(detailtotal))
        else:
            print "assert note and report ok"





if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
