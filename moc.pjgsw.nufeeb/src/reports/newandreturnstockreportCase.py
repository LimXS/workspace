#*-* coding:UTF-8 *-*
import time
import datetime
import unittest
from common import browserClass
import requests
import re
import json
import xml
import traceback
browser=browserClass.browser()

class nowanrestockreportTest(unittest.TestCase):
    u'''商品进货/退货统计（报表）&单据中心'''

    def setUp(self):
        self.driver=browser.startBrowser('chrome')
        browser.set_up(self.driver)
        time.sleep(2)


        dom = xml.dom.minidom.parse(r'C:\workspace\moc.pjgsw.nufeeb\src\data\report')

        module1=browser.xmlRead(self.driver,dom,"module",1)
        module2=browser.xmlRead(self.driver,dom,'module',2)

        browser.openModule2(self.driver,module1,module2)

        cookie = [item["name"] + "=" + item["value"] for item in self.driver.get_cookies()]
        #print cookie
        self.cookiestr = ';'.join(item for item in cookie)
        #self.cookiestr=self.driver.get_cookies()
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


    def testnowanrestockReport(self):
        u'''商品进货/退货统计（报表）&单据中心'''
        #单据中心数据
        header={'cookie':self.cookiestr,"Content-Type": "application/json"}
        pagedic=browser.notecentel(header)
        print u"单据中心................................."

        notejhdjt=[]
        notejhhin=[]
        notejhhout=[]
        notenumber=[]
        for j in range(len(pagedic["itemList"])):
            #单据明细
            number=pagedic["itemList"][j]["number"]
            Vchcode=pagedic["itemList"][j]["vchcode"]
            Vchtype=pagedic["itemList"][j]["vchtypeid"]
            #noteurl="http://beefun.wsgjp.com.cn/Beefun/Bill/StockBackBill.gspx?Vchtype="+str(Vchtype)+"&Vchcode="+str(Vchcode)+"&Mode=Read"
            noteurl="http://beefun.wsgjp.com.cn/Beefun/Bill/StockChangeBill.gspx?Vchtype="+str(Vchtype)+"&Vchcode="+str(Vchcode)+"&Mode=Read"
            notedetail=requests.get(noteurl,headers=header)
            #print "notedetail....................."
            #print notedetail.text


            #进货、退货明细
            if number[:3]=='JT-'or number[:3]=='JH-':
                noteitem=re.findall("invoicetotal(.*?)brandname",notedetail.text)
                #print len(noteitem)
                for a in range(len(noteitem)):
                    notejhd=noteitem[a].replace("\"","")
                    #print noteitem
                    itemdetail=re.findall(":(.*?),",notejhd)
                    notejhdjt.append(itemdetail)
                    notenumber.append(number)


            #换货明细
            elif number[:3]=='JHH':
                #print "JHH"
                #换出商品
                tempoutdatails=re.findall("(?<=outdetails\":\[)(.*?)brandname\":null\}\]",notedetail.text)
                #print len(tempoutdatails)
                #print tempoutdatails
                tempoutdet=re.findall("invoicetotal(.*?)brandname",tempoutdatails[0]+"brandname")
                #print len(tempoutdet)
                #print tempoutdet[0]
                for c in range(len(tempoutdet)):
                    tempout=tempoutdet[c].replace("\"","")
                    outdetail=re.findall(":(.*?),",tempout)
                    #print len(outdetail)
                    #print outdetail
                    notejhhout.append(outdetail)
                    notenumber.append(number)

                #换入商品
                tempindetails=re.findall("(?<=indetails\":\[).*?(?=outdetails)",notedetail.text)
                #print len(tempindetails)
                #print tempindetails
                tempindet=re.findall("invoicetotal(.*?)brandname",tempindetails[0])
                #print len(tempindet)
                #print tempindet[0]

                for b in range(len(tempindet)):
                    tempin=tempindet[b].replace("\"","")
                    #print noteitem
                    indetail=re.findall(":(.*?),",tempin)
                    #print len(indetail)
                    #print indetail
                    notejhhin.append(indetail)
                    notenumber.append(number)

            else:
                #print u"不是商品进货/退货模式的单据(单据中心)"
                #print number
                continue

            #进货、退货、换货单据页面header
            noteheader=re.findall("brandname\":null\}\],\"type\"(.*?)fc_total",notedetail.text)
            noteheader=noteheader[0].replace("\"","")
            noteheader=re.findall(":(.*?),",noteheader)

            #单据明细和单据统计比较
            print u"第"+str(j+1)+u"行单据和其明细比较................."
            #日期
            dat=pagedic["itemList"][j]["date"]
            notedat=noteheader[43][:10]
            self.assernote(dat,notedat,u"日期不相同（单据中心和其明细）","note date ok",number)

            #单据编号
            self.assernote(number,noteheader[11],u"单据编号不相同（单据中心和其明细）","note number ok",number)

            #单据类型
            vchtype=pagedic["itemList"][j]["vchtype"]
            if number[:3]=='JH-':
                notetype=u'进货入库单'
            elif number[:3]=='JT-':
                notetype=u'进货退货单'
            elif number[:3]=='JHH':
                notetype=u'进货换货单'
            else:
                notetype=number
                print u"无此种单据模式(单据类型)"
            self.assernote(vchtype,notetype,u"单据类型不相同（单据中心和其明细）","note type ok",number)

            #单据金额
            totalmon=float(pagedic["itemList"][j]["total"])
            totalmon=str("%.4f"%totalmon)
            dtotalmon=float(noteheader[8])
            dtotalmon=str("%.4f"%dtotalmon)
            self.assernote(totalmon,dtotalmon,u"单据金额不相同（单据中心和其明细）","note money ok",number)

            #摘要
            summary=pagedic["itemList"][j]["summary"]
            notesum=noteheader[12]
            self.assernote(summary,notesum,u"摘要不相同（单据中心和其明细）","note summary ok",number)

            #经手人
            efullname=pagedic["itemList"][j]["efullname"]
            notepass= noteheader[39]
            self.assernote(efullname,notepass,u"经手人不相同（单据中心和其明细）","note pass people ok",number)

            #制单人
            postfullname=pagedic["itemList"][j]["postfullname"]
            notepost=noteheader[41]
            self.assernote(postfullname,notepost,u"制单人不相同（单据中心和其明细）","note create peopele ok",number)

            #往来单位
            btypename=pagedic["itemList"][j]["btypename"]
            notecom=noteheader[38]
            self.assernote(btypename,notecom,u"往来单位不相同（单据中心和其明细）","note company ok",number)

            #仓库
            kfullname=pagedic["itemList"][j]["kfullname"]
            notecat=noteheader[2]
            self.assernote(kfullname,notecat,u"仓库不相同（单据中心和其明细）","note cate ok",number)

            #过账人
            inputfullname=pagedic["itemList"][j]["inputfullname"]
            noteinput=noteheader[41]
            self.assernote(inputfullname,noteinput,u"过账人不相同（单据中心和其明细）","note ok people ok",number)

            #业务类型
            #inputfullname=pagedic["itemList"][j]["inputfullname"]

            #附加说明
            comment=pagedic["itemList"][j]["comment"]
            noetcomment=noteheader[13]
            self.assernote(comment,noetcomment,u"附加说明不相同（单据中心和其明细）","note comment ok",number)

            #过账时间
            overtime=pagedic["itemList"][j]["overtime"]
            ordeovdate=noteheader[43]
            self.assernote(overtime,ordeovdate,u"过账时间不相同（单据中心和其原始单据）","note overtime ok",number)



        print "\n"
        print u"商品进货/退货统计（报表)"
        #common data
        today = datetime.date.today()
        overday=today+datetime.timedelta(days=-6)
        #print "totaldata................."

        todayda=today.strftime('%Y-%m-%d %H:%M:%S')
        overdayda=overday.strftime('%Y-%m-%d %H:%M:%S')

        today=today.strftime('%Y-%m-%d')
        overday=overday.strftime('%Y-%m-%d')

        timeArray1 = time.strptime(todayda, "%Y-%m-%d %H:%M:%S")
        timeArray2 = time.strptime(overdayda, "%Y-%m-%d %H:%M:%S")

        tostamp=int(time.mktime(timeArray1))
        overstamp=int(time.mktime(timeArray2))

        #报名统计数据页面
        b="{\"mode\":\"pbuy\",\"reporttype\":0,\"querytype\":0,\"StartDate\":\"\/Date("+str(overstamp*1000)+")\\/\",\"EndDate\":\"\/Date("+str(tostamp*1000)+")\\/\",\"dlytype\":[0,1,2],\"pTypeid\":null,\"eTypeid\":null,\"kTypeid\":null,\"bTypeid\":null,\"brandid\":null,\"saveDate\":false,\"pId\":null,\"pfullname\":\"\",\"bId\":null,\"bfullname\":\"\",\"eId\":null,\"efullname\":\"\",\"kId\":null,\"kfullname\":\"\",\"brandname\":\"\",\"startDate\":\""+str(overday)+"\",\"endDate\":\""+str(today)+"\",\"filter\":1,\"leveal\":1}"
        data3={"__Params":b}
        header2={'cookie':self.cookiestr,"Content-Type": "application/x-www-form-urlencoded"}
        retotalurl2="http://beefun.wsgjp.com/Beefun/Report/ProductsIn.gspx"
        totaldata=requests.post(url=retotalurl2,data=data3,headers=header2)
        #print totaldata.text
        #放列表，每个位置一列数据
        report=re.findall("rows\":\[(.*?)\],\"fieldSizes",totaldata.text)
        #print report[0]
        report=report[0].replace("\"","")
        inandrelist=re.findall("\[(.*?)\]",report)
        #print len(inandrelist)
        #print inandrelist[0]

        reportlist=[]
        for m in range(len(inandrelist)):
            temp=re.findall("(.*?),",inandrelist[m])
            reportlist.append(temp)
        #放reportlist里面 其格式为reportlist[m][m]第m列第m个字段
        #print len(reportlist)

        #报表明细
        k=0
        redetailnumbers=0
        retointonum=0
        retointomoney=0
        retooutnum=0
        retooutmoney=0
        retoitemnum=0
        retoitemmoney=0
        retotaxtomoney=0
        for sigreport in reportlist:
            pTypeid=sigreport[4]
            header={'cookie':self.cookiestr,"Content-Type":"application/x-www-form-urlencoded"}
            detailurl="http://beefun.wsgjp.com/Beefun/Report/ProductsInDetails.gspx"
            dedata2="{\"mode\":\"pbuy\",\"pTypeid\":\""+pTypeid+"\",\"bTypeid\":null,\"eTypeid\":null,\"kTypeid\":null,\"dlytype\":[0,1,2],\"StartDate\":\"\/Date("+str(overstamp*1000)+")\\/\",\"EndDate\":\"\/Date("+str(tostamp*1000)+")\\/\",\"filter\":0,\"leveal\":1,\"querytype\":0,\"reporttype\":0,\"pfullname\":\"\",\"sonnum\":0,\"bfullname\":\"\",\"efullname\":\"\",\"kfullname\":\"\",\"isnullflag\":\"1\"}"

            dedata2={"__Params":dedata2}
            detai2=requests.post(url=detailurl,data=dedata2,headers=header)
            #print detai2.text
            ddetail=detai2
            detailid=re.findall("PagerBottom\" id=\"(.*?)\"",detai2.text)

            datail=re.findall("rows\":\[(.*?)\],\"fieldSizes",detai2.text)
            datail=datail[0].replace("\"","")
            dataillis=re.findall("\[(.*?)\]",datail)
            #print len(dataillis)
            #print dataillis[0]
            k=k+1
            redetailnumbers=redetailnumbers+len(dataillis)

            print u"报表第"+str(k)+u"行数据:"+sigreport[5]

            detlist=[]
            deortax=0.00
            deortaxmon=0.00
            for m in dataillis:

                temp=re.findall("(.*?),",m)
                try:
                    notenumber.remove(str(temp[3]))
                except:
                    print(traceback.format_exc())
                    print u"单据中心无此单据编号"
                    print str(temp[3])
                print u"明细数据："+str(temp[3])
                number=temp[3]
                Vchcode=temp[0]
                Vchtype=temp[1]
                reurl="http://beefun.wsgjp.com.cn/Beefun/Bill/StockChangeBill.gspx?Vchtype="+str(Vchtype)+"&Vchcode="+str(Vchcode)+"&Mode=Read"
                redddata=requests.get(reurl,headers=header)


                #原始单据头
                reheader=browser.getnotehead(redddata)

                #进货单/退货单
                if number[:3]=='JH-' or number[:3]=='JT-':
                    #print "JHJT.............................."
                    #print redddata.text
                    rejhd=re.findall("invoicetotal(.*?)brandname",redddata.text)
                    for a in range(len(rejhd)):
                        rejhdjt=rejhd[a].replace("\"","")
                        #print noteitem
                        jhdjt=re.findall(":(.*?),",rejhdjt)
                        #print itemdetail
                        #商品名字一致就进行比较
                        if jhdjt[69]==temp[8]:

                            break

                #退货换货单
                elif number[:3]=='JHH':
                    #换出商品
                    #print "redddata.text................."
                    #print redddata.text
                    tempoutdatails=re.findall("(?<=outdetails\":\[)(.*?)brandname\":null\}\]",redddata.text)
                    #print len(tempoutdatails)
                    #print tempoutdatails
                    tempoutdet=re.findall("invoicetotal(.*?)brandname",tempoutdatails[0]+"brandname")

                    for c in range(len(tempoutdet)):
                        tempout=tempoutdet[c].replace("\"","")
                        jhhout=re.findall(":(.*?),",tempout)
                        if temp[8]==jhhout[69]:
                            jhhf=0
                            jhdjt=jhhout
                            break
                        #print "out.............."
                        #print outdetail

                    #换入商品
                    tempindetails=re.findall("(?<=indetails\":\[).*?(?=outdetails)",redddata.text)
                    #print "in......................."
                    #print tempindetails
                    tempindet=re.findall("invoicetotal(.*?)brandname",tempindetails[0])
                    for b in range(len(tempindet)):
                        tempin=tempindet[b].replace("\"","")
                        jhhin=re.findall(":(.*?),",tempin)
                        if temp[8]==jhhin[69]:
                            jhhf=1
                            jhdjt=jhhin
                            break


                else:
                    print u"无此单据类型（报表明细）"
                    print number

                #日期
                dedate=reheader[43][:10]
                timeStamp=temp[2][9:-1]
                dateArray = datetime.datetime.utcfromtimestamp(float(timeStamp)/1000)
                threeDayAgo = dateArray + datetime.timedelta(days = 1)
                otherStyleTime = threeDayAgo.strftime("%Y-%m-%d")
                self.assernote(dedate,otherStyleTime,u"日期不相同（报表明细和原始单据）","reportdetail date ok",number)

                #编号
                denum=reheader[11]
                rednum=temp[3]
                self.assernote(denum,rednum,u"编号不相同（报表明细和原始单据）","reportdetail number ok",number)

                #摘要
                desumm=reheader[12]
                rednum=temp[4]
                self.assernote(desumm,rednum,u"摘要不相同（报表明细和原始单据）","reportdetail summary ok",number)

                #仓库名称
                decate=reheader[2]
                recate=temp[17]
                self.assernote(decate,recate,u"仓库名称不相同（报表明细和原始单据）","reportdetail cate ok",number)

                #供应商名称
                decomp=reheader[38]
                recomp=temp[15]
                self.assernote(decomp,recomp,u"供应商名称不相同（报表明细和原始单据）","reportdetail company ok",number)


                #退货数量
                jtnum=float(jhdjt[14])
                if number[:3]=='JH-':
                    jtnum=0.0000
                if number[:3]=='JHH':
                    if jhhf==1:
                        jtnum=0.0000

                rejtnum=float(temp[18])

                jtnum=str("%.4f"%jtnum)
                rejtnum=str("%.4f"%rejtnum)

                self.assernote(jtnum,rejtnum,u"退货数量不相同（报表明细和原始单据）","reportdetail return numbers ok",number)

                #进货数量
                jhdnum=float(jhdjt[14])
                if number[:3]=='JHH':
                    if jhhf==0:
                        jhdnum=0.00
                if number[:3]=='JT-':
                    jhdnum=0.0000
                rejdhnum=float(temp[19])

                jhdnum=str("%.4f"%jhdnum)
                rejdhnum=str("%.4f"%rejdhnum)

                self.assernote(jhdnum,rejdhnum,u"进货数量不相同（报表明细和原始单据）","reportdetail into numbers ok",number)

                #单价
                desig=float(jhdjt[8])
                resig=float(temp[21])
                desig=str("%.4f"%desig)
                resig=str("%.4f"%resig)

                self.assernote(desig,resig,u"进货单价不相同（报表明细和原始单据）","reportdetail sigle price ok",number)

                #含税金额、税额
                if number[:3]=='JH-':
                    deortax=deortax+float(jhdjt[16])
                    deortaxmon=deortaxmon+float(jhdjt[10])

                elif number[:3]=='JT-':
                    #print "JT-"
                    deortax=deortax-float(jhdjt[16])
                    deortaxmon=deortaxmon-float(jhdjt[10])

                elif number[:3]=='JHH':
                    #print "JHH"
                    if jhhf==0:
                        deortax=deortax-float(jhdjt[16])
                        deortaxmon=deortaxmon-float(jhdjt[10])

                    else:
                        deortax=deortax+float(jhdjt[16])
                        deortaxmon=deortaxmon+float(jhdjt[10])



                #print "jhdjt..................................."
                #print jhdjt
                #金额
                jhdjtmon=float(jhdjt[7])
                jhdjtmon=str("%.4f"%jhdjtmon)
                if number[:3]=='JHH':
                    if jhhf==0:
                        jhdjtmon="-"+jhdjtmon
                if number[:3]=='JT-':
                    jhdjtmon="-"+jhdjtmon
                remon=float(temp[20])
                remon=str("%.4f"%remon)
                #print "jhdjt........................................."
                #print jhdjt
                self.assernote(jhdjtmon,remon,u"金额不相同（报表明细和原始单据）","reportdetail money ok",number)

                #商品编号
                jhdcode=jhdjt[73]
                sigrecode=sigreport[0]
                self.assernote(jhdcode,sigrecode,u"商品编号不相同（报表和原始单据）","reportdetail item code",number)


                detlist.append(temp)



            #明细数据对比
            #放detlist里面 其格式为detlist[m][m]第m列第m个字段
            #print len(detlist)
            #print detlist[0][5]


            intoret=0
            intonum=0
            intosigle=0
            intoprice=0
            retunum=0
            reintonum=0
            retusigle=0
            reprice=0
            exinto=0
            exchangenum=0
            exchangesigle=0
            exprice=0
            exprice2=0

            delibacknum=0
            delintonum=0
            delinmoney=0
            for temdetail in detlist:
                if sigreport[5]!=temdetail[8]:
                    print u"商品名字不一致"
                    print temdetail[8]
                    print sigreport[5]
                #进货统计(退货数量，进货数量，单价，金额)
                #print "temdetail..........................................................."
                #print temdetail
                if temdetail[3][:3]=='JH-':
                    intoret+=float(temdetail[18])
                    intonum+=float(temdetail[19])
                    intosigle+=float(temdetail[21])
                    intoprice+=float(temdetail[20])
                #退货统计
                elif temdetail[3][:3]=='JT-':
                    retunum+=float(temdetail[18])
                    reintonum+=float(temdetail[19])
                    retusigle+=float(temdetail[21])
                    reprice+=float(temdetail[20])
                #换货统计
                elif temdetail[3][:3]=='JHH':
                    exinto+=float(temdetail[18])
                    exchangenum+=float(temdetail[19])
                    exchangesigle+=float(temdetail[21])
                    if float(temdetail[20])>0:
                       exprice+=float(temdetail[20])
                    if float(temdetail[20])<0:
                        exprice2+=float(temdetail[20])
                else:
                    print "flag wrong"

                delibacknum=delibacknum+float(temdetail[18])
                delintonum=delintonum+float(temdetail[19])
                delinmoney=delinmoney+float(temdetail[20])




            #报表页面和其明细统计对比

            #商品名称

            print u"报表和其明细............................"
            #进货入库数量
            reportintonum=float(sigreport[23])
            reportintonum=str("%.4f"%reportintonum)
            intonum=float(intonum)+float(exchangenum)
            intonum=str("%.4f"%intonum)
            self.assernote(reportintonum,intonum,u"进货入库数量不相同（报表和其明细）","report into number ok",sigreport[5])

            retointonum=retointonum+float(sigreport[23])



            #进货入库金额

            reportintoprice=float(sigreport[24])
            reportintoprice=str("%.4f"%reportintoprice)
            intoprice=float(intoprice)

            intoprice=float(exprice)+float(intoprice)
            #print float(exprice)
            #print intoprice
            intoprice=str("%.4f"%intoprice)
            self.assernote(reportintoprice,intoprice,u"进货入库金额不相同（报表和其明细）","report into price ok",sigreport[5])

            retointomoney=retointomoney+float(sigreport[24])

            #进货退货数量

            reportrenum=float(sigreport[25])
            reportrenum=str("%.4f"%reportrenum)
            reintonum=float(retunum)+float(exinto)
            reintonum=str("%.4f"%reintonum)
            self.assernote(reportrenum,reintonum,u"进货退货数量不相同（报表和其明细）","report return number ok",sigreport[5])

            retooutnum=retooutnum+float(sigreport[25])

            #进货退货金额
            reportreprice=float(sigreport[26])
            reportreprice=str("%.4f"%reportreprice)
            if float(exprice2)<0:
                reprice=abs(float(reprice))+abs(float(exprice2))
            else:
                reprice=abs(float(reprice))
            #print float(exprice)
            reprice=str("%.4f"%reprice)
            self.assernote(reportreprice,reprice,u"进货退货金额不相同（报表和其明细）","report return money ok",sigreport[5])

            retooutmoney=retooutmoney+float(sigreport[26])

            #退货率

            reportrerate=float(sigreport[28])
            reportrerate=str("%.4f"%reportrerate)
            #进行计算退货数量/进货数量
            rate=float(reintonum)/float(intonum)
            rate=str("%.4f"%rate)
            rate=float(rate)*100
            rate=str("%.4f"%rate)
            self.assernote(reportrerate,rate,u"退货率不相同（报表和其明细）","report return rate ok",sigreport[5])

            #进货数量
            reportinto=float(sigreport[18])
            reportinto=str("%.4f"%reportinto)
            into=float(intonum)-float(reintonum)
            into=str("%.4f"%into)
            self.assernote(reportinto,into,u"进货数量不相同（报表和其明细）","report into numbers ok",sigreport[5])

            retoitemnum=retoitemnum+float(sigreport[18])


            #进货均价
            #zheqian reportavprice=float(sigreport[19])
            reportavprice=float(sigreport[14])
            reportavprice=str("%.4f"%reportavprice)
            if into!='0.0000':
                intoave=(float(intoprice)-float(reprice))/float(into)
                intoave=str("%.4f"%intoave)
            else:
                intoave='0.0000'
            self.assernote(reportavprice,intoave,u"进货均价不相同（报表和其明细）","report into ave price ok",sigreport[5])



            #进货金额

            #zhe qian reportintomoney=float(sigreport[20])
            reportintomoney=float(sigreport[15])
            reportintomoney=str("%.4f"%reportintomoney)
            #金额
            intomoney=float(intoprice)-float(reprice)
            intomoney=str("%.4f"%intomoney)
            self.assernote(reportintomoney,intomoney,u"进货金额不相同（报表和其明细）","report into money ok",sigreport[5])

            retoitemmoney=float(sigreport[15])+retoitemmoney

            #税额

            retaxmoney=float(sigreport[13])
            retaxmoney=str("%.4f"%retaxmoney)
            deortaxmon=str("%.4f"%deortaxmon)
            self.assernote(retaxmoney,deortaxmon,u"税额不相同（报表原始单据）","report tax money ok",sigreport[5])



            #含税单价
            #print "sigreport............................."
            #print sigreport
            reporttaxsigle=float(sigreport[19])
            reporttaxsigle=str("%.4f"%reporttaxsigle)
            taxintoave=float(sigreport[20])/float(sigreport[18])
            taxintoave=str("%.4f"%taxintoave)
            self.assernote(reporttaxsigle,taxintoave,u"含税单价不相同（报表和其明细）","report tax ave price ok",sigreport[5])

            #含税合计
            #sigreport[15]

            #print "sigreport........................."
            #print sigreport
            reporttax=float(sigreport[20])
            reporttax=str("%.4f"%reporttax)
            deortax=str("%.4f"%deortax)
            self.assernote(reporttax,deortax,u"含税合计不相同（报表和其原始单据）","report tax total ok",sigreport[5])


            retotaxtomoney=retotaxtomoney+float(sigreport[20])

            #赠品
            #sigreport[22]

            print u"报表明细和明细数据统计............................"
            #报表页面明细合计页面数据
            #页面统计数据
            header={'cookie':self.cookiestr,"Content-Type": "application/json"}
            detailsumda={"pagerId":detailid[0]}
            detailsumurl="http://beefun.wsgjp.com/Carpa.Web/Carpa.Web.Script.DataService.ajax/GetPagerSummary"
            desum=requests.post(url=detailsumurl,headers=header,data=json.dumps(detailsumda))
            dedata=json.loads(desum.text)
            #print "dedata...................................."
            #print dedata
            #退货数量
            retomoney=float(dedata["alloutqty"]["value"])
            retomoney=str("%.4f"%retomoney)
            delibacknum=str("%.4f"%delibacknum)
            self.assernote(delibacknum,retomoney,u"退货数量不相同（明细账本和页面统计）","reportdetail return numbers ok",sigreport[5])

            #进货数量
            retomoney=float(dedata["backqty"]["value"])
            retomoney=str("%.4f"%retomoney)
            delintonum=str("%.4f"%delintonum)
            self.assernote(delintonum,retomoney,u"进货数量不相同（明细账本和页面统计）","reportdetail into numbers ok",sigreport[5])

            #金额
            retomoney=float(dedata["tptotal"]["value"])
            retomoney=str("%.4f"%retomoney)
            delinmoney=str("%.4f"%delinmoney)
            self.assernote(delinmoney,retomoney,u"金额不相同（明细账本和页面统计）","reportdetail total money ok",sigreport[5])



            #总条数
            delistnums=float(len(detlist))
            numlis=re.findall("itemCount\":(.*?),",ddetail.text)
            retollist=float(numlis[0])
            self.assernote(delistnums,retollist,u"单据条数不相同（明细数据和明细统计）","reportdetail lists numbers ok",sigreport[5])




            print "\n"

        #商品进货/退货统计（报表）页面和页面统计
        #取页面统计数据
        id=re.findall("PagerBottom\" id=\"(.*?)\"",totaldata.text)
        id=id[0]
        print u"报表页面和它页面的统计..............................."
        header={'cookie':self.cookiestr,"Content-Type": "application/json"}
        sumurl="http://beefun.wsgjp.com/Carpa.Web/Carpa.Web.Script.DataService.ajax/GetPagerSummary"
        sumda={"pagerId":id}
        resum=requests.post(url=sumurl,headers=header,data=json.dumps(sumda))
        sumdata=json.loads(resum.text)
        #print "sumdata.........................................."
        #print id
        #print sumdata
        #print sumdata["Message"]

        #进货入库数量
        sumreintonum=float(sumdata["inqty"]["value"])
        sumreintonum=str("%.4f"%sumreintonum)
        retointonum=str("%.4f"%retointonum)
        self.assernote(sumreintonum,retointonum,u"进货入库数量不相同（商品进货/退货统计（报表）页面和页面统计）","reporttotal into numbers ok",u"商品进货/退货统计（报表）页面和页面统计进货入库数量")

        #进货入库金额
        sumreintomoney=float(sumdata["intotal"]["value"])
        sumreintomoney=str("%.4f"%sumreintomoney)
        retointomoney=str("%.4f"%retointomoney)
        self.assernote(sumreintomoney,retointomoney,u"进货入库金额不相同（商品进货/退货统计（报表）页面和页面统计）","reporttotal into money total ok",u"商品进货/退货统计（报表）页面和页面统计进货入库金额")

        #进货退货数量
        sumreoutnum=float(sumdata["backqty"]["value"])
        sumreoutnum=str("%.4f"%sumreoutnum)
        retooutnum=str("%.4f"%retooutnum)
        self.assernote(sumreoutnum,retooutnum,u"进货退货数量不相同（商品进货/退货统计（报表）页面和页面统计）","reporttotal return numbers total ok",u"商品进货/退货统计（报表）页面和页面统计进货退货数量")


        #进货退货金额
        sumreoutmoney=float(sumdata["backtotal"]["value"])
        sumreoutmoney=str("%.4f"%sumreoutmoney)
        retooutmoney=str("%.4f"%retooutmoney)
        self.assernote(sumreoutmoney,retooutmoney,u"进货退货金额不相同（商品进货/退货统计（报表）页面和页面统计）","reporttotal return money total ok",u"商品进货/退货统计（报表）页面和页面统计进货退货金额")


        #进货数量
        sumreitemnum=float(sumdata["qty"]["value"])
        sumreitemnum=str("%.4f"%sumreitemnum)
        retoitemnum=str("%.4f"%retoitemnum)
        self.assernote(sumreitemnum,retoitemnum,u"进货数量不相同（商品进货/退货统计（报表）页面和页面统计）","reporttotal items into total ok",u"商品进货/退货统计（报表）页面和页面统计进货数量")

        #进货金额
        #print "sumreintomoney.........."
        #print sumdata
        sumreitemmoney=float(sumdata["tptotal"]["value"])
        sumreitemmoney=str("%.4f"%sumreitemmoney)
        retoitemmoney=str("%.4f"%retoitemmoney)
        self.assernote(sumreitemmoney,retoitemmoney,u"进货金额不相同（商品进货/退货统计（报表）页面和页面统计）","reporttotal items money total ok",u"商品进货/退货统计（报表）页面和页面统计进货金额")

        #含税合计
        sumretaxoney=float(sumdata["total"]["value"])
        sumretaxoney=str("%.4f"%sumretaxoney)
        retotaxtomoney=str("%.4f"%retotaxtomoney)
        self.assernote(sumretaxoney,retotaxtomoney,u"含税合计不相同（商品进货/退货统计（报表）页面和页面统计）","reporttotal tax total ok",u"商品进货/退货统计（报表）页面和页面统计含税合计")

        #总条数
        pagelist=float(len(reportlist))
        totlist=re.findall("itemCount\":(.*?),",totaldata.text)
        totlist=float(totlist[0])

        self.assernote(pagelist,totlist,u"总条数不相同（报表页面和它页面的统计）","report totlelist ok",u"商品进货/退货统计（报表）页面和页面统计总条数")


        #商品进货/退货统计（报表）页面明细条数
        print u"商品进货/退货统计（报表）页面明细条数:"+str(redetailnumbers)
        #单据中心明细数据的明细条数
        notedetailnumber=len(notejhdjt)+len(notejhhin)+len(notejhhout)
        print u"单据中心明细数据的明细条数:"+str(notedetailnumber)

        if len(notenumber)!=0:
            print u"从单据中心生成报表有数据遗漏....."
            print "notenumber....."
            print len(notenumber)
            print notenumber
        else:
            print "assert note and report ok"


        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()