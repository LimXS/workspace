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

class stockspannertTest(unittest.TestCase):
    u'''报表-库存报表-生产组装单统计'''

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


    def teststockSpanner(self):
        u'''报表-库存报表-生产组装单统计'''
        #单据中心
        #单据中心数据
        header={'cookie':self.cookiestr,"Content-Type": "application/json"}
        header2={'cookie':self.cookiestr,"Content-Type": "application/x-www-form-urlencoded"}
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


            #生产组装单单据
            if number[:3]=='ZZ-':
                print u"单据号为："+str(number)+u"进行对比............................."
                noteurl="http://beefun.wsgjp.com/Beefun/Bill/AssemblyBill.gspx?Vchtype="+str(Vchtype)+"&Vchcode="+str(Vchcode)+"&Mode=Read"
                notedetail=requests.get(noteurl,headers=header)
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

                self.assernote(str(vchtype),str(notetype[0][:-1]),u"单据类型不相同（单据中心和其明细）","note type ok",number)

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
                if btypename==None:
                    btypename='null'
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

        #报表-库存报表-拆装单统计
        print u"报表-库存报表-拆装单统计..........................."
        #取拆装单统计页面id
        stamp=browser.gettimestamp()
        today=stamp[2]
        startday=stamp[3]
        reurlid="http://beefun.wsgjp.com/Beefun/Report/AssemblyQuery.gspx"
        reidda="{\"kOutId\":null,\"kfullnameout\":\"全部仓库\",\"kInId\":null,\"kfullnameint\":null,\"eId\":null,\"efullname\":\"全部职员\",\"departtypeid\":null,\"deptname\":null,\"startDate\":\""+startday+"\",\"endDate\":\""+today+"\",\"SaveDate\":false,\"kfullnamein\":\"全部仓库\",\"departname\":\"全部部门\"}"
        redidata={"__Params":reidda}
        reidte=requests.post(url=reurlid,data=redidata,headers=header2)
        #print reidte.text
        reid=browser.getpageid(reidte)
        #print reid

        #取拆装单统计页面数据
        print "取拆装单统计页面数据......................................."
        relisturl="http://beefun.wsgjp.com/Carpa.Web/Carpa.Web.Script.DataService.ajax/GetPagerData"
        relisdat={"pagerId":reid,"queryParams":{"level":1,"partypeid":"00000","profileid":0,"startDate":startday,"endDate":today,"kOutId":None,"kInId":None,"eId":None,"kfullnameout":"全部仓库","kfullnamein":"全部仓库","efullname":"全部职员","etypetypeid":None,"departtypeid":None,"departname":"全部部门","ptypetypeid":"00000"},"orders":None,"filter":None,"first":0,"count":100000}
        relis=requests.post(url=relisturl,data=json.dumps(relisdat),headers=header)
        relists=json.loads(relis.text)
        #print relis.text

        m=0
        inums=0
        inmoney=0
        outnums=0
        outmoney=0
        for redata in relists["itemList"]["rows"]:
            m=m+1
            #报表页面数据
            print u"报表页面数据第"+str(m)+u"行数据:"+str(redata[10])
            #编号
            recode=redata[1]

            #名称
            rename=redata[10]

            #报表页面明细单据
            print u"报表页面明细单据......................"

            #明细页面id
            #print u"报表页面明细id......................"
            deidurl="http://beefun.wsgjp.com/Beefun/Report/AssemblyBillQuery.gspx"
            deidda="{\"ptypeid\":\""+str(redata[8])+"\",\"startDate\":\""+startday+"\",\"endDate\":\""+today+"\",\"pfullname\":\"\",\"kOutId\":null,\"kInId\":null,\"eId\":null,\"etypetypeid\":null,\"departtypeid\":null}"
            dedidata={"__Params":deidda}
            deidte=requests.post(url=deidurl,data=dedidata,headers=header2)
            #print deidte.text
            deid=browser.getpageid(deidte)
            #print deid

            #明细页面数据
            dedaurl="http://beefun.wsgjp.com/Carpa.Web/Carpa.Web.Script.DataService.ajax/GetPagerData"
            deda={"pagerId":deid,"queryParams":None,"orders":None,"filter":None,"first":0,"count":100000}
            delis=requests.post(url=dedaurl,data=json.dumps(deda),headers=header)
            delists=json.loads(delis.text)
            #print delists

            delissuminnum=0
            delissuminmoney=0
            delissumoutnum=0
            delissumoutmoney=0

            for dedata in delists["itemList"]["rows"]:
                #每一条明细数据

                #原始单据
                Vchtype=dedata[9]
                Vchcode=dedata[8]

                orurl="http://beefun.wsgjp.com/Beefun/Bill/AssemblyBill.gspx?Vchtype="+str(Vchtype)+"&Vchcode="+str(Vchcode)+"&Mode=Read"
                ordata=requests.get(orurl,headers=header)

                #头
                orheader=browser.getnotehead2(ordata)

                orinthis=[]
                oroutthis=[]
                #入库
                inlis=browser.dbnotedatain(ordata)
                for indetail in inlis:
                    inlisdetail=browser.dbnotedetail(indetail)
                    #商品名称
                    if inlisdetail[60]==dedata[1]:
                        orinthis=inlisdetail
                        break

                #出库
                outlis=browser.dbnotedataout(ordata)
                for outdetail in outlis:
                    outlisdetail=browser.dbnotedetail(outdetail)
                    #商品名称
                    if outlisdetail[60]==dedata[1]:
                        oroutthis=outlisdetail
                        break


                print u"报表明细和原始单据："+str(dedata[12])
                #日期
                ordate=orheader[31][9:-1]
                ordate=browser.handlestampdays(ordate,0)
                dedate=dedata[11]
                self.assernote(dedate,ordate,u"日期不相同（报表明细和原始单据）","reportdetail date ok",dedata[12])



                #单据编号
                orcode=orheader[11]
                decode=dedata[12]
                self.assernote(decode,orcode,u"单据编号不相同（报表明细和原始单据）","reportdetail code ok",dedata[12])

                #入库仓库
                orincate=orheader[2]
                deincate=dedata[14]
                self.assernote(deincate,orincate,u"入库仓库不相同（报表明细和原始单据）","reportdetail in cate ok",dedata[12])

                #出库仓库
                oroutcate=orheader[4]
                deoutcate=dedata[15]
                self.assernote(deoutcate,oroutcate,u"出库仓库不相同（报表明细和原始单据）","reportdetail out cate ok",dedata[12])

                #摘要
                orsummary=orheader[12]
                desummary=dedata[10]
                self.assernote(desummary,orsummary,u"摘要不相同（报表明细和原始单据）","reportdetail summary ok",dedata[12])


                if len(orinthis)>0 and len(oroutthis)>0:
                    #入库数量
                    orinnums=float(orinthis[5])
                    #入库金额
                    orinmoney=float(orinthis[7])
                    #出库数量
                    oroutnums=float(oroutthis[5])
                    #出库金额
                    oroutmoney=float(oroutthis[7])
                    oritemcode=orinthis[64]
                else:
                    if len(oroutthis)>0:
                        orinnums=0
                        orinmoney=0
                        oroutnums=float(oroutthis[5])
                        oroutmoney=float(oroutthis[7])
                        oritemcode=oroutthis[64]
                    else:
                        orinnums=float(orinthis[5])
                        #入库金额
                        orinmoney=float(orinthis[7])
                        oroutnums=0
                        oroutmoney=0
                        oritemcode=orinthis[64]

                #入库数量
                orinnums=str("%.4f"%orinnums)
                delisinums=dedata[20]
                delisinums=str("%.4f"%delisinums)
                self.assernote(delisinums,orinnums,u"出库数量不相同（报表明细和原始单据）","reportdetail in numbers ok",dedata[12])

                delissuminnum=delissuminnum+dedata[20]

                #入库金额
                orinmoney=str("%.4f"%orinmoney)
                delisinmoney=dedata[19]
                delisinmoney=str("%.4f"%delisinmoney)
                self.assernote(delisinmoney,orinmoney,u"入库金额不相同（报表明细和原始单据）","reportdetail in money ok",dedata[12])

                delissuminmoney=delissuminmoney+dedata[19]

                #出库数量
                oroutnums=str("%.4f"%oroutnums)
                delisoutums=dedata[18]
                delisoutums=str("%.4f"%delisoutums)
                self.assernote(delisoutums,oroutnums,u"出库数量不相同（报表明细和原始单据）","reportdetail out numbers ok",dedata[12])

                delissumoutnum=delissumoutnum+dedata[18]

                #出库金额
                oroutmoney=str("%.4f"%oroutmoney)
                delisoutmoney=dedata[17]
                delisoutmoney=str("%.4f"%delisoutmoney)
                self.assernote(delisoutmoney,oroutmoney,u"出库金额不相同（报表明细和原始单据）","reportdetail out money ok",dedata[12])

                delissumoutmoney=delissumoutmoney+dedata[17]

                #商品编号
                deitemcode=dedata[0]
                self.assernote(deitemcode,oritemcode,u"商品编号不相同（报表明细和原始单据）","reportdetail item code ok",dedata[12])




            #明细页面统计
            print u"报表明细页面统计数据......................"
            desumdaurl="http://beefun.wsgjp.com/Carpa.Web/Carpa.Web.Script.DataService.ajax/GetPagerSummary"
            desumda={"pagerId":deid}
            deto=requests.post(url=desumdaurl,data=json.dumps(desumda),headers=header)
            #print reto.text
            detotal=json.loads(deto.text)
            #print detotal


            #入库数量
            relisinnums=float(redata[18])
            deinums=float(detotal["qty2"]["value"])
            self.assernote(relisinnums,deinums,u"入库数量不相同（报表页面和明细）","report in numbers ok",redata[10])

            delissuminnum=float(delissuminnum)
            self.assernote(delissuminnum,deinums,u"入库数量不相同（报表明细和其页面统计）","reportdetail total in numbers ok",redata[10])


            inums=inums+float(redata[18])

            #入库金额
            relisinmoney=float(redata[17])
            deinmoney=float(detotal["total2"]["value"])
            self.assernote(relisinmoney,deinmoney,u"入库金额不相同（报表页面和明细）","report in money ok",redata[10])

            delissuminmoney=float(delissuminmoney)
            self.assernote(delissuminmoney,deinmoney,u"入库金额不相同（报表明细和其页面统计）","reportdetail self total in money ok",redata[10])

            inmoney=inmoney+float(redata[17])

            #出库数量
            relisoutnums=float(redata[16])
            deoutums=float(detotal["qty"]["value"])
            self.assernote(relisoutnums,deoutums,u"出库数量不相同（报表页面和明细）","report out numbers ok",redata[10])

            delissumoutnum=float(delissumoutnum)
            self.assernote(delissumoutnum,deoutums,u"出库数量不相同（报表明细和其页面统计）","reportdetail self total out numbers ok",redata[10])

            outnums=outnums+float(redata[16])

            #出库金额
            relisoutmoney=float(redata[15])
            deoutmoney=float(detotal["total"]["value"])
            self.assernote(relisoutmoney,deoutmoney,u"出库金额不相同（报表页面和明细）","report out money ok",redata[10])

            delissumoutmoney=float(delissumoutmoney)
            self.assernote(str(delissumoutmoney),str(deoutmoney),u"出库金额不相同（报表明细和其页面统计）","reportdetail self total out money ok",redata[10])

            outmoney=outmoney+float(redata[15])


            #总条数
            delistotal=float(len(delists["itemList"]["rows"]))
            depagesumlis=re.findall("itemCount\":(.*?),",deidte.text)
            depagesumlis=float(depagesumlis[0])
            self.assernote(delistotal,depagesumlis,u"拆装总条数不相同（报表明细和其页面统计）","reportdetail total lists ok",redata[10])



        #取拆装单统计页面统计数据
        print "拆装单统计页面统计数据..................................."
        retourl="http://beefun.wsgjp.com/Carpa.Web/Carpa.Web.Script.DataService.ajax/GetPagerSummary"
        retodat={"pagerId":reid}
        reto=requests.post(url=retourl,data=json.dumps(retodat),headers=header)
        #print reto.text
        retotal=json.loads(reto.text)

        #入库数量
        resuminnums=retotal["qty1"]["value"]
        resuminnums=str("%.4f"%resuminnums)
        inums=str("%.4f"%inums)
        self.assernote(resuminnums,inums,u"入库数量不相同（报表页面和它页面的统计）","reportself in numbers ok",u"拆装单统计")


        #入库金额
        resuminmoney=retotal["total1"]["value"]
        resuminmoney=str("%.4f"%resuminmoney)
        inmoney=str("%.4f"%inmoney)
        self.assernote(resuminmoney,inmoney,u"入库金额不相同（报表页面和它页面的统计）","reportself in money ok",u"拆装单统计")


        #出库数量
        resumoutnums=retotal["qty"]["value"]
        resumoutnums=str("%.4f"%resumoutnums)
        outnums=str("%.4f"%outnums)
        self.assernote(resumoutnums,outnums,u"出库数量不相同（报表页面和它页面的统计）","reportself out numbers ok",u"拆装单统计")


        #出库金额
        resumoutmoney=retotal["total"]["value"]
        resumoutmoney=str("%.4f"%resumoutmoney)
        outmoney=str("%.4f"%outmoney)
        self.assernote(resumoutmoney,outmoney,u"出库金额不相同（报表页面和它页面的统计）","reportself out money ok",u"拆装单统计")

        #总条数
        retolistsnums=float(relists["itemCount"])
        resumlistsnums=float(len(relists["itemList"]["rows"]))
        self.assernote(retolistsnums,resumlistsnums,u"数据总条数不相同（报表页面和它页面的统计）","reportself lists numbers ok",u"拆装单统计")





if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
