#*-* coding:UTF-8 *-*
from common import loggingClass
import  stockcompareapi
import time
import re
import unittest
import  xml.dom.minidom
import traceback
from common import browserClass
browser=browserClass.browser()

class stockmanageTest(unittest.TestCase):
    u'''进货-进货订单管理'''

    def setUp(self):
        self.driver=browser.startBrowser('chrome')
        browser.set_up(self.driver)
        cookie = [item["name"] + "=" + item["value"] for item in self.driver.get_cookies()]
        #print cookie
        self.cookiestr = ';'.join(item for item in cookie)
        self.header={'cookie':self.cookiestr,"Content-Type": "application/json"}
        browser.delaytime(2)
        self.comdom=xml.dom.minidom.parse(r'C:\workspace\nufeeb.button\data\commonlocation')
        self.dom = xml.dom.minidom.parse(r'C:\workspace\nufeeb.button\stock\stocklocation')

        self.modulename=browser.xmlRead(self.dom,"module",0)
        self.moduledetail=browser.xmlRead(self.dom,'moduledetail',1)

        #页面id
        self.pageurl=browser.xmlRead(self.dom,"manageurl",0)
        self.pageid=browser.getalertid(self.pageurl,self.header)
        pass


    def tearDown(self):
        print "test over"
        self.driver.close()
        pass

    def teststockmanage(self):
        u'''进货-进货订单管理.'''
        browser.openModule2(self.driver,self.modulename,self.moduledetail)
        cookies=browser.cookieSave(self.driver)
        header3={'cookie':cookies,"Content-Type": "application/json"}


        #print self.pageid

        btypeidtext=browser.requestget(self.pageurl,self.header)
        btypeid=re.findall("\"btypeid\":\"(.*?)\",",btypeidtext)
        #print btypeid
        btypeid=btypeid[0]


        #commid,id
        commid=browser.getallcommonid(self.comdom)

        try:
            #刷新
            btnrefresh=commid["basetype"]+self.pageid+browser.xmlRead(self.dom,"btnrefresh",0)
            browser.findXpath(self.driver,btnrefresh).click()



            #修改
            change=self.pageid+browser.xmlRead(self.dom,"btnModify",0)
            browser.findId(self.driver,change).click()
            #browser.openModule2(self.driver,self.modulename,self.moduledetail)
            browser.exjscommin(self.driver,"退出")
            browser.exjscommin(self.driver,"废弃退出")
            change=self.pageid+browser.xmlRead(self.dom,"btnModify",0)
            js="$(\"div[class=GridBodyCellText]:contains('001')\").first().attr(\"id\",\"p1\")"
            browser.delaytime(1)
            browser.excutejs(self.driver,js)
            browser.findId(self.driver,"p1").click()
            browser.findId(self.driver,change).click()
            #browser.openModule2(self.driver,self.modulename,self.moduledetail)
            browser.exjscommin(self.driver,"退出")
            browser.exjscommin(self.driver,"保存单据")

            #审核
            check=self.pageid+browser.xmlRead(self.dom,"check",0)

            checkurl="http://beefun.wsgjp.com/Beefun/Report/OrderAudit.gspx?isshowgrid=false&audittype=1&ctype=0&vchtype=stockorder&btypeid="+btypeid
            checkid=browser.getalertid(checkurl,self.header)
            #print checkid

            #-审核通过
            checkok=checkid+browser.xmlRead(self.dom,"btnAuditPass",0)
            browser.delaytime(1)
            #print checkok

            js="$(\"div[class=GridBodyCellText]:contains('网店客户')\").first().attr(\"id\",\"checkid\")"
            browser.delaytime(1)
            browser.excutejs(self.driver,js)
            browser.findId(self.driver,"checkid").click()
            browser.exjscommin(self.driver,"审核")
            browser.exjscommin(self.driver,"审核通过")

            #-关闭
            checkclose=checkid+commid["btnexit"]
            #print checkclose
            browser.delaytime(1)
            browser.findId(self.driver,check).click()
            browser.findId(self.driver,checkclose).click()
            time.sleep(1)
            browser.findId(self.driver,check).click()

            browser.delaytime(1)
            browser.delaytime(3,self.driver)
            browser.findId(self.driver,checkok).click()


            #执行情况
            exinfo=self.pageid+browser.xmlRead(self.dom,"btnExecInfo",0)
            browser.findId(self.driver,exinfo).click()
            browser.openModule2(self.driver,self.modulename,self.moduledetail)

            #更多
            btnMore=self.pageid+browser.xmlRead(self.dom,"btnMore",0)

            #更多-复制为进货订单
            morecpinstock=commid["basetype"]+self.pageid+browser.xmlRead(self.dom,"btnCopyBuyOrder",0)+browser.xmlRead(self.dom,"moredetail",0)
            for a in range(2):
                #print morecpinstock
                browser.findId(self.driver,btnMore).click()
                browser.findXpath(self.driver,morecpinstock).click()
                browser.accAlert(self.driver,0)
            browser.findId(self.driver,btnMore).click()
            browser.findXpath(self.driver,morecpinstock).click()
            browser.accAlert(self.driver,1)
            time.sleep(1)
            browser.openModule2(self.driver,self.modulename,self.moduledetail)

            #更多-删除

            moredel=commid["basetype"]+self.pageid+browser.xmlRead(self.dom,"btnDel",0)+browser.xmlRead(self.dom,"moredetail",0)
            #print moredel
            browser.findId(self.driver,btnMore).click()
            browser.findXpath(self.driver,moredel).click()
            browser.accAlert(self.driver,0)
            browser.findId(self.driver,btnMore).click()
            browser.findXpath(self.driver,moredel).click()
            browser.accAlert(self.driver,1)
            browser.delaytime(1)

            #更多-复制为销售订单
            morecpsale=commid["basetype"]+self.pageid+browser.xmlRead(self.dom,"btnCopyOrder",0)+browser.xmlRead(self.dom,"moredetail",0)
            #print morecpsale
            browser.findId(self.driver,btnMore).click()
            browser.findXpath(self.driver,morecpsale).click()
            browser.accAlert(self.driver,0)
            browser.findId(self.driver,btnMore).click()
            browser.findXpath(self.driver,morecpsale).click()
            browser.accAlert(self.driver,1)
            time.sleep(1)
            browser.openModule2(self.driver,self.modulename,self.moduledetail)

            #更多-终止并完成
            moreforce=commid["basetype"]+self.pageid+browser.xmlRead(self.dom,"btnForceOver",0)+browser.xmlRead(self.dom,"moredetail",0)
            #print moreforce
            browser.findId(self.driver,btnMore).click()
            browser.findXpath(self.driver,moreforce).click()
            browser.accAlert(self.driver,0)
            browser.findId(self.driver,btnMore).click()
            browser.findXpath(self.driver,moreforce).click()
            browser.accAlert(self.driver,1)
            time.sleep(1)
            browser.openModule2(self.driver,self.modulename,self.moduledetail)



            #更多-订单审核配置
            moreset=commid["basetype"]+self.pageid+browser.xmlRead(self.dom,"btnOrderConfig",0)+browser.xmlRead(self.dom,"moredetail",0)
            #print moreset
            browser.findId(self.driver,btnMore).click()
            browser.findXpath(self.driver,moreset).click()
            jsclose="$(\"button:contains('退出')\").last().click()"
            browser.delaytime(1)
            browser.excutejs(self.driver,jsclose)
            browser.findId(self.driver,btnMore).click()
            browser.findXpath(self.driver,moreset).click()
            jssave="$(\"button:contains('保存')\").click()"
            time.sleep(1)
            browser.excutejs(self.driver,jssave)
            browser.accAlert(self.driver,1)

            itemgrid=browser.xmlRead(self.dom,"itemgrid",0)

            #仓库选择框
            catesel=commid["basetype"]+self.pageid+itemgrid+str(10)+"]"
            browser.findXpath(self.driver,catesel).click()
            browser.doubleclick(self.driver,self.pageid+browser.xmlRead(self.dom,"grid_kfullname",0))

            #-添加,-关闭
            browser.catesel(self.driver)

            #选中
            browser.doubleclick(self.driver,self.pageid+browser.xmlRead(self.dom,"grid_kfullname",0))
            js="$(\"button:contains('选中')\").click()"
            time.sleep(1)
            browser.excutejs(self.driver,js)


            #经手人选择框
            peosel=commid["basetype"]+self.pageid+itemgrid+str(11)+"]"
            browser.delaytime(1)
            browser.findXpath(self.driver,peosel).click()
            browser.doubleclick(self.driver,self.pageid+browser.xmlRead(self.dom,"grid_ename",0))

            #-添加，-关闭
            js="$(\"input[class=ButtonEdit]\").last().attr(\"id\",\"tempid\");"
            browser.catesel(self.driver,js,"tempid")

            #-选中
            browser.findXpath(self.driver,peosel).click()
            browser.doubleclick(self.driver,self.pageid+browser.xmlRead(self.dom,"grid_ename",0))

            js="$(\"button:contains('选中')\").click()"
            time.sleep(1)
            browser.excutejs(self.driver,js)

            #查询条件
            selcon=self.pageid+browser.xmlRead(self.dom,"btnOrderQuery",0)
            browser.findId(self.driver,selcon).click()
            conurl="http://beefun.wsgjp.com/Beefun/Carrier/OrderQueryCondition.gspx"
            conid=browser.getalertid(conurl,header3)
            #print conid

            #-关闭
            conclose=conid+commid["btnexit"]
            browser.delaytime(1)
            browser.findId(self.driver,conclose).click()
            browser.findId(self.driver,selcon).click()

            #-确定
            conok=conid+commid["button"]+str(1)
            browser.findId(self.driver,conok).click()

            #往来单位
            browser.findId(self.driver,selcon).click()
            js="$(\"input[id$=edBType]\").last().attr(\"id\",\"bid\")"
            browser.delaytime(1)
            browser.excutejs(self.driver,js)
            browser.classbtype(self.driver,"bid")
            browser.findId(self.driver,conok).click()

            #经手人
            browser.findId(self.driver,selcon).click()
            js="$(\"input[id$=edEType]\").last().attr(\"id\",\"eid\")"
            browser.delaytime(1)
            browser.excutejs(self.driver,js)
            browser.passpeoplesel(self.driver,"eid")
            browser.findId(self.driver,conok).click()


            #更多-打印
            #moredel=commid["basetype"]+self.pageid+browser.xmlRead(dom,"btnDel",0)+browser.xmlRead(dom,"moredetail",0)
            #退出
            pageexit=self.pageid+commid["selclose"]
            browser.findId(self.driver,pageexit).click()
            browser.openModule2(self.driver,self.modulename,self.moduledetail)

        except:
            print traceback.format_exc()
            filename=browser.xmlRead(self.dom,'filename',0)
            browser.delaytime(1)
            browser.getpicture(self.driver,filename+u"进货-进货订单管理.png")

    def assertskmanagebeforecheck(self):
        u'''进货-进货订单管理-审核之前'''
        try :
            f=open(r'C:\\workspace\\nufeeb.button\\data\\temp','r')
            number=str(f.read())
            f.close()

            self.pageid=self.pageid+"grid_pager1"
            browser.openModule2(self.driver,self.modulename,self.moduledetail)
            #获取页面数据
            url="http://beefun.wsgjp.com/Carpa.Web/Carpa.Web.Script.DataService.ajax/GetPagerData"
            datas={"pagerId":""+self.pageid+"","queryParams":{"vchType":7,"xTypeid":"","isComplete":"1","isAudit":-1,"isExport":"-1","dlytype":-1},"orders":None,"filter":None,"first":0,"count":25}

            cookies=browser.cookieSave(self.driver)
            headers={'cookie':cookies,"Content-Type": "application/json"}
            pageorderdata=browser.requestpost(url,datas,headers,1)
            #print "pageorderdata..................................."
            #print pageorderdata
            self.pageorderdata=browser.datatrunjson2(pageorderdata)
            #print pageorderdata["itemList"]
            pageorder=[]

            if number=='':
                loggingClass.addlogmes("info","stockmanageTest-test_assertskmanagebeforecheck-",u"进货-新增进货订单-保存失败,进货订单管理无数据，随便选一个进行审核")
                for order in self.pageorderdata["itemList"]:
                    if order["summary"]!="":
                        if order["auditover"]=="false":
                                pageorder=order
                                break
                print "pageorder...."
                print pageorder
            else:
                browser.delaytime(1)
                js="$(\"div:contains('"+number+"')\").last().attr(\"id\",\"manid\")"
                browser.delaytime(1)
                browser.excutejs(self.driver,js)
                browser.findId(self.driver,"manid").click()

                #订单头数据
                for order in self.pageorderdata["itemList"]:
                    if order["number"]==number:
                        pageorder=order
                        break
                print "pageorder...."
                print pageorder

                if pageorder=='':
                    loggingClass.addlogmes("info","stockmanageTest-test_assertskmanagebeforecheck-",u"进货-新增进货订单-保存成功,进货订单管理找不到该订单，随便选一个进行审核")
                    for order in self.pageorderdata["itemList"]:
                        if order["summary"]!="":
                            if order["auditover"]=="false":
                                pageorder=order
                                break
                    print "pageorder...."
                    print pageorder

            #商品详情
            #itdatas={"hashdata":{"toqty":0,"untoqty":4,"repairqty":0,"repairtotal":0,"tototal":0,"untototal":65.4346,"isdelivered":0,"checked":0,"vchcode":"154274986485752489","vchtype":7,"date":"\/Date(1482681600000)\/","number":pageorder["number"],"todate":"\/Date(1482681600000)\/","comment":"assert Button comment","summary":"assert Button summary","btypeid":"2605638079543104347","bpartypeid":"00000","etypeid":"2605638088210451192","ktypeid":"2605638079543104740","auditover":False,"ename":"001","dfullname":"","kfullname":"主仓库","bname":"网店客户","artotal":0,"aptotal":316393.41,"r_warnup":0,"orderover1":0,"createtypename":"本地创建","createtype":0,"reccnt":0,"total":68.34,"tptotal":65.43,"dptotal":73.18,"default_audited":0,"default_auditorid":None,"default_audittime":None,"default_auditremark":"","finance_audited":0,"finance_auditorid":0,"finance_audittime":None,"finance_auditremark":"","isexport":0,"earnest":0,"finance_auditorname":"","business_auditorname":"","inputfullname":"xsx","receiverpeople":None,"receivercellphone":None,"receivertelephone":None,"receiverzipcode":None,"province":None,"city":None,"district":None,"receiveraddress":None,"isneedinvoice":None}}
            itdatas={"hashdata":{"toqty":0,"untoqty":0,"repairqty":4,"repairtotal":0,"tototal":pageorder["tototal"],"untototal":pageorder["untototal"],"isdelivered":0,"checked":0,"vchcode":pageorder["vchcode"],"vchtype":7,"date":"\/Date(1482681600000)\/","number":pageorder["number"],"todate":"\/Date(1482681600000)\/","comment":pageorder["comment"],"summary":pageorder["summary"],"btypeid":pageorder["btypeid"],"bpartypeid":"00000","etypeid":pageorder["etypeid"],"ktypeid":pageorder["ktypeid"],"auditover":False,"ename":pageorder["ename"],"dfullname":"","kfullname":pageorder["kfullname"],"bname":pageorder["bname"],"artotal":0,"aptotal":pageorder["tototal"],"r_warnup":0,"orderover1":0,"createtypename":pageorder["createtypename"],"createtype":pageorder["createtype"],"reccnt":0,"total":pageorder["total"],"tptotal":pageorder["tptotal"],"dptotal":pageorder["dptotal"],"default_audited":0,"default_auditorid":None,"default_audittime":None,"default_auditremark":"","finance_audited":0,"finance_auditorid":0,"finance_audittime":None,"finance_auditremark":"","isexport":0,"earnest":0,"finance_auditorname":"","business_auditorname":"","inputfullname":pageorder["inputfullname"],"receiverpeople":None,"receivercellphone":None,"receivertelephone":None,"receiverzipcode":None,"province":None,"city":None,"district":None,"receiveraddress":None,"isneedinvoice":None}}
            iturl="http://beefun.wsgjp.com/Beefun/Beefun.Carrier.OrderManager.ajax/GetDetailsByorderid"
            itemdatas=browser.requestpost(iturl,itdatas,headers,1)
            itemdatas=browser.datatrunjson2(itemdatas)
            print itemdatas
            #print itemdatas[0]["pfullname"]


            #数据库数据
            orderdatas=browser.getmysqldlyndxOrder(number,pageorder["summary"])
            orderitems=browser.getmysqlitems(number,pageorder["summary"])

            print "mysql..."
            print orderdatas
            print orderitems

            #断言数据
            comapi=stockcompareapi.stockcompary()
            caseassert="stockmanageTest-test_assertskmanagebeforecheck-"+str(pageorder['number'])

            #是否审核
            if str(pageorder["auditover"])=="false":
                ischeck=0
            else:
                ischeck=100
            comapi.commonfun(caseassert,ischeck,orderdatas[9],u"进货-进货订单管理-订单头-是否审核和数据库不一致")
            #日期
            comapi.commonfun(caseassert,browser.handlestamp(pageorder["date"]),orderdatas[3],u"进货-进货订单管理-订单头-日期和数据库不一致")
            #订单编号
            comapi.commonfun(caseassert,pageorder["number"],orderdatas[11],u"进货-进货订单管理-订单头-订单编号和数据库不一致")
            #往来单位
            comapi.commonfun(caseassert,pageorder["bname"],orderdatas[0],u"进货-进货订单管理-订单头-往来单位和数据库不一致")
            #仓库名称
            comapi.commonfun(caseassert,pageorder["kfullname"],orderdatas[2],u"进货-进货订单管理-订单头-仓库名称和数据库不一致")
            #经手人
            comapi.commonfun(caseassert,pageorder["ename"],orderdatas[1],u"进货-进货订单管理-订单头-经手人和数据库不一致")
            #交货日期
            comapi.commonfun(caseassert,browser.handlestamp(pageorder["todate"]),orderdatas[6],u"进货-进货订单管理-订单头-交货日期和数据库不一致")

            #税后金额
            comapi.commonfun(caseassert,str("%.4f"%pageorder["total"]),str(orderdatas[12]),u"进货-进货订单管理-订单头-税后金额和数据库不一致")
            #已付订金金额

            #附加说明
            comapi.commonfun(caseassert,pageorder["comment"],str(orderdatas[5]),u"进货-进货订单管理-订单头-附加说明和数据库不一致")



            #是否完成
            comapi.commonfun(caseassert,pageorder["reccnt"],str('0'),u"进货-进货订单管理-订单头-是否完成验证失败")
            #业务审核人
            comapi.commonfun(caseassert,pageorder["business_auditorname"],str(''),u"进货-进货订单管理-订单头-业务审核人验证失败")
            #审核时间
            if pageorder["finance_audittime"]=='false':
                comtime=''
            else:
                comtime=pageorder["finance_audittime"]
            comapi.commonfun(caseassert,comtime,str(''),u"进货-进货订单管理-订单头-审核时间验证失败")
            #审核说明
            comapi.commonfun(caseassert,pageorder["default_auditremark"],str(''),u"进货-进货订单管理-订单头-审核说明验证失败")
            #创建类型
            comapi.commonfun(caseassert,pageorder["createtypename"],str(u'本地创建'),u"进货-进货订单管理-订单头-创建类型验证失败")

            htoqty=0
            huntoqty=0
            htomoney=0
            hunmoney=0
            dpmytotal=0
            mytotal=0
            for itemde in itemdatas:
                flag=0

                for myit in orderitems:
                    if myit[0]==itemde["ptypecode"]:
                        dpmytotal+=myit[7]
                        mytotal+=myit[10]
                        #商品编号
                        #comapi.commonfun(caseassert,itemde["ptypecode"],str(orderdatas[5]),u"进货-进货订单管理-商品明细-商品编号和数据库不一致")

                        #商品名称
                        comapi.commonfun(caseassert,itemde["pfullname"],str(myit[1]),u"进货-进货订单管理-商品明细-商品名称和数据库不一致")

                        #商品简名
                        comapi.commonfun(caseassert,itemde["pname"],str(myit[4]),u"进货-进货订单管理-商品明细-商品简名和数据库不一致")

                        #规格

                        #型号

                        #单位
                        comapi.commonfun(caseassert,itemde["ptypeunit"],str(myit[2]),u"进货-进货订单管理-商品明细-单位和数据库不一致")

                        #商品重量


                        #商品总重量

                        #数量
                        comapi.commonfun(caseassert,str("%.2f"%itemde["qty"]),str("%.2f"%myit[17]),u"进货-进货订单管理-商品明细-数量和数据库不一致")

                        #单价
                        comapi.commonfun(caseassert,itemde["tpprice"],str("%.2f"%myit[9]),u"进货-进货订单管理-商品明细-单价和数据库不一致")

                        #金额
                        comapi.commonfun(caseassert,itemde["tptotal"],str("%.2f"%myit[10]),u"进货-进货订单管理-商品明细-金额和数据库不一致")

                        #状态

                        #备注
                        comapi.commonfun(caseassert,itemde["comment"],str(myit[15]),u"进货-进货订单管理-商品明细-备注金额和数据库不一致")

                        #未完成数量
                        huntoqty+=myit[17]-myit[16]
                        comapi.commonfun(caseassert,itemde["untoqty"],str("%.1f"%(myit[17]-myit[16])),u"进货-进货订单管理-商品明细-未完成数量和数据库不一致")

                        #完成数量
                        htoqty+=myit[16]
                        comapi.commonfun(caseassert,itemde["toqty"],str("%.1f"%myit[16]),u"进货-进货订单管理-商品明细-完成数量和数据库不一致")

                        #补订数量
                        #comapi.commonfun(caseassert,itemde["repairqty"],str(orderdatas[5]),u"进货-进货订单管理-商品明细-商品编号和数据库不一致")

                        #未完成金额
                        hunmoney+=(myit[17]-myit[16])*myit[9]
                        comapi.commonfun(caseassert,"%.2f"%itemde["untototal"],str("%.2f"%((myit[17]-myit[16])*myit[9])),u"进货-进货订单管理-商品明细-未完成金额和数据库不一致")

                        #完成金额
                        htomoney+=myit[16]*myit[9]
                        comapi.commonfun(caseassert,"%.2f"%itemde["tototal"],str("%.2f"%(myit[16]*myit[9])),u"进货-进货订单管理-商品明细-完成金额和数据库不一致")

                        #补订金额
                        #comapi.commonfun(caseassert,itemde["repairtotal"],str(orderdatas[5]),u"进货-进货订单管理-商品明细-商品编号和数据库不一致")

                        flag=1
                        break
                if flag!=1:
                    print u"进货-进货订单管理-数据和页面商品信息不吻合，有遗漏"
                    print u'订单号为:'+itemde[0]
                    break


            #折前金额
            comapi.commonfun(caseassert,"%.2f"%pageorder["dptotal"],str("%.2f"%dpmytotal),u"进货-进货订单管理-订单头-折前金额与商品明细不合")

            #金额
            comapi.commonfun(caseassert,pageorder["tptotal"],str("%.2f"%mytotal),u"进货-进货订单管理-订单头-完成数量与商品明细不合")

            #完成数量
            comapi.commonfun(caseassert,pageorder["toqty"],str("%.1f"%htoqty),u"进货-进货订单管理-订单头-金额与商品明细不合")

            #未完成数量
            comapi.commonfun(caseassert,pageorder["untoqty"],str("%.1f"%huntoqty),u"进货-进货订单管理-订单头-未完成数量与商品明细不合")

            #补订数量
            #comapi.commonfun(caseassert,pageorder["business_auditorname"],str("%.4f"%htoqty),u"进货-进货订单管理-订单头-业务审核人验证失败")

            #未完成金额
            comapi.commonfun(caseassert,"%.4f"%pageorder["untototal"],str("%.4f"%hunmoney),u"进货-进货订单管理-订单头-未完成金额与商品明细不合")

            #完成金额
            comapi.commonfun(caseassert,"%.4f"%pageorder["tototal"],str("%.4f"%htomoney),u"进货-进货订单管理-订单头-完成金额与商品明细不合")

            #补订金额
            #comapi.commonfun(caseassert,pageorder["business_auditorname"],str(orderdatas[5]),u"进货-进货订单管理-订单头-业务审核人验证失败")

            self.success=1

        except:
            print traceback.format_exc()
            self.success=0
            filename=browser.xmlRead(self.comdom,'filename',0)
            browser.delaytime(1)
            browser.getpicture(self.driver,filename+u"断言进货-进货订单管理-审核之前.png")

    def assertskmanageaftercheck(self):
        u'''进货-进货订单管理-审核之后'''
        try:
            if self.success==0:
                loggingClass.addlogmes("info","stockmanageTest-test_assertskmanagebeforecheck-",u"进货-进货订单管理-审核失败，随便选一个已审核的数据")

            else:
                print

        except:
            print traceback.format_exc()
            filename=browser.xmlRead(self.comdom,'filename',0)
            browser.delaytime(1)
            browser.getpicture(self.driver,filename+u"断言进货-进货订单管理-审核之后.png")



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
