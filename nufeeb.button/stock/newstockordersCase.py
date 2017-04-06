#*-* coding:UTF-8 *-*
import time
from common import loggingClass
import unittest
import  xml.dom.minidom
import traceback
import stockcompareapi
from common import browserClass
browser=browserClass.browser()

class newstockordersTest(unittest.TestCase):
    u'''进货-新增进货订单'''

    def setUp(self):
        self.driver=browser.startBrowser('chrome')
        browser.set_up(self.driver)
        cookie = [item["name"] + "=" + item["value"] for item in self.driver.get_cookies()]
        #print cookie
        self.cookiestr = ';'.join(item for item in cookie)
        browser.delaytime(2)
        header={'cookie':self.cookiestr,"Content-Type": "application/json"}
        self.comdom=xml.dom.minidom.parse(r'C:\workspace\nufeeb.button\data\commonlocation')
        self.dom = xml.dom.minidom.parse(r'C:\workspace\nufeeb.button\stock\stocklocation')

        self.modulename=browser.xmlRead(self.dom,"module",0)
        self.moduledetail=browser.xmlRead(self.dom,'moduledetail',0)

        browser.openModule2(self.driver,self.modulename,self.moduledetail)
        browser.delaytime(1)
        cookies=browser.cookieSave(self.driver)
        self.header3={'cookie':cookies,"Content-Type": "application/json"}
        self.header4={'cookie':cookies,"Content-Type": "application/x-www-form-urlencoded"}

        #页面id
        pageurl=browser.xmlRead(self.dom,"newurl",0)
        self.pageid=browser.getalertid(pageurl,header)
        self.pageid=self.pageid[:-1]
        self.commid=browser.getallcommonid(self.comdom)

        #需要从数据库取数比较的数据放到astdic
        self.astdic={}
        self.items=[]

        #定义位置
        browser.delaytime(1)
        self.edBType=self.pageid+browser.xmlRead(self.dom,"edBType",0)
        self.edEType=self.pageid+browser.xmlRead(self.dom,"edEType",0)
        self.edKType=self.pageid+browser.xmlRead(self.dom,"edKType",0)
        self.edSummary=self.pageid+browser.xmlRead(self.dom,"edSummary",0)
        self.edComment=self.pageid+browser.xmlRead(self.dom,"edComment",0)

        self.qty=browser.xmlRead(self.dom,"grid_assqty",0)
        self.dpprice=browser.xmlRead(self.dom,"grid_assdpprice",0)

    def tearDown(self):
        print "test over"
        self.driver.close()
        pass



    def testnewstockorders(self):
        u'''进货-新增进货订单.'''
        try:
            #供货单位
            browser.doubleclick(self.driver,self.edBType)
            companyurl="http://beefun.wsgjp.com/Beefun/Selector/BTypeSelector.gspx?Add=True&HideStoppedItem=True&ShowFreight=false&Bcategory=1&FilterStr="
            companyid=browser.getalertid(companyurl,self.header3)
            #print companyid

            #-往来单位，供应商选择
            #-翻页
            browser.pagewhich(self.driver,self.commid["basetype"],companyid,self.commid["typenext"],self.commid["typetopbe"],self.commid["typebe"],self.commid["typetopnext"])

            #-关闭
            comclose=companyid+self.commid["selclose"]
            browser.delaytime(1)
            browser.findId(self.driver,comclose).click()
            browser.doubleclick(self.driver,self.edBType)


            #-添加
            comadd=companyid+self.commid["btnAdd"]
            browser.delaytime(1)
            #print comadd
            browser.findId(self.driver,comadd).click()

            addurl="http://beefun.wsgjp.com/Beefun/BaseInfo/BTypeInfo.gspx?Mode=Add&ParId=0&ParTypeId=00000&type=add&id=2605638079543104347&InfoType=&classpath="
            addid=browser.getalertid(addurl,self.header3)
            #print addid

            #--往来单位信息框
            #--保存并新增
            time.sleep(1)
            comsaadd=addid+self.commid["btnSaveAdd"]
            browser.delaytime(1)
            browser.findId(self.driver,comsaadd).click()
            browser.accAlert(self.driver,1)
            #--保存并关闭
            comsaclose=addid+self.commid["btnSaveClose"]
            browser.delaytime(1)
            browser.findId(self.driver,comsaclose).click()
            browser.accAlert(self.driver,1)
            #--关闭
            comexit=addid+self.commid["selclose"]
            browser.delaytime(1)
            browser.findId(self.driver,comexit).click()

            #-查看基本信息
            combainfo=companyid+self.commid["btnDetail"]
            browser.delaytime(1)
            browser.findId(self.driver,combainfo).click()

            combainurl="http://beefun.wsgjp.com/Beefun/BaseInfo/BTypeInfo.gspx?Mode=Read&id=2605638079543104347&classpath="
            combainid=browser.getalertid(combainurl,self.header3)
            #print combainid
            #--往来单位信息框，关闭
            combainclose=combainid+self.commid["selclose"]
            browser.delaytime(1)
            browser.findId(self.driver,combainclose).click()

            #-选中
            browser.doubleclick(self.driver,self.edBType)
            browser.delaytime(1)
            comsel=companyid+self.commid["selbtn"]
            browser.findId(self.driver,comsel).click()

            #browser.findId(self.driver,comclose).click()

            #经手人
            browser.delaytime(1)
            browser.doubleclick(self.driver,self.edEType)

            ppeopleurl="http://beefun.wsgjp.com/Beefun/Selector/ETypeSelector.gspx?Add=True&HideStoppedItem=True&ShowFreight=false&Bcategory=1&FilterStr="
            ppeoid=browser.getalertid(ppeopleurl,self.header3)
            #print ppeoid

            #-业务员选择框
            #-添加
            ppeoadd=ppeoid+self.commid["btnAdd"]
            browser.delaytime(1)
            browser.findId(self.driver,ppeoadd).click()
            ppeourl="http://beefun.wsgjp.com/Beefun/BaseInfo/ETypeInfo.gspx?Mode=Add&ParId=0&ParTypeId=00000&type=add&id=2605638088210451192&InfoType=&classpath="
            ppinid=browser.getalertid(ppeourl,self.header3)
            time.sleep(1)
            #print ppinid

            #--内部职员信息框
            #--保存并新增
            ppsaadd=ppinid+self.commid["btnSaveAdd"]
            browser.delaytime(1)
            browser.findId(self.driver,ppsaadd).click()
            browser.accAlert(self.driver,1)

            #--保存并关闭
            ppsacl=ppinid+self.commid["btnSaveClose"]
            browser.delaytime(1)
            browser.findId(self.driver,ppsacl).click()
            browser.accAlert(self.driver,1)

            #---所属部门
            ppdepart=ppinid+browser.xmlRead(self.dom,"edDepartment",0)
            browser.delaytime(1)
            browser.doubleclick(self.driver,ppdepart)
            ppdepurl="http://beefun.wsgjp.com/Beefun/Selector/DepartmentSelector.gspx"
            ppdeid=browser.getalertid(ppdepurl,self.header3)
            #print ppdeid

            #---关闭
            ppdeclo=ppdeid+self.commid["selclose"]
            browser.delaytime(1)
            browser.findId(self.driver,ppdeclo).click()
            browser.doubleclick(self.driver,ppdepart)

            #---选中
            ppdesel=ppdeid+self.commid["selbtn"]
            browser.delaytime(1)
            browser.findId(self.driver,ppdesel).click()

            #--关闭
            ppinfoclo=ppinid+self.commid["selclose"]
            browser.delaytime(1)
            browser.findId(self.driver,ppinfoclo).click()

            #-关闭
            ppeoexit=ppeoid+self.commid["selclose"]
            browser.delaytime(1)
            browser.findId(self.driver,ppeoexit).click()
            browser.doubleclick(self.driver,self.edEType)

            #-选中
            ppeosel=ppeoid+self.commid["selbtn"]
            browser.findId(self.driver,ppeosel).click()

            #交货日期

            #收货仓库

            browser.delaytime(1)
            browser.doubleclick(self.driver,self.edKType)

            cateurl="http://beefun.wsgjp.com/Beefun/Selector/KTypeSelector.gspx?Add=True&HideStoppedItem=True&ShowFreight=false&Bcategory=1&FilterStr="
            cateid=browser.getalertid(cateurl,self.header3)
            #print cateid

            #-仓库选择框
            #-添加
            cateadd=cateid+self.commid["btnAdd"]
            browser.findId(self.driver,cateadd).click()
            cateinfourl="http://beefun.wsgjp.com/Beefun/BaseInfo/KTypeEdit.gspx?Mode=Add&ParId=0&ParTypeId=00000&type=add&id=2605638079543104740&InfoType=&classpath="
            cateinid=browser.getalertid(cateinfourl,self.header3)
            #print cateinid

            #--仓库信息-信息框
            #--保存并新增
            browser.delaytime(1)
            browser.exjscommin(self.driver,"保存并新增")
            browser.accAlert(self.driver,1)
            browser.exjscommin(self.driver,"保存并关闭")
            browser.accAlert(self.driver,1)
            browser.exjscommin(self.driver,"关闭")
            '''
            cainsaadd=cateinid+self.commid["btnSaveAdd"]
            browser.delaytime(1)
            browser.findId(self.driver,cainsaadd).click()
            browser.accAlert(self.driver,1)


            #--保存并关闭
            cainsacl=cateinid+self.commid["btnSaveClose"]
            browser.findId(self.driver,cainsacl).click()
            browser.accAlert(self.driver,1)

            #--关闭
            cainclose=cateinid+self.commid["selclose"]
            browser.delaytime(1)
            browser.findId(self.driver,cainclose).click()
            '''
            #-关闭
            cateclose=cateid+self.commid["selclose"]
            browser.delaytime(1)
            browser.findId(self.driver,cateclose).click()
            browser.doubleclick(self.driver,self.edKType)

            #-选中
            catesel=cateid+self.commid["selbtn"]
            browser.delaytime(1)
            browser.findId(self.driver,catesel).click()

            #摘要

            browser.findId(self.driver,self.edSummary).send_keys(u"中文蘩軆饕餮！@#￥%……&*（）？； 。.Button summary")

            #附加说明

            browser.findId(self.driver,self.edComment).send_keys(u"Button comment中文蘩軆饕餮！@#￥%……&*（）？； 。.")

            #商品编号
            self.itemone=self.commid["basetype"]+self.pageid+browser.xmlRead(self.dom,"nitemcode",0)
            browser.findXpath(self.driver,self.itemone).click()
            itemsel=self.pageid+self.commid["itname"]
            browser.doubleclick(self.driver,itemsel)

            itemurl="http://beefun.wsgjp.com/Beefun/Selector/PTypeSelector.gspx?Add=True&HideStoppedItem=True&DontClose=True&VchType=7&BTypeId=2605638079543104347&KTypeId=2605638079543104740&MultiSelect=True"
            itemid=browser.getalertid(itemurl,self.header3)
            #print itemid

            #-库存商品选择框
            #-添加
            itemadd=itemid+self.commid["btnAdd"]
            browser.findId(self.driver,itemadd).click()

            iteminurl="http://beefun.wsgjp.com/Beefun/BaseInfo2/PTypeEdit.gspx?Mode=Add&ParId=0&ParTypeId=00000&type=add&id=869585272784951&InfoType=&classpath="
            itemadid=browser.getalertid(iteminurl,self.header3)
            #print itemadid
            browser.stockitemselectadd(self.driver,self.commid,itemadid)

            #-翻页
            browser.pagewhich(self.driver,self.commid["basetype"],itemid,self.commid["typenext"],self.commid["typetopbe"],self.commid["typebe"],self.commid["typetopnext"])

            #-关闭
            itaddclo=itemid+self.commid["selclose"]
            browser.findId(self.driver,itaddclo).click()
            browser.doubleclick(self.driver,itemsel)

            #-选中
            itaddsel=itemid+browser.xmlRead(self.dom,"btnKeepSelect",0)
            browser.findId(self.driver,itaddsel).click()

            #-选中并关闭
            itaddselclo=itemid+self.commid["selbtn"]
            browser.findId(self.driver,itaddselclo).click()

            itemgrid=browser.xmlRead(self.dom,"itemgrid",0)

            #grid
            #单位
            itemunit=self.commid["basetype"]+self.pageid+itemgrid+str(18)+"]/div"
            time.sleep(1)
            browser.doubleclick(self.driver,itemunit,1)

            #-选择商品的计量单位
            uniturl="http://beefun.wsgjp.com/Beefun/Selector/PTypeUnitSelector.gspx?PTypeId=869585272784951&BTypeId=2605638079543104347&KTypeId=2605638079543104740&prop1=0&prop2=0"
            unittext=browser.requestget(uniturl,self.header3)
            unitid=browser.getstockid(unittext)

            #-关闭
            unitclose=unitid[:10]+self.commid["btnexit"]
            #print unitclose
            browser.findId(self.driver,unitclose).click()
            browser.doubleclick(self.driver,itemunit,1)

            #-确定
            browser.findId(self.driver,unitid).click()

            #数量
            itqty=self.commid["basetype"]+self.pageid+itemgrid+str(24)+"]"
            browser.findXpath(self.driver,itqty).click()

            browser.doubleclick(self.driver,self.pageid+self.qty)

            qtyurl="http://beefun.wsgjp.com/Beefun/Bill/PTypeMultiUnitInput.gspx?PTypeId=869585272784951&UCode=1&URate=1&Qty=1"
            qtyid=browser.getalertid(qtyurl,self.header3)
            #print qtyid

            #-取消
            qtycan=qtyid+self.commid["btnexit"]
            browser.findId(self.driver,qtycan).click()
            browser.doubleclick(self.driver,self.pageid+self.qty)

            #-确定
            qtyok=qtyid+self.commid["btnOK"]
            #time.sleep(1)
            #print qtyok
            browser.findId(self.driver,qtyok).click()

            #折前单价
            itdpprice=self.commid["basetype"]+self.pageid+itemgrid+str(28)+"]"
            browser.delaytime(1)
            browser.findXpath(self.driver,itdpprice).click()
            browser.doubleclick(self.driver,self.pageid+self.dpprice)
            time.sleep(1)

            dppriceurl="http://beefun.wsgjp.com/Beefun/Selector/PTypePriceSelector.gspx?PTypeId=869585272784951&UCode=1&KTypeId=2605638079543104740&BTypeId=2605638079543104347"
            dptext=browser.requestget(dppriceurl,self.header3)
            dpid=browser.getstockid(dptext)
            #print dpid

            #-关闭
            dpcan=dpid[:10]+self.commid["btnexit"]
            browser.delaytime(1)
            browser.findId(self.driver,dpcan).click()
            browser.doubleclick(self.driver,self.pageid+self.dpprice)

            #-确定
            browser.findId(self.driver,dpid).click()

            #录单配置
            billcon=self.pageid+browser.xmlRead(self.dom,"btnBillConfig",0)
            browser.delaytime(1)
            browser.findId(self.driver,billcon).click()

            conurl="http://beefun.wsgjp.com/Beefun/Bill/BillConfig.gspx"
            condata={"__Params":"{\"vchtype\":7}"}
            context=browser.requestpost(conurl,condata,self.header4)
            conid=browser.getstockid(context)
            #print conid

            #-退出
            conclose=conid[:10]+self.commid["btnClose"]
            browser.delaytime(1)
            browser.findId(self.driver,conclose).click()
            browser.findId(self.driver,billcon).click()

            #-保存
            browser.findId(self.driver,conid).click()
            browser.accAlert(self.driver,1)


            #导入商品明细
            importdetail=self.pageid+browser.xmlRead(self.dom,"btnImportDetail",0)
            browser.delaytime(1)
            browser.findId(self.driver,importdetail).click()
            importurl="http://beefun.wsgjp.com/Beefun/Bill/BillImport/ImportBillDetail.gspx"
            importid=browser.getalertid(importurl,self.header3)
            #print importid

            #-导入文件
            imfile=importid+self.commid["button"]+str(1)
            browser.delaytime(1)
            browser.findId(self.driver,imfile).click()
            browser.accAlert(self.driver,1)

            #-取消
            imcan=importid+self.commid["btnexit"]
            browser.findId(self.driver,imcan).click()

            #打印
            #保存退出
            saclose=self.pageid+self.commid["selclose"]
            browser.findId(self.driver,saclose).click()

            #-保存单据
            browser.exjscommin(self.driver,"保存单据")


            #-废弃退出
            browser.findXpath(self.driver,self.itemone).click()
            browser.doubleclick(self.driver,itemsel)
            browser.exjscommin(self.driver,"选中")
            browser.findId(self.driver,saclose).click()
            browser.exjscommin(self.driver,"废弃退出")

            browser.openModule2(self.driver,self.modulename,self.moduledetail)

            #付定金
            payment=self.pageid+browser.xmlRead(self.dom,"btnPayment",0)
            browser.findId(self.driver,payment).click()
            browser.delaytime(1)
            browser.accAlert(self.driver,1)

            browser.findXpath(self.driver,self.itemone).click()
            browser.doubleclick(self.driver,itemsel)
            browser.exjscommin(self.driver,"选中并关闭")

            browser.doubleclick(self.driver,self.edBType)
            browser.exjscommin(self.driver,"选中")
            browser.doubleclick(self.driver,self.edKType)
            browser.exjscommin(self.driver,"选中")
            browser.findId(self.driver,payment).click()
            browser.exjscommin(self.driver,"退出")
            browser.exjscommin(self.driver,"存入草稿")
            browser.exjscommin(self.driver,"退出")

            browser.openModule2(self.driver,self.modulename,self.moduledetail)

        except:
            print traceback.format_exc()
            filename=browser.xmlRead(self.comdom,'filename',0)
            browser.delaytime(1)
            browser.getpicture(self.driver,filename+u"进货-新增进货订单.png")

    #获取数据dic 页面的
    def getassertdic(self):
        #asslists
        try:
            self.flag=1
            jsorlot=browser.xmlRead(self.dom,"edNumber",0)
            orlot=self.pageid+jsorlot
            ordercode=browser.jsinputgetval(self.driver,orlot,jsorlot)
            self.astdic['number']=ordercode

            todatejsid=browser.xmlRead(self.dom,"edToDate",0)
            todateid=self.pageid+todatejsid
            todate=browser.jsinputgetval(self.driver,todateid,todatejsid)
            self.astdic['todate']=todate

            edatejsid=browser.xmlRead(self.dom,"edDate",0)
            edateid=self.pageid+edatejsid
            eddate=browser.jsinputgetval(self.driver,edateid,edatejsid)
            self.astdic['eddate']=eddate

            comp=browser.jsinputgetval(self.driver,self.edBType,browser.xmlRead(self.dom,"edBType",0))
            self.astdic['btype']=comp

            peo=browser.jsinputgetval(self.driver,self.edEType,browser.xmlRead(self.dom,"edEType",0))
            self.astdic['etype']=peo

            cate=browser.jsinputgetval(self.driver,self.edKType,browser.xmlRead(self.dom,"edKType",0))
            self.astdic['ktype']=cate

            Summary=browser.jsinputgetval(self.driver,self.edSummary,browser.xmlRead(self.dom,"edSummary",0))
            self.astdic['Summary']=Summary

            Comment=browser.jsinputgetval(self.driver,self.edComment,browser.xmlRead(self.dom,"edComment",0))
            self.astdic['Comment']=Comment

            #print "self.astdic.........."
            #print self.astdic

            #商品的
            #self.items
            #item=["UserCode","FullName","Unit1","assQty","assdpPrice","dpTotal","discount","asstpPrice","tpTotal","tax","taxTotal","assprice","total","comment"]
            divjq=[0,1,5,20]
            li=[0,21]
            creatjs="var tempdiv= document.createElement('div');tempdiv.id = 'tempdivid';document.body.appendChild(tempdiv);"
            browser.delaytime(1)
            browser.excutejs(self.driver,creatjs)
            for no in li:
                temp=[]
                for n in divjq:
                    js="var a=$(\"div[class=GridBodyCellText]\").eq("+str(n+no)+").text();$(\"#tempdivid\").attr(\"value\",a)"
                    browser.delaytime(1)
                    browser.excutejs(self.driver,js)
                    sigle=browser.findId(self.driver,"tempdivid").get_attribute("value")
                    #browser.delaytime(1)
                    temp.append(sigle)

                for n in range(9,19):
                    js="var a=$(\"div[class=GridBodyCellText]\").eq("+str(n+no)+").text();$(\"#tempdivid\").attr(\"value\",a)"
                    browser.delaytime(1)
                    browser.excutejs(self.driver,js)
                    sigle=browser.findId(self.driver,"tempdivid").get_attribute("value")
                    temp.append(sigle)
                #print "temp.........."
                #print temp
                self.items.append(temp)
            #print " self.items........"
            #print  self.items

        except:
            print traceback.format_exc()
            filename=browser.xmlRead(self.comdom,'filename',0)
            browser.getpicture(self.driver,filename+u"进货-新增进货订单-断言取值失败.png")
            #print "取值错误"
            self.flag=0

    def test_assnskSave(self):
        u'''断言j进货-进货订单-保存'''
        try:
            browser.doubleclick(self.driver,self.edBType)
            browser.exjscommin(self.driver,"选中")
            browser.doubleclick(self.driver,self.edEType)
            browser.exjscommin(self.driver,"选中")
            browser.doubleclick(self.driver,self.edKType)
            browser.exjscommin(self.driver,"选中")
            browser.findId(self.driver,self.edSummary).send_keys(u"assert Button summary")
            browser.findId(self.driver,self.edComment).send_keys(u"assert Button comment")

            li=1
            row=4
            itemnamexpath=self.commid["basetype"]+self.pageid+browser.xmlRead(self.dom,"namehalf",0)+str(li)+"]/td["+str(row)+"]"
            browser.findXpath(self.driver,itemnamexpath).click()
            itemname=self.pageid+browser.xmlRead(self.dom,"grid_pfullname",0)
            browser.doubleclick(self.driver,itemname)
            browser.exjscommin(self.driver,"选中",1)
            browser.delaytime(1)
            js="$(\"div[class=GridBodyCellText]:contains('1M有编码')\").attr(\"id\",\"secitemid\")"
            browser.delaytime(1)
            browser.excutejs(self.driver,js)
            browser.findId(self.driver,"secitemid").click()
            browser.exjscommin(self.driver,"选中并关闭")

            browser.findId(self.driver,self.pageid+self.qty).send_keys('3')
            item2xpathdpprice=self.commid["basetype"]+self.pageid+browser.xmlRead(self.dom,"namehalf",0)+str(li+1)+"]/td["+str(row+24)+"]"
            browser.findXpath(self.driver,item2xpathdpprice).click()
            browser.findId(self.driver,self.pageid+self.dpprice).send_keys('19.86')
            item2xpathdiscount=self.commid["basetype"]+self.pageid+browser.xmlRead(self.dom,"namehalf",0)+str(li+1)+"]/td["+str(row+26)+"]"
            browser.findXpath(self.driver,item2xpathdiscount).click()
            browser.findId(self.driver,self.pageid+browser.xmlRead(self.dom,"grid_discount",0)).send_keys('0.87')
            item2xpathtax=self.commid["basetype"]+self.pageid+browser.xmlRead(self.dom,"namehalf",0)+str(li+1)+"]/td["+str(row+29)+"]"
            browser.findXpath(self.driver,item2xpathtax).click()
            browser.findId(self.driver,self.pageid+browser.xmlRead(self.dom,"grid_tax",0)).send_keys('5.62')
            item2xpathbz=self.commid["basetype"]+self.pageid+browser.xmlRead(self.dom,"namehalf",0)+str(li+1)+"]/td["+str(row+35)+"]"
            browser.findXpath(self.driver,item2xpathbz).click()
            browser.findId(self.driver,self.pageid+browser.xmlRead(self.dom,"grid_comment",0)).send_keys('beizhu item2 assert')

            browser.findId(self.driver,self.edComment).click()

            #获取assertdic
            self.getassertdic()

            browser.exjscommin(self.driver,"保存")
            browser.exjscommin(self.driver,"保存单据")

            f=open(r'C:\\workspace\\nufeeb.button\\data\\temp','w')
            f.write(str(self.astdic['number']))
            f.close()

            if self.flag==0:
                loggingClass.addlogmes("info","newstockordersTest-test_assnskSave-",u"进货-新增进货订单-保存失败,没有进行断言")
                pass
            else:
                #print self.astdic
                #print self.items
                #数据库订单头数据
                orderdatas=browser.getmysqldlyndxOrder(self.astdic['number'],self.astdic['Summary'])
                #print "mysql............."
                #print orderdatas
                #数据库商品数据
                orderitems=browser.getmysqlitems(self.astdic['number'],self.astdic['Summary'])
                print orderitems
                #print len(orderitems)
                comapi=stockcompareapi.stockcompary()
                caseassert="newstockordersTest-test_assnskSave-"+str(self.astdic['number'])

                #订单头
                #录单日期
                comapi.commonfun(caseassert,self.astdic["eddate"],orderdatas[3],u"进货-新增进货订单-订单头-录单日期和数据库不一致")
                #供货单位
                comapi.commonfun(caseassert,self.astdic["btype"],orderdatas[0],u"进货-新增进货订单-订单头-供货单位和数据库不一致")
                #经手人
                comapi.commonfun(caseassert,self.astdic["etype"],orderdatas[1],u"进货-新增进货订单-订单头-经手人和数据库不一致")
                #交货日期
                comapi.commonfun(caseassert,self.astdic["todate"],orderdatas[6],u"进货-新增进货订单-订单头-交货日期和数据库不一致")
                #收货仓库
                comapi.commonfun(caseassert,self.astdic["ktype"],orderdatas[2],u"进货-新增进货订单-订单头-收货仓库和数据库不一致")
                #摘要
                comapi.commonfun(caseassert,self.astdic["Summary"],orderdatas[4],u"进货-新增进货订单-订单头-摘要和数据库不一致")
                #附加说明
                comapi.commonfun(caseassert,self.astdic["Comment"],orderdatas[5],u"进货-新增进货订单-订单头-附加说明和数据库不一致")

                #商品详情
                for item in self.items:
                    mysqlitem=[]
                    for code in orderitems:
                        if code[0]==item[0]:
                            mysqlitem=code
                            break
                    #商品编号
                    comapi.commonfun(caseassert,item[0],str(mysqlitem[0]),u"进货-新增进货订单-商品明细-附加说明和数据库不一致")
                    #商品名称
                    comapi.commonfun(caseassert,item[1],str(mysqlitem[1]),u"进货-新增进货订单-商品明细-商品名称和数据库不一致")
                    #单位
                    comapi.commonfun(caseassert,item[2],str(mysqlitem[2]),u"进货-新增进货订单-商品明细-单位和数据库不一致")
                    #数量
                    comapi.commonfun(caseassert,browser.strconfloat(item[4]),str(mysqlitem[5]),u"进货-新增进货订单-商品明细-数量和数据库不一致")
                    #折前单价
                    comapi.commonfun(caseassert,browser.strconfloat(item[5]),str(mysqlitem[6]),u"进货-新增进货订单-商品明细-折前单价和数据库不一致")
                    #折前金额
                    comapi.commonfun(caseassert,browser.strconfloat(item[6]),str(mysqlitem[7]),u"进货-新增进货订单-商品明细-折前金额和数据库不一致")
                    #折扣
                    comapi.commonfun(caseassert,browser.strconfloat(item[7]),str(mysqlitem[8]),u"进货-新增进货订单-商品明细-折扣和数据库不一致")
                    #单价
                    comapi.commonfun(caseassert,browser.strconfloat(item[8]),str(mysqlitem[9]),u"进货-新增进货订单-商品明细-单价和数据库不一致")
                    #金额
                    comapi.commonfun(caseassert,browser.strconfloat(item[9]),str(mysqlitem[10]),u"进货-新增进货订单-商品明细-金额和数据库不一致")
                    #税率
                    comapi.commonfun(caseassert,browser.strconfloat(item[10]),str(mysqlitem[11]),u"进货-新增进货订单-商品明细-税率和数据库不一致")
                    #税额
                    comapi.commonfun(caseassert,browser.strconfloat(item[11]),str(mysqlitem[12]),u"进货-新增进货订单-商品明细-税额和数据库不一致")
                    #税后单价
                    comapi.commonfun(caseassert,browser.strconfloat(item[12]),str(mysqlitem[13]),u"进货-新增进货订单-商品明细-税后单价和数据库不一致")
                    #税后金额
                    comapi.commonfun(caseassert,browser.strconfloat(item[13]),str(mysqlitem[14]),u"进货-新增进货订单-商品明细-税后金额和数据库不一致")
                    #comapi.commonfun(caseassert,browser.strconfloat(item[13]),str(100),u"进货-新增进货订单-商品明细-税后金额和数据库不一致")
                    #备注
                    comapi.commonfun(caseassert,item[3].strip(),str(mysqlitem[15]),u"进货-新增进货订单-商品明细-备注和数据库不一致")



        except:
            print traceback.format_exc()
            filename=browser.xmlRead(self.comdom,'filename',0)
            browser.delaytime(1)
            browser.getpicture(self.driver,filename+u"断言进货-新增进货订单-进货订单保存.png")
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
