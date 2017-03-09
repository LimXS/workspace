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

class itempackagemanTest(unittest.TestCase):
    u'''商品-商品套餐管理'''

    def setUp(self):
        self.driver=browser.startBrowser('chrome')
        browser.set_up(self.driver)
        cookie = [item["name"] + "=" + item["value"] for item in self.driver.get_cookies()]
        #print cookie
        self.cookiestr = ';'.join(item for item in cookie)

        browser.delaytime(2)
        pass


    def tearDown(self):
        print "test over"
        self.driver.close()
        pass



    def testitempackageMan(self):
        u'''商品-商品套餐管理'''
        header={'cookie':self.cookiestr,"Content-Type": "application/json"}
        dom = xml.dom.minidom.parse(r'C:\workspace\proxynufeeb.button\itemmodule\itemlocation')
        modulename=browser.xmlRead(dom,"module",0)
        moduledetail=browser.xmlRead(dom,'moduledetail',2)

        browser.openModule2(self.driver,modulename,moduledetail)
        browser.delaytime(1)
        cookies=browser.cookieSave(self.driver)
        header3={'cookie':cookies,"Content-Type": "application/json"}
        header4={'cookie':cookies,"Content-Type": "application/x-www-form-urlencoded"}

        #页面id
        pageurl=browser.xmlRead(dom,"itempackurl",0)
        pageid=browser.halfid(pageurl,header)
        #print pageid

        #commid
        commid=browser.getcommonid(dom)

        try:
            #复制新增
            js="$(\"button:contains(保存)\").first().click()"
            selone="$(\"input[type=checkbox]\").eq(3).click()"
            cp="$(\"div[class=GridBodyCellText]:contains('tao001')\").attr(\"id\",\"cpid\")"
            browser.delaytime(1)
            browser.excutejs(self.driver,cp)
            browser.findId(self.driver,"cpid").click()
            browser.exjscommin(self.driver,"复制新增")
            js2="var a=$(\"input[id$=edCode]\").val();$(\"input[id$=edCode]\").val(a+'"+str(browser.getrandnumber())+"')"
            browser.delaytime(1)
            browser.excutejs(self.driver,js2)
            browser.exjscommin(self.driver,"保存并继续")
            browser.exjscommin(self.driver,"确定")
            browser.exjscommin(self.driver,"退出")
            browser.exjscommin(self.driver,"复制新增")
            browser.delaytime(1)
            browser.excutejs(self.driver,js2)
            browser.excutejs(self.driver,js)

            browser.excutejs(self.driver,selone)
            browser.exjscommin(self.driver,"删除")
            browser.accAlert(self.driver,1)
            browser.exjscommin(self.driver,"确定")
            browser.delaytime(1)
            browser.excutejs(self.driver,selone)
            browser.exjscommin(self.driver,"删除")
            browser.accAlert(self.driver,1)
            browser.exjscommin(self.driver,"确定")

            #新增
            #print "新增......"
            addpack=pageid+commid["button"]+str(1)
            browser.delaytime(1)
            browser.findId(self.driver,addpack).click()
            createCombo=browser.xmlRead(dom,"createCombo",0)
            combol=browser.xmlRead(dom,"combol",0)
            #手工添加
            addhand=commid["basetype"]+pageid+createCombo+str(0)+combol
            #print addhand
            browser.findXpath(self.driver,addhand).click()
            browser.delaytime(1)

            addhandurl="http://dba.wsgjp.com.cn/Beefun/EShopCombo/EShopComboCreate.gspx"
            ahdata={"__Params":"{\"mode\":\"new\"}"}
            ahidtext=browser.requestpost(addhandurl,ahdata,header4)
            ahid=browser.getdraftalterid(ahidtext,1)
            ahid=ahid[:10]
            #print ahid

            #套餐名称，套餐编码，备注，商品信息
            code=browser.getrandnumber()
            edName=browser.xmlRead(dom,"edName",0)
            browser.findId(self.driver,ahid+edName).send_keys(u"中文测试饕餮壹贰！@#￥%……&*（）；button_test"+str(code))
            edCode=browser.xmlRead(dom,"edCode",0)
            browser.findId(self.driver,ahid+edCode).send_keys("buttontest"+str(code))
            edRemark=browser.xmlRead(dom,"edRemark",0)
            browser.findId(self.driver,ahid+edRemark).send_keys(u"中文测试饕餮壹贰！@#￥%……&*（）；buttontestremain")
            iteminfo=commid["basetype"]+ahid+str(browser.xmlRead(dom,"comcp",0))[:-4]
            browser.delaytime(1)
            #print iteminfo
            browser.findXpath(self.driver,iteminfo).click()
            itname=browser.xmlRead(dom,"itname",0)
            #print ahid+itname
            browser.doubleclick(self.driver,ahid+itname)
            seliturl="http://dba.wsgjp.com.cn/Beefun/EShopProduct/PTypeAndComboSelector.gspx?showSuit=False&MultiSelect=True&ptypeType=0"
            selid=browser.halfid(seliturl,header3)
            selid=selid[:10]
            #print selid

            #-翻页
            browser.delaytime(1)
            browser.pagewhich(self.driver,commid["basetype"],selid,commid["ptnext"],commid["ptbe"],commid["pttopnext"],commid["pttoplast"])

            #-取消
            itcancel=selid+commid["btnexit"]
            browser.findId(self.driver,itcancel).click()
            browser.findXpath(self.driver,iteminfo).click()
            browser.doubleclick(self.driver,ahid+itname)
            browser.delaytime(1)

            #-添加
            itadd=selid+commid["btnAdd"]
            #print itadd
            browser.findId(self.driver,itadd).click()
            itaddurl="http://dba.wsgjp.com.cn/Beefun/BaseInfo2/PTypeEdit.gspx?Mode=Add&ParTypeId=00000&type=add"
            alitaddid=browser.getalertid(itaddurl,header3)
            #print alitaddid
            #--售价管理
            salemoman=commid["basetype"]+alitaddid+"c2"+commid["addwhich"]
            browser.findXpath(self.driver,salemoman).click()
            #商品图片管理
            picman=commid["basetype"]+alitaddid+"c3"+commid["addwhich"]
            browser.findXpath(self.driver,picman).click()
            #--基本信息
            itbainfo=commid["basetype"]+alitaddid+"c1"+commid["addwhich"]
            browser.findXpath(self.driver,itbainfo).click()


            #--商品名称
            #browser.findId(self.driver,alitaddid+commid["edFullName"]).send_keys("test")
            #--保存并关闭
            browser.findId(self.driver,alitaddid+commid["btnSaveClose"]).click()

            browser.accAlert(self.driver,1)
            #--保存并新增
            browser.findId(self.driver,alitaddid+commid["btnSaveAdd"]).click()
            browser.accAlert(self.driver,1)
            #--关闭
            browser.findId(self.driver,alitaddid+commid["selclose"]).click()

            #-确定
            itcom=selid+commid["btnok"]
            browser.findId(self.driver,itcom).click()

            #-选择关闭
            itselclose=browser.xmlRead(dom,"itbtnseandclo",0)
            browser.findId(self.driver,selid+itselclose).click()
            browser.delaytime(1)


            #保存并继续
            ahsacon=ahid+commid["btnSaveContinue"]
            browser.findId(self.driver,ahsacon).click()
            browser.delaytime(3,self.driver)
            browser.exjscommin(self.driver,"确定")

            #退出
            browser.exjscommin(self.driver,"退出")

            #保存
            browser.delaytime(1)
            browser.findId(self.driver,addpack).click()
            browser.delaytime(1,self.driver)
            browser.findXpath(self.driver,addhand).click()
            browser.delaytime(3,self.driver)

            ahsave=ahid+commid["btnSave"]
            browser.findId(self.driver,ahsave).click()
            browser.exjscommin(self.driver,"确定")
            browser.exjscommin(self.driver,"退出")


            #导入套餐
            addimport=commid["basetype"]+pageid+createCombo+str(1)+combol
            browser.findId(self.driver,addpack).click()
            browser.findXpath(self.driver,addimport).click()
            importurl="http://dba.wsgjp.com.cn/Beefun/IniPeriod/ImportCombo.gspx"
            importtext=browser.requestget(importurl,header3)
            importid=browser.getlableid(importtext)
            importid=importid[:10]
            #print importid

            #-导入
            browser.delaytime(1)
            BtnImport=browser.xmlRead(dom,"BtnImport",0)
            importcon=importid+BtnImport
            browser.delaytime(1)
            browser.findId(self.driver,importcon).click()
            browser.exjscommin(self.driver,"确定")

            #-关闭
            browser.exjscommin(self.driver,"关闭")


            #删除
            browser.delaytime(1)
            selcon=commid["basetype"]+pageid+browser.xmlRead(dom,"selitem",0)
            browser.findXpath(self.driver,selcon).click()
            browser.delaytime(1)
            deltcon=pageid+commid["button"]+str(4)
            browser.findId(self.driver,deltcon).click()
            browser.accAlert(self.driver,0)
            browser.findId(self.driver,deltcon).click()
            browser.accAlert(self.driver,1)
            browser.delaytime(1)
            js="$(\"button:contains('确定')\").click()"
            browser.delaytime(1)
            self.driver.execute_script(js)

            #编辑
            editcon=pageid+commid["button"]+str(2)
            browser.findId(self.driver,editcon).click()
            browser.delaytime(1)
            browser.delaytime(3,self.driver)

            #-保存
            browser.exjscommin(self.driver,"保存",1)
            #-退出
            browser.findId(self.driver,editcon).click()
            browser.delaytime(2,self.driver)
            browser.exjscommin(self.driver,"退出")

            #批量编辑
            browser.delaytime(1)
            browser.findXpath(self.driver,selcon).click()
            browser.delaytime(1)
            editscon=pageid+commid["button"]+str(5)
            browser.findId(self.driver,editscon).click()
            quickEditMenu=browser.xmlRead(dom,"quickEditMenu",0)

            #启用停用
            openstop=commid["basetype"]+pageid+quickEditMenu+str(0)+combol
            #print openstop
            browser.delaytime(1)
            browser.findXpath(self.driver,openstop).click()

            #-关闭
            browser.exjscommin(self.driver,"关闭")
            #-确认
            browser.findId(self.driver,editscon).click()
            browser.findXpath(self.driver,openstop).click()
            browser.exjscommin(self.driver,"确认")


            #修改同步库存
            browser.delaytime(1)
            #print selcon
            browser.findXpath(self.driver,selcon).click()
            browser.delaytime(1)
            browser.findId(self.driver,editscon).click()
            changestock=commid["basetype"]+pageid+quickEditMenu+str(1)+combol
            browser.findXpath(self.driver,changestock).click()
            browser.delaytime(1)

            #-关闭
            browser.exjscommin(self.driver,"关闭")

            #-确认
            browser.findId(self.driver,editscon).click()
            browser.findXpath(self.driver,changestock).click()
            browser.delaytime(1)
            browser.exjscommin(self.driver,"确认")

            #修改套餐编码
            browser.delaytime(1)
            browser.findXpath(self.driver,selcon).click()
            browser.delaytime(1)
            browser.findId(self.driver,editscon).click()
            changecode=commid["basetype"]+pageid+quickEditMenu+str(2)+combol
            browser.findXpath(self.driver,changecode).click()
            browser.delaytime(1)

            #-取消
            browser.exjscommin(self.driver,"取消")


            #-确认
            browser.findId(self.driver,editscon).click()
            browser.findXpath(self.driver,changecode).click()
            browser.exjscommin(self.driver,"确认")


            #修改套餐名称
            browser.delaytime(1)
            browser.findXpath(self.driver,selcon).click()
            browser.delaytime(1)
            browser.findId(self.driver,editscon).click()
            changename=commid["basetype"]+pageid+quickEditMenu+str(3)+combol
            browser.findXpath(self.driver,changename).click()

            #-取消
            browser.exjscommin(self.driver,"取消")

            #-确认
            browser.findId(self.driver,editscon).click()
            browser.findXpath(self.driver,changename).click()
            browser.delaytime(1)
            browser.exjscommin(self.driver,"确认")


            #修改打印配置
            browser.delaytime(1)
            browser.findXpath(self.driver,selcon).click()
            browser.delaytime(1)
            browser.findId(self.driver,editscon).click()
            changeprint=commid["basetype"]+pageid+quickEditMenu+str(4)+combol
            browser.findXpath(self.driver,changeprint).click()

            #-关闭
            browser.exjscommin(self.driver,"关闭")

            #-确认
            browser.findId(self.driver,editscon).click()
            browser.findXpath(self.driver,changeprint).click()
            browser.exjscommin(self.driver,"确认")


            #修改套餐明细
            browser.delaytime(1)
            browser.findXpath(self.driver,selcon).click()
            browser.delaytime(1)
            browser.findId(self.driver,editscon).click()
            changedetail=commid["basetype"]+pageid+quickEditMenu+str(5)+combol
            browser.findXpath(self.driver,changedetail).click()

            js="$(\"input[id$=grid_grid]\").attr('local',$(\"input[id$=grid_grid]\").attr('id'));$(\"input[id$=grid_grid]\").attr('id','itemid');"
            browser.delaytime(1)
            browser.excutejs(self.driver,js)
            chdetailid=browser.findId(self.driver,"itemid").get_attribute("local")
            chdetailid=chdetailid[:10]

            chcondeit="itemid"
            browser.delaytime(2)
            browser.doubleclick(self.driver,chcondeit)

            #--本地商品SKU列表，取消
            browser.exjscommin(self.driver,"取消")
            browser.doubleclick(self.driver,chcondeit)

            #--本地商品SKU列表，添加
            browser.exjscommin(self.driver,"添加")
            browser.skupagesalman(self.driver)

            #---保存并关闭
            browser.exjscommin(self.driver,"保存并关闭")
            browser.accAlert(self.driver,1)
            #---保存并新增
            browser.exjscommin(self.driver,"保存并新增")
            browser.accAlert(self.driver,1)
            #---关闭
            browser.exjscommin(self.driver,"关闭")

            #--本地商品SKU列表，搜索
            js="$(\"div[id$=btnFilter]\").click()"
            browser.delaytime(1)
            browser.excutejs(self.driver,js)
            #--本地商品SKU列表，确定
            browser.exjscommin(self.driver,"确定")


            #--本地商品SKU列表，选中关闭
            itemgrid=commid["basetype"]+chdetailid+browser.xmlRead(dom,"editdetail",0)
            browser.findXpath(self.driver,itemgrid).click()
            browser.delaytime(1)
            browser.doubleclick(self.driver,chcondeit)
            browser.delaytime(1)
            browser.exjscommin(self.driver,"取消")

            #--本地商品SKU列表，新增套餐明细
            addcomgrid=commid["basetype"]+chdetailid+browser.xmlRead(dom,"editaddcon",0)
            browser.delaytime(1)
            browser.findXpath(self.driver,addcomgrid).click()
            browser.delaytime(1)
            addconedit=chdetailid+browser.xmlRead(dom,"gridaddptyc",0)
            browser.delaytime(1)
            browser.doubleclick(self.driver,addconedit)
            browser.delaytime(1)

            #---翻页
            browser.pagechoice(self.driver,2)

            #---关闭
            browser.exjscommin(self.driver,"关闭")

            #-取消
            browser.exjscommin(self.driver,"取消")

            #查询
            pagesel=pageid+commid["button"]+str(6)
            browser.findId(self.driver,pagesel).click()

            #-保存
            browser.delaytime(2)
            browser.findXpath(self.driver,selcon).click()
            browser.delaytime(1)
            browser.findId(self.driver,editscon).click()
            browser.findXpath(self.driver,changedetail).click()
            chdetailsave=chdetailid+commid["button"]+str(1)
            browser.delaytime(1)
            browser.findId(self.driver,chdetailsave).click()
            browser.delaytime(1)
            browser.buttonclick(self.driver)


            browser.openModule2(self.driver,modulename,moduledetail)
            browser.findId(self.driver,pagesel).click()


        except:
            print traceback.format_exc()
            filename=browser.xmlRead(dom,'filename',0)
            browser.delaytime(1)
            browser.getpicture(self.driver,filename+u"商品-商品套餐管理.png")



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
