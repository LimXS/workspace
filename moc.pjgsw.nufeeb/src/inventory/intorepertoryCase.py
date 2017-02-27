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

class intorepertoryTest(unittest.TestCase):
    u'''进货入库单'''
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


    def testintoRepertory(self):
        u'''进货入库单'''
        dom = xml.dom.minidom.parse(r'C:\workspace\moc.pjgsw.nufeeb\src\data\basedata')

        module='moudle'
        modulename=browser.xmlRead(self.driver,dom,module,2)
        moduledetail=browser.xmlRead(self.driver,dom,'page',2)
        browser.openModule2(self.driver,modulename,moduledetail)

        success=""
        newstock=browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\checkdata','r',1,'aaa')
        flagnum=newstock[0].strip()
        managestcok=browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\checkdata2','r',1,'aaa')
        try:
            stockorder=browser.xmlRead(self.driver,dom,'stockorder',0)
            time.sleep(1)
            browser.findXpath(self.driver,stockorder).click()
            closeorder=browser.xmlRead(self.driver,dom,'closeorder',0)
            time.sleep(1)
            browser.findXpath(self.driver,closeorder).click()
            print u"进货订单关闭按钮成功"

        except:
            print u"进货订单关闭按钮失败"
            print(traceback.format_exc())

        browser.findXpath(self.driver,stockorder).click()
        flagorder1=browser.xmlRead(self.driver,dom,'flagorder1',0)
        flagorder2=browser.xmlRead(self.driver,dom,"flagorder2",0)
        try:
            for n in range(1,10):
                xpath=flagorder1+str(n)+flagorder2
                status=browser.elementisexist(self.driver,xpath)
                if status==True:
                    if browser.findXpath(self.driver,xpath).text==flagnum:
                        print flagnum
                        print u"上一步进货订单管理审核通过,测试通过"
                        browser.findXpath(self.driver,xpath).click()
                        success=0
                        #提交之前的数据

                        #去数据进行比对，进货订单数据
                        url="http://beefun.wsgjp.com/Beefun/Bill/OrderSelector.gspx"
                        headers={'cookie':self.cookiestr}
                        a="{\"btypeid\":null,\"isBtypeEnable\":true,\"bfullname\":null,\"isKtypeEnable\":true,\"vchtype\":\"stockorder\",\"isShowSameNumber\":true,\"wholeSale\":false,\"wmsOrder\":false}"
                        data2={"__Params":a}
                        #获取接口返回数据
                        intodata=requests.post(url,headers=headers,data=data2)
                        #print "intodata.........................."
                        #print intodata.text
                        #进行提取
                        intodata=re.findall("rows\":(.*?),\"fieldSizes",intodata.text)
                        '''
                        print "len1...................................."
                        print len(intodata)
                    '''
                        #每一条订单的所有内容放到一个列表里面
                        intodata=intodata[0][1:-1]
                        intodata=re.findall("\[(.*?)\]",intodata)

                        #print "intodata................."
                        #print intodata

                        for k in range(len(intodata)):
                            temdata=re.findall("(.*?),",intodata[k]+",")
                            if temdata[3][1:-1]==flagnum:
                                print temdata[3][1:-1]
                                break

                        #print "temdata...................."
                        #print temdata

                        intodata=temdata

                        #进货单总信息
                        #录单日期
                        ordate=newstock[1]
                        paordate=intodata[4][1:-1]
                        try:
                            self.assertEqual(ordate.strip(),paordate.strip(),msg=u"录单日期不一致")
                            print u"录单日期一致"
                        except AssertionError,msg:
                            print msg
                            print ordate
                            print paordate

                        #往来单位
                        company=newstock[2]
                        pacompany=intodata[5][1:-1]
                        try:
                            self.assertEqual(company.strip(),pacompany.strip(),msg=u"往来单位不一致")
                            print u"往来单位一致"
                        except AssertionError,msg:
                            print msg
                            print company
                            print pacompany

                        #交货日期
                        okdate=newstock[4]
                        paokdate=intodata[7][1:-1]
                        try:
                            self.assertEqual(okdate.strip(),paokdate.strip(),msg=u"交货日期不一致")
                            print u"交货日期一致"
                        except AssertionError,msg:
                            print msg
                            print okdate
                            print paokdate

                        #经手人
                        peopel=newstock[3]
                        papeople=intodata[10][1:-1]
                        try:
                            self.assertEqual(peopel.strip(),papeople.strip(),msg=u"经手人不一致")
                            print u"经手人一致"
                        except AssertionError,msg:
                            print msg
                            print peopel
                            print papeople

                        #仓库
                        reven=newstock[5]
                        pareven=intodata[16][1:-1]
                        try:
                            self.assertEqual(reven.strip(),pareven.strip(),msg=u"仓库不一致")
                            print u"仓库一致"
                        except AssertionError,msg:
                            print msg
                            print reven
                            print pareven

                        #附加说明
                        addcom=newstock[7]
                        paaddcom=intodata[13][1:-1]
                        try:
                            self.assertEqual(addcom.strip(),paaddcom.strip(),msg=u"附加说明不一致")
                            print u"附加说明一致"
                        except AssertionError,msg:
                            print msg
                            print addcom
                            print paaddcom

                        #摘要
                        note=newstock[6]
                        panote=intodata[14][1:-1]
                        try:
                            self.assertEqual(note.strip(),panote.strip(),msg=u"摘要不一致")
                            print u"摘要一致"
                        except AssertionError,msg:
                            print msg
                            print note
                            print panote

                        #进货单明细信息
                        #获取其明细信息
                        ordercode=intodata[0][1:-1]
                        ktypeid=intodata[15][1:-1]
                        btypeid=intodata[6][1:-1]

                        urldetail="http://beefun.wsgjp.com/Beefun/Beefun.Bill.OrderSelector.ajax/GetOrderDetails"
                        headers={'cookie':self.cookiestr,"Content-Type": "application/json; charset=UTF-8"}
                        data={"querydata":{"ordercode":ordercode,"ktypeid":ktypeid,"btypeid":btypeid,"vchtype":7,"wmsOrder":False,"ischecked":True,"ptypeid":0}}
                        intodatadetail=requests.post(urldetail,headers=headers,data=json.dumps(data))

                        intodatadetail=intodatadetail.text

                        intodatadetail=re.sub("null","\"None\"",intodatadetail)
                        intodatadetail=re.sub("false","\"False\"",intodatadetail)
                        intodatadetail=re.sub("new Date\(","\"",intodatadetail)
                        intodatadetail=re.sub("\)","\"",intodatadetail)

                        #print "intodatadetail.................................."
                        #print intodatadetail

                        time.sleep(1)
                        #每一个商品所以信息放一个位置，有多长就有几个，里面是字典
                        intodatadetail=json.loads(intodatadetail)
                        #print "intodatadetail.................................."
                        #print intodatadetail

                        for j in range(len(intodatadetail)):
                            stockitemdetail=intodatadetail[j]

                            #商品编号
                            pagecode=stockitemdetail["ptypecode"]
                            code=newstock[14+j].strip()
                            try:
                                self.assertEqual(pagecode.strip(),code.strip(),msg=u"商品编号不一致")
                                print u"商品编号一致"
                            except AssertionError,msg:
                                print msg
                                print pagecode
                                print code

                            #商品名称
                            pagname=stockitemdetail["pfullname"]
                            name=newstock[8+j]

                            try:
                                self.assertEqual(pagname.strip(),name.strip(),msg=u"商品名称不一致")
                                print u"商品名称一致"
                            except AssertionError,msg:
                                print msg
                                print pagname
                                print name

                            #数量
                            pageqty=stockitemdetail["qty"]
                            pageqty=str("%.4f"%pageqty)

                            qty=float(newstock[10+j])
                            qty=str("%.4f"%qty)

                            try:
                                self.assertEqual(pageqty.strip(),qty.strip(),msg=u"数量不一致")
                                print u"数量一致"
                            except AssertionError,msg:
                                print msg
                                print pageqty
                                print qty

                            #单价
                            pageprice=stockitemdetail["asstpprice"]
                            pageprice=str("%.4f"%pageprice)
                            if j==0:
                                price=float(newstock[18])
                            else:
                                price=float(newstock[12])
                            price=str("%.4f"%price)

                            try:
                                self.assertEqual(pageprice.strip(),price.strip(),msg=u"单价不一致")
                                print u"单价一致"
                            except AssertionError,msg:
                                print msg
                                print pageprice
                                print price


                            #金额
                            pagetotal=float(stockitemdetail["tptotal"])
                            pagetotal=str("%.4f"%pagetotal)
                            if j==0:
                                total=float(newstock[19])
                            else:
                                total=float(newstock[17])
                            total=str("%.4f"%total)

                            try:
                                self.assertEqual(pagetotal.strip(),total.strip(),msg=u"金额不一致")
                                print u"金额一致"
                            except AssertionError,msg:
                                print msg
                                print pagetotal
                                print total


                            #折前单价
                            dpsigle=float(newstock[12+j])
                            pagetemp=float(stockitemdetail["dpprice"])
                            self.assernote(dpsigle,pagetemp,u"折前单价不相同","折前单价相同","折前单价")

                            #折前金额
                            dpmoney=float(newstock[16+j])
                            pagetemp=float(stockitemdetail["dptotal"])
                            self.assernote(dpmoney,pagetemp,u"折前金额不相同","折前金额相同","折前金额")

                            #折扣
                            pagetemp=float(stockitemdetail["discount"])
                            discount=float(newstock[23+j])
                            self.assernote(discount,pagetemp,u"折扣不相同","折扣相同","折扣")

                            #税率
                            tax=float(newstock[25+j])
                            pagetemp=float(stockitemdetail["tax"])
                            self.assernote(tax,pagetemp,u"税率不相同","税率相同","税率")

                            if j==0:
                                taxtotal=float(newstock[20])
                                taxsigle=float(newstock[21])
                                taxmoney=float(newstock[22])
                            else:
                                taxtotal=float(0)
                                taxsigle=float(newstock[13])
                                taxmoney=float(newstock[17])

                            #税额
                            pagetemp=float(stockitemdetail["taxtotal"])
                            self.assernote(taxtotal,pagetemp,u"税额不相同","税额相同","税额")

                            #税后单价
                            pagetemp=float(stockitemdetail["assprice"])
                            self.assernote(taxsigle,pagetemp,u"税后单价不相同","税后单价相同","税后单价")

                            #税后金额
                            pagetemp=float(stockitemdetail["total"])
                            self.assernote(taxmoney,pagetemp,u"税后金额不相同","税后金额相同","税后金额")

                            #print "stockitemdetail.............................."
                            #print stockitemdetail


                        break
            if success!=0:
                print u"上一步进货订单管理递交该流程失败，未能找到此订单，测试不通过"
                for n in range(1,4):
                    xpath=flagorder1+str(n)+flagorder2
                    status=browser.elementisexist(self.driver,xpath)
                    if status==True:
                        checkid=browser.findXpath(self.driver,xpath).text
                        print checkid
                        browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\checkdata3','w',0,checkid)
                        break

            selectorder=browser.xmlRead(self.driver,dom,'selectorder',0)
            browser.findXpath(self.driver,selectorder).click()
        except:
            print u"选择进入订单入库失败"
            print(traceback.format_exc())

        #部门
        try:
            department=browser.xmlRead(self.driver,dom,'department',0)
            #time.sleep(2)
            browser.findXpath(self.driver,department).click()
            closedep=browser.xmlRead(self.driver,dom,'closedep',0)
            browser.findXpath(self.driver,closedep).click()
            browser.findXpath(self.driver,department).click()
            selectdep=browser.xmlRead(self.driver,dom,'selectdep',0)
            browser.findXpath(self.driver,selectdep).click()
            print u"部门选择成功，并测试关闭按钮"
        except:
            print u"选择部门失败"
            print(traceback.format_exc())

        #进行保存
        try:
            intoifsave=browser.xmlRead(self.driver,dom,'intoifsave',0)
            browser.findXpath(self.driver,intoifsave).click()
            intosave=browser.xmlRead(self.driver,dom,'intosave',0)
            browser.findXpath(self.driver,intosave).click()
        except:
            print u"进货单保存失败"
            print(traceback.format_exc())


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
