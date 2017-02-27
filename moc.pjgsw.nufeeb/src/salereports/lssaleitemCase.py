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

class lssaleitenTest(unittest.TestCase):
    u'''报表-批发零售报表-零售商品统计'''

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


    def testLssaleitemTest(self):
        u'''报表-批发零售报表-零售商品统计'''

        header={'cookie':self.cookiestr,"Content-Type": "application/json"}
        header2={'cookie':self.cookiestr,"Content-Type": "application/x-www-form-urlencoded"}

        stamp=browser.gettimestamp()
        #报表取数
        #页面id
        urlid="http://beefun.wsgjp.com/Beefun/Bill/Retail/RetailPTypeQuery.gspx"
        pagedata=browser.pageidsum(urlid,header)
        pageid=pagedata[0]

        #一周内页面数据
        urldata="http://beefun.wsgjp.com/Carpa.Web/Carpa.Web.Script.DataService.ajax/GetPagerData"
        pagelistdata={"pagerId":pageid,"queryParams":{"vchcode":0,"number":None,"vchtype":0,"poststate":1,"ktypeid":0,"btypeid":0,"etypeid":0,"vipcardid":0,"datefield":"overtime","tablesimple":"b","begindate":stamp[3],"enddate":stamp[2],"mintotal":None,"maxtotal":None,"filtermode":"quickquery","filterstr":"","kfullname":None,"efullname":None},"orders":None,"filter":None,"first":0,"count":100000}
        #pagetext=requests.post(url=urldata,data=json.dumps(pagelistdata),headers=header)
        #pagelists=browser.datatrunjson(pagetext)
        pagelists=browser.pagedetail(urldata,pagelistdata,header)
        #print pagelists
        notelistout=[]
        notelistback=[]


        #单据中心
        pagedic=browser.notecentel(header)
        print u"单据中心................................."
        #总条数
        #print "pagedic...."
        #print pagedic
        itemcount=str(pagedic["itemCount"])
        pagelisttotal=str(len(pagedic["itemList"]))
        self.assernote(pagelisttotal,itemcount,u"总条数不相同（单据中心和和它页面）","note total list  ok","单据中心总条数")


        notetotalmoney=0.00

        for j in range(len(pagedic["itemList"])):
            #单据
            number=pagedic["itemList"][j]["number"]

            if number[:3]=='LS-':
                #print
                print u"单据号为："+str(number)
                vchcode=pagedic["itemList"][j]["vchcode"]
                vchtypeid=pagedic["itemList"][j]["vchtypeid"]
                noteurl="http://beefun.wsgjp.com/Beefun/Bill/SaleBill.gspx?Vchtype="+str(vchtypeid)+"&Vchcode="+vchcode+"&Mode=Read"
                notetext=requests.get(url=noteurl,headers=header)
            elif number[:3]=='LT-':
                print u"单据号为："+str(number)
                vchcode=pagedic["itemList"][j]["vchcode"]
                vchtypeid=pagedic["itemList"][j]["vchtypeid"]
                noteurl="http://beefun.wsgjp.com/Beefun/Bill/SaleBackBill.gspx?Vchtype="+str(vchtypeid)+"&Vchcode="+vchcode+"&Mode=Read"
                notetext=requests.get(url=noteurl,headers=header)
                #print notetext.text
                #noteheader=browser.getnotehead2(notetext)
            else:
                continue

            #原始单据头
            noteheader=browser.getnotehead2(notetext)
            #原始单据明细
            notedetail=browser.salenoteoutdata(notetext)
            for a in notedetail:
                detail=browser.dbnotedetail(a)
                if number[:3]=='LS-':
                    notelistout.append(detail)
                elif number[:3]=='LT-':
                    notelistback.append(detail)

            #print "notelistout..........."
            #print notelistout


            #日期
            dat=pagedic["itemList"][j]["date"]
            notedat=noteheader[43][:10]
            self.assernote(dat,notedat,u"日期不相同（单据中心和其明细）","note date ok",number)

            #单据编号
            self.assernote(number,noteheader[11],u"单据编号不相同（单据中心和其明细）","note number ok",number)

            #单据类型
            vchtype=pagedic["itemList"][j]["vchtype"]
            notetype=re.findall("\<title\>(.*?)\</title\>",notetext.text)
            if number[:3]=='LS-':
                    self.assernote(str(vchtype),str(notetype[0]),u"单据类型不相同（单据中心和其明细）","note type ok",number)
            elif number[:3]=='LT-':
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







        #print pagelists
        #报表核对
        #页面sum
        #pagesum=pagedata[1]

        n=0
        salenum=0
        renum=0
        addnum=0
        money=0
        dismoney=0
        for item in pagelists["itemList"]["rows"]:
            n=n+1
            print u"报表第"+str(n)+u"行数据:"+str(item[19])

            coroutnum=0
            corbacknum=0
            cordpmoney=0
            cormoney=0

            itcode=0
            #print "item...."
            #print item
            for detail in notelistout:
                #print "detail"
                #print detail

                if item[20]==detail[74]:

                    coroutnum+=float(detail[19])
                    cordpmoney+=float(detail[10])
                    cormoney+=float(detail[12])
                    if itcode==0:
                        #商品编号
                        self.assernote(str(item[17]),str(detail[78]),u"商品编号不相同（零售商品统计报表明细商品）","report item code ok",u"商品编号")
                        itcode=1
                else:
                    continue

            for detail in notelistback:
                #print detail
                if item[20]==detail[74]:
                    corbacknum+=float(detail[19])
                    cordpmoney-=float(detail[10])
                    cormoney-=float(detail[12])
                    if itcode==0:
                        #商品编号
                        self.assernote(str(item[17]),str(detail[78]),u"商品编号不相同（零售商品统计报表明细商品）","report item code ok",u"商品编号")
                        itcode=1
                else:
                    continue


            #零售数量
            float(item[3])
            salenum+=float(item[3])
            self.assernote(str(float(item[3])),str(float(coroutnum)),u"零售数量不相同（零售商品统计报表明细商品）","report item out nums ok",u"零售数量")

            #退货数量
            renum+=float(item[4])
            self.assernote(str(float(item[4])),str(float(corbacknum)),u"退货数量不相同（零售商品统计报表明细商品）","report item back nums ok",u"退货数量")


            #数量小计
            addnum+=float(item[5])
            self.assernote(str(float(item[5])),str(float(item[3])-float(item[4])),u"数量小计不相同（零售商品统计报表明细商品）","report item count nums ok",u"数量小计")

            #辅助数量

            #单价
            if item[10]=='false':
                sigle=0.0
            else:
                sigle=float(item[10])
            orcountsigle=cordpmoney/(float(item[3])-float(item[4]))
            self.assernote(str("%.4f"%sigle),str("%.4f"%orcountsigle),u"单价不相同（零售商品统计报表明细商品）","report item sigle ok",u"单价")

            #金额
            float(item[5])
            money+=float(item[6])
            self.assernote(str(float(item[6])),str(cordpmoney),u"金额不相同（零售商品统计报表明细商品）","report item money ok",u"金额")

            #平均折扣
            if item[8]=='false':
                disavg=0.0
            else:
                disavg=float(item[8])
            comdisavg=round(cormoney/cordpmoney,2)
            self.assernote(str("%.2f"%disavg),str("%.2f"%comdisavg),u"平均折扣不相同（零售商品统计报表明细商品）","report item avg discount ok",u"平均折扣")

            #折扣均价
            if item[9]=='false':
                avprice=0.0
            else:
                avprice=float(item[9])
            countprice=round(cordpmoney/(float(item[3])-float(item[4]))*cormoney/cordpmoney,4)
            self.assernote(str("%.4f"%avprice),str("%.4f"%countprice),u"折扣均价不相同（零售商品统计报表明细商品）","report item discount sigle ok",u"折扣均价")
            #print cordpmoney/(float(item[2])-float(item[3]))*cormoney/cordpmoney

            #折后金额
            #float(item[7])
            dismoney+=float(item[7])
            self.assernote(str(float(item[7])),str(cormoney),u"折后金额不相同（零售商品统计报表明细商品）","report item discount money ok",u"折后金额")


        #页面统计sum
        urlsum="http://beefun.wsgjp.com/Carpa.Web/Carpa.Web.Script.DataService.ajax/GetPagerSummary"
        sumdata={"pagerId":pageid}
        sumtext=requests.post(url=urlsum,data=json.dumps(sumdata),headers=header)
        pagesum=browser.datatrunjson(sumtext)
        #零售数量
        #print pageid
        #print pagesum
        self.assernote(str(pagesum["retailqty"]["value"]),str(salenum),u"零售数量不相同（零售商品统计报表和其页面统计）","report sum sale numbers ok",u"零售数量")

        #退货数量
        self.assernote(str(pagesum["backqty"]["value"]),str(renum),u"退货数量不相同（零售商品统计报表和其页面统计）","report sum return number ok",u"退货数量")

        #数量小计
        self.assernote(str(pagesum["qty"]["value"]),str(addnum),u"数量小计不相同（零售商品统计报表和其页面统计）","report sum count number ok",u"数量小计")

        #金额
        self.assernote(str(pagesum["dptotal"]["value"]),str(money),u"金额不相同（零售商品统计报表和其页面统计）","report sum money ok",u"金额")

        #折后金额
        self.assernote(str(pagesum["total"]["value"]),str(dismoney),u"折后金额不相同（零售商品统计报表和其页面统计）","report sum discount money ok",u"折后金额")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()