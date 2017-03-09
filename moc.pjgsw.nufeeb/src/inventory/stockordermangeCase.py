#*-* coding:UTF-8 *-*
import time
import unittest
import  xml.dom.minidom
import traceback
import re
import json
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )


from common import browserClass
browser=browserClass.browser()

class stockordermanageTest(unittest.TestCase):
    u'''进货订单管理'''

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

    def teststockManage(self):
        u'''进货订单管理'''
        dom = xml.dom.minidom.parse(r'C:\workspace\moc.pjgsw.nufeeb\src\data\basedata')

        module='moudle'
        modulename=browser.xmlRead(self.driver,dom,module,1)
        moduledetail=browser.xmlRead(self.driver,dom,'page',1)

        browser.openModule2(self.driver,modulename,moduledetail)

        stockdata=browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\checkdata','r',1,'aaa')
        flagnum=stockdata[0].strip()
        print "checkdata no............"
        print flagnum
        success=''
        checkstockorder=browser.xmlRead(self.driver,dom,"checkstockorder",0)
        checknote=browser.xmlRead(self.driver,dom,"checknote",0)
        checkok=browser.xmlRead(self.driver,dom,"checkok",0)
        checkclose=browser.xmlRead(self.driver,dom,"checkclose",0)
        #订单编号
        num=browser.xmlRead(self.driver,dom,"ordernum",0)
        num2=browser.xmlRead(self.driver,dom,'ordernum',1)
        num3=browser.xmlRead(self.driver,dom,'ordernum',2)
        for n in range(1,10):
            xpath=num+str(n)+num2+str(8)+num3
            dataxpath=num+str(n)+num2+str(3)+num3
            status=browser.elementisexist(self.driver,xpath)
            if status==True:
                #print "number.........................."
                #print browser.findXpath(self.driver,xpath).text
                if browser.findXpath(self.driver,xpath).text==flagnum:
                    print u"进货订单提交至进货订单管理成功，测试通过"
                    browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\checkdata2','w',0,flagnum)
                    browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\checkdata2','a+',0,'\n')
                    checkbox=num+str(n)+num2+str(2)+"]/input"
                    #time.sleep(2)
                    #获得此时页面数据
                    url="http://beefun.wsgjp.com/Beefun/Carrier/OrderManager.gspx?vchtype=stockorder"
                    headers={'cookie':self.cookiestr}
                    pagedata=browser.handleorderRead(self.driver,url,headers)
                    resault=re.findall("(?<=\"toqty\").*?(?=\"toqty\")",pagedata)

                    #print "resault..................................."
                    #print resault
                    #detail=[]
                    for j in range(2,len(resault)-3):
                        erplis=re.findall(":(.*?),",resault[j])
                        if erplis[11][1:-1]==flagnum:
                            break

                    #print "erplis........................."
                    #print erplis
                    #将获得的数据进行对比
                    #往来单位
                    try:
                       company=erplis[22][1:-1]
                       self.assertEqual(stockdata[2].strip(),company.strip(),msg=u"往来单位不一致")
                       print u"往来单位一致"
                    except AssertionError,msg:
                        print msg
                        print str(stockdata[2].strip())
                        print erplis[22][1:-1]
                    #仓库名称
                    try:
                        repertory=erplis[21][1:-1]
                        self.assertEqual(stockdata[5].strip(),repertory.strip(),msg=u"仓库名称不一致")
                        print u"仓库名称一致"
                    except AssertionError,msg:
                        print msg
                        print stockdata[5].strip()
                        print erplis[21][1:-1]
                    #经手人
                    try:
                        handpeople=erplis[20][1:-1]
                        self.assertEqual(stockdata[3].strip(),handpeople.strip(),msg=u"经手人不一致")
                        print u"经手人一致"
                    except AssertionError,msg:
                        print msg
                        print str(stockdata[3].strip())
                        print erplis[20][1:-1]
                    #交货日期
                    try:
                        timeint=int(erplis[12][9:-1])/1000
                        #print timeint
                        x = time.localtime(timeint)
                        timeStr=time.strftime("%Y-%m-%d",x)
                        self.assertEqual(stockdata[4].strip(),timeStr,msg=u"交货日期不一致")
                        print u"交货日期一致"
                    except AssertionError,msg:
                        print msg
                        print stockdata[4].strip()
                        print timeStr

                    #折前金额
                    beforeprice=float(erplis[32][:-2])
                    pr1=stockdata[16].strip()
                    pr2=stockdata[17].strip()
                    pr=float(pr1)+float(pr2)
                    self.assernote(pr,beforeprice,u"折前金额不相同",u"折前金额一致",u"折前金额")

                    #金额
                    try:
                        pr1=stockdata[19].strip()
                        pr2=stockdata[17].strip()
                        pr=float(pr1)+float(pr2)
                        pr=str("%.2f"%pr)
                        erpprice=erplis[31][:-2]
                        self.assertEqual(erpprice,pr,msg=u"金额不一致")
                        print u"金额一致"
                    except AssertionError,msg:
                        print msg
                        print erpprice
                        print pr

                    #税后金额
                    afterprice=float(erplis[30][:-2])
                    pr1=stockdata[22].strip()
                    pr2=stockdata[17].strip()
                    pr=float(pr1)+float(pr2)
                    self.assernote(pr,afterprice,u"税后金额不相同",u"税后金额一致",u"税后金额")

                    #附加说明
                    try:
                        comment=erplis[13][1:-1]
                        self.assertEqual(stockdata[7].strip(),comment.strip(),msg=u"附加说明不一致")
                        print u"附加说明一致"
                    except AssertionError,msg:
                        print msg
                        print str(stockdata[7].strip())
                        print comment

                    #获取商品详细数据
                    detailurl="http://beefun.wsgjp.com/Beefun/Beefun.Carrier.OrderManager.ajax/GetDetailsByorderid"
                    detailheaders={'cookie':self.cookiestr,'Content-Type': 'application/json'}
                    vchcode=erplis[8][1:-1]
                    vchtype=erplis[9]
                    summary=erplis[14][1:-1]
                    btypeid=erplis[15][1:-1]
                    etypeid=erplis[17][1:-1]
                    ktypeid=erplis[18][1:-1]
                    ename=handpeople
                    kfullname=repertory

                    erpnum=erplis[1][:-5]


                    detaildata={"hashdata":{"toqty":0,"untoqty":int(erpnum),"repairqty":0,"repairtotal":0,"tototal":0,"untototal":float(erpprice[:-3]),"isdelivered":0,"checked":0,"vchcode":vchcode,"vchtype":int(vchtype),"date":"\/Date(1466092800000)\/","number":flagnum,"todate":"\/Date(1466092800000)\/","comment":comment,"summary":summary,"btypeid":btypeid,"bpartypeid":"00000","etypeid":etypeid,"ktypeid":ktypeid,"auditover":False,"ename":ename,"kfullname":kfullname,"bname":company,"artotal":0,"aptotal":0,"r_warnup":0,"orderover1":0,"createtypename":"本地创建","createtype":0,"reccnt":0,"total":float(beforeprice),"tptotal":float(erpprice),"dptotal":float(afterprice),"default_audited":0,"default_auditorid":None,"default_audittime":None,"default_auditremark":"","finance_audited":0,"finance_auditorid":0,"finance_audittime":None,"finance_auditremark":"","isexport":0,"earnest":0,"finance_auditorname":"","business_auditorname":"","receiverpeople":None,"receivercellphone":None,"receivertelephone":None,"receiverzipcode":None,"province":None,"city":None,"district":None,"receiveraddress":None,"isneedinvoice":None}}
                    detail=browser.orderRead(self.driver,detailurl,json.dumps(detaildata),detailheaders)
                    beforejson=re.findall("(?<=\{)(.*?)(?=\})",detail)
                    #lenth=len(beforejson)
                    a=[]
                    b=[]
                    c=[]
                    d=[]
                    e=[]
                    f=[]
                    for k in range(len(beforejson)):
                        bedetail="{"+beforejson[k]+"}"
                        itemdetial=json.loads(bedetail)
                        #进行数据比对
                        #编号
                        try:
                            pagecode=stockdata[14+k]
                            self.assertEqual(str(itemdetial["ptypecode"]).strip(),pagecode.strip(),msg=u"具体编号不一致")
                            print u"编号一致"
                        except AssertionError,msg:
                            print msg
                            print str(itemdetial["ptypecode"]).strip()
                            print pagecode
                        #名字
                        try:
                            pagename=stockdata[8+k]
                            self.assertEqual(str(itemdetial["pfullname"]).strip(),pagename.strip(),msg=u"具体名字不一致")
                            print u"具体名字一致"
                        except AssertionError,msg:
                            print msg
                            print itemdetial["pfullname"]
                            print pagename
                        #数量
                        try:
                            qtnum=float(stockdata[10+k])
                            qtnum=str("%.4f"%qtnum)
                            apiqty=float(itemdetial["qty"])
                            apiqty=str("%.4f"%apiqty)
                            self.assertEqual(apiqty.strip(),qtnum.strip(),msg=u"具体数量不一致")
                            print u"具体数量一致"
                        except AssertionError,msg:
                            print msg
                            print apiqty
                            print qtnum
                        #单价
                        try:
                            if k==0:
                               singeprice=float(stockdata[18])
                            else:
                                singeprice=float(stockdata[12])
                            singeprice=str("%.4f"%singeprice)
                            #print "itemdetial....................................."
                            #print itemdetial
                            apisigle=float(itemdetial["asstpprice"])
                            apisigle=str("%.4f"%apisigle)
                            self.assertEqual(apisigle.strip(),singeprice.strip(),msg=u"具体单价不一致")
                            print u"具体单价一致"
                        except AssertionError,msg:
                            print msg
                            print apisigle
                            print singeprice
                        #金额
                        try:
                            if k==0:
                                money=float(stockdata[19])
                            else:
                                money=float(stockdata[17])
                            money=str("%.4f"%money)

                            apimoney=float(itemdetial["tptotal"])
                            apimoney=str("%.4f"%apimoney)

                            self.assertEqual(apimoney.strip(),money.strip(),msg=u"具体金额不一致")
                            print u"具体金额一致"
                        except AssertionError,msg:
                            print msg
                            print itemdetial["total"]
                            print money

                        #页面明细:未完成数量，完成数量，补订数量，未完成金额，完成金额，补定金额
                        untoqty=float(itemdetial["untoqty"])
                        untoqty=str("%.4f"%untoqty)
                        a.append(untoqty)
                        browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\checkdata2','a+',0,untoqty)
                        browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\checkdata2','a+',0,'\n')

                        toqty=float(itemdetial["toqty"])
                        toqty=str("%.4f"%toqty)
                        b.append(toqty)
                        browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\checkdata2','a+',0,toqty)
                        browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\checkdata2','a+',0,'\n')

                        repairqty=float(itemdetial["repairqty"])
                        repairqty=str("%.4f"%repairqty)
                        c.append(repairqty)
                        browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\checkdata2','a+',0,repairqty)
                        browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\checkdata2','a+',0,'\n')


                        untototal=float(itemdetial["untototal"])
                        untototal=str("%.4f"%untototal)
                        d.append(untototal)
                        browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\checkdata2','a+',0,untototal)
                        browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\checkdata2','a+',0,'\n')

                        tototal=float(itemdetial["tototal"])
                        tototal=str("%.4f"%tototal)
                        e.append(tototal)
                        browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\checkdata2','a+',0,tototal)
                        browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\checkdata2','a+',0,'\n')

                        repairtotal=float(itemdetial["repairtotal"])
                        repairtotal=str("%.4f"%repairtotal)
                        f.append(repairtotal)
                        browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\checkdata2','a+',0,repairtotal)
                        browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\checkdata2','a+',0,'\n')


                    #未完成数量
                    try:
                        qt1=a[0].strip()
                        qt2=a[1].strip()
                        qt=float(qt1)+float(qt2)
                        qt=str("%.4f"%qt)
                        erpnum=float(erplis[1])
                        erpnum=str("%.4f"%erpnum)
                        self.assertEqual(str(qt),erpnum,msg=u"未完成数量不一致")
                        print u"未完成数量一致"
                    except AssertionError,msg:
                        print msg
                        print qt
                        print erpnum

                    #完成数量
                    try:
                        qt1=b[0].strip()
                        qt2=b[1].strip()
                        qt=float(qt1)+float(qt2)
                        qt=str("%.4f"%qt)
                        erpnum=float(erplis[0])
                        erpnum=str("%.4f"%erpnum)
                        self.assertEqual(str(qt),erpnum,msg=u"完成数量不一致")
                        print u"完成数量一致"
                    except AssertionError,msg:
                        print msg
                        print qt
                        print erpnum

                     #补订数量
                    try:
                        qt1=c[0].strip()
                        qt2=c[1].strip()
                        qt=float(qt1)+float(qt2)
                        qt=str("%.4f"%qt)
                        erpnum=float(erplis[2])
                        erpnum=str("%.4f"%erpnum)
                        self.assertEqual(str(qt),erpnum,msg=u"补订数量不一致")
                        print u"补订数量一致"
                    except AssertionError,msg:
                        print msg
                        print qt
                        print erpnum

                    #未完成金额
                    try:
                        qt1=d[0].strip()
                        qt2=d[1].strip()
                        qt=float(qt1)+float(qt2)
                        qt=str("%.4f"%qt)
                        erpnum=float(erplis[5])
                        erpnum=str("%.4f"%erpnum)
                        self.assertEqual(str(qt),erpnum,msg=u"未完成金额不一致")
                        print u"未完成金额一致"
                    except AssertionError,msg:
                        print msg
                        print qt
                        print erpnum

                    #完成金额
                    try:
                        qt1=e[0].strip()
                        qt2=e[1].strip()
                        qt=float(qt1)+float(qt2)
                        qt=str("%.4f"%qt)
                        erpnum=float(erplis[4])
                        erpnum=str("%.4f"%erpnum)
                        self.assertEqual(str(qt),erpnum,msg=u"完成金额不一致")
                        print u"完成金额一致"
                    except AssertionError,msg:
                        print msg
                        print qt
                        print erpnum

                     #补订金额
                    try:
                        qt1=f[0].strip()
                        qt2=f[1].strip()
                        qt=float(qt1)+float(qt2)
                        qt=str("%.4f"%qt)
                        erpnum=float(erplis[3])
                        erpnum=str("%.4f"%erpnum)
                        self.assertEqual(str(qt),erpnum,msg=u"补订金额不一致")
                        print u"补订金额一致"
                    except AssertionError,msg:
                        print msg
                        print qt
                        print erpnum


                    try:
                        browser.findXpath(self.driver,checkbox).click()
                        browser.findXpath(self.driver,checkstockorder).click()
                        browser.findXpath(self.driver,checkclose).click()
                        browser.findXpath(self.driver,checkstockorder).click()
                        browser.findXpath(self.driver,checknote).send_keys(u"上一步进货订单提交至进货订单管理成功")
                        browser.findXpath(self.driver,checkok).click()
                        success=0
                        print u"进货订单管理审核关闭按钮测试通过"
                        break
                    except:
                        print u"审核上一步提交的订货单失败"
                        print(traceback.format_exc())

        if success!=0:
            print u"进货订单提交至进货订单管理后找不到该订单，测试不通过"
            for n in range(1,10):
                xpath=num+str(n)+num2+str(7)+num3
                status=browser.elementisexist(self.driver,xpath)
                if status==True:
                    checkbox=num+str(n)+num2+str(2)+"]/input"
                    print checkbox
                    stockmangeid=browser.findXpath(self.driver,xpath).text
                    print stockmangeid
                    browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\checkdata2','w',0,stockmangeid)
                    #time.sleep(2)
                    try:
                        browser.findXpath(self.driver,checkbox).click()
                        browser.findXpath(self.driver,checkstockorder).click()
                        browser.findXpath(self.driver,checkclose).click()
                        browser.findXpath(self.driver,checkstockorder).click()
                        browser.findXpath(self.driver,checknote).send_keys(u"上一步进货订单提交至进货订单管理失败")
                        #browser.findXpath(self.driver,checkok).click()
                        break
                    except:
                        print u"上一步进货订单提交至进货订单管理失败,审核本步已有订货单失败"
                        print(traceback.format_exc())



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
