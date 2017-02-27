#*-* coding:UTF-8 *-*
from selenium.webdriver.common.action_chains import ActionChains
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

class newstockreportTest(unittest.TestCase):
    u'''报表进货订单统计'''

    def setUp(self):
        self.driver=browser.startBrowser('chrome')
        browser.set_up(self.driver)
        time.sleep(2)

        '''
        f=open(r"E:\cookie.txt","r")
        cookie=f.read()
        self.cookiestr =cookie
        '''
        dom = xml.dom.minidom.parse(r'C:\workspace\moc.pjgsw.nufeeb\src\data\basedata')

        module='moudle'
        modulename=browser.xmlRead(self.driver,dom,module,1)
        moduledetail=browser.xmlRead(self.driver,dom,'page',1)
        browser.openModule2(self.driver,modulename,moduledetail)

        cookie = [item["name"] + "=" + item["value"] for item in self.driver.get_cookies()]
        self.cookiestr = ';'.join(item for item in cookie)


        time.sleep(2)
        #self.cookiestr=self.driver.get_cookies()


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

    def testnewstockReport(self):
        u'''报表进货订单统计'''
        dom = xml.dom.minidom.parse(r'c:\workspace\moc.pjgsw.nufeeb\src\data\report')
        module='module'
        module=browser.xmlRead(self.driver,dom,module,0)
        getstock=browser.xmlRead(self.driver,dom,'getstock',0)
        getstockreport=browser.xmlRead(self.driver,dom,'getstockreport',0)

        closeinto=browser.xmlRead(self.driver,dom,'closeinto',0)
        okinto=browser.xmlRead(self.driver,dom,'okinto',0)

        try:
            browser.openModule3(self.driver,module,getstock,getstockreport)
            browser.findXpath(self.driver,closeinto).click()
            print u"进入页面前关闭按钮测试成功"
        except:
            print u"进入页面前关闭按钮测试失败"
            print(traceback.format_exc())

        #进入报告页面
        time.sleep(2)
        browser.openModule3(self.driver,module,getstock,getstockreport)
        browser.findXpath(self.driver,okinto).click()




        #取订货订单管理全部数据
        #审核未审核都获取
        url="http://beefun.wsgjp.com.cn/Carpa.Web/Carpa.Web.Script.DataService.ajax/GetPagerData"
        headers={'cookie':self.cookiestr,'Content-Type': 'application/json'}
        data={"pagerId":"$609e9e2b$grid_pager1","queryParams":{"vchType":7,"xTypeid":"","isComplete":"1","isAudit":-1,"isExport":"-1","dlytype":-1},"orders":None,"filter":None,"first":0,"count":100000}

        managedata=requests.post(url,headers=headers,data=json.dumps(data))
        managedata=managedata.text

        #完成未完成都获取
        data3={"pagerId":"$609e9e2b$grid_pager1","queryParams":{"vchType":7,"xTypeid":"","isComplete":"0","isAudit":-1,"isExport":"-1","dlytype":-1},"orders":None,"filter":None,"first":0,"count":100000}
        managedata=requests.post(url,headers=headers,data=json.dumps(data3))
        managedata=managedata.text
        #按日期排序
        data2={"pagerId":"$609e9e2b$grid_pager1","queryParams":None,"orders":[{"dataField":"date","ascending":True}],"filter":None,"first":0,"count":100000}
        managedata=requests.post(url,headers=headers,data=json.dumps(data2))
        managedata=managedata.text

        #取每个订单的时间戳，订货日期
        orderdate=re.findall("\"date\":new Date\((.*?)\),",managedata)
        #print "orderdate........"
        #print "orderdate........"
        #print len(orderdate)

        #取每个订单的时间戳，到货日期
        okdate=re.findall("\"todate\":new Date\((.*?)\),",managedata)

        #将每个订单转换为字典
        managedata=managedata.replace(":true",":\"True\"")
        managedata=managedata.replace(":false",":\"False\"")
        managedata=re.sub("new(.*?),","\"None\",",managedata)


        #print "managedata.................."
        #print managedata
        #print len(managedata)
        totaloederstock=''
        try:
            managedata=json.loads(managedata)
            #订单总数
            totaloederstock=len(managedata["itemList"])
        except:
            print u"订单管理页面转换json失败"
            print "managedata.................."
            print managedata
            print managedata["Message"]
            print(traceback.format_exc())

        #print "totaloederstock.........."
        #print totaloederstock

        if totaloederstock>0:
            totalitem=[]

            for a in range(totaloederstock):
                #是否审核，0未审核，1已审核，只取已审核数据
                checked=managedata["itemList"][a]["default_audited"]
                if checked==0:
                    continue
                #订单编号
                number=managedata["itemList"][a]["number"]

                #获取每个订单详细数据并进行统计
                toqty=managedata["itemList"][a]["toqty"]
                untoqty=managedata["itemList"][a]["untoqty"]
                repairqty=managedata["itemList"][a]["repairqty"]
                repairtotal=managedata["itemList"][a]["repairtotal"]
                tototal=managedata["itemList"][a]["tototal"]
                untototal=managedata["itemList"][a]["untototal"]
                vchcode=managedata["itemList"][a]["vchcode"]
                comment=managedata["itemList"][a]["comment"]
                vchtype=managedata["itemList"][a]["vchtype"]
                summary=managedata["itemList"][a]["summary"]
                btypeid=managedata["itemList"][a]["btypeid"]
                etypeid=managedata["itemList"][a]["etypeid"]
                ktypeid=managedata["itemList"][a]["ktypeid"]
                ename=managedata["itemList"][a]["ename"]
                #仓库名称
                kfullname=managedata["itemList"][a]["kfullname"]
                #单位名称
                bname=managedata["itemList"][a]["bname"]
                total=managedata["itemList"][a]["total"]
                tptotal=managedata["itemList"][a]["tptotal"]
                dptotal=managedata["itemList"][a]["dptotal"]

                detailurl="http://beefun.wsgjp.com/Beefun/Beefun.Carrier.OrderManager.ajax/GetDetailsByorderid"
                detailheaders={'cookie':self.cookiestr,'Content-Type': 'application/json'}
                detaildata={"hashdata":{"toqty":toqty,"untoqty":untoqty,"repairqty":repairqty,"repairtotal":repairtotal,"tototal":tototal,"untototal":untototal,"isdelivered":0,"checked":0,"vchcode":vchcode,"vchtype":vchtype,"date":"\/Date(1466092800000)\/","number":number,"todate":"\/Date(1466092800000)\/","comment":comment,"summary":summary,"btypeid":btypeid,"bpartypeid":"00000","etypeid":etypeid,"ktypeid":ktypeid,"auditover":False,"ename":ename,"kfullname":kfullname,"bname":bname,"artotal":0,"aptotal":0,"r_warnup":0,"orderover1":0,"createtypename":"本地创建","createtype":0,"reccnt":0,"total":total,"tptotal":tptotal,"dptotal":dptotal,"default_audited":0,"default_auditorid":None,"default_audittime":None,"default_auditremark":"","finance_audited":0,"finance_auditorid":0,"finance_audittime":None,"finance_auditremark":"","isexport":0,"earnest":0,"finance_auditorname":"","business_auditorname":"","receiverpeople":None,"receivercellphone":None,"receivertelephone":None,"receiverzipcode":None,"province":None,"city":None,"district":None,"receiveraddress":None,"isneedinvoice":None}}
                detail=browser.orderRead(self.driver,detailurl,json.dumps(detaildata),detailheaders)
                detail=json.loads(detail)

                #print "detail..................."
                #print detail
                #进货单管理每一行数据具体数据
                items=[]
                for k in range(len(detail)):
                    #print "detail.........................................."
                    #print detail[k]
                    #商品编号
                    item=[]
                    ptypecode=detail[k]["ptypecode"]
                    item.append(ptypecode)

                    #商品名字
                    pfullname=detail[k]["pfullname"]
                    item.append(pfullname)

                    #单位编号

                    #单位名称
                    bname=managedata["itemList"][a]["bname"]
                    item.append(bname)

                    #进货日期
                    ordate=orderdate[a]
                    item.append(ordate)

                    #到货日期
                    kodate=okdate[a]
                    item.append(kodate)

                    #数量
                    qty=detail[k]["qty"]
                    item.append(qty)

                    #单价
                    price=detail[k]["price"]
                    item.append(price)

                    #金额
                    total=detail[k]["total"]
                    item.append(total)

                    #未完成数量
                    untoqty=detail[k]["untoqty"]
                    item.append(untoqty)

                    #完成数量
                    toqty=detail[k]["toqty"]
                    item.append(toqty)

                    #补订数量
                    repairqty=detail[k]["repairqty"]
                    item.append(repairqty)

                    #未完成金额，六位小数
                    untototal=detail[k]["untototal"]
                    item.append(untototal)

                    #完成金额
                    tototal=detail[k]["tototal"]
                    item.append(tototal)

                    #补订金额，六位小数
                    repairtotal=detail[k]["repairtotal"]
                    item.append(repairtotal)

                    #订货金额
                    tptotal=detail[k]["tptotal"]
                    item.append(tptotal)

                    #订货单价
                    asstpprice=detail[k]["asstpprice"]
                    item.append(asstpprice)

                    #
                    #
                    #print "item............."
                    #print item

                    items.append(item)
                #进货订单管理已审核所有订单明细
                totalitem.append(items)

        else:
            print u"进货订单管理无已审核数据"
            #flagmange=0

        #print "totalitem..............."
        #print len(totalitem)
        #print totalitem

        #totalitem相同的商品进行合并
        '''
        for a in range(len(totalitem)):
            for b in range(len(totalitem[a])):
        '''
        #进入明细数据页面
        try:
            exitdetail=browser.xmlRead(self.driver,dom,'exitdetail',0)
            for j in range(1,10):
                detailxpath=browser.xmlRead(self.driver,dom,'reportdetail1',0)+str(j)+browser.xmlRead(self.driver,dom,'reportdetail2',0)
                status=browser.elementisexist(self.driver,detailxpath)
                #print "status................"
                #print detailxpath
                #print status
                if status==True:
                    doubledetail =browser.findXpath(self.driver,detailxpath)
                    ActionChains(self.driver).double_click(doubledetail).perform()
                    print u"进入第"+str(j)+u"条明细数据页面成功，测试通过"
                    time.sleep(2)
                    browser.findXpath(self.driver,exitdetail).click()
                    print u"退出第"+str(j)+u"条明细数据页面成功，测试通过"
                    break
                '''
                else:
                    if j==1:
                       print "进货订单报表页面无数据"
                    break
                '''
        except:
            print u"进货订单报告页面明细页面失败"
            print(traceback.format_exc())

        #取报表页面数据#订货订单页面id

        url2="http://beefun.wsgjp.com.cn/Beefun/Report/PTypeSaleOrderStatistic.gspx?vchtype=stockorder"
        #headers={'cookie':cookie,'Content-Type': 'application/json'}
        headers={'cookie':self.cookiestr,'Content-Type': 'application/x-www-form-urlencoded'}
        timeStamp=time.time()
        timeArray = time.localtime(timeStamp)
        otherStyleTime = time.strftime("%Y-%m-%d", timeArray)
        #print otherStyleTime

        threeDayAgo = (datetime.datetime.now() - datetime.timedelta(days = 6))
        timeStamp = int(time.mktime(threeDayAgo.timetuple()))
        otherStyleTime2 = threeDayAgo.strftime("%Y-%m-%d")
        #print otherStyleTime2

        a="{\"startDate\":\""+otherStyleTime2+"\",\"endDate\":\""+otherStyleTime+"\",\"index\":0,\"btypeid\":0}"
        #a="{\"startDate\":\"2016-06-14\",\"endDate\":\"2016-06-20\",\"index\":0,\"btypeid\":0}"
        data={"__Params":a}
        #data={"__Params":"{'startDate':'2016-06-14','endDate':'2016-06-20','index':0,'btypeid':0}"}
        erpdata=requests.post(url=url2,data=data,headers=headers)

        #报表统计数据
        pageapi=erpdata.text
        pageapi=re.findall("rows\":(.*?),\"fieldSizes",pageapi)

        id=re.findall("PagerBottom\" id=\"(.*?)\"",erpdata.text)
        retolist=erpdata

        '''
        print "pageapi number.............."
        print len(pageapi)
        print pageapi[0]
        print len(pageapi)
        '''
        if len(pageapi)==0:
            print u"进货订单统计无数据，测试不通过"
        #print pageapi[0]

        #报表统计数据
        pageapi=pageapi[0][1:-1]
        pageapi1=re.findall("\[(.*?)\]",pageapi)

        print u"pageapi1...............进货订单报表统计数据"
        #print pageapi1
        #print len(pageapi1)

        #每一种商品进行比对（进货订单报告统计的每一列，子页面）
        retoordernum=0
        retorenum=0
        retocomtonum=0
        retostopnum=0
        retonocomnum=0
        retomoney=0
        retogivemoney=0
        retoremoney=0
        retocommoney=0
        retostopmoney=0
        retonocommoney=0

        for n in range(0,len(pageapi1)):
            #取报告页面每一种商品的详细数据
            print "pageapi:"+str(n)+"............................"
            #print pageapi1[n]
            typeid=re.findall("(.*?),",pageapi1[n]+",")
            #print "typeid....................................."
            #print typeid
            typeid=typeid[14][1:-1]
            #print "typeid.........................."
            #print typeid
            url="http://beefun.wsgjp.com/Beefun/Report/PTypeSaleOrderStatisticDetails.gspx?vchtype=stockorder"
            a="{\"startdate\":\""+otherStyleTime2+"\",\"enddate\":\""+otherStyleTime+"\",\"startDate\":\""+otherStyleTime2+"\",\"endDate\":\""+otherStyleTime+"\",\"typeid\":\""+str(typeid)+"\",\"fullname\":\"\",\"isCompleteFlag\":\"0\",\"btypeid\":0}"
            #print a
            data={"__Params":a}
            erpdata=requests.post(url=url,data=data,headers=headers)

            #报表每种商品明细
            pageapi=erpdata.text
            pageapi=re.findall("rows\":(.*?),\"fieldSizes",pageapi)
            pageapi=pageapi[0][1:-1]

            #报表每种商品明细，每种商品信息放一个位置
            pageapi=re.findall("\[(.*?)\]",pageapi)

            #每一列商品明细进行统计
            print "pageapi..............................."
            #print pageapi
            print len(pageapi)

            #报表明细，一种种商品的信息
            '''
            pagedetail=re.findall("(.*?),",pageapi[n]+",")
            print "pagedetail.................."
            print pagedetail
           '''
            #print len(pagedetail)

            #报表统计页面一种商品放进一个列表中
            pageapilist=re.findall("(.*?),",pageapi1[n]+",")
            #标志
            #flagno=pageapi1[n][7][1:-1]

            #商品编号
            pagecode=pageapilist[8][1:-1]
            print "pageapilist......................."
            #print pageapilist
            '''

            print "pagecode"
            print pagecode
            '''
            #商品名称
            pagename=pageapilist[9][1:-1]

            apisigle=0.00

            apiqty=0.00
            apiagqty=0.00
            apiokqty=0.00
            apistopqty=0.00
            apiunqty=0.00

            apimoney=0.00
            apiagmoney=0.00
            apiokmoney=0.00
            apistopmoney=0.00
            apiunmoney=0.00

            apiother=0.00

            print u"进货订单报告统计页面第"+str(n+1)+u"行进行数据比对......."
            print u"进货订单报告统计页面第"+str(n+1)+u"行进行数据与进货订单管理明细比对......."



            for k in range(len(pageapi)):
                print u"第"+str(k+1)+u"行明细商品......."
                #进货订单报告统计页面明细进货商品
                reportdetail=re.findall("(.*?),",pageapi[k]+",")
                print "reportdetail......................"
                #print reportdetail

                #进货订单管理订单明细
                itemslist=[]
                for j in range(len(totalitem)):
                    for de in range(len(totalitem[j])):
                        #若商品编号商品名字一致
                        '''
                        print "totalitem.........."
                        print totalitem[j][de][0]
                        print totalitem[j][de][1]
                        print "reportdetail.........."
                        print reportdetail[0][1:-1]
                        print reportdetail[1][1:-1]
                        '''
                        if str(totalitem[j][de][0])==str(reportdetail[0][1:-1]) and str(totalitem[j][de][1])==str(reportdetail[1][1:-1]):
                            itemlis=totalitem[j][de]
                            #print "加入............................................."
                            #print itemlis
                            itemslist.append(itemlis)


                item=itemslist[k]
                #print "item..............................."
                #print item

                #商品编号
                reportno=reportdetail[0][1:-1]
                #进货订单报表和其明细
                try:
                    self.assertEqual(pagecode,reportno,msg=u"商品编号不一致")
                    print "assert pagecode ok"
                except AssertionError,msg:
                    print msg
                    print u"进货订单报表统计页面："+str(pagecode)
                    print u"进货订单报表明细页面(明细第"+str(k+1)+u"行)："+str(reportno)


                #进货订单报表明细和订货订单管理明细比对
                try:
                    itemno=item[0]
                    self.assertEqual(itemno,reportno,msg=u"商品编号不一致")
                    print "assert itemno ok"
                except AssertionError,msg:
                    print msg
                    print u"进货订单管理商品明细页面："+str(itemno)
                    print u"进货订单报表明细页面(明细第"+str(k+1)+u"行)："+str(reportno)

                #商品名称
                reportname=reportdetail[1][1:-1]
                #进货订单报表和其明细
                try:
                    self.assertEqual(pagename,reportname,msg=u"商品名称不一致")
                    print "assert pagename ok"
                except AssertionError,msg:
                    print msg
                    print u"进货订单报表统计页面："+str(pagename)
                    print u"进货订单报表明细页面(明细第"+str(k+1)+u"行)："+str(reportname)

                #进货订单报表明细和订货订单管理明细比对
                try:
                    itemname=item[1]
                    self.assertEqual(itemname,reportname,msg=u"商品名称不一致")
                    print "assert itemno ok"
                except AssertionError,msg:
                    print msg
                    print u"进货订单管理商品明细页面："+str(itemname)
                    print u"进货订单报表明细页面(明细第"+str(k+1)+u"行)："+str(reportname)

                #单位名称
                reportcompany=reportdetail[10][1:-1]
                try:
                    itemcompany=item[2]
                    self.assertEqual(itemcompany,reportcompany,msg=u"单位名称不一致")
                    print "assert itemcompany ok"
                except AssertionError,msg:
                    print msg
                    print u"进货订单管理商品明细页面："+str(itemcompany)
                    print u"进货订单报表明细页面(明细第"+str(k+1)+u"行)："+str(reportcompany)

                #订货日期
                reportintime=reportdetail[13][9:-1]
                try:
                    itemintime=item[3]
                    self.assertEqual(itemintime,reportintime,msg=u"订货日期不一致")
                    print "assert itemcompany ok"
                except AssertionError,msg:
                    print msg
                    print u"进货订单管理商品明细页面："+str(itemintime)
                    print u"进货订单报表明细页面(明细第"+str(k+1)+u"行)："+str(reportintime)

                #到货日期
                reportoktime=reportdetail[14][9:-1]
                try:
                    itemoktime=item[4]
                    self.assertEqual(itemoktime,reportoktime,msg=u"到货日期不一致")
                    print "assert itemoktime ok"
                except AssertionError,msg:
                    print msg
                    print u"进货订单管理商品明细页面："+str(itemoktime)
                    print u"进货订单报表明细页面(明细第"+str(k+1)+u"行)："+str(reportoktime)


                #订货数量
                nowqty=float(reportdetail[12])
                nowqty=str("%.4f"%nowqty)
                #print "nowqty........................."
                #print nowqty

                apiqty=float(apiqty)+float(reportdetail[12])
                apiqty=str("%.4f"%apiqty)
                #print "apiqty..................."
                #print apiqty
                try:
                    itemqty=float(item[5])
                    itemqty=str("%.4f"%itemqty)
                    self.assertEqual(itemqty,nowqty,msg=u"订货数量不一致")
                    print "assert itemqty ok"
                except AssertionError,msg:
                    print msg
                    print u"进货订单管理商品明细页面："+str(itemqty)
                    print u"进货订单报表明细页面(明细第"+str(k+1)+u"行)："+str(nowqty)

                #补订数量
                apiagqty=float(apiagqty)+float(reportdetail[15])
                apiagqty=str("%.4f"%apiagqty)

                nowagqty=float(reportdetail[15])
                nowagqty=str("%.4f"%nowagqty)
                try:
                    itemagqty=float(item[10])
                    itemagqty=str("%.4f"%itemagqty)
                    self.assertEqual(itemagqty,nowagqty,msg=u"补订数量不一致")
                    print "assert nowagqty ok"
                except AssertionError,msg:
                    print msg
                    print u"进货订单管理商品明细页面："+str(itemagqty)
                    print u"进货订单报表明细页面(明细第"+str(k+1)+u"行)："+str(nowagqty)

                #完成数量
                apiokqty=float(apiokqty)+float(reportdetail[16])
                apiokqty=str("%.4f"%apiokqty)

                nowokqty=float(reportdetail[16])
                nowokqty=str("%.4f"%nowokqty)
                try:
                    itemokqty=float(item[9])
                    itemokqty=str("%.4f"%itemokqty)
                    self.assertEqual(itemokqty,nowokqty,msg=u"完成数量不一致")
                    print "assert itemqty ok"
                except AssertionError,msg:
                    print msg
                    print u"进货订单管理商品明细页面："+str(itemokqty)
                    print u"进货订单报表明细页面(明细第"+str(k+1)+u"行)："+str(nowokqty)

                #终止完成数量
                apistopqty=float(apistopqty)+float(reportdetail[17])
                apistopqty=str("%.4f"%apistopqty)

                nowstopqty=float(reportdetail[17])
                nowstopqty=str("%.4f"%nowstopqty)

                #未完成数量
                apiunqty=float(apiunqty)+float(reportdetail[18])
                apiunqty=str("%.4f"%apiunqty)

                nowunqty=float(reportdetail[18])
                nowunqty=str("%.4f"%nowunqty)

                try:
                    itemunqty=float(item[8])
                    itemunqty=str("%.4f"%itemunqty)
                    self.assertEqual(itemunqty,nowunqty,msg=u"未完成数量不一致")
                    print "assert itemunqty ok"
                except AssertionError,msg:
                    print msg
                    print u"进货订单管理商品明细页面："+str(itemunqty)
                    print u"进货订单报表明细页面(明细第"+str(k+1)+u"行)："+str(nowunqty)

                #订货金额
                apimoney=float(apimoney)+float(reportdetail[19])
                apimoney=str("%.4f"%apimoney)

                nowmoney=float(reportdetail[19])
                nowmoney=str("%.2f"%nowmoney)
                try:
                    #itemtaxmoney=float(item[7])
                    itemmoney=round(float(item[14]),2)
                    print "item.........................................."
                    #print item
                    #print "reportdetail.........................."
                    #print reportdetail
                    itemmoney=str("%.2f"%itemmoney)
                    self.assertEqual(itemmoney,nowmoney,msg=u"订货金额不一致")
                    print "assert itemmoney ok"
                except AssertionError,msg:
                    print msg
                    print u"进货订单管理商品明细页面："+str(itemmoney)
                    print u"进货订单报表明细页面(明细第"+str(k+1)+u"行)："+str(nowmoney)

                #补订金额
                apiagmoney=float(apiagmoney)+float(reportdetail[20])
                apiagmoney=str("%.6f"%apiagmoney)

                nowagmoney=float(reportdetail[20])
                nowagmoney=str("%.6f"%nowagmoney)

                try:
                    itemagmoney=float(item[13])
                    itemagmoney=str("%.6f"%itemagmoney)
                    self.assertEqual(itemagmoney,nowagmoney,msg=u"补订金额不一致")
                    print "assert itemagmoney ok"
                except AssertionError,msg:
                    print msg
                    print u"进货订单管理商品明细页面："+str(itemagmoney)
                    print u"进货订单报表明细页面(明细第"+str(k+1)+u"行)："+str(nowagmoney)

                #完成金额
                apiokmoney=float(apiokmoney)+float(reportdetail[21])
                apiokmoney=str("%.4f"%apiokmoney)

                nowokmoney=float(reportdetail[21])
                nowokmoney=str("%.2f"%nowokmoney)
                try:
                    itemokmoney=float(item[12])
                    itemokmoney=str("%.2f"%itemokmoney)
                    self.assertEqual(itemokmoney,nowokmoney,msg=u"完成金额不一致")
                    print "assert itemokmoney ok"
                except AssertionError,msg:
                    print msg
                    print u"进货订单管理商品明细页面："+str(itemokmoney)
                    print u"进货订单报表明细页面(明细第"+str(k+1)+u"行)："+str(nowokmoney)

                #终止完成金额
                apistopmoney=float(apistopmoney)+float(reportdetail[22])
                apistopmoney=str("%.4f"%apistopmoney)

                nowstopmoney=float(reportdetail[22])
                nowstopmoney=str("%.4f"%nowstopmoney)

                #未完成金额
                apiunmoney=float(apiunmoney)+float(reportdetail[23])
                apiunmoney=str("%.6f"%apiunmoney)

                nowunmoney=float(reportdetail[23])
                nowunmoney=str("%.6f"%nowunmoney)
                try:
                    itemunmoney=float(item[11])
                    itemunmoney=str("%.6f"%itemunmoney)
                    self.assertEqual(str(itemunmoney),str(nowunmoney),msg=u"未完成金额不一致")
                    print "assert itemunmoney ok"
                except AssertionError,msg:
                    print msg
                    print u"进货订单管理商品明细页面："+str(nowunmoney)
                    print u"进货订单报表明细页面(明细第"+str(k+1)+u"行)："+str(apiunmoney)

                #赠品
                apiother=float(apiother)+float(reportdetail[25])
                apiother=str("%.4f"%apiother)

                nowother=float(reportdetail[25])
                nowother=str("%.4f"%nowother)


            #明细商品统计的订货定价
            print u"进货订单报表和报表明细"
            apisigle=float(apimoney)/float(apiqty)
            apisigle=round(apisigle,4)
            apisigle=str("%.4f"%apisigle)

            #订货订单报表统计数据，进行比对


            #订货定价
            pagesigle=float(pageapilist[28])
            pagesigle=str("%.4f"%pagesigle)
            retogivemoney=retogivemoney+float(pageapilist[28])

            try:
                self.assertEqual(pagesigle,apisigle,msg=u"订货定价不一致")
                print "assert pagesigle ok"
            except AssertionError,msg:
                print msg
                print u"进货订单报表统计页面："+str(pagesigle)
                print u"进货订单报表明细页面明细统计结果："+str(apisigle)

            #订货数量
            pageqty=float(pageapilist[18])
            pageqty=str("%.4f"%pageqty)

            retoordernum=retoordernum+float(pageapilist[18])
            try:
                self.assertEqual(pageqty,apiqty,msg=u"订货数量不一致")
                print "assert pageqty ok"
            except AssertionError,msg:
                print msg
                print u"进货订单报表统计页面："+str(pageqty)
                print u"进货订单报表明细页面明细统计结果："+str(apiqty)


            #补订数量
            pageagqty=float(pageapilist[19])
            pageagqty=str("%.4f"%pageagqty)

            retorenum=retorenum+float(pageapilist[19])
            try:
                self.assertEqual(pageagqty,apiagqty,msg=u"补订数量不一致")
                print "assert pageagqty ok"
            except AssertionError,msg:
                print msg
                print u"进货订单报表统计页面："+str(pageagqty)
                print u"进货订单报表明细页面明细统计结果："+str(apiagqty)

            #完成数量
            pageokqty=float(pageapilist[20])
            pageokqty=str("%.4f"%pageokqty)

            retocomtonum=retocomtonum+float(pageapilist[20])

            try:
                self.assertEqual(pageokqty,apiokqty,msg=u"完成数量不一致")
                print "assert pageokqty ok"
            except AssertionError,msg:
                print msg
                print u"进货订单报表统计页面："+str(pageokqty)
                print u"进货订单报表明细页面明细统计结果："+str(apiokqty)

            #终止完成数量
            pagestopqty=float(pageapilist[21])
            pagestopqty=str("%.4f"%pagestopqty)

            retostopnum=retostopnum+float(pageapilist[21])

            try:
                self.assertEqual(pagestopqty,apistopqty,msg=u"终止完成数量不一致")
                print "assert pagestopqty ok"
            except AssertionError,msg:
                print msg
                print u"进货订单报表统计页面："+str(pagestopqty)
                print u"进货订单报表明细页面明细统计结果："+str(apistopqty)

            #未完成数量
            pageunqty=float(pageapilist[22])
            pageunqty=str("%.4f"%pageunqty)

            retonocomnum=retonocomnum+float(pageapilist[22])

            try:
                self.assertEqual(pageunqty,apiunqty,msg=u"未完成数量不一致")
                print "assert pageunqty ok"
            except AssertionError,msg:
                print msg
                print u"进货订单报表统计页面："+str(pageunqty)
                print u"进货订单报表明细页面明细统计结果："+str(apiunqty)

            #订货金额
            pagemoney=float(pageapilist[23])
            pagemoney=str("%.4f"%pagemoney)

            retomoney=retomoney+float(pageapilist[23])

            try:
                self.assertEqual(pagemoney,apimoney,msg=u"订货金额不一致")
                print "assert pagemoney ok"
            except AssertionError,msg:
                print msg
                print u"进货订单报表统计页面："+str(pagemoney)
                print u"进货订单报表明细页面明细统计结果："+str(apimoney)

            #补订金额
            pageagmoney=float(pageapilist[24])
            pageagmoney=str("%.6f"%pageagmoney)

            retoremoney=retoremoney+float(pageapilist[24])
            try:
                self.assertEqual(pageagmoney,apiagmoney,msg=u"补订金额不一致")
                print "assert pageagmoney ok"
            except AssertionError,msg:
                print msg
                print u"进货订单报表统计页面："+str(pageagmoney)
                print u"进货订单报表明细页面明细统计结果："+str(apiagmoney)

            #完成金额
            pageokmoney=float(pageapilist[25])
            pageokmoney=str("%.4f"%pageokmoney)

            retocommoney=retocommoney+float(pageapilist[25])
            try:
                self.assertEqual(pageokmoney,apiokmoney,msg=u"完成金额不一致")
                print "assert pageokmoney ok"
            except AssertionError,msg:
                print msg
                print u"进货订单报表统计页面："+str(pageokmoney)
                print u"进货订单报表明细页面明细统计结果："+str(apiokmoney)

            #终止完成金额
            pagestopmoney=float(pageapilist[26])
            pagestopmoney=str("%.4f"%pagestopmoney)

            retostopmoney=retostopmoney+float(pageapilist[26])
            try:
                self.assertEqual(pagestopmoney,apistopmoney,msg=u"终止完成金额不一致")
                print "assert pagestopmoney ok"
            except AssertionError,msg:
                print msg
                print u"进货订单报表统计页面："+str(pagestopmoney)
                print u"进货订单报表明细页面明细统计结果："+str(apistopmoney)

            #未完成金额

            pageunmoney=float(pageapilist[27])
            pageunmoney=str("%.6f"%pageunmoney)

            retonocommoney=retonocommoney+float(pageapilist[27])
            try:
                self.assertEqual(pageunmoney,str(apiunmoney),msg=u"未完成金额不一致")
                print "assert pageunmoney ok"
            except AssertionError,msg:
                print msg
                print u"进货订单报表统计页面："+str(pageunmoney)
                print u"进货订单报表明细页面明细统计结果："+str(apiunmoney)

            #赠品
            other=float(pageapilist[29])
            other=str("%.4f"%other)

            try:
                self.assertEqual(other,apiother,msg=u"赠品不一致")
                print "assert other ok"
            except AssertionError,msg:
                print msg
                print u"进货订单报表统计页面："+str(other)
                print u"进货订单报表明细页面明细统计结果："+str(apiother)

            #明细具体总条数
            redelist=float(len(pageapi))
            detotlist=re.findall("itemCount\":(.*?),",erpdata.text)
            #print "detotlist..........................."
            #print detotlist
            detotlist=float(detotlist[0][:-1])


            self.assernote(redelist,detotlist,u"总条数不相同（进货订单报表明细页面和它页面的统计）","report totlelist ok",u"进货订单报表明细页面和它页面的统计总条数")

        #报表页面和其统计数据
        print u"报表页面和它页面的统计..............................."
        header={'cookie':self.cookiestr,"Content-Type": "application/json"}
        sumurl="http://beefun.wsgjp.com/Carpa.Web/Carpa.Web.Script.DataService.ajax/GetPagerSummary"
        sumda={"pagerId":id[0]}
        resum=requests.post(url=sumurl,headers=header,data=json.dumps(sumda))
        #print "resum............................."
        #print resum
        #print id
        sumdata=json.loads(resum.text)

        #数据总数
        totaloederstock=float(len(pageapi1))
        totlist=re.findall("itemCount\":(.*?),",retolist.text)
        totlist=float(totlist[0])
        print "totlist.............."
        #print totlist
        #totlist=float(totlist[0])

        self.assernote(totaloederstock,totlist,u"总条数不相同（报表页面和它页面的统计）","report totlelist ok",u"进货订单）页面和页面统计总条数")


        #订货数量
        sumreordernum=float(sumdata["qty"]["value"])
        sumreordernum=str("%.4f"%sumreordernum)

        retoordernum=str("%.4f"%retoordernum)
        self.assernote(sumreordernum,retoordernum,u"订货数量不相同（进货订单报表（报表）页面和页面统计）","reporttotal order qty ok",u"进货订单报表（报表）页面和页面统计订货数量")

        #补订数量
        sumrerenum=float(sumdata["repairqty"]["value"])
        sumrerenum=str("%.4f"%sumrerenum)

        retorenum=str("%.4f"%retorenum)
        self.assernote(sumrerenum,retorenum,u"补订数量不相同（进货订单报表（报表）页面和页面统计）","reporttotal qty numbers ok",u"进货订单报表（报表）页面和页面统计补订数量")

        #完成数量
        sumrecomnum=float(sumdata["completeqty"]["value"])
        sumrecomnum=str("%.4f"%sumrecomnum)

        retocomtonum=str("%.4f"%retocomtonum)
        self.assernote(sumrecomnum,retocomtonum,u"完成数量不相同（进货订单报表（报表）页面和页面统计）","reporttotal complete qty ok",u"进货订单报表（报表）页面和页面统计完成数量")

        #终止完成数量
        sumrestopnum=float(sumdata["forcecompleteqty"]["value"])
        sumrestopnum=str("%.4f"%sumrestopnum)

        retostopnum=str("%.4f"%retostopnum)
        self.assernote(sumrestopnum,retostopnum,u"终止完成数量不相同（进货订单报表（报表）页面和页面统计）","reporttotal stop qty ok",u"进货订单报表（报表）页面和页面统计终止完成数量")

        #未完成数量
        sumrenocomnum=float(sumdata["nocompleteqty"]["value"])
        sumrenocomnum=str("%.4f"%sumrenocomnum)

        retonocomnum=str("%.4f"%retonocomnum)
        self.assernote(sumrenocomnum,retonocomnum,u"订货数量不相同（进货订单报表（报表）页面和页面统计）","reporttotal nocomplete qty ok",u"进货订单报表（报表）页面和页面统计未完成数量")

        #订货金额
        sumremoney=float(sumdata["ordertotal"]["value"])
        sumremoney=str("%.4f"%sumremoney)

        retomoney=str("%.4f"%retomoney)
        self.assernote(sumremoney,retomoney,u"订货金额不相同（进货订单报表（报表）页面和页面统计）","reporttotal order money ok",u"进货订单报表（报表）页面和页面统计订货金额")

        #补订金额
        sumreremoney=float(sumdata["repairtotal"]["value"])
        sumreremoney=str("%.4f"%sumreremoney)

        retoremoney=str("%.4f"%retoremoney)
        self.assernote(sumreremoney,retoremoney,u"补订金额不相同（进货订单报表（报表）页面和页面统计）","reporttotal repair money ok",u"进货订单报表（报表）页面和页面统计补订金额")

        #完成金额
        sumrecommoney=float(sumdata["completetotal"]["value"])
        sumrecommoney=str("%.4f"%sumrecommoney)

        retocommoney=str("%.4f"%retocommoney)
        self.assernote(sumrecommoney,retocommoney,u"完成金额不相同（进货订单报表（报表）页面和页面统计）","reporttotal complete moeny ok",u"进货订单报表（报表）页面和页面统计完成金额")

        #终止完成金额
        sumrestopmoney=float(sumdata["forcecompletetotal"]["value"])
        sumrestopmoney=str("%.4f"%sumrestopmoney)

        retostopmoney=str("%.4f"%retostopmoney)
        self.assernote(sumrestopmoney,retostopmoney,u"终止完成金额不相同（进货订单报表（报表）页面和页面统计）","reporttotal forcecomplete money ok",u"进货订单报表（报表）页面和页面统计终止完成金额")

        #未完成金额
        sumrenocommoney=float(sumdata["nocompletetotal"]["value"])
        sumrenocommoney=str("%.4f"%sumrenocommoney)

        retonocommoney=str("%.4f"%retonocommoney)
        self.assernote(sumrenocommoney,retonocommoney,u"未完成金额不相同（进货订单报表（报表）页面和页面统计）","reporttotal nocomplete money ok",u"进货订单报表（报表）页面和页面统计未完成金额")

        #赠品



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
