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

class newstockordersTest(unittest.TestCase):
    u'''进货-新增进货订单'''

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



    def testnewstockorders(self):
        u'''进货-新增进货订单.'''
        header={'cookie':self.cookiestr,"Content-Type": "application/json"}
        comdom=xml.dom.minidom.parse(r'C:\workspace\proxynufeeb.button\data\commonlocation')
        dom = xml.dom.minidom.parse(r'C:\workspace\proxynufeeb.button\stock\stocklocation')

        modulename=browser.xmlRead(dom,"module",0)
        moduledetail=browser.xmlRead(dom,'moduledetail',0)

        browser.openModule2(self.driver,modulename,moduledetail)
        time.sleep(1)
        cookies=browser.cookieSave(self.driver)
        header3={'cookie':cookies,"Content-Type": "application/json"}
        header4={'cookie':cookies,"Content-Type": "application/x-www-form-urlencoded"}

        #页面id
        pageurl=browser.xmlRead(dom,"newurl",0)
        pageid=browser.getalertid(pageurl,header)
        pageid=pageid[:-1]
        #print pageid

        #commid,id
        commid=browser.getallcommonid(comdom)
        #id=browser.getcommonid(dom)


        try:
            #供货单位
            time.sleep(1)
            edBType=pageid+browser.xmlRead(dom,"edBType",0)
            browser.delaytime(1)
            browser.doubleclick(self.driver,edBType)
            companyurl="http://dba.wsgjp.com.cn/Beefun/Selector/BTypeSelector.gspx?Add=True&HideStoppedItem=True&ShowFreight=false&Bcategory=1&FilterStr="
            companyid=browser.getalertid(companyurl,header3)
            #print companyid

            #-往来单位，供应商选择
            #-翻页
            browser.pagewhich(self.driver,commid["basetype"],companyid,commid["typenext"],commid["typetopbe"],commid["typebe"],commid["typetopnext"])

            #-关闭
            comclose=companyid+commid["selclose"]
            browser.delaytime(1)
            browser.findId(self.driver,comclose).click()
            browser.doubleclick(self.driver,edBType)


            #-添加
            comadd=companyid+commid["btnAdd"]
            browser.delaytime(1)
            #print comadd
            browser.findId(self.driver,comadd).click()

            addurl="http://dba.wsgjp.com.cn/Beefun/BaseInfo/BTypeInfo.gspx?Mode=Add&ParId=0&ParTypeId=00000&type=add&id=2605638079543104347&InfoType=&classpath="
            addid=browser.getalertid(addurl,header3)
            #print addid

            #--往来单位信息框
            #--保存并新增
            time.sleep(1)
            comsaadd=addid+commid["btnSaveAdd"]
            browser.delaytime(1)
            browser.findId(self.driver,comsaadd).click()
            browser.accAlert(self.driver,1)
            #--保存并关闭
            comsaclose=addid+commid["btnSaveClose"]
            browser.delaytime(1)
            browser.findId(self.driver,comsaclose).click()
            browser.accAlert(self.driver,1)
            #--关闭
            comexit=addid+commid["selclose"]
            browser.delaytime(1)
            browser.findId(self.driver,comexit).click()

            #-查看基本信息
            combainfo=companyid+commid["btnDetail"]
            browser.delaytime(1)
            browser.findId(self.driver,combainfo).click()

            combainurl="http://dba.wsgjp.com.cn/Beefun/BaseInfo/BTypeInfo.gspx?Mode=Read&id=2605638079543104347&classpath="
            combainid=browser.getalertid(combainurl,header3)
            #print combainid
            #--往来单位信息框，关闭
            combainclose=combainid+commid["selclose"]
            browser.delaytime(1)
            browser.findId(self.driver,combainclose).click()

            #-选中
            browser.doubleclick(self.driver,edBType)
            browser.delaytime(1)
            comsel=companyid+commid["selbtn"]
            browser.findId(self.driver,comsel).click()


            #browser.findId(self.driver,comclose).click()

            #经手人
            edEType=pageid+browser.xmlRead(dom,"edEType",0)
            browser.delaytime(1)
            browser.doubleclick(self.driver,edEType)

            ppeopleurl="http://dba.wsgjp.com.cn/Beefun/Selector/ETypeSelector.gspx?Add=True&HideStoppedItem=True&ShowFreight=false&Bcategory=1&FilterStr="
            ppeoid=browser.getalertid(ppeopleurl,header3)
            #print ppeoid

            #-业务员选择框
            #-添加
            ppeoadd=ppeoid+commid["btnAdd"]
            browser.delaytime(1)
            browser.findId(self.driver,ppeoadd).click()
            ppeourl="http://dba.wsgjp.com.cn/Beefun/BaseInfo/ETypeInfo.gspx?Mode=Add&ParId=0&ParTypeId=00000&type=add&id=2605638088210451192&InfoType=&classpath="
            ppinid=browser.getalertid(ppeourl,header3)
            time.sleep(1)
            #print ppinid

            #--内部职员信息框
            #--保存并新增
            ppsaadd=ppinid+commid["btnSaveAdd"]
            browser.delaytime(1)
            browser.findId(self.driver,ppsaadd).click()
            browser.accAlert(self.driver,1)

            #--保存并关闭
            ppsacl=ppinid+commid["btnSaveClose"]
            browser.delaytime(1)
            browser.findId(self.driver,ppsacl).click()
            browser.accAlert(self.driver,1)

            #---所属部门
            ppdepart=ppinid+browser.xmlRead(dom,"edDepartment",0)
            browser.delaytime(1)
            browser.doubleclick(self.driver,ppdepart)
            ppdepurl="http://dba.wsgjp.com.cn/Beefun/Selector/DepartmentSelector.gspx"
            ppdeid=browser.getalertid(ppdepurl,header3)
            #print ppdeid

            #---关闭
            ppdeclo=ppdeid+commid["selclose"]
            browser.delaytime(1)
            browser.findId(self.driver,ppdeclo).click()
            browser.doubleclick(self.driver,ppdepart)

            #---选中
            ppdesel=ppdeid+commid["selbtn"]
            browser.delaytime(1)
            browser.findId(self.driver,ppdesel).click()

            #--关闭
            ppinfoclo=ppinid+commid["selclose"]
            browser.delaytime(1)
            browser.findId(self.driver,ppinfoclo).click()

            #-关闭
            ppeoexit=ppeoid+commid["selclose"]
            browser.delaytime(1)
            browser.findId(self.driver,ppeoexit).click()
            browser.doubleclick(self.driver,edEType)

            #-选中
            ppeosel=ppeoid+commid["selbtn"]
            browser.findId(self.driver,ppeosel).click()

            #交货日期

            #收货仓库
            edKType=pageid+browser.xmlRead(dom,"edKType",0)
            browser.delaytime(1)
            browser.doubleclick(self.driver,edKType)

            cateurl="http://dba.wsgjp.com.cn/Beefun/Selector/KTypeSelector.gspx?Add=True&HideStoppedItem=True&ShowFreight=false&Bcategory=1&FilterStr="
            cateid=browser.getalertid(cateurl,header3)
            #print cateid

            #-仓库选择框
            #-添加
            cateadd=cateid+commid["btnAdd"]
            browser.findId(self.driver,cateadd).click()
            cateinfourl="http://dba.wsgjp.com.cn/Beefun/BaseInfo/KTypeEdit.gspx?Mode=Add&ParId=0&ParTypeId=00000&type=add&id=2605638079543104740&InfoType=&classpath="
            cateinid=browser.getalertid(cateinfourl,header3)
            browser.exjscommin(self.driver,"确定")
            #print cateinid

            #--仓库信息-信息框
            #--保存并新增
            time.sleep(1)
            cainsaadd=cateinid+commid["btnSaveAdd"]
            browser.delaytime(1)
            browser.findId(self.driver,cainsaadd).click()
            browser.accAlert(self.driver,1)

            #--保存并关闭
            cainsacl=cateinid+commid["btnSaveClose"]
            browser.findId(self.driver,cainsacl).click()
            browser.accAlert(self.driver,1)

            #--关闭
            cainclose=cateinid+commid["selclose"]
            browser.delaytime(1)
            browser.findId(self.driver,cainclose).click()

            #-关闭
            cateclose=cateid+commid["selclose"]
            browser.delaytime(1)
            browser.findId(self.driver,cateclose).click()
            browser.doubleclick(self.driver,edKType)

            #-选中
            catesel=cateid+commid["selbtn"]
            browser.delaytime(1)
            browser.findId(self.driver,catesel).click()

            #摘要
            edSummary=pageid+browser.xmlRead(dom,"edSummary",0)
            browser.findId(self.driver,edSummary).send_keys(u"中文测试饕餮壹贰123！@#￥%……&*（）()； abcButton summary")

            #附加说明
            edComment=pageid+browser.xmlRead(dom,"edComment",0)
            browser.findId(self.driver,edComment).send_keys(u"Button comment中文测试饕餮壹贰123！@#￥%……&*（）()； abc")

            #商品编号
            itemone=commid["basetype"]+pageid+browser.xmlRead(dom,"nitemcode",0)
            browser.findXpath(self.driver,itemone).click()
            itemsel=pageid+commid["itname"]
            browser.doubleclick(self.driver,itemsel)

            itemurl="http://dba.wsgjp.com.cn/Beefun/Selector/PTypeSelector.gspx?Add=True&HideStoppedItem=True&DontClose=True&VchType=7&BTypeId=2605638079543104347&KTypeId=2605638079543104740&MultiSelect=True"
            itemid=browser.getalertid(itemurl,header3)
            #print itemid

            #-库存商品选择框
            #-添加
            itemadd=itemid+commid["btnAdd"]
            browser.findId(self.driver,itemadd).click()

            iteminurl="http://dba.wsgjp.com.cn/Beefun/BaseInfo2/PTypeEdit.gspx?Mode=Add&ParId=0&ParTypeId=00000&type=add&id=869585272784951&InfoType=&classpath="
            itemadid=browser.getalertid(iteminurl,header3)
            #print itemadid
            browser.stockitemselectadd(self.driver,commid,itemadid)

            #-翻页
            browser.pagewhich(self.driver,commid["basetype"],itemid,commid["typenext"],commid["typetopbe"],commid["typebe"],commid["typetopnext"])

            #-关闭
            itaddclo=itemid+commid["selclose"]
            browser.findId(self.driver,itaddclo).click()
            browser.doubleclick(self.driver,itemsel)

            #-选中
            itaddsel=itemid+browser.xmlRead(dom,"btnKeepSelect",0)
            browser.findId(self.driver,itaddsel).click()

            #-选中并关闭
            itaddselclo=itemid+commid["selbtn"]
            browser.findId(self.driver,itaddselclo).click()

            itemgrid=browser.xmlRead(dom,"itemgrid",0)

            #grid
            #单位
            itemunit=commid["basetype"]+pageid+itemgrid+str(18)+"]/div"
            time.sleep(1)
            browser.doubleclick(self.driver,itemunit,1)

            #-选择商品的计量单位
            uniturl="http://dba.wsgjp.com.cn/Beefun/Selector/PTypeUnitSelector.gspx?PTypeId=869585272784951&BTypeId=2605638079543104347&KTypeId=2605638079543104740&prop1=0&prop2=0"
            unittext=browser.requestget(uniturl,header3)
            unitid=browser.getstockid(unittext)

            #-关闭
            unitclose=unitid[:10]+commid["btnexit"]
            #print unitclose
            browser.findId(self.driver,unitclose).click()
            browser.doubleclick(self.driver,itemunit,1)

            #-确定
            browser.findId(self.driver,unitid).click()

            #数量
            itqty=commid["basetype"]+pageid+itemgrid+str(24)+"]"
            browser.findXpath(self.driver,itqty).click()
            qty=browser.xmlRead(dom,"grid_assqty",0)
            browser.doubleclick(self.driver,pageid+qty)

            qtyurl="http://dba.wsgjp.com.cn/Beefun/Bill/PTypeMultiUnitInput.gspx?PTypeId=869585272784951&UCode=1&URate=1&Qty=1"
            qtyid=browser.getalertid(qtyurl,header3)
            #print qtyid

            #-取消
            qtycan=qtyid+commid["btnexit"]
            browser.findId(self.driver,qtycan).click()
            browser.doubleclick(self.driver,pageid+qty)

            #-确定
            qtyok=qtyid+commid["btnOK"]
            #time.sleep(1)
            #print qtyok
            browser.findId(self.driver,qtyok).click()

            #折前单价
            itdpprice=commid["basetype"]+pageid+itemgrid+str(28)+"]"
            browser.delaytime(1)
            browser.findXpath(self.driver,itdpprice).click()
            dpprice=browser.xmlRead(dom,"grid_assdpprice",0)
            browser.doubleclick(self.driver,pageid+dpprice)
            time.sleep(1)

            dppriceurl="http://dba.wsgjp.com.cn/Beefun/Selector/PTypePriceSelector.gspx?PTypeId=869585272784951&UCode=1&KTypeId=2605638079543104740&BTypeId=2605638079543104347"
            dptext=browser.requestget(dppriceurl,header3)
            dpid=browser.getstockid(dptext)
            #print dpid

            #-关闭
            dpcan=dpid[:10]+commid["btnexit"]
            browser.delaytime(1)
            browser.findId(self.driver,dpcan).click()
            browser.doubleclick(self.driver,pageid+dpprice)

            #-确定
            browser.findId(self.driver,dpid).click()

            #录单配置
            billcon=pageid+browser.xmlRead(dom,"btnBillConfig",0)
            browser.delaytime(1)
            browser.findId(self.driver,billcon).click()

            conurl="http://dba.wsgjp.com.cn/Beefun/Bill/BillConfig.gspx"
            condata={"__Params":"{\"vchtype\":7}"}
            context=browser.requestpost(conurl,condata,header4)
            conid=browser.getstockid(context)
            #print conid

            #-退出
            conclose=conid[:10]+commid["btnClose"]
            browser.delaytime(1)
            browser.findId(self.driver,conclose).click()
            browser.findId(self.driver,billcon).click()

            #-保存
            browser.findId(self.driver,conid).click()
            browser.accAlert(self.driver,1)


            #导入商品明细
            importdetail=pageid+browser.xmlRead(dom,"btnImportDetail",0)
            browser.delaytime(1)
            browser.findId(self.driver,importdetail).click()
            importurl="http://dba.wsgjp.com.cn/Beefun/Bill/BillImport/ImportBillDetail.gspx"
            importid=browser.getalertid(importurl,header3)
            #print importid

            #-导入文件
            imfile=importid+commid["button"]+str(1)
            browser.delaytime(1)
            browser.findId(self.driver,imfile).click()
            browser.accAlert(self.driver,1)

            #-取消
            imcan=importid+commid["btnexit"]
            browser.findId(self.driver,imcan).click()



            #打印
            #保存退出
            saclose=pageid+commid["selclose"]
            browser.findId(self.driver,saclose).click()

            #-保存单据
            browser.exjscommin(self.driver,"保存单据")

            #-废弃退出
            browser.findXpath(self.driver,itemone).click()
            browser.doubleclick(self.driver,itemsel)
            browser.exjscommin(self.driver,"选中")
            browser.findId(self.driver,saclose).click()
            browser.exjscommin(self.driver,"废弃退出")

            browser.openModule2(self.driver,modulename,moduledetail)

            #付定金
            payment=pageid+browser.xmlRead(dom,"btnPayment",0)
            browser.findId(self.driver,payment).click()
            browser.delaytime(1)
            browser.accAlert(self.driver,1)

            browser.findXpath(self.driver,itemone).click()
            browser.doubleclick(self.driver,itemsel)
            browser.exjscommin(self.driver,"选中并关闭")

            browser.doubleclick(self.driver,edBType)
            browser.exjscommin(self.driver,"选中")
            browser.doubleclick(self.driver,edKType)
            browser.exjscommin(self.driver,"选中")
            browser.findId(self.driver,payment).click()
            browser.exjscommin(self.driver,"退出")
            browser.exjscommin(self.driver,"存入草稿")
            browser.exjscommin(self.driver,"退出")

            browser.openModule2(self.driver,modulename,moduledetail)



        except:
            print traceback.format_exc()
            filename=browser.xmlRead(comdom,'filename',0)
            browser.delaytime(1)
            browser.getpicture(self.driver,filename+u"进货-新增进货订单.png")



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
