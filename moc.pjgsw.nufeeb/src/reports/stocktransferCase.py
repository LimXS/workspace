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

class stocktransferTest(unittest.TestCase):
    u'''报表-库存报表-调拨单统计'''

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

    def teststockTransfer(self):
        u'''报表-库存报表-调拨单统计'''
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
            #noteurl="http://beefun.wsgjp.com.cn/Beefun/Bill/StockBackBill.gspx?Vchtype="+str(Vchtype)+"&Vchcode="+str(Vchcode)+"&Mode=Read"
            #print "notedetail....................."
            #print notedetail.text

            #调拨单据
            if number[:3]=='DB-':
                Vchcode=pagedic["itemList"][j]["vchcode"]
                Vchtype=pagedic["itemList"][j]["vchtypeid"]
                print u"单据号为："+str(number)+u"进行对比............................."
                noteurl="http://beefun.wsgjp.com/Beefun/Bill/GoodsTransBill.gspx?Vchtype="+str(Vchtype)+"&Vchcode="+str(Vchcode)+"&Mode=Read"
                notedetail=requests.get(noteurl,headers=header)

                #print "notedetail....................."
                #print notedetail.text
                #原始单据头
                noteheader=browser.getnotehead2(notedetail)

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

                self.assernote(str(vchtype),str(notetype[0][:2]),u"单据类型不相同（单据中心和其明细）","note type ok",number)

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
                if btypename==None:
                    btypename='null'
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

        #报表-库存报表-调拨单统计
        print u'报表-库存报表-调拨单统计...................................'
        #获得页面id
        day=browser.gettimestamp()
        header2={'cookie':self.cookiestr,"Content-Type": "application/x-www-form-urlencoded"}
        idurl='http://beefun.wsgjp.com/Beefun/Report/GoodsTransBillQuery.gspx'
        dbdurlda="{\"kOutId\":null,\"kfullnameout\":\"全部仓库\",\"kInId\":null,\"kfullnameint\":null,\"eId\":null,\"efullname\":\"全部职员\",\"departtypeid\":null,\"deptname\":null,\"startDate\":\""+str(day[3])+"\",\"endDate\":\""+str(day[2])+"\",\"SaveDate\":false,\"kfullnamein\":\"全部仓库\",\"departname\":\"全部部门\"}"
        iddata={"__Params":dbdurlda}
        resid=requests.post(url=idurl,headers=header2,data=iddata)
        repageid=browser.getpageid(resid)

        header={'cookie':self.cookiestr,"Content-Type": "application/json"}
        #报表页面数据
        reurl="http://beefun.wsgjp.com/Carpa.Web/Carpa.Web.Script.DataService.ajax/GetPagerData"
        reda={"pagerId":repageid,"queryParams":{"level":1,"partypeid":"00000","profileid":0,"startDate":str(day[3]),"endDate":str(day[2]),"kOutId":None,"kInId":None,"eId":None,"kfullnameout":"全部仓库","kfullnamein":"全部仓库","efullname":"全部职员","filterzero":0,"etypetypeid":None,"departtypeid":None,"departname":"全部部门","leveal":1},"orders":None,"filter":None,"first":0,"count":100000}
        redata=requests.post(url=reurl,data=json.dumps(reda),headers=header)
        redatlist=json.loads(redata.text)

        n=0
        reportdbnums=0
        reportdbmoney=0
        for data in redatlist["itemList"]["rows"]:
            n=n+1
            print u"调拨单第"+str(n)+u"行数据："+data[10]+ "............."

            #取明细数据
            #页面id
            redeurlid="http://beefun.wsgjp.com/Beefun/Report/GoodsTransBillQueryDetails.gspx"
            #deidda="{\"ptypeid\":\""+str(data[8])+"\",\"startDate\":\""+str(day[3])+",\"endDate\":\""+str(day[2])+"\",\"pfullname\":\"\",\"kOutId\":null,\"kInId\":null,\"eId\":null,\"etypetypeid\":null,\"departtypeid\":null}"
            deidda2="{\"ptypeid\":\""+str(data[8])+"\",\"startDate\":\""+str(day[3])+"\",\"endDate\":\""+str(day[2])+"\",\"pfullname\":\"\",\"kOutId\":null,\"kInId\":null,\"eId\":null,\"etypetypeid\":null,\"departtypeid\":null}"
            rededaid={"__Params":deidda2}
            resdeid=requests.post(url=redeurlid,headers=header2,data=rededaid)
            #print resdeid.text
            redepageid=browser.getpageid(resdeid)



            #明细页面数据
            rededaurl="http://beefun.wsgjp.com/Carpa.Web/Carpa.Web.Script.DataService.ajax/GetPagerData"
            rededadata={"pagerId":redepageid,"queryParams":None,"orders":None,"filter":None,"first":0,"count":100000}
            rededata=requests.post(url=rededaurl,data=json.dumps(rededadata),headers=header)
            rededatlist=json.loads(rededata.text)

            redetomoney=0
            redetonums=0
            m=0
            for dbdata in rededatlist["itemList"]["rows"]:
                m=m+1
                print u"调拨单明细第"+str(m)+u"行数据："+dbdata[12]+ "............."

                #商品名称
                dbitemname=dbdata[1]
                rename=data[10]
                self.assernote(rename,dbitemname,u"商品名称不相同（报表和其明细）","report item name ok",dbdata[12])

                #原始单据
                orurl="http://beefun.wsgjp.com/Beefun/Bill/GoodsTransBill.gspx?Vchtype="+str(dbdata[9])+"&Vchcode="+str(dbdata[8])+"&Mode=Read"
                ordetail=requests.get(orurl,headers=header)
                #print ordetail.text
                #原始单据头
                orheader=browser.getnotehead2(ordetail)

                #原始单据明细
                ordetotal=re.findall("\"details\":(.*?)freightbtypeid",ordetail.text)
                orlists=re.findall("outposition(.*?)urate2",ordetotal[0])
                for orlist in orlists:
                    orlistda=orlist.replace("\"",'')
                    orlistdata=re.findall(":(.*?),",orlistda)
                    #商品名字
                    oritemname=orlistdata[60]
                    if oritemname==dbitemname:
                        break



                #日期
                dbdate=dbdata[11]
                ordat=orheader[43][:10]
                self.assernote(dbdate,ordat,u"单据编号不相同（报表明细和原始单据）","reportdetail date ok",dbdata[12])

                #单据编号
                dbnum=dbdata[12]
                ornum=orheader[11]
                self.assernote(dbnum,ornum,u"单据编号不相同（报表明细和原始单据）","reportdetail note number ok",dbdata[12])

                #出库仓库
                dboutcate=dbdata[14]
                oroutcate=orheader[2]
                self.assernote(dboutcate,oroutcate,u"出库仓库不相同（报表明细和原始单据）","reportdetail out cate ok",dbdata[12])

                #入库仓库
                dbintocate=dbdata[15]
                orintocate=orheader[4]
                self.assernote(dbintocate,orintocate,u"入库仓库不相同（报表明细和原始单据）","reportdetail into cate ok",dbdata[12])

                #摘要
                dbsummary=dbdata[10]
                orsumm=orheader[12]
                self.assernote(dbsummary,orsumm,u"摘要不相同（报表明细和原始单据）","reportdetail summary ok",dbdata[12])

                #商品编号
                dbitemcode=dbdata[0]
                recode=data[1]

                #oritemnum=orheader[11]

                self.assernote(recode,dbitemcode,u"商品编号不相同（报表和其明细）","report item number ok",dbdata[12])





                #调拨数量
                dbnumbers=float(dbdata[18])
                ornums=float(orlistdata[5])
                dbnumbers=str("%.4f"%dbnumbers)
                ornums=str("%.4f"%ornums)
                self.assernote(dbnumbers,ornums,u"调拨数量不相同（报表明细和原始单据）","reportdetail numbers ok",dbdata[12])

                redetonums=redetonums+float(dbdata[18])


                #调拨金额
                dbmoney=float(dbdata[17])
                dbmoney=str("%.4f"%dbmoney)
                ormoney=float(orlistdata[7])
                ormoney=str("%.4f"%ormoney)
                self.assernote(dbmoney,ormoney,u"调拨金额不相同（报表明细和原始单据）","reportdetail money ok",dbdata[12])

                redetomoney=redetomoney+float(dbdata[17])




            #明细页面统计
            redesumdata=browser.reportsumdata(redepageid,header)
            #print "redesumdata.................."
            #print redesumdata


            #调拨数量
            renums=data[14]
            renums=str("%.4f"%renums)
            redetonums=str("%.4f"%redetonums)
            self.assernote(redetonums,renums,u"调拨数量不相同（报表和报表明细）","report total numbers ok",dbdata[12])


            desumnum=float(redesumdata["qty"]["value"])
            desumnum=str("%.4f"%desumnum)
            self.assernote(redetonums,desumnum,u"调拨数量不相同（报表明细和其统计）","reportdetail total numbers ok",dbdata[12])

            reportdbnums=reportdbnums+float(data[14])


            #调拨金额
            remoney=data[15]
            remoney=str("%.4f"%remoney)
            redetomoney=str("%.4f"%redetomoney)
            self.assernote(redetomoney,remoney,u"调拨金额不相同（报表和报表明细）","report total money ok",dbdata[12])

            desummoney=float(redesumdata["total"]["value"])
            desummoney=str("%.4f"%desummoney)
            self.assernote(redetomoney,desummoney,u"调拨金额不相同（报表明细和其统计）","reportdetail total money ok",dbdata[12])

            reportdbmoney=reportdbmoney+float(data[15])


            #总条数
            depageto=re.findall("itemCount\":(.*?),",resdeid.text)
            depageto=float(depageto[0])
            delistnum=float(len(rededatlist["itemList"]["rows"]))
            self.assernote(depageto,delistnum,u"调拨总条数不相同（报表明细和其页面统计）","reportdetail total lists ok",dbdata[12])




        #报表页面统计数据
        print u'报表页面统计数据...........................'
        resumdata=browser.reportsumdata(repageid,header)

        #数量
        resumnum=resumdata["qty"]["value"]
        resumnum=str("%.4f"%resumnum)
        reportdbnums=str("%.4f"%reportdbnums)
        self.assernote(resumnum,reportdbnums,u"调拨金额不相同（报表和其统计）","report sum total numbers ok","报表页面统计数据数量")

        #金额
        resummoney=float(resumdata["total"]["value"])
        resummoney=str("%.4f"%resummoney)
        reportdbmoney=str("%.4f"%reportdbmoney)
        self.assernote(resummoney,reportdbmoney,u"调拨金额不相同（报表和其统计）","report sum total money ok","报表页面统计数据金额")


        #总条数
        pageto=re.findall("itemCount\":(.*?),",resid.text)
        pageto=float(pageto[0])
        relistnum=float(len(redatlist["itemList"]["rows"]))
        self.assernote(pageto,relistnum,u"调拨总条数不相同（报表和其页面统计）","reportl total lists ok","报表页面统计数据总条数")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
