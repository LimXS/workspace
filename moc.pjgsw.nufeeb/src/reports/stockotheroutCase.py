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

class stockotheroutTest(unittest.TestCase):
    u'''报表-库存报表-其他出库单统计'''

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

    def teststockotherOut(self):
        u'''报表-库存报表-其他出库单统计'''
        #单据中心
        #单据中心数据
        header={'cookie':self.cookiestr,"Content-Type": "application/json"}
        pagedic=browser.notecentel(header)
        print u"单据中心................................."

        #总条数
        itemcount=str(pagedic["itemCount"])
        pagelisttotal=str(len(pagedic["itemList"]))
        self.assernote(pagelisttotal,itemcount,u"总条数不相同（单据中心和和它页面）","note total list  ok","单据中心总条数")

        notelisttotal=[]
        notetotalmoney=0.00
        for j in range(len(pagedic["itemList"])):
            #单据明细
            number=pagedic["itemList"][j]["number"]
            Vchcode=pagedic["itemList"][j]["vchcode"]
            Vchtype=pagedic["itemList"][j]["vchtypeid"]
            #noteurl="http://beefun.wsgjp.com.cn/Beefun/Bill/StockBackBill.gspx?Vchtype="+str(Vchtype)+"&Vchcode="+str(Vchcode)+"&Mode=Read"
            #print "notedetail....................."
            #print notedetail.text

            #其他出库单据
            if number[:3]=='QC-':
                print u"单据号为："+str(number)+u"进行对比............................."
                noteurl="http://beefun.wsgjp.com/Beefun/Bill/OtherSaleBill.gspx?Vchtype="+str(Vchtype)+"&Vchcode="+str(Vchcode)+"&Mode=Read"
                notedetail=requests.get(noteurl,headers=header)

                #原始单据头
                noteheader=browser.getnotehead(notedetail)

                #原始单据明细
                notedetotal=re.findall("outposition(.*?)brandname",notedetail.text)
                for a in notedetotal:
                    notelisttotal.append(number)

                #日期
                dat=pagedic["itemList"][j]["date"]
                notedat=noteheader[43][:10]
                self.assernote(dat,notedat,u"日期不相同（单据中心和其明细）","note date ok",number)

                #单据编号
                self.assernote(number,noteheader[11],u"单据编号不相同（单据中心和其明细）","note number ok",number)

                #单据类型
                vchtype=pagedic["itemList"][j]["vchtype"]
                notetype=re.findall("\<title\>(.*?)\</title\>",notedetail.text)

                self.assernote(str(vchtype),str(notetype[0]),u"单据类型不相同（单据中心和其明细）","note type ok",number)

                #单据金额
                totalmon=float(pagedic["itemList"][j]["total"])
                totalmon=str("%.4f"%totalmon)
                dtotalmon=float(noteheader[8])
                dtotalmon=str("%.4f"%dtotalmon)
                self.assernote(totalmon,dtotalmon,u"单据金额不相同（单据中心和其明细）","note money ok",number)
                notetotalmoney=notetotalmoney+float(pagedic["itemList"][j]["total"])

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

        #单据中心数据总条数
        notetotalnum=len(notelisttotal)

        #单据中心其他出库单总金额
        '''
        notesumurl="http://beefun.wsgjp.com.cn/Carpa.Web/Carpa.Web.Script.DataService.ajax/GetPagerSummary"
        noteid={"pagerId": "$c3e1bf43$grid_pager1"}
        notesum=requests.post(url=notesumurl,headers=header,data=json.dumps(noteid))
        notesumdata=json.loads(notesum.text)
        notesummoney=float(notesumdata["total"]["value"])
        notesummoney=str("%.4f"%notesummoney)
        notetotalmoney=str("%.4f"%notetotalmoney)

        self.assernote(notesummoney,notetotalmoney,u"单据中心其他出库单总金额不相同（单据中心和本页面统计）","note total other out money  ok","单据中心和本页面统计总金额")
        '''


        #报表-库存报表-其他出库单统计
        print u"报表-库存报表-其他出库单统计...................................."
        urlid="http://beefun.wsgjp.com/Beefun/Report/OtherOrderQuery.gspx?mode=4"
        pageid=requests.get(urlid,headers=header)

        id=re.findall("PagerBottom\" id=\"(.*?)\"",pageid.text)
        id=id[0]

        vchtype=re.findall("vchtype\":(.*?),",pageid.text)
        vchtype=vchtype[0]

        #报表页面数据
        stamp=browser.gettimestamp()
        begindate=stamp[3]
        enddate=stamp[2]



        #页面具体数据
        retotalurl="http://beefun.wsgjp.com/Carpa.Web/Carpa.Web.Script.DataService.ajax/GetPagerData"
        totlda={"pagerId":id,"queryParams":{"etypeid":"","ktypeid":"2605638079543104740,2605638079543104822","ptypetypeid":None,"departtypeid":None,"efullname":None,"kfullname":None,"pfullname":None,"deptname":None,"eid":None,"kid":None,"leveal":1,"orderstr":" ORDER  BY p.rowindex asc","filterred":0,"filterzero":0,"vchtype":vchtype,"begindate":begindate,"enddate":enddate,"beginhour":0,"endhour":24,"mode":None,"btypeid":"","bfullname":None},"orders":None,"filter":None,"first":0,"count":100000}
        retotl=requests.post(url=retotalurl,headers=header,data=json.dumps(totlda))
        #print retotl.text
        totaldata=json.loads(retotl.text)

        #页面统计数据
        sumda={"pagerId":id}
        resumurl="http://beefun.wsgjp.com/Carpa.Web/Carpa.Web.Script.DataService.ajax/GetPagerSummary"
        resum=requests.post(url=resumurl,headers=header,data=json.dumps(sumda))
        sumdata=json.loads(resum.text)

        #print resum.text
        #每一行所有数据(每种商品入库信息)
        reporttotalmoney=0.00
        reporttotalnum=0.00
        detailtotal=0
        m=0
        for temp in totaldata["itemList"]["rows"]:
            m=m+1
            print u"其他出库单统计第"+str(m)+"行:"+str(temp[2])

            #取每种商品入库明细单据
            overday=stamp[1]*1000
            today=stamp[0]*1000
            #页面id
            detailidurl="http://beefun.wsgjp.com/Beefun/Report/OtherOrderQueryDetails.gspx?mode=4"
            deurldata2="{\"pfullname\":\"\",\"sonnum\":0,\"ptypetypeid\":\""+str(temp[0])+"\",\"isnullflag\":1,\"begindate\":\"\/Date("+str(overday)+")\/\",\"enddate\":\"\/Date("+str(today)+")\/\"}"
            deurldata={"__Params":deurldata2}
            header2={'cookie':self.cookiestr,"Content-Type": "application/x-www-form-urlencoded"}
            detail=requests.post(detailidurl,data=deurldata,headers=header2)
            ddetail=detail
            #print detail.text
            detailid=re.findall("PagerBottom\" id=\"(.*?)\"",detail.text)
            #detailid=detailid[0]
            #页面数据
            detailurl="http://beefun.wsgjp.com/Carpa.Web/Carpa.Web.Script.DataService.ajax/GetPagerData"
            dedata={"pagerId":detailid[0],"queryParams":None,"orders":None,"filter":None,"first":0,"count":100000}
            datail=requests.post(url=detailurl,headers=header,data=json.dumps(dedata))
            detaillist=browser.reportgetdata(datail)
            #print len(detaillist)

            detailtotal=detailtotal+int(len(detaillist))

            #名称
            detomoney=0.0000
            detonums=0.0000
            rename=temp[2]
            n=0
            for p in detaillist:
                n=n+1
                data=re.findall("(.*?),",p+",")
                print u"其他出库单明细第"+str(n)+"行:"+str(data[4])
                try:
                    notelisttotal.remove(str(data[4]))
                except:
                    print(traceback.format_exc())
                    print u"单据中心无此单据编号"
                    print str(data[4])

                #商品名称
                dename=data[6]
                self.assernote(rename,dename,u"商品名称不相同（报表页面和其明细数据）","report name ok",data[4])

                #原始单据
                orurl="http://beefun.wsgjp.com/Beefun/Bill/OtherStockBill.gspx?Vchtype="+str(data[1])+"&Vchcode="+str(data[0])+"&Mode=Read"
                orurldata=requests.get(orurl,headers=header)
                #print orurldata.text
                #原始单据头
                headerdata=browser.getnotehead(orurldata)

                #日期
                redate=browser.handlestamp(data[2][9:-1])
                ordate=browser.handlestamp(headerdata[6][9:-1])
                self.assernote(redate,ordate,u"日期不相同（明细数据和原始单据）","reportdetail date ok",data[4])

                #单据编号
                redecode=data[4]
                orcode=headerdata[11]
                self.assernote(redecode,orcode,u"单据编号不相同（明细数据和原始单据）","reportdetail code ok",data[4])

                #摘要
                redesumm=data[5]
                orsumm=headerdata[12]
                self.assernote(redesumm,orsumm,u"摘要不相同（明细数据和原始单据）","reportdetail summary ok",data[4])


                #仓库名称
                redecate=data[12]
                orcate=headerdata[2]
                self.assernote(redecate,orcate,u"仓库名称不相同（明细数据和原始单据）","reportdetail catename ok",data[4])

                #原始单据具体数据
                ordatatext=re.findall("outposition(.*?)brandname",orurldata.text)
                for q in ordatatext:
                    orlist=q.replace("\"","")
                    ordata=re.findall(":(.*?),",orlist)
                    if ordata[60]==data[6]:
                        break


                #其他入库数量
                ornums=float(ordata[5])
                ornums=str("%.4f"%ornums)
                redenum=float(data[13])
                redenum=str("%.4f"%redenum)
                self.assernote(redenum,ornums,u"其他出库数量不相同（明细数据和原始单据）","reportdetail other into number ok",data[4])

                detonums=float(data[13])+detonums

                #其他入库金额
                ormoney=float(ordata[7])
                ormoney=str("%.4f"%ormoney)
                redemoney=float(data[15])
                redemoney=str("%.4f"%redemoney)
                self.assernote(redemoney,ormoney,u"仓库名称不相同（明细数据和原始单据）","reportdetail other into money ok",data[4])

                detomoney=float(data[15])+detomoney


                #商品编号
                reitemcode=temp[1]
                oritemcode=ordata[64]

                self.assernote(reitemcode,oritemcode,u"商品编号不相同（报表页面和原始单据）","reportdetail items code ok",rename)


            #报表页面明细合计页面数据
            #页面统计数据
            detailsumda={"pagerId":detailid[0]}
            detailsumurl="http://beefun.wsgjp.com/Carpa.Web/Carpa.Web.Script.DataService.ajax/GetPagerSummary"
            desum=requests.post(url=detailsumurl,headers=header,data=json.dumps(detailsumda))
            dedata=json.loads(desum.text)

            #数量
            renum=float(temp[10])
            renum=str("%.4f"%renum)
            detonums=str("%.4f"%detonums)

            retonum=float(dedata["qty"]["value"])
            retonum=str("%.4f"%retonum)


            self.assernote(renum,detonums,u"数量不相同（报表页面和其明细数据）","reportdetail items numbers ok",rename)
            self.assernote(detonums,retonum,u"数量不相同（明细数据和明细统计）","reportdetail total numbers ok",rename)

            reporttotalnum=reporttotalnum+float(renum)

            #金额
            remoney=float(temp[12])
            remoney=str("%.4f"%remoney)
            detomoney=str("%.4f"%detomoney)

            retomoney=float(dedata["total"]["value"])
            retomoney=str("%.4f"%retomoney)

            self.assernote(remoney,detomoney,u"金额不相同（报表页面和其明细数据）","reportdetail items money ok",rename)
            self.assernote(detomoney,retomoney,u"金额不相同（明细数据和明细统计）","reportdetail total money ok",rename)

            reporttotalmoney=reporttotalmoney+float(remoney)

            #单据条数
            #print "detail................................"
            #print detail
            delistnum=float(len(detaillist))
            numlis=re.findall("itemCount\":(.*?),",ddetail.text)
            retollist=float(numlis[0])
            self.assernote(delistnum,retollist,u"单据条数不相同（明细数据和明细统计）","reportdetail lists numbers ok",rename)


        #报名页面和它页面的统计
        #数量
        print u"报表页面和它页面的统计..............................."
        totnum=float(sumdata["qty"]["value"])
        totnum=str("%.4f"%totnum)
        reporttotalnum=str("%.4f"%reporttotalnum)

        self.assernote(totnum,reporttotalnum,u"数量不相同（报表页面和它页面的统计）","reportself number ok",u"其它出库单统计")

        #金额
        totmoney=float(sumdata["total"]["value"])
        totmoney=str("%.4f"%totmoney)

        reporttotalmoney=str("%.4f"%reporttotalmoney)

        self.assernote(totmoney,reporttotalmoney,u"金额不相同（报表页面和它页面的统计）","reportself money ok",u"其它出库单统计")

        #总条数
        pagelist=float(len(totaldata["itemList"]["rows"]))
        totlist=float(totaldata["itemCount"])


        self.assernote(pagelist,totlist,u"总条数不相同（报表页面和它页面的统计）","report totlelist ok",u"其它入库单统计")

        print u"单据中心和其他出库单统计数据...................."
        #单据中心和其他入库单统计数据
        if len(notelisttotal)!=0:
            print u"单据中心统计到其他出库单统计报表有多余或者遗漏"
            print u"单据中心数据总条数："+str(notetotalnum)
            print u"其他出库单统计数据总条数："+str(int(detailtotal))
        else:
            print "assert note and report ok"



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
