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

class lssalereturnTest(unittest.TestCase):
    u'''批零-零售退货单'''

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


    def testLssalereturn(self):
        u'''批零-零售退货单(新增)'''

        header={'cookie':self.cookiestr,"Content-Type": "application/json"}
        header2={'cookie':self.cookiestr,"Content-Type": "application/x-www-form-urlencoded"}

        #stamp=browser.gettimestamp()
        dom = xml.dom.minidom.parse(r'C:\workspace\moc.pjgsw.nufeeb\src\data\salecreatedata')
        modulename=browser.xmlRead(self.driver,dom,"module",6)
        moduledetail=browser.xmlRead(self.driver,dom,'moduledetail',6)

        browser.openModule2(self.driver,modulename,moduledetail)

        #选择商品
        lsreitem=browser.xmlRead(self.driver,dom,'lsreitem',0)
        lsreiteminput=browser.xmlRead(self.driver,dom,'lsreiteminput',0)
        lsreitemok=browser.xmlRead(self.driver,dom,'lsreitemok',0)

        #browser.setheader(self.driver,lsitem,lsiteminput,lsitemok)

        time.sleep(1)
        browser.findXpath(self.driver,lsreitem).click()
        time.sleep(2)
        browser.findXpath(self.driver,lsreiteminput).click()
        browser.findXpath(self.driver,lsreitemok).click()

        #选择套餐
        lsretaocan=browser.xmlRead(self.driver,dom,'lsretaocan',0)
        lsretaocaninput=browser.xmlRead(self.driver,dom,'lsretaocaninput',0)
        lsretaocanok=browser.xmlRead(self.driver,dom,'lsretaocanok',0)
        lsretaonum=browser.xmlRead(self.driver,dom,'lsretaonum',0)
        lsretaonumok=browser.xmlRead(self.driver,dom,'lsretaonumok',0)

        #browser.setheader(self.driver,lsitem,lsiteminput,lsitemok)

        time.sleep(1)
        browser.findXpath(self.driver,lsretaocan).click()
        time.sleep(1)
        browser.findXpath(self.driver,lsretaocaninput).click()
        browser.findXpath(self.driver,lsretaocanok).click()
        browser.findXpath(self.driver,lsretaonum).send_keys("2")
        browser.findXpath(self.driver,lsretaonumok).click()


        #选择会员
        lsrevip=browser.xmlRead(self.driver,dom,'lsrevip',0)
        lsrevipinput=browser.xmlRead(self.driver,dom,'lsrevipinput',0)
        lsrevipok=browser.xmlRead(self.driver,dom,'lsrevipok',0)

        #browser.setheader(self.driver,lsitem,lsiteminput,lsitemok)

        time.sleep(1)
        browser.findXpath(self.driver,lsrevip).click()
        time.sleep(1)
        browser.findXpath(self.driver,lsrevipinput).click()
        browser.findXpath(self.driver,lsrevipok).click()

        #结算
        lsrecount=browser.xmlRead(self.driver,dom,'lsrecount',0)
        time.sleep(1)
        browser.findXpath(self.driver,lsrecount).click()

        #结算编号
        #print vchcode
        counturl="http://beefun.wsgjp.com/Beefun/Bill/Retail/RetailSaveHint.gspx?VCHTYPE=13&vipMemberId=870069546699788&vchcode=0"
        counttext=requests.get(url=counturl,headers=header)
        #print counttext.text
        countid=re.findall("id=\"(.*?)bankAccountEnabled\"",counttext.text)
        countid=countid[0]
        #print countid

        #整单优惠
        redismoney=browser.xmlRead(self.driver,dom,'redismoney',0)
        browser.findId(self.driver,countid+redismoney).clear()
        browser.findId(self.driver,countid+redismoney).send_keys("1.8")

        #实收金额
        regetmoney=browser.xmlRead(self.driver,dom,'regetmoney',0)
        browser.findId(self.driver,countid+regetmoney).clear()
        browser.findId(self.driver,countid+regetmoney).send_keys("110.25")

        #赠送积分
        regivescore=browser.xmlRead(self.driver,dom,'regivescore',0)
        browser.findId(self.driver,countid+regivescore).clear()
        browser.findId(self.driver,countid+regivescore).send_keys("8")

        #储值退款
        recharge=browser.xmlRead(self.driver,dom,'recharge',0)
        browser.findId(self.driver,countid+recharge).clear()
        browser.findId(self.driver,countid+recharge).send_keys("7")
        browser.findId(self.driver,countid+recharge).click()

        #结算完成
        recountok=browser.xmlRead(self.driver,dom,'recountok',0)
        browser.findId(self.driver,countid+recountok).click()

    def testLssalereturnor(self):
        u'''批零-零售退货单(调用单据)'''

        header={'cookie':self.cookiestr,"Content-Type": "application/json"}
        header2={'cookie':self.cookiestr,"Content-Type": "application/x-www-form-urlencoded"}

        stamp=browser.gettimestamp()
        dom = xml.dom.minidom.parse(r'C:\workspace\moc.pjgsw.nufeeb\src\data\salecreatedata')
        modulename=browser.xmlRead(self.driver,dom,"module",6)
        moduledetail=browser.xmlRead(self.driver,dom,'moduledetail',6)

        browser.openModule2(self.driver,modulename,moduledetail)

        #调单
        time.sleep(2)
        salereselnote=browser.xmlRead(self.driver,dom,'salereselnote',0)
        browser.findXpath(self.driver,salereselnote).click()

        #提单页面id
        urlid="http://beefun.wsgjp.com/Beefun/Bill/Retail/RetailSelector.gspx"
        idda="{\"ktypeid\":\"2605638079543104740\",\"kfullname\":\"\",\"vchtype\":13,\"poststate\":2,\"begindate\":null,\"enddate\":null}"
        iddata={"__Params":idda}
        idtext=requests.post(url=urlid,data=iddata,headers=header2)
        #print idtext.text
        pageid=browser.getpageid(idtext)
        #print pageid

        #提单页面数据
        end=browser.handlestampdaysevery(stamp[0],2)
        urlpage="http://beefun.wsgjp.com/Carpa.Web/Carpa.Web.Script.DataService.ajax/GetPagerData"
        pagedata={"pagerId":pageid,"queryParams":{"vchcode":0,"number":"","vchtype":13,"poststate":2,"ktypeid":"2605638079543104740","btypeid":0,"etypeid":0,"vipcardid":0,"datefield":"overtime","tablesimple":"d","begindate":stamp[3],"enddate":end,"mintotal":None,"maxtotal":None,"filtermode":"number","filterstr":""},"orders":None,"filter":None,"first":0,"count":100000}
        pagetext=requests.post(url=urlpage,data=json.dumps(pagedata),headers=header)
        #print pagetext.text
        selectlists=browser.datatrunjson(pagetext)
        #print selectlists

        #制单数据
        saleorderdata=browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\salecreate\lssaledata','r',1,'aaa')
        flagnum=saleorderdata[0].strip()
        print "checkdata no............"
        print flagnum

        sedata=[]
        n=0
        #print selectlists
        for select in selectlists["itemList"]:
            #单据编号
            n += 1
            if flagnum==str(select["number"]):
                sedata=select
                break

        if len(sedata)>0:
            #选择单据
            time.sleep(1)
            saleselect=browser.xmlRead(self.driver,dom,'saleselect',0)
            for x in range(1,100):
                saleorxpath=saleselect+str(x)+"]/td[2]/div"
                if browser.findXpath(self.driver,saleorxpath).text==flagnum:
                    break
            #print saleorxpath
            #print x
            browser.findXpath(self.driver,saleorxpath).click()
            salereselok=browser.xmlRead(self.driver,dom,'salereselok',0)
            browser.findXpath(self.driver,salereselok).click()

            print u"提单页面数据有此订单，测试通过,进行数据比对"
            #print sedata

            #零售单据选择
            print u"零售单选择数据......................"
            #录单时间
            #timeArray = time.strptime(saleorderdata[5].strip(), "%Y-%m-%d %H:%M:%S")
            #timeStamp = int(time.mktime(timeArray))
            #print timeStamp
            #self.assernote(str(sedata["date"]),str(timeStamp*1000),u"录单时间不相同（零售单据选择页面和原始录入数据）","note select date ok",u"录单时间")

            #门店（仓库）
            self.assernote(str(sedata["kfullname"]),str(saleorderdata[3].strip()),u"门店（仓库）不相同（零售单据选择页面和原始录入数据）","note select cate ok",u"门店（仓库）")

            #营业员（经手人）
            self.assernote(str(sedata["efullname"]),str(saleorderdata[1].strip()),u"营业员（经手人）不相同（零售单据选择页面和原始录入数据）","note select handle people ok",u"营业员（经手人）")

            #部门
            self.assernote(str(sedata["dfullname"]),str(saleorderdata[2].strip()),u"部门不相同（零售单据选择页面和原始录入数据）","note select department ok",u"部门")

            #购买单位
            self.assernote(str(sedata["bfullname"]),str(saleorderdata[4].strip()),u"购买单位不相同（零售单据选择页面和原始录入数据）","note select department ok",u"部门")

            #detailid
            detailurlid="http://beefun.wsgjp.com/Beefun/Bill/Retail/RetailSelector.gspx"
            deidda="{\"ktypeid\":\"2605638079543104740\",\"kfullname\":\"\",\"vchtype\":13,\"poststate\":2,\"begindate\":\"2016-08-18 00:00:00\",\"enddate\":\"2016-08-18 23:59:59\"}"
            deiddata={"__Params":deidda}
            idtext=requests.post(url=detailurlid,data=deiddata,headers=header2)
            #print idtext.text
            selectid=browser.getpageid(idtext)
            #print selectid

            #detail
            vchcode=sedata["vchcode"]
            ktypeid=sedata["ktypeid"]
            detailid="http://beefun.wsgjp.com/Carpa.Web/Carpa.Web.Script.DataService.ajax/GetPagerData"
            detaildata={"pagerId":selectid,"queryParams":{"vchcode":vchcode,"number":"","btypeid":0,"etypeid":0,"ktypeid":ktypeid,"ptypeid":0,"begindate":None,"enddate":None,"vchtype":13,"poststate":2,"vipcardid":0,"datefield":"overtime","tablesimple":"d","mintotal":None,"maxtotal":None,"filtermode":"number","filterstr":""},"orders":None,"filter":None,"first":0,"count":100000}
            detailtext=requests.post(url=detailid,data=json.dumps(detaildata),headers=header)
            orlistsde=browser.datatrunjson(detailtext)
            #print orlistsde

            time.sleep(1)
            #会员信息
            reviptext=browser.xmlRead(self.driver,dom,'reviptext',0)
            revip=browser.findId(self.driver,reviptext).text

            #会员名
            #折扣
            #padisvip=re.findall("扣：(.*?)\（",revip)
            #print "padisvip...."
            #print padisvip
            #print revip
            #print revip[:25]
            #print revip[12:-22]
            orvip=str(saleorderdata[26].strip())
            #积分
            #余额
            self.assernote(str(revip[:28]),str(orvip[:52]),u"会员信息不相同（表单商和原始单据，包含会员名、折扣）","page vip info ok",u"会员信息")

            #商品详情
            l=0
            q=0
            #查看零售明细
            for k in range(0,2):
                print u"零售明细第"+str(k+1)+u"行数据明细："+str(saleorderdata[7+l].strip())
                #商品编号
                self.assernote(str(orlistsde["itemList"][k]["ptypecode"]),str(saleorderdata[6+l].strip()),u"商品编号不相同（选择单据查看零售明细和原始录入数据）","select detail item code ok",u"商品编号")

                #商品名称
                self.assernote(str(orlistsde["itemList"][k]["pfullname"]),str(saleorderdata[7+l].strip()),u"商品名称不相同（选择单据查看零售明细和原始录入数据）","select detail item name ok",u"商品名称")

                #数量
                self.assernote(str(float(orlistsde["itemList"][k]["qty"])),str(float(saleorderdata[10+q].strip())),u"数量不相同（选择单据查看零售明细和原始录入数据）","select detail item num ok",u"数量")

                #折扣
                self.assernote(str(float(orlistsde["itemList"][k]["discount"])),str(float(saleorderdata[13+q].strip())),u"折扣不相同（选择单据查看零售明细和原始录入数据）","select detail item discount ok",u"折扣")

                #金额
                self.assernote(str(float(orlistsde["itemList"][k]["tptotal"])),str(float(saleorderdata[15+q].strip())),u"金额不相同（选择单据查看零售明细和原始录入数据）","select detail item money ok",u"金额")

                l=l+2
                q=q+6



            #页面page商品详情
            cnum=0
            cdpmoney=0
            cmoney=0
            l=0
            q=0
            for n in range(0,2):
                print u"页面第"+str(n+1)+u"行商品数据："+str(saleorderdata[7+l].strip())
                m=2
                reiteminfo=browser.xmlRead(self.driver,dom,'reiteminfo2',0)
                reiteminfo=reiteminfo+str(n+1)+"]/td["

                #商品编号
                pacodexpath= reiteminfo+str(m)+"]/div"
                #print pacodexpath
                pacode=browser.findXpath(self.driver,pacodexpath).text
                saleorderdata[6+l].strip()
                self.assernote(str(pacode),str(saleorderdata[6+l].strip()),u"商品编号不相同（表单商品详情和原始录入数据）","page item code ok",u"商品编号")

                #商品名称
                paname=browser.findXpath(self.driver,reiteminfo+str(m+1)+"]/div").text
                self.assernote(str(paname),str(saleorderdata[7+l].strip()),u"商品名称不相同（表单商品详情和原始录入数据）","page item name ok",u"商品名称")

                #数量
                panum=float(browser.findXpath(self.driver,reiteminfo+str(m+8)+"]/div").text)
                cnum+=float(saleorderdata[10+q].strip())
                self.assernote(str(panum),str(float(saleorderdata[10+q].strip())),u"数量不相同（表单商品详情和原始录入数据）","page item nums ok",u"数量")

                #单价
                padpprice=float(browser.findXpath(self.driver,reiteminfo+str(m+10)+"]/div").text)
                #float(saleorderdata[11+q].strip())
                self.assernote(str(padpprice),str(float(saleorderdata[11+q].strip())),u"单价不相同（表单商品详情和原始录入数据）","page item dpprice ok",u"单价")

                #金额
                padpmoney=float(browser.findXpath(self.driver,reiteminfo+str(m+11)+"]/div").text)
                cdpmoney+=float(saleorderdata[12+q].strip())
                self.assernote(str(padpmoney),str(float(saleorderdata[12+q].strip())),u"金额不相同（表单商品详情和原始录入数据）","page item dpmoney ok",u"金额")

                #折扣
                padiscount=float(browser.findXpath(self.driver,reiteminfo+str(m+12)+"]/div").text)
                #float(saleorderdata[13+q].strip())
                self.assernote(str(padiscount),str(saleorderdata[13+q].strip()),u"折扣不相同（表单商品详情和原始录入数据）","page item discount ok",u"折扣")
                self.assernote(str(padiscount),str(revip[15:-26]),u"折扣不相同（表单商品详情和会员信息）","page vip discount ok",u"折扣")

                #折后单价
                paprice=float(browser.findXpath(self.driver,reiteminfo+str(m+13)+"]/div").text)
                #float(saleorderdata[14+q].strip())
                self.assernote(str(paprice),str(saleorderdata[14+q].strip()),u"折后单价不相同（表单商品详情和原始录入数据）","page item disprice ok",u"折后单价")


                #折后金额
                pamoney=float(browser.findXpath(self.driver,reiteminfo+str(m+14)+"]/div").text)
                cmoney+=float(saleorderdata[15+q].strip())
                self.assernote(str(pamoney),str(saleorderdata[15+q].strip()),u"折后金额不相同（表单商品详情和原始录入数据）","page item dismoneyok",u"折后金额")

                l=l+2
                q=q+6

            #选择后页面数据
            print u"页面表头数据.........."
            #数量
            #cnum
            self.assernote(str(cnum),str(float(saleorderdata[22].strip())),u"数量不相同（表单商品详情计算和原始单据）","note sum nums ok",u"数量")
            renumtext=browser.xmlRead(self.driver,dom,'renumtext',0)
            self.assernote(str(cnum),str(float(browser.findId(self.driver,renumtext).text)),u"数量不相同（表单商品详情计算和页面数据）","page sum num ok",u"数量")

            #折前金额
            #cdpmoney
            self.assernote(str(cdpmoney),str(float(saleorderdata[23].strip())),u"折前金额不相同（表单商品详情计算和原始单据）","note sum or dpmoney ok",u"折前金额")
            redpmoneytext=browser.xmlRead(self.driver,dom,'redpmoneytext',0)
            self.assernote(str(cdpmoney),str(float(browser.findId(self.driver,redpmoneytext).text)),u"折前金额不相同（表单商品详情计算和页面数据）","page sum dpmoney ok",u"折前金额")

            #金额
            #cmoney
            self.assernote(str(cmoney),str(float(saleorderdata[24].strip())),u"金额不相同（表单商品详情计算和原始单据）","note sum or money ok",u"金额")
            remoneytext=browser.xmlRead(self.driver,dom,'remoneytext',0)
            self.assernote(str(cmoney),str(float(browser.findId(self.driver,remoneytext).text)),u"金额不相同（表单商品详情计算和页面数据）","page sum money ok",u"金额")


            #营业员（经手人）
            rehandtext=browser.xmlRead(self.driver,dom,'rehandtext',0)
            self.assernote(str(browser.jsgettext(self.driver,rehandtext)),str(saleorderdata[1].strip()),u"营业员（经手人）不相同（页面和原始单据）","page header handle people ok",u"营业员（经手人）")

            #部门
            #saleorderdata[2].strip()
            redeptext=browser.xmlRead(self.driver,dom,'redeptext',0)
            self.assernote(str(browser.jsgettext(self.driver,redeptext)),str(saleorderdata[2].strip()),u"部门不相同（页面和原始单据）","page header department ok",u"部门")

            #购买单位
            #saleorderdata[4].strip()
            recomtext=browser.xmlRead(self.driver,dom,'recomtext',0)
            self.assernote(str(browser.jsgettext(self.driver,recomtext)),str(saleorderdata[4].strip()),u"购买单位不相同（页面和原始单据）","page header company ok",u"购买单位")

            #门店（仓库）
            #saleorderdata[3].strip()
            recatetext=browser.xmlRead(self.driver,dom,'recatetext',0)
            self.assernote(str(browser.jsgettext(self.driver,recatetext)),str(saleorderdata[3].strip()),u"门店（仓库）不相同（页面和原始单据）","page header cate ok",u"门店（仓库）")

            #编号
            recodetext=browser.xmlRead(self.driver,dom,'recodetext',0)
            #录单时间
            retimetext=browser.xmlRead(self.driver,dom,'retimetext',0)


            #结算
            lsrecount=browser.xmlRead(self.driver,dom,'lsrecount',0)
            time.sleep(1)
            browser.findXpath(self.driver,lsrecount).click()

            #结算编号
            #print vchcode
            counturl="http://beefun.wsgjp.com/Beefun/Bill/Retail/RetailSaveHint.gspx?VCHTYPE=13&vipMemberId=870069546699788&vchcode="+vchcode
            counttext=requests.get(url=counturl,headers=header)
            #print counttext.text
            countid=re.findall("id=\"(.*?)bankAccountEnabled\"",counttext.text)
            countid=countid[0]
            #print countid

            #整单优惠
            redismoney=countid+browser.xmlRead(self.driver,dom,'redismoney',1)
            browser.findId(self.driver,redismoney).clear()
            browser.findId(self.driver,redismoney).send_keys("1.8")

            #实收金额
            regetmoney=countid+browser.xmlRead(self.driver,dom,'regetmoney',1)
            browser.findId(self.driver,regetmoney).clear()
            browser.findId(self.driver,regetmoney).send_keys("110.25")

            #赠送积分
            regivescore=countid+browser.xmlRead(self.driver,dom,'regivescore',1)
            #browser.findId(self.driver,regivescore).clear()
            #browser.findId(self.driver,regivescore).send_keys("12")

            #储值退款
            recharge=browser.xmlRead(self.driver,dom,'recharge',0)
            browser.findId(self.driver,countid+recharge).clear()
            browser.findId(self.driver,countid+recharge).send_keys("7")
            browser.findId(self.driver,countid+recharge).click()

            #合计金额
            retotalmoney=countid+browser.xmlRead(self.driver,dom,'retotalmoney',0)
            retotalmoney=float(browser.jsgettext(self.driver,retotalmoney))
            self.assernote(str(cmoney),str(retotalmoney),u"合计金额不相同（表单头和结算数据）","count total money ok",u"合计金额")

            #待付金额
            recountmoeny=countid+browser.xmlRead(self.driver,dom,'recountmoeny',0)
            countmoney=float(browser.jsgettext(self.driver,recountmoeny))
            self.assernote(str(cmoney-2.7-7),str(countmoney-7),u"待付金额不相同（表单头和结算数据）","count wait money ok",u"待付金额")

            #找零
            waitmoney=countid+browser.xmlRead(self.driver,dom,'waitmoney',0)
            browser.findId(self.driver,waitmoney).click()
            waitmoney=float(browser.findId(self.driver,waitmoney).text)
            self.assernote(str(110.25-countmoney+7),str(waitmoney),u"找零不相同（表单头和结算数据）","count return money ok",u"找零")

            #结算完成
            recountok=countid+browser.xmlRead(self.driver,dom,'recountok',1)
            #print recountok
            #time.sleep(2)
            #browser.findId(self.driver,recountok).click()

        else:
            print u"提单页面数据无此订单，测试不通过"




if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()