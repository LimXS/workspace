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

class itemsaleTest(unittest.TestCase):
    u'''报表-批发零售报表-商品销售统计'''

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
        '''
        f=open(r"E:\cookie.txt","w")
        f.write(self.cookiestr)
        f.close()
        '''

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

    def testitemSale(self):
        u'''报表-批发零售报表-销商品销售统计'''
        browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\salereports\analysischeck','w',0,"")


        header={'cookie':self.cookiestr,"Content-Type": "application/json"}
        header2={'cookie':self.cookiestr,"Content-Type": "application/x-www-form-urlencoded"}

        #单据中心
        pagedic=browser.notecentel(header)

        print u"单据中心..............................."
        notelisttotal=[]
        #总条数
        itemcount=str(pagedic["itemCount"])
        pagelisttotal=str(len(pagedic["itemList"]))
        self.assernote(pagelisttotal,itemcount,u"总条数不相同（单据中心和和它页面）","note total list  ok","单据中心总条数")

        notexsxt=[]
        notexhin=[]
        notexhout=[]
        notenumber=[]
        for j in range(len(pagedic["itemList"])):
            #单据明细
            number=pagedic["itemList"][j]["number"]
            Vchcode=pagedic["itemList"][j]["vchcode"]
            Vchtype=pagedic["itemList"][j]["vchtypeid"]

            #print "notedetail....................."
            #print notedetail.text


            #进货、退货明细
            if number[:3]=='XS-'or number[:3]=='XT-':
                if number[:3]=='XS-':
                    noteouturl="http://beefun.wsgjp.com.cn/Beefun/Bill/SaleBill.gspx?Vchtype="+str(Vchtype)+"&Vchcode="+str(Vchcode)+"&Mode=Read"
                    notedetail=requests.get(noteouturl,headers=header)
                elif number[:3]=='XT-':
                    notebackurl="http://beefun.wsgjp.com.cn/Beefun/Bill/SaleBackBill.gspx?Vchtype="+str(Vchtype)+"&Vchcode="+str(Vchcode)+"&Mode=Read"
                    notedetail=requests.get(notebackurl,headers=header)

                else:
                    print u"不是XS也不是XT..............."
                    notedetail=[]

                noteitem=re.findall("promovchcode(.*?)brandname",notedetail.text)
                #print len(noteitem)
                for a in range(len(noteitem)):
                    tempnotexsxt=noteitem[a].replace("\"","")
                    #print noteitem
                    itemdetail=re.findall(":(.*?),",tempnotexsxt)
                    notexsxt.append(itemdetail)
                    notenumber.append(number)


            #换货明细
            elif number[:3]=='XH-':
                noteexurl="http://beefun.wsgjp.com.cn/Beefun/Bill/SaleChangeBill.gspx?Vchtype="+str(Vchtype)+"&Vchcode="+str(Vchcode)+"&Mode=Read"
                notedetail=requests.get(noteexurl,headers=header)
                #print "JHH"
                #换出商品
                tempoutdatails=re.findall("(?<=outdetails\":\[)(.*?)brandname\":null\}\]",notedetail.text)
                #print len(tempoutdatails)
                #print tempoutdatails
                #print "tempoutdatails............................................."
                tempoutdet=re.findall("promovchcode(.*?)brandname",tempoutdatails[0]+"brandname")
                #print len(tempoutdet)
                #print tempoutdet[0]
                for c in range(len(tempoutdet)):
                    tempout=tempoutdet[c].replace("\"","")
                    outdetail=re.findall(":(.*?),",tempout)
                    #print len(outdetail)
                    #print outdetail
                    notexhout.append(outdetail)
                    notenumber.append(number)

                #换入商品
                tempindetails=re.findall("(?<=indetails\":\[).*?(?=outdetails)",notedetail.text)
                #print len(tempindetails)
                #print tempindetails
                tempindet=re.findall("promovchcode(.*?)brandname",tempindetails[0])
                #print len(tempindet)
                #print tempindet[0]

                for b in range(len(tempindet)):
                    tempin=tempindet[b].replace("\"","")
                    #print noteitem
                    indetail=re.findall(":(.*?),",tempin)
                    #print len(indetail)
                    #print indetail
                    notexhin.append(indetail)
                    notenumber.append(number)
            elif number[:2]=='LS':
                noteexurl="http://beefun.wsgjp.com/Beefun/Bill/SaleBill.gspx?Vchtype="+str(Vchtype)+"&Vchcode="+str(Vchcode)+"&Mode=Read"
                notedetail=requests.get(noteexurl,headers=header)
                #orheader=browser.getnotehead2(notedetail)

            elif number[:2]=='LT':
                noteexurl="http://beefun.wsgjp.com/Beefun/Bill/SaleBackBill.gspx?Vchtype="+str(Vchtype)+"&Vchcode="+str(Vchcode)+"&Mode=Read"
                notedetail=requests.get(noteexurl,headers=header)
                #orheader=browser.getnotehead2(notedetail)

            else:
                #print u"不是商品进货/退货模式的单据(单据中心)"
                #print number
                continue

            #进货、退货、换货单据页面header
            '''
            noteheader=re.findall("brandname\":null\}\],\"type\"(.*?)fc_total",notedetail.text)
            noteheader=noteheader[0].replace("\"","")
            noteheader=re.findall(":(.*?),",noteheader)
            '''
            noteheader=browser.getnotehead(notedetail)

            #单据明细和单据统计比较
            print u"第"+str(j+1)+u"行单据和其明细(原始单据)比较:"+str(noteheader[11])
            #日期
            dat=pagedic["itemList"][j]["date"]
            notedat=noteheader[43][:10]
            self.assernote(dat,notedat,u"日期不相同（单据中心和其明细）","note date ok",number)

            #单据编号
            self.assernote(number,noteheader[11],u"单据编号不相同（单据中心和其明细）","note number ok",number)

            #单据类型
            vchtype=pagedic["itemList"][j]["vchtype"]
            if number[:3]=='XS-':
                notetype=u'销售出库单'
            elif number[:3]=='XT-':
                notetype=u'销售退货'
            elif number[:3]=='XH-':
                notetype=u'销售换货单'
            elif number[:3]=='LT-':
                notetype=u'销售退货'
            elif number[:3]=='LS-':
                notetype=u'销售出库单'
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

        #报表-批发零售报表-销商品销售统计
        print u"报表-批发零售报表-商品销售统计......................................"
        stamp=browser.gettimestamp()
        overday=stamp[1]*1000
        today=stamp[0]*1000
        #页面id
        idurl="http://beefun.wsgjp.com/Beefun/Report/ProductsSale.gspx"
        b="{\"mode\":\"psale\",\"reporttype\":0,\"querytype\":1,\"StartDate\":\"\/Date("+str(overday)+")\/\",\"EndDate\":\"\/Date("+str(today)+")\/\",\"dlytype\":[0,1,2],\"pTypeid\":null,\"eTypeid\":null,\"kTypeid\":null,\"bTypeid\":null,\"brandid\":null,\"saveDate\":false,\"pId\":null,\"pfullname\":\"\",\"bId\":null,\"bfullname\":\"\",\"eId\":null,\"efullname\":\"\",\"kId\":null,\"kfullname\":\"\",\"brandname\":\"\",\"startDate\":\""+str(stamp[3])+"\",\"endDate\":\""+str(stamp[2])+"\",\"filter\":1,\"leveal\":1}"
        data3={"__Params":b}
        idtext=requests.post(url=idurl,data=data3,headers=header2)
        #print idtext.text
        pageid=browser.getpageid(idtext)
        #print pageid

        #报表页面统计数据获取
        relistssumurl="http://beefun.wsgjp.com/Carpa.Web/Carpa.Web.Script.DataService.ajax/GetPagerSummary"
        relistssumdata={"pagerId":pageid}
        relistssumtext=requests.post(url=relistssumurl,data=json.dumps(relistssumdata),headers=header)
        relistssum=browser.datatrunjson(relistssumtext)

        #报表页面数据
        relistsurl="http://beefun.wsgjp.com/Carpa.Web/Carpa.Web.Script.DataService.ajax/GetPagerData"
        relistsdata={"pagerId":pageid,"queryParams":{"mode":"psale","pTypeid":None,"bTypeid":None,"eTypeid":None,"kTypeid":None,"dlytype":[0,1,2],"brandid":None,"StartDate":stamp[3],"EndDate":stamp[2],"filter":"3","leveal":1,"querytype":1,"reporttype":0,"pfullname":"","bfullname":"","efullname":"","kfullname":"","brandname":""},"orders":None,"filter":None,"first":0,"count":100000}
        reliststext=requests.post(url=relistsurl,data=json.dumps(relistsdata),headers=header)
        #print "reliststext......................"
        #print reliststext.text
        relists=browser.reportgetdata(reliststext)
        #print relists
        #print len(relists)
        m=0
        coutnum=0
        cmoney=0
        ctaxtotal=0
        ctaxmoney=0
        cselfmoeny=0
        cin=0

        for listdata in relists:
            m=m+1
            redata=browser.getdetaildata(listdata)
            print u"报表第"+str(m)+u"行数据:"+str(redata[5])

            #报表-销售明细账本
            #id
            redeurlid="http://beefun.wsgjp.com/Beefun/Report/ProductsSaleDetails.gspx"
            reiddeda="{\"mode\":\"psale\",\"pTypeid\":\""+str(redata[4])+"\",\"bTypeid\":null,\"eTypeid\":null,\"kTypeid\":null,\"dlytype\":[0,1,2],\"StartDate\":\""+stamp[3]+"\",\"EndDate\":\""+stamp[2]+"\",\"filter\":0,\"leveal\":1,\"querytype\":1,\"reporttype\":0,\"pfullname\":\"\",\"sonnum\":0,\"bfullname\":\"全部单位\",\"efullname\":\"全部职员\",\"kfullname\":\"全部仓库\",\"isnullflag\":\"1\",\"brandname\":\"全部品牌\"}"
            reiddedata={"__Params":reiddeda}
            redeidtext=requests.post(url=redeurlid,data=reiddedata,headers=header2)
            #print "detail page id..................."
            depageid=browser.getpageid(redeidtext)
            #print depageid

            #报表-销售明细账本lists
            #print "detail lists............................"
            redeurl="http://beefun.wsgjp.com/Carpa.Web/Carpa.Web.Script.DataService.ajax/GetPagerData"
            rededata={"pagerId":depageid,"queryParams":None,"orders":None,"filter":None,"first":0,"count":100000}
            redeliststext=requests.post(url=redeurl,data=json.dumps(rededata),headers=header)
            #print redeliststext.text
            redelists=browser.reportgetdata(redeliststext)

            reitemrenum=0
            reitemnum=0
            reitemmoney=0
            n=0
            cdetaxtotal=0
            cdetaxmoney=0
            cdeselfmoney=0

            reitresaleoutmoeny=0
            reitresaleretmoney=0

            for delistdata in redelists:
                n=n+1
                rededata=browser.getdetaildata(delistdata)
                print u"销售明细账账本第"+str(n)+u"行数据："+str(rededata[3])

                #原始单据
                orrenum=0
                orreout=0
                flag=0
                #ordatanow=[]
                Vchtype=rededata[1]
                Vchcode=rededata[0]

                #进货、退货明细
                if rededata[3][:2]=='XS'or rededata[3][:2]=='XT':
                    if rededata[3][:2]=='XS':
                        noteouturl="http://beefun.wsgjp.com.cn/Beefun/Bill/SaleBill.gspx?Vchtype="+str(Vchtype)+"&Vchcode="+str(Vchcode)+"&Mode=Read"
                        notedetail=requests.get(noteouturl,headers=header)
                    elif rededata[3][:2]=='XT':
                        notebackurl="http://beefun.wsgjp.com.cn/Beefun/Bill/SaleBackBill.gspx?Vchtype="+str(Vchtype)+"&Vchcode="+str(Vchcode)+"&Mode=Read"
                        notedetail=requests.get(notebackurl,headers=header)

                    else:
                        print u"不是XS也不是XT..............."


                    #header
                    orheader=browser.getnotehead2(notedetail)

                    ordetail=browser.salenoteoutdata(notedetail)
                    #print len(ordetail)
                    for ortemp in ordetail:
                        temp=browser.dbnotedetail(ortemp)
                        #print "temp............"
                        #print temp
                        #print temp[74]
                        #print temp[78]
                        if temp[74]==rededata[8]:
                            ordatanow=temp
                            if rededata[3][:2]=='XS':
                                #销售退货数量
                                orrenum=0
                                #销售chu库数量
                                orreout=float(ordatanow[19])

                            elif rededata[3][:2]=='XT':
                                #销售退货数量
                                orrenum=float(ordatanow[19])
                                #销售chu库数量
                                orreout=0
                            else:
                                print u"不是XS也不是XT..............."
                            break

                #换货明细
                elif rededata[3][:2]=='XH':
                    noteexurl="http://beefun.wsgjp.com.cn/Beefun/Bill/SaleChangeBill.gspx?Vchtype="+str(Vchtype)+"&Vchcode="+str(Vchcode)+"&Mode=Read"
                    notedetail=requests.get(noteexurl,headers=header)
                    #header
                    orheader=browser.getnotehead2(notedetail)
                    #换入-
                    orindata=browser.saleexnotedatain(notedetail)
                    #print "orindata.................."
                    #print len(orindata)
                    #print orindata

                    for orintemp in orindata:
                        temp=browser.dbnotedetail(orintemp)
                        if temp[74]==rededata[8]:
                            ordatanow=temp
                            #销售退货数量
                            orrenum=float(ordatanow[19])
                            #销售chu库数量
                            orreout=0
                            break

                    #换出+
                    oroutdata=browser.saleexnotedataout(notedetail)
                    for orouttemp in oroutdata:
                        temp=browser.dbnotedetail(orouttemp)
                        if temp[74]==rededata[8]:
                            ordatanow=temp
                            flag=1
                            #销售退货数量
                            orrenum=0
                            #销售chu库数量
                            orreout=float(ordatanow[19])
                            break


                elif rededata[3][:2]=='LS' or rededata[3][:2]=='LT':
                    if rededata[3][:2]=='LS':
                        noteexurl="http://beefun.wsgjp.com/Beefun/Bill/SaleBill.gspx?Vchtype="+str(Vchtype)+"&Vchcode="+str(Vchcode)+"&Mode=Read"
                        notedetail=requests.get(noteexurl,headers=header)

                    elif rededata[3][:2]=='LT':
                        noteexurl="http://beefun.wsgjp.com/Beefun/Bill/SaleBackBill.gspx?Vchtype="+str(Vchtype)+"&Vchcode="+str(Vchcode)+"&Mode=Read"
                        notedetail=requests.get(noteexurl,headers=header)
                    orheader=browser.getnotehead2(notedetail)
                    ordetail=browser.salenoteoutdata(notedetail)
                    for ortemp in ordetail:
                        temp=browser.dbnotedetail(ortemp)
                        #print "temp............"
                        #print temp
                        #print temp[74]
                        #print temp[78]
                        if temp[74]==rededata[8]:
                            ordatanow=temp
                            if rededata[3][:2]=='LS':
                                #销售退货数量
                                orrenum=0
                                #销售chu库数量
                                orreout=float(ordatanow[19])

                            elif rededata[3][:2]=='LT':
                                #销售退货数量
                                orrenum=float(ordatanow[19])
                                #销售chu库数量
                                orreout=0

                else:
                    #print u"不是商品进货/退货模式的单据(单据中心)"
                    #print number
                    continue


                #商品编号
                redecode=rededata[6]
                recode=redata[0]
                self.assernote(recode,redecode,u"商品编号不相同（商品销售统计和销售明细账本）","report item code ok",rededata[3])

                #商品名称
                redename=rededata[8]
                rename=redata[5]
                self.assernote(rename,redename,u"商品名称不相同（商品销售统计和销售明细账本）","report item name ok",rededata[3])

                #日期
                self.assernote(browser.handlestampdays(rededata[2][9:-1],1),orheader[43][:10],u"日期不相同（销售明细账本和原始单据）","reportdetail date ok",rededata[3])

                #单据编号
                self.assernote(rededata[3],orheader[11],u"单据编号不相同（销售明细账本和原始单据）","reportdetail number ok",rededata[3])

                #摘要
                self.assernote(rededata[4],orheader[12],u"摘要不相同（销售明细账本和原始单据）","reportdetail summary ok",rededata[3])

                #仓库名称
                #print "rededata,orheader,ordatanow......................"
                #print rededata
                #print orheader
                #print ordatanow
                redecate=rededata[17]

                #orheader[2]在途仓库
                if flag==1:
                    orcate=orheader[4]
                else:
                    orcate=orheader[2]
                self.assernote(redecate,orcate,u"仓库名称不相同（销售明细账本和原始单据）","reportdetail cate ok",rededata[3])

                #客户名称
                redecom=rededata[15]
                self.assernote(redecom,orheader[38],u"客户名称不相同（销售明细账本和原始单据）","reportdetail company ok",rededata[3])

                #经手人
                redepeople=rededata[5]
                self.assernote(str(redepeople.strip()),str(orheader[39]),u"经手人不相同（销售明细账本和原始单据）","reportdetail hand people ok",rededata[3])

                #销售退货数量
                rederenums=float(rededata[19])
                reitemrenum=reitemrenum+float(rededata[19])

                rederenums=str("%.4f"%rederenums)
                orrenum=str("%.4f"%orrenum)
                self.assernote(rederenums,orrenum,u"销售退货数量不相同（销售明细账本和原始单据）","reportdetail return numbers ok",rededata[3])

                #销售出库数量
                redenums=float(rededata[18])
                reitemnum=reitemnum+float(rededata[18])

                redenums=str("%.4f"%redenums)
                orreout=str("%.4f"%orreout)
                self.assernote(redenums,orreout,u"销售出库数量不相同（销售明细账本和原始单据）","reportdetail out numbers ok",rededata[3])

                #print "ordatanow..................."
                #print ordatanow
                #单价
                redesigle=float(rededata[21])
                self.assernote(redesigle,float(ordatanow[13]),u"单价不相同（销售明细账本和原始单据）","reportdetail sigle price ok",rededata[3])
                if float(rededata[21])<0.01 and float(rededata[21])!=0.0:
                    sigleprice=0.01
                else:
                    sigleprice=rededata[21]
                reitresaleoutmoeny=reitresaleoutmoeny+float(sigleprice)*float(rededata[18])
                reitresaleretmoney=reitresaleretmoney+float(sigleprice)*float(rededata[19])

                #金额
                redemoney=float(rededata[20])
                reitemmoney=reitemmoney+float(rededata[20])

                if float(orrenum)>0:
                    nowmoney="-"+str(ordatanow[12])
                else:
                    nowmoney=str(ordatanow[12])
                self.assernote(redemoney,float(nowmoney),u"金额不相同（销售明细账本和原始单据）","reportdetail money ok",rededata[3])

                #print "ordatanow............"
                #print ordatanow
                if rededata[3][:2]=="XT" or rededata[3][:2]=="LT":
                    #税额
                    cdetaxtotal=cdetaxtotal-float(ordatanow[15])
                    #价税合计
                    cdetaxmoney=cdetaxmoney-float(ordatanow[21])
                    #成本
                    cdeselfmoney=cdeselfmoney-float(float(ordatanow[62]))
                elif rededata[3][:2]=="XS" or rededata[3][:2]=="LS":
                    #税额
                    cdetaxtotal=cdetaxtotal+float(ordatanow[15])
                    #价税合计
                    cdetaxmoney=cdetaxmoney+float(ordatanow[21])
                    #成本
                    cdeselfmoney=cdeselfmoney+float(float(ordatanow[62]))
                else:
                    if flag==0:
                        #税额
                        cdetaxtotal=cdetaxtotal-float(ordatanow[15])
                        #价税合计
                        cdetaxmoney=cdetaxmoney-float(ordatanow[21])
                        #成本
                        cdeselfmoney=cdeselfmoney-float(float(ordatanow[62]))
                    else:
                        #税额
                        cdetaxtotal=cdetaxtotal+float(ordatanow[15])
                        #价税合计
                        cdetaxmoney=cdetaxmoney+float(ordatanow[21])
                        #成本
                        cdeselfmoney=cdeselfmoney+float(float(ordatanow[62]))

            #报表-销售明细账本sum
            #print "detail sum............................"
            redesumurl="http://beefun.wsgjp.com/Carpa.Web/Carpa.Web.Script.DataService.ajax/GetPagerSummary"
            redesumdata={"pagerId":depageid}
            redesumtext=requests.post(url=redesumurl,data=json.dumps(redesumdata),headers=header)
            redelistssum=browser.datatrunjson(redesumtext)
            #print redelistssum
            #销售退货数量
            redesumbacknums=float(redelistssum["backqty"]["value"])
            self.assernote(redesumbacknums,reitemrenum,u"销售退货数量不相同（销售明细账本和其页面统计）","reportdetail sum re numbers ok",u"销售明细账本和其页面统计销售退货数量")

            #写入数据 itemreturn analysis 使用
            browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\salereports\analysischeck','a+',0,str(redesumbacknums))
            browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\salereports\analysischeck','a+',0,'\n')

            #销售出库数量
            redesumoutnums=float(redelistssum["alloutqty"]["value"])
            self.assernote(redesumoutnums,reitemnum,u"销售出库数量不相同（销售明细账本和其页面统计）","reportdetail sum out numbers ok",u"销售明细账本和其页面统计销售出库数量")

            #写入数据 itemreturn analysis 使用
            browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\salereports\analysischeck','a+',0,str(redesumoutnums))
            browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\salereports\analysischeck','a+',0,'\n')

            #金额
            redesummoeny=float(redelistssum["tptotal"]["value"])
            self.assernote(str(redesummoeny),str(reitemmoney),u"金额不相同（销售明细账本和其页面统计）","reportdetail sum money ok",u"销售明细账本和其页面统计金额")

            browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\salereports\analysischeck','a+',0,str(redesummoeny))
            browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\salereports\analysischeck','a+',0,'\n')
            #写入销售入库金额，销售退货金额,商品编号,商品名称
            browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\salereports\analysischeck','a+',0,str(reitresaleoutmoeny))
            browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\salereports\analysischeck','a+',0,'\n')
            #print reitresaleretmoney
            browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\salereports\analysischeck','a+',0,str(reitresaleretmoney))
            browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\salereports\analysischeck','a+',0,'\n')
            browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\salereports\analysischeck','a+',0,str(redata[0]))
            browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\salereports\analysischeck','a+',0,'\n')
            browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\salereports\analysischeck','a+',0,str(redata[5]))
            browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\salereports\analysischeck','a+',0,'\n')


            #报表list
            #销售数量
            print u"商品销售统计........................"
            #print "redata........................."
            #print redata
            renums=float(redata[16])
            self.assernote(renums,reitemnum-reitemrenum,u"销售数量不相同（商品销售统计和销售明细账本）","report sale numbers ok",redata[5])

            coutnum=coutnum+float(redata[16])

            #赠品数量
            #regives=redata[]

            #平均单价
            resigle=float(redata[25])
            if reitemnum-reitemrenum!=0:
                recountsigle=reitemmoney/(reitemnum-reitemrenum)
                recountsigle=round(recountsigle,4)
            else:
                recountsigle=0

            self.assernote(resigle,recountsigle,u"平均单价不相同（商品销售统计和销售明细账本）","report ave sigle price ok",redata[5])

            #金额
            #print "redata.........................................."
            #print redata
            remoney=float(redata[26])
            self.assernote(str(remoney),str(reitemmoney),u"金额不相同（商品销售统计和销售明细账本）","report money ok",redata[5])

            cmoney=cmoney+float(redata[26])

            #税额
            retaxs=float(redata[24])
            self.assernote(str(retaxs),str(cdetaxtotal),u"税额不相同（商品销售统计和原始单据）","report tax total ok",redata[5])

            ctaxtotal=ctaxtotal+float(redata[24])

            #含税单价
            retaxsinge=float(redata[17])
            if float(redata[16])!=0:
                pagetaxsigle=float(redata[18])/float(redata[16])
                pagetaxsigle=round(pagetaxsigle,4)
            else:
                pagetaxsigle=0.0
            self.assernote(str(retaxsinge),str(pagetaxsigle),u"含税单价不相同（商品销售统计页面）","report tax sigle ok",redata[5])

            #价税合计
            retaandmonto=float(redata[18])
            self.assernote(str(retaandmonto),str(cdetaxmoney),u"价税合计不相同（商品销售统计和原始单据）","report tax money ok",redata[5])

            ctaxmoney=ctaxmoney+float(redata[18])

            #销售成本
            recost=float(redata[23])
            self.assernote(str(recost),str(cdeselfmoney),u"销售成本不相同（商品销售统计和原始单据）","report self money ok",redata[5])

            cselfmoeny=cselfmoeny+float(redata[23])

            #毛利
            reincome=float(redata[19])
            pageicome=float(redata[26])-float(redata[23])
            self.assernote(str(reincome),str(pageicome),u"毛利不相同（商品销售统计页面）","report self income ok",redata[5])

            cin=cin+float(redata[19])

            #毛利率
            retaincome=float(redata[22])
            retaincome=str("%.4f"%retaincome)
            if float(redata[26])!=0:
                pataincome=float(redata[19])/float(redata[26])*100
                pataincome=round(pataincome,2)
                pataincome=str("%.4f"%pataincome)
                #pataincome=str(pataincome)+"%"
            else:
                pataincome='0.0000'
            #print "redata......................"
            #print redata
            self.assernote(str(retaincome),str(pataincome),u"毛利率不相同（商品销售统计页面）","report precent income ok",redata[5])

            #销售比重
            resaleweight=float(redata[20])
            csaleweight=float(redata[26])/float(relistssum["tptotal"]["value"])*100
            csaleweight=round(csaleweight,2)
            if csaleweight==-0.0:
                csaleweight=0.0
            self.assernote(str(resaleweight),str(csaleweight),u"销售比重不相同（商品销售统计页面）","report sale weight ok",redata[5])

            #利润比重
            reinweight=float(redata[21])
            cinweight=float(redata[19])/float(relistssum["income"]["value"])*100
            cinweight=round(cinweight,2)
            self.assernote(str(reinweight),str(cinweight),u"利润比重不相同（商品销售统计页面）","report income weight ok",redata[5])



        #报表页面统计数据

        #print "relistssumtext........................"
        #print relistssumtext.text

        #print relistssum
        #销售数量
        resumnums=float(relistssum["qty"]["value"])
        self.assernote(resumnums,coutnum,u"销售数量不相同（商品销售统计和其页面统计）","report sum sale numbers ok",u"商品销售统计和其页面统计销售数量")

        #赠品数量
        resumpresentqty=float(relistssum["presentqty"]["value"])

        #金额
        resummoney=float(relistssum["tptotal"]["value"])
        self.assernote(str(resummoney),str(cmoney),u"金额不相同（商品销售统计和其页面统计）","report sum money ok",u"商品销售统计和其页面统计金额")

        #税额
        resumtaxmoney=float(relistssum["taxtotal"]["value"])
        self.assernote(str(resumtaxmoney),str(ctaxtotal),u"税额不相同（商品销售统计和其页面统计）","report sum taxtotal ok",u"商品销售统计和其页面统计税额")

        #价税合计
        resumtamoto=float(relistssum["total"]["value"])
        self.assernote(str(resumtamoto),str(ctaxmoney),u"价税合计不相同（商品销售统计和其页面统计）","report sum tax money ok",u"商品销售统计和其页面统计价税合计")

        #销售成本
        resumcost=float(relistssum["costtotal"]["value"])
        self.assernote(str(resumcost),str(cselfmoeny),u"销售成本不相同（商品销售统计和其页面统计）","report sum self money ok",u"商品销售统计和其页面统计销售成本")

        #毛利
        resumincome=float(relistssum["income"]["value"])
        self.assernote(str(resumincome),str(cin),u"毛利不相同（商品销售统计和其页面统计）","report sum cin ok",u"商品销售统计和其页面统计毛利")



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
