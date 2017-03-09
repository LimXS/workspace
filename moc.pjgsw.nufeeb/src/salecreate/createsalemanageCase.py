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

class createsalemanageTest(unittest.TestCase):
    u'''批零-销售订单管理'''

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

    def testcreatesaleManage(self):
        u'''批零-销售订单管理'''
        dom = xml.dom.minidom.parse(r'C:\workspace\moc.pjgsw.nufeeb\src\data\salecreatedata')
        modulename=browser.xmlRead(self.driver,dom,"module",1)
        moduledetail=browser.xmlRead(self.driver,dom,'moduledetail',1)

        browser.openModule2(self.driver,modulename,moduledetail)

        saleorderdata=browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\saleordercheckdata','r',1,'aaa')
        flagnum=saleorderdata[0].strip()
        print "checkdata no............"
        print flagnum


        #销售订单管理页面Id
        header={'cookie':self.cookiestr,"Content-Type": "application/json"}
        #header2={'cookie':self.cookiestr,"Content-Type": "application/x-www-form-urlencoded"}

        pageidurl="http://beefun.wsgjp.com/Beefun/Carrier/OrderManager.gspx?vchtype=saleorder"
        pageidtext=requests.get(url=pageidurl,headers=header)
        #print pageidtext.text
        pageid=browser.getpageid(pageidtext)
        #print pageid

        #取管理lists
        managelistsurl="http://beefun.wsgjp.com/Carpa.Web/Carpa.Web.Script.DataService.ajax/GetPagerData"
        managelistdata={"pagerId":pageid,"queryParams":{"vchType":8,"xTypeid":"","isComplete":"0","isAudit":-1,"isExport":"-1","dlytype":-1},"orders":None,"filter":None,"first":0,"count":1000}
        managelisttext=requests.post(url=managelistsurl,data=json.dumps(managelistdata),headers=header)
        manlisdic=browser.datatrunjson(managelisttext)
        #print managelist


        #取商品明细
        comment=''
        kfullname=''
        ename=''
        bname=''
        total=0
        tptotal=0
        dptotal=0
        mandetaildic=''
        for listdata in manlisdic["itemList"]:
            #print listdata

            #订单编号
            number=listdata["number"]
            if number==flagnum:
                print u"进货订单提交至进货订单管理成功，测试通过"
                #获取每个订单详细数据并进行统计
                #print "listdata............................"
                #print listdata

                toqty=float(listdata["toqty"])
                untoqty=float(listdata["untoqty"])
                repairqty=float(listdata["repairqty"])
                repairtotal=listdata["repairtotal"]
                tototal=listdata["tototal"]
                untototal=listdata["untototal"]
                vchcode=listdata["vchcode"]
                comment=listdata["comment"]
                vchtype=listdata["vchtype"]
                summary=listdata["summary"]
                btypeid=listdata["btypeid"]
                etypeid=listdata["etypeid"]
                ktypeid=listdata["ktypeid"]
                ename=listdata["ename"]
                #仓库名称
                kfullname=listdata["kfullname"]
                #单位名称
                bname=listdata["bname"]
                total=listdata["total"]
                tptotal=listdata["tptotal"]
                dptotal=listdata["dptotal"]


                manurldetail="http://beefun.wsgjp.com/Beefun/Beefun.Carrier.OrderManager.ajax/GetDetailsByorderid"
                mandetaildata={"hashdata":{"toqty":toqty,"untoqty":untoqty,"repairqty":repairqty,"repairtotal":repairtotal,"tototal":tototal,"untototal":untototal,"isdelivered":0,"checked":0,"vchcode":vchcode,"vchtype":vchtype,"date":"\/Date(1466092800000)\/","number":number,"todate":"\/Date(1466092800000)\/","comment":comment,"summary":summary,"btypeid":btypeid,"bpartypeid":"00000","etypeid":etypeid,"ktypeid":ktypeid,"auditover":False,"ename":ename,"kfullname":kfullname,"bname":bname,"artotal":0,"aptotal":0,"r_warnup":0,"orderover1":0,"createtypename":"本地创建","createtype":0,"reccnt":0,"total":total,"tptotal":tptotal,"dptotal":dptotal,"default_audited":0,"default_auditorid":None,"default_audittime":None,"default_auditremark":"","finance_audited":0,"finance_auditorid":0,"finance_audittime":None,"finance_auditremark":"","isexport":0,"earnest":0,"finance_auditorname":"","business_auditorname":"","receiverpeople":None,"receivercellphone":None,"receivertelephone":None,"receiverzipcode":None,"province":None,"city":None,"district":None,"receiveraddress":None,"isneedinvoice":None}}
                mandetail=requests.post(url=manurldetail,data=json.dumps(mandetaildata),headers=header)
                mandetaildicl=browser.datatrunjson(mandetail)

                #print "mandetaildicl..................."
                #print mandetaildicl
                mandetaildic=mandetaildicl[0]
                break

        #日期
        saleorderdata[1].strip()

        #往来单位
        self.assernote(str(bname),str(saleorderdata[2].strip()),u"往来单位不正确（原始订单和销售管理页面）",u"往来单位正确",u"往来单位")

        #仓库名称
        self.assernote(str(kfullname),str(saleorderdata[6].strip()),u"仓库名称不正确（原始订单和销售管理页面）",u"仓库名称正确",u"仓库名称")

        #经手人
        self.assernote(str(ename),str(saleorderdata[3].strip()),u"经手人不正确（原始订单和销售管理页面）",u"经手人正确",u"经手人")

        #交货日期
        saleorderdata[5].strip()

        #折前金额
        self.assernote(str(dptotal),str(saleorderdata[13].strip()),u"折前金额不正确（原始订单和销售管理页面）",u"折前金额正确",u"折前金额")

        #金额
        self.assernote(str(tptotal),str(saleorderdata[16].strip()),u"金额不正确（原始订单和销售管理页面）",u"金额正确",u"金额")

        #税后金额
        self.assernote(str(total),str(saleorderdata[20].strip()),u"税后金额不正确（原始订单和销售管理页面）",u"税后金额正确",u"税后金额")

        #已收定金金额

        #附加说明
        self.assernote(comment,saleorderdata[8].strip(),u"附加说明不正确（原始订单和销售管理页面）",u"附加说明正确",u"附加说明")

        #商品明细
        #商品编号
        self.assernote(str(mandetaildic["ptypecode"]),str(saleorderdata[9].strip()),u"商品编号不正确（原始订单商品明细和销售管理页面）",u"商品编号正确",u"商品编号")

        #商品名称
        self.assernote(str(mandetaildic["pfullname"]),str(saleorderdata[10].strip()),u"商品名称不正确（原始订单商品明细和销售管理页面）",u"商品名称正确",u"商品名称")

        #数量
        self.assernote(str(mandetaildic["qty"]),str(float(saleorderdata[11].strip())),u"数量不正确（原始订单商品明细和销售管理页面）",u"数量正确",u"数量")

        #单价
        self.assernote(str(mandetaildic["tpprice"]),str(saleorderdata[15].strip()),u"单价不正确（原始订单商品明细和销售管理页面）",u"单价正确",u"单价")

        #金额
        self.assernote(str(mandetaildic["tptotal"]),str(saleorderdata[16].strip()),u"金额不正确（原始订单商品明细和销售管理页面）",u"金额正确",u"金额")

        #选中进行审核
        manordernum1=browser.xmlRead(self.driver,dom,'manordernum1',0)
        manordernum2=browser.xmlRead(self.driver,dom,'manordernum2',0)
        maninput1=browser.xmlRead(self.driver,dom,'maninput1',0)
        maninput2=browser.xmlRead(self.driver,dom,'maninput2',0)
        for k in range(1,10):
            xpath=manordernum1+str(k)+manordernum2
            #print xpath
            if browser.findXpath(self.driver,xpath).text==flagnum:
                inputxpath=maninput1+str(k)+maninput2
                time.sleep(2)
                browser.findXpath(self.driver,inputxpath).click()
                mancheck=browser.xmlRead(self.driver,dom,'mancheck',0)
                browser.findXpath(self.driver,mancheck).click()
                mancheckok=browser.xmlRead(self.driver,dom,'mancheckok',0)
                browser.findXpath(self.driver,mancheckok).click()
                break



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
