#*-* coding:UTF-8 *-*
'''
@author: xsx
'''
from selenium import webdriver
import time
import traceback
from baseClass import base
import requests
import json
import  re
class browser(base):

    def __init__(self):
        '''
        Constructor
        '''
        #base.__init__(self)

        pass
    
    #启动浏览器
    def startBrowser(self,browserType):
        try:
            if browserType.upper()=='CHROME':
                options = webdriver.ChromeOptions()
                options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
                driver=webdriver.Chrome(chrome_options=options)
            elif browserType.upper()=='IE':
                driver=webdriver.Ie()
            elif browserType.upper()=='FIREFOX' or browserType.upper()=='FF':
                driver=webdriver.Firefox()
            else:
                driver=u"无此浏览器类型"
            return driver
        except:
            print(u'启动浏览器失败')

        
        
    #判断元素是否存在
    def elementisexist(self,driver,element):   
        try:
            try:
                #d=baseClass.BaseClass()
                driver.implicitly_wait(10)
                base.findXpath(self,driver,element)
                status=True
            except:
                status=False
            return status
        except:
            print(u"判断元素是否存在失败")
            print(traceback.format_exc())
            
            

    
    def openModule2(self,driver,module,modulename):
        driver.implicitly_wait(15)
        base.findXpath(self,driver,module).click()
        driver.implicitly_wait(10)
        base.findXpath(self,driver,modulename).click()

    
    
    def openModule3(self,driver,module,modulename,moduledetail):

        driver.implicitly_wait(15)
        self.delaytime(1)
        base.findXpath(self,driver,module).click()
        driver.implicitly_wait(15)
        self.delaytime(1)
        base.findXpath(self,driver,modulename).click()
        driver.implicitly_wait(15)
        self.delaytime(1)
        base.findXpath(self,driver,moduledetail).click()

    
    def openModule4(self,driver,module,modulename,moduledetail,modulenade):
        base.findXpath(self,driver,module).click()
        base.findXpath(self,driver,modulename).click()
        self.delaytime(2)
        base.findXpath(self,driver,moduledetail).click()
        base.findXpath(self,driver,modulenade).click()


    #登录毕方
    def loginUser(self,driver,name,user,pwd,login,logname,username,password):

        self.findId(driver,name).clear()
        self.findId(driver,name).send_keys(logname)
        self.findId(driver,user).clear()
        self.findId(driver,user).send_keys(username)
        self.findId(driver,pwd).clear()
        self.findId(driver,pwd).send_keys(password)
        self.findId(driver,user).click()

        self.findId(driver,login).click()
        self.delaytime(2)
 
        return driver

    
    #进行授权
    def acccomfirm(self,driver,loginname,password,loginbtn,acc,accid,accpwd):
        try:
            base.findId(self,driver, loginname).clear()
            base.findId(self,driver, loginname).send_keys(accid)
            base.findId(self,driver, password).clear()
            base.findId(self,driver, password).send_keys(accpwd)
            base.findId(self,driver, loginbtn).click()
            #self.delaytime(2)
            base.findXpath(self,driver,acc).click()
            self.delaytime(2)
        except:
            print(u"授权失败")
            print(traceback.format_exc())
            
 

    #获取动态元素
    def getdtnamicElement(self,driver,str1,str2,btn,flag,begin,end):
        try:
            for a in range(begin,end):                      
                base.findXpath(self,driver,btn).click()
                #driver.find_element_by_xpath("html/body/table[3]/tbody/tr[2]/td[4]/table/tbody/tr/td[2]/div/div[2]/div[2]/div/table[2]/tbody/tr[2]/td[2]/table/tbody/tr/td[2]/div/table/tbody/tr[2]/td[2]/table/tbody/tr[1]/td[2]/table/tbody/tr/td[2]/div/div").click()
                xpath=str1+str(a)+str2
                self.elementisexist(driver,xpath)
                print xpath
                if self.elementisexist(driver,xpath)==True:
                    if base.findXpath(self,driver,xpath).text==str(flag):
                        print base.findXpath(self,driver,xpath).text
                        base.findXpath(self,driver,xpath).click()
                        self.delaytime(2)
                        break
            return a
        except:
            print(u"选择获取动态元素失败")
            print(traceback.format_exc())
    
    
       
    
    #获取当前数据一共有几列        
    def getlines(self,driver,str1,str2):  
        try:
            for n in range(1,20):
                orderid=str1+str(n)+str2
                if self.elementisexist(driver,orderid) ==False:
                    break
            print "all lines:"+str(n)
            return n     
        except:
            print(u"选择行数失败")
            print(traceback.format_exc())
            
            
    def set_up(self,driver,*c):
        #url="http://beefun.wsgjp.com/"
        if len(c)!=0:
            url=c[0]
        else:
            url="http://beefun.wsgjp.com/"
        driver.get(url)
        driver.maximize_window()
        driver.implicitly_wait(15)
        
        name="$1b8bb415$corpName"
        user="$1b8bb415$userName"
        pwd="$1b8bb415$pwdEdit"
        login="$1b8bb415$btnLogin"
        loginname="xsx123456"
        username="xsx"
        password="grasp147+"
        self.loginUser(driver,name ,user,pwd,login,loginname,username,password)
        self.delaytime(3)
        self.exjscommin(driver,"关闭")
        self.exjscommin(driver,"确定")

    #单据中心
    def notecentel(self,header):
        url="http://beefun.wsgjp.com.cn/Carpa.Web/Carpa.Web.Script.DataService.ajax/GetPagerData"
        #header={'cookie':self.cookiestr,"Content-Type": "application/json"}
        data={"pagerId":"$c3e1bf43$grid_pager1","queryParams":None,"orders":None,"filter":None,"first":0,"count":100000}
        page=requests.post(url,headers=header,data=json.dumps(data))
        #print page.text
        page=page.text
        page=page.replace("false","\"False\"")
        #print page
        #放字典，每一条一个位置
        pagedic=json.loads(page)
        #print pagedic
        #print pagedic["Message"]
        return  pagedic

    #报表提取页面
    def reportgetdata(self,data):
        #print "page.................................."
        #print data.text
        page=re.findall("rows\":\[(.*?)\],\"fieldSizes",data.text)
        #print page
        page=page[0].replace("\"","")
        pagelist=re.findall("\[(.*?)\]",page)

        return pagelist

    def reportgetdata2(self,data):
        #print "page.................................."
        #print data.text
        page=re.findall("rows\":\[(.*?)\],\"fieldTypes",data.text)
        #print page
        page=page[0].replace("\"","")
        pagelist=re.findall("\[(.*?)\]",page)

        return pagelist

    #原始单据头
    def getnotehead(self,data):
        reheader=re.findall("brandname\":null\}\],\"type\"(.*?)fc_total",data.text)
        reheader=reheader[0].replace("\"","")
        reheader=re.findall(":(.*?),",reheader)
        return reheader

    def getnotefoot(self,data):
        reheader=re.findall("dataBind(.*?)\"details\":",data.text)
        reheader=reheader[0].replace("\"","")
        refoot=re.findall(":(.*?),",reheader)
        return refoot


    def getnotehead2(self,data):
        reheader=re.findall("\}\],\"type\"(.*?)fc_total",data.text)
        reheader=reheader[0].replace("\"","")
        reheader=re.findall(":(.*?),",reheader)
        return reheader

    #报损单原始单据头
    def getfewernoethead(self,ornote):
        fewnoteheader=re.findall("dataBind\(\'\{\"(.*?)\"details",ornote.text)
        #print fewnoteheader
        fewnoteheader=fewnoteheader[0].replace("\"","")
        fewheader=re.findall(":(.*?),",fewnoteheader)
        return  fewheader


    #获得报表页面id
    def getpageid(self,data,*c):
        if len(c)>0:
            id=re.findall("PagerBottom\" id=\"(.*?)\"",data)
            id=id[0]
        else:
            id=re.findall("PagerBottom\" id=\"(.*?)\"",data.text)
            id=id[0]
        return id

    #报表页面统计数据
    def reportsumdata(self,id,header):
        reurlsum="http://beefun.wsgjp.com/Carpa.Web/Carpa.Web.Script.DataService.ajax/GetPagerSummary"
        resumda={"pagerId":id}
        resumdata=requests.post(url=reurlsum,data=json.dumps(resumda),headers=header)
        data=json.loads(resumdata.text)
        return data

    #调拨单原始单据详细数据入库
    def dbnotedatain(self,data):
        incatlis=re.findall("indetails\":\[(.*?)outdetails",data.text)
        #print incatlis
        #print len(incatlis)
        inlisdata=re.findall("outposition(.*?)brandname",incatlis[0])

        return inlisdata

    #调拨单原始单据详细数据出库
    def dbnotedataout(self,data):
        outcatlis=re.findall("outdetails\":\[(.*?)\"fc_total\"",data.text)
        #print outcatlis
        #print len(outcatlis)
        outlisdata=re.findall("outposition(.*?)brandname",outcatlis[0])
        #print outlisdata
        #print len(outlisdata)
        return outlisdata

    #调拨单原始单据详细数据
    def dbnotedetail(self,data):

        outlisdata=data.replace("\"","")
        #print inlisdata
        oroutdata=re.findall(":(.*?),",outlisdata)
        #print oroutdata
        #print len(oroutdata)
        return oroutdata

    #替换false,true,newdate并转json
    def datatrunjson(self,data):
        dicmanbe=data.text.replace("isnullflag","ifflag")
        dicmanbe=dicmanbe.replace("false","\"false\"")
        dicmanbe=dicmanbe.replace("true","\"false\"")
        dicmanbe=dicmanbe.replace("null","\"false\"")
        dicmanbe=dicmanbe.replace("new Date(","\"")
        dicmanbe=dicmanbe.replace("),","\",")
        #print "dicmanbe.................."
        #print dicmanbe
        manlisdic=json.loads(dicmanbe)
        return manlisdic

    def datatrunjson2(self,data):
        dicmanbe=data.replace("false","\"false\"")
        dicmanbe=dicmanbe.replace("true","\"true\"")
        dicmanbe=dicmanbe.replace("null","\"false\"")
        dicmanbe=dicmanbe.replace("new Date(","\"")
        dicmanbe=dicmanbe.replace(")","\"")
        #print dicmanbe
        manlisdic=json.loads(dicmanbe)
        return manlisdic

    #提取页面
    def getdetaildata(self,data):
        detail=re.findall("(.*?),",data)
        return detail

    #总条数
    def totallist(self,data):
        totlist=re.findall("itemCount\":(.*?),",data.text)
        return totlist[0]

    #销售订单原始单据
    def salenotedata(self,data):
        ornotelists=re.findall("details\":(.*?)\"draft\"",data.text)
        #print ornotelists[0]
        ornotedata=re.findall("(?<=vchcode).*?(?=vchcode)",ornotelists[0]+",vchcode")
        return ornotedata


    def setheader(self,driver,module,modulename,moduledetail):
        try:
            base.findXpath(self,driver,module).click()
            base.findXpath(self,driver,modulename).click()
            base.findXpath(self,driver,moduledetail).click()
        except :
            print(u"setheader失败")
            print(traceback.format_exc())


    #销售订单原始单据
    def salenoteoutdata(self,data):
        ornotelists=re.findall("details\":(.*?)\}\],\"type\"",data.text)
        #print ornotelists[0]
        ornotedata=re.findall("(?<=promovchcode).*?(?=promovchcode)",ornotelists[0]+",promovchcode")
        return ornotedata

    #销售换货单原始单据详细数据入库
    def saleexnotedatain(self,data):
        incatlis=re.findall("indetails\":\[(.*?)outdetails",data.text)
        #print incatlis
        #print len(incatlis)
        inlisdata=re.findall("promovchcode(.*?)brandname",incatlis[0])

        return inlisdata

    #销售换货单原始单据详细数据出库
    def saleexnotedataout(self,data):
        outcatlis=re.findall("outdetails\":\[(.*?)\"fc_total\"",data.text)
        #print outcatlis
        #print len(outcatlis)
        outlisdata=re.findall("promovchcode(.*?)brandname",outcatlis[0])
        #print outlisdata
        #print len(outlisdata)
        return outlisdata

    #库存状况
    def catestatus(self,header,flag):
        urlid="http://beefun.wsgjp.com/Beefun/Report/StockStateReportNew.gspx"
        idtext=requests.get(url=urlid,headers=header)
        id=self.getpageid(idtext)
        #明细
        urllist="http://beefun.wsgjp.com/Carpa.Web/Carpa.Web.Script.DataService.ajax/GetPagerData"
        #datalists={"pagerId":id,"queryParams":{"level":1,"isHavesons":True,"isReflash":True,"ktypeids":None,"isShowSaleNumber":False,"isQuery":False,"zeroshowtype":"0","isshowstop":False,"filtermode":"quickquery","filtertext":""},"orders":None,"filter":None,"first":0,"count":10000}
        #主仓库id
        datalist2={"pagerId":id,"queryParams":{"level":1,"isHavesons":True,"isReflash":True,"ktypeids":"2605638079543104740","isShowSaleNumber":False,"isQuery":False,"zeroshowtype":"0","isshowstop":False,"filtermode":"quickquery","filtertext":""},"orders":None,"filter":None,"first":0,"count":100000}
        #在途仓库
        datalist3={"pagerId":id,"queryParams":{"level":1,"isHavesons":True,"isReflash":True,"ktypeids":"2605638079543104822","isShowSaleNumber":False,"isQuery":False,"zeroshowtype":"0","isshowstop":False,"filtermode":"quickquery","filtertext":""},"orders":None,"filter":None,"first":0,"count":100000}
        if flag==0:
            datalists=datalist2
        else:
            datalists=datalist3
        pagetext=requests.post(url=urllist,data=json.dumps(datalists),headers=header)

        pagelists=self.datatrunjson(pagetext)

        #sum
        urlsum="http://beefun.wsgjp.com/Carpa.Web/Carpa.Web.Script.DataService.ajax/GetPagerSummary"
        sumdata={"pagerId":id}
        sumtext=requests.post(url=urlsum,data=json.dumps(sumdata),headers=header)
        sumlist=self.datatrunjson(sumtext)

        a=[]
        a.append(pagelists)
        a.append(sumlist)
        return a

    #科目详情
    def subjectdetail(self,vcode,header):
        #销售收入[3]、销售成本[2]、应交税金[4]、应付款合计[5]
        saledataurl="http://beefun.wsgjp.com/Beefun/Beefun.Bill.SaleBackBill.ajax/LoadDlyaString"
        saledata={"vchcode":vcode}
        saletext=requests.post(url=saledataurl,data=json.dumps(saledata),headers=header)
        saletext=saletext.text.replace(u"：",":")
        saletext=saletext.replace("\"","\\r")
        #print "saletext........."
        #print saletext
        sale=re.findall(":(.*?)\\\\r",saletext)
        return sale


    #科目详情
    def subjectdetail2(self,url,vcode,header):
        #销售收入[3]、销售成本[2]、应交税金[4]、应付款合计[5]
        saledata={"vchcode":vcode}
        saletext=requests.post(url=url,data=json.dumps(saledata),headers=header)
        saletext=saletext.text.replace(u"：",":")
        saletext=saletext.replace("\"","\\r")
        #print "saletext........."
        #print saletext
        sale=re.findall(":(.*?)\\\\r",saletext)
        return sale

    def pageidsum(self,urlid,header):
        urlidtext=requests.get(url=urlid,headers=header)
        #print urlidtext.text
        id=self.getpageid(urlidtext)

        #detail
        #urldetail="http://beefun.wsgjp.com/Carpa.Web/Carpa.Web.Script.DataService.ajax/GetPagerData"

        #sum
        #print id
        urlsum2="http://beefun.wsgjp.com/Carpa.Web/Carpa.Web.Script.DataService.ajax/GetPagerSummary"
        sumdata2={"pagerId":id}
        sumtext2=requests.post(url=urlsum2,data=json.dumps(sumdata2),headers=header)
        #print sumtext2.text
        sumdic2=self.datatrunjson(sumtext2)

        a=[]
        a.append(id)
        a.append(sumdic2)
        return a

    def pagedetail(self,urlid,data,header,*c):
        if len(c)==0:
            pagetext=requests.post(url=urlid,data=json.dumps(data),headers=header)
            pagelists=self.datatrunjson(pagetext)
        else:
            pagetext=requests.post(url=urlid,data=data,headers=header)
            pagelists=pagetext.text
        return pagelists

    #js
    def exjsgettext(self,driver,xid,type1,type2):
        self.delaytime(2)
        js="var code=document.getElementById('"+xid+"').value;"+xid+".setAttribute('value',code);"
        driver.execute_script(js)
        text=self.findId(driver,xid).get_attribute("value")
        #print id
        self.handleFile(driver,r'C:\workspace\moc.pjgsw.nufeeb\src\salecreate\lssaledata',type1,0,text)
        self.handleFile(driver,r'C:\workspace\moc.pjgsw.nufeeb\src\salecreate\lssaledata',type2,0,'\n')

    #写入
    def writebyattr(self,driver,xid,attr,type1,type2,xpath):
        if attr!="":
            text=self.findId(driver,xid).get_attribute(attr)
        else:
            if xpath=="":
               text=self.findId(driver,xid).text
            else:
                text=self.findXpath(driver,xid).text
        #print id
        self.handleFile(driver,r'C:\workspace\moc.pjgsw.nufeeb\src\salecreate\lssaledata',type1,0,text)
        self.handleFile(driver,r'C:\workspace\moc.pjgsw.nufeeb\src\salecreate\lssaledata',type2,0,'\n')

    #js获取数据

    def jsgettext(self,driver,xid):
        self.delaytime(2)
        js="var code=document.getElementById('"+xid+"').value;"+xid+".setAttribute('value',code);"
        driver.execute_script(js)
        text=self.findId(driver,xid).get_attribute("value")
        return text

    #页面统计数据
    def funpagesum(self,pageid,header):
        urlsum="http://beefun.wsgjp.com/Carpa.Web/Carpa.Web.Script.DataService.ajax/GetPagerSummary"
        sumdata={"pagerId":pageid}
        sumtext=requests.post(url=urlsum,data=json.dumps(sumdata),headers=header)
        sumdata=json.loads(sumtext.text)
        return sumdata

    def vipinfo(self,header):
        #pageid
        urlid="http://beefun.wsgjp.com/Beefun/VipMember/VipMemberList.gspx"
        urltextid=requests.get(url=urlid,headers=header)
        pageid=self.getpageid(urltextid)
        #detail
        urldetail="http://beefun.wsgjp.com/Carpa.Web/Carpa.Web.Script.DataService.ajax/GetPagerData"
        datade={"pagerId":pageid,"queryParams":None,"orders":None,"filter":None,"first":0,"count":100000}
        detailtext=requests.post(url=urldetail,data=json.dumps(datade),headers=header)
        detail=self.datatrunjson(detailtext)
        return  detail

    def reportdetail(self,data,header):
        url="http://beefun.wsgjp.com/Carpa.Web/Carpa.Web.Script.DataService.ajax/GetPagerData"
        detail=self.pagedetail(url,data,header)
        return  detail

    def halfid(self,url,header):
        idtext=self.requestget(url,header)
        #print idtext
        pageid=self.getpageid(idtext,1)
        pageid=str(pageid[:-11])
        return pageid

    def getdraftalterid(self,data,*c):
        if len(c)>0:
            id=re.findall("Edit\" id=\"(.*?)\"",data)
            id=id[0]
        else:
            id=re.findall("Edit\" id=\"(.*?)\"",data)
            id=id[0][:-8]
        return str(id)

    def getnotedraft(self,data,):
        id=re.findall("Grid\" id=\"(.*?)\"",data)
        id=id[0][:-4]
        return str(id)

    def getstockid(self,data):
        id=re.findall("Button\" id=\"(.*?)\"",data)
        id=id[0]
        return str(id)

    def getlableid(self,data):
        id=re.findall("Label\" id=\"(.*?)\"",data)
        id=id[0]
        return str(id)

    def getpicture(self,driver,filename):
        pic=driver.get_screenshot_as_file(filename)
        self.delaytime(1)
        return pic

    #上一页，下一页，第一页，最后一页
    def pagewhich(self,driver,basetype,typeid,pnext,topebefore,before,topnext):
        #下一页
        typenext=basetype+typeid+pnext
        #print typenext
        self.findXpath(driver,typenext).click()
        #第一页
        typetopbe=basetype+typeid+topebefore
        self.findXpath(driver,typetopbe).click()
        #上一页
        typebe=basetype+typeid+before
        self.findXpath(driver,typebe).click()
        #最后一页
        typetopnext=basetype+typeid+topnext
        self.findXpath(driver,typetopnext).click()

    #弹出框id
    def getalertid(self,url,header,*c):
        text=self.requestget(url,header)
        id=self.getdraftalterid(text,1)
        if len(c)==0:
            id=id[:10]
        return id

    #common id
    def getcommonid(self,dom):
        button=self.xmlRead(dom,"button",0)
        basetype=self.xmlRead(dom,"basetype",0)
        refresh=self.xmlRead(dom,"refresh",0)
        btnexit=self.xmlRead(dom,"btnexit",0)
        selok=self.xmlRead(dom,"selok",0)
        selbtn=self.xmlRead(dom,"selbtn",0)
        selclose=self.xmlRead(dom,"selclose",0)
        btnSure=self.xmlRead(dom,"btnSure",0)
        btnok=self.xmlRead(dom,'btnok',0)
        btnClose=self.xmlRead(dom,'btnClose',0)
        CancelBtn=self.xmlRead(dom,'CancelBtn',0)
        btnSave=self.xmlRead(dom,'btnSave',0)
        btnSaveContinue=self.xmlRead(dom,'btnSaveContinue',0)
        btnSaveAdd=self.xmlRead(dom,'btnSaveAdd',0)
        btnSaveClose=self.xmlRead(dom,'btnSaveClose',0)
        edFullName=self.xmlRead(dom,'edFullName',0)
        btnFilter=self.xmlRead(dom,'btnFilter',0)
        pnext=self.xmlRead(dom,'typenext',0)
        topnext=self.xmlRead(dom,'typetopnext',0)
        before=self.xmlRead(dom,'typebe',0)
        topebefore=self.xmlRead(dom,'typetopbe',0)

        ptnext=self.xmlRead(dom,'ptnext',0)
        ptbe=self.xmlRead(dom,'ptbe',0)
        pttopnext=self.xmlRead(dom,'pttopnext',0)
        pttoplast=self.xmlRead(dom,'pttoplast',0)


        addwhich=self.xmlRead(dom,'addwhich',0)

        selitem=self.xmlRead(dom,'selitem',0)
        btnAdd=self.xmlRead(dom,'btnAdd',0)


        a={"btnFilter":btnFilter,"ptnext":ptnext,"ptbe":ptbe,"pttopnext":pttopnext,"pttoplast":pttoplast,"button":button,"basetype":basetype,"refresh":refresh,"btnexit":btnexit,"selok":selok,"selbtn":selbtn,"pnext":pnext,"topnext":topnext,"before":before,"topebefore":topebefore,"btnok":btnok}
        a["btnClose"]=btnClose
        a["selclose"]=selclose
        a["btnSure"]=btnSure
        a["CancelBtn"]=CancelBtn
        a["addwhich"]=addwhich
        a["selitem"]=selitem
        a["btnSave"]=btnSave
        a["btnSaveContinue"]=btnSaveContinue
        a["btnAdd"]=btnAdd
        a["edFullName"]=edFullName
        a["btnSaveAdd"]=btnSaveAdd
        a["btnSaveClose"]=btnSaveClose
        return a

    def getallcommonid(self,dom):
        module=self.xmlRead(dom,"module",0)
        filename=self.xmlRead(dom,"filename",0)
        basetype=self.xmlRead(dom,"basetype",0)
        selclose=self.xmlRead(dom,"selclose",0)
        btnClose=self.xmlRead(dom,"btnClose",0)
        btnexit=self.xmlRead(dom,"btnexit",0)
        selok=self.xmlRead(dom,"selok",0)
        refrdragt=self.xmlRead(dom,"refrdragt",0)
        refresh=self.xmlRead(dom,'refresh',0)
        typetopnext=self.xmlRead(dom,'typetopnext',0)
        typenext=self.xmlRead(dom,'typenext',0)
        typebe=self.xmlRead(dom,'typebe',0)
        typetopbe=self.xmlRead(dom,'typetopbe',0)
        selnote=self.xmlRead(dom,'selnote',0)
        btnok=self.xmlRead(dom,'btnok',0)
        btnOK=self.xmlRead(dom,'btnOK',0)
        seloppeo=self.xmlRead(dom,'seloppeo',0)
        selbtn=self.xmlRead(dom,'selbtn',0)
        selbtnall=self.xmlRead(dom,'selbtnall',0)
        button=self.xmlRead(dom,'button',0)
        btnDetail=self.xmlRead(dom,'btnDetail',0)
        btnAdd=self.xmlRead(dom,'btnAdd',0)
        btnSaveAdd=self.xmlRead(dom,'btnSaveAdd',0)
        btnSaveClose=self.xmlRead(dom,'btnSaveClose',0)
        itname=self.xmlRead(dom,'itname',0)
        addwhich=self.xmlRead(dom,'addwhich',0)
        grid_pfullname=self.xmlRead(dom,'grid_pfullname',0)
        grid_assqty=self.xmlRead(dom,'grid_assqty',0)
        grid_assdpprice=self.xmlRead(dom,'grid_assdpprice',0)
        grid_kfullname=self.xmlRead(dom,'grid_kfullname',0)
        grid_ename=self.xmlRead(dom,'grid_ename',0)
        initempart=self.xmlRead(dom,'initempart',0)
        outitempart=self.xmlRead(dom,'outitempart',0)
        btnMore=self.xmlRead(dom,'btnMore',0)
        grid_fullname=self.xmlRead(dom,'grid_fullname',0)
        grid_total=self.xmlRead(dom,'grid_total',0)
        btnSave=self.xmlRead(dom,'btnSave',0)

        a={"btnSave":btnSave,"grid_total":grid_total,"grid_fullname":grid_fullname,"btnMore":btnMore,"outitempart":outitempart,"initempart":initempart,"grid_ename":grid_ename,"grid_kfullname":grid_kfullname,"grid_assdpprice":grid_assdpprice,"grid_assqty":grid_assqty,"grid_pfullname":grid_pfullname,"btnOK":btnOK,"addwhich":addwhich,"itname":itname,"btnSaveAdd":btnSaveAdd,"btnSaveClose":btnSaveClose,"btnDetail":btnDetail,"btnAdd":btnAdd,"basetype":basetype,"selnote":selnote,"btnok":btnok,"seloppeo":seloppeo,"selbtn":selbtn,"selbtnall":selbtnall,"refrdragt":refrdragt,"refresh":refresh,"typetopnext":typetopnext,"typenext":typenext,"typebe":typebe,"typetopbe":typetopbe,"module":module,"filename":filename,"selclose":selclose,"btnClose":btnClose,"btnexit":btnexit,"button":button,"selok":selok}
        return a


    def stockitemselectadd(self,driver,commid,skuitaddid):
        #---售价管理
        salemoman=commid["basetype"]+skuitaddid+"c2"+commid["addwhich"]
        #print  salemoman
        self.findXpath(driver,salemoman).click()
        #--商品图片管理
        picman=commid["basetype"]+skuitaddid+"c3"+commid["addwhich"]
        self.findXpath(driver,picman).click()

        #---基本信息
        itbainfo=commid["basetype"]+skuitaddid+"c1"+commid["addwhich"]
        self.findXpath(driver,itbainfo).click()

        #---保存并关闭
        self.findId(driver,skuitaddid+commid["btnSaveClose"]).click()
        self.accAlert(driver,1)
        #---保存并新增
        self.findId(driver,skuitaddid+commid["btnSaveAdd"]).click()
        self.accAlert(driver,1)
        #---关闭
        self.findId(driver,skuitaddid+commid["selclose"]).click()

    #仓库选择框/收货仓库/经手人（2）/往来单位选择框（1） 添加 关闭
    def catesel(self,driver,*c):
        #添加
        js="$(\"button:contains('添加')\").click()"
        self.delaytime(1)
        self.excutejs(driver,js)
        #-保存并新增
        js="$(\"button:contains('保存并新增')\").click()"
        self.delaytime(1)
        self.excutejs(driver,js)
        self.accAlert(driver,1)

        #-保存并关闭
        js="$(\"button:contains('保存并关闭')\").click()"
        self.delaytime(1)
        self.excutejs(driver,js)
        self.accAlert(driver,1)

        if len(c)==2:
            #-所属部门
            js=c[0]
            #self.delaytime(1)
            self.excutejs(driver,js)
            self.delaytime(1)
            self.doubleclick(driver,c[1])

            #--部门选择框，关闭
            js="$(\"button:contains('选中')\").last().click()"
            self.delaytime(1)
            self.excutejs(driver,js)
            self.doubleclick(driver,c[1])
            #部门选择框，选中
            js="$(\"button:contains('关闭')\").last().click()"
            self.delaytime(1)
            self.excutejs(driver,js)


        #-关闭
        js="$(\"button:contains('关闭')\").eq(2).click()"
        self.delaytime(1)
        self.excutejs(driver,js)

        if len(c)==3:
            #查看单位基本信息
            js="$(\"button:contains('查看单位基本信息')\").last().click()"
            self.delaytime(1)
            self.excutejs(driver,js)
            #-关闭
            js="$(\"button:contains('关闭')\").last().click()"
            self.delaytime(1)
            self.excutejs(driver,js)
            #翻页
            self.pagewhich(driver,c[0]["basetype"],c[2],c[0]["typenext"],c[0]["typetopbe"],c[0]["typebe"],c[0]["typetopnext"])

        #关闭
        js="$(\"button:contains('关闭')\").click()"
        self.delaytime(1)
        self.excutejs(driver,js)

        if len(c)==3:
            self.doubleclick(driver,c[1])
            js="$(\"button:contains('选中')\").click()"
            self.delaytime(1)
            self.excutejs(driver,js)

    #部门选择框\付款账户
    def departsel(self,driver,dblid):
        self.doubleclick(driver,dblid)
        #关闭
        self.delaytime(1)
        js="$(\"button:contains('关闭')\").click()"
        self.delaytime(1)
        self.excutejs(driver,js)
        self.delaytime(1)
        self.doubleclick(driver,dblid)
        self.delaytime(1)
        self.delaytime(3,driver)
        #选中
        js="$(\"button:contains('选中')\").last().click()"
        self.delaytime(1)
        self.excutejs(driver,js)

    #录单配置
    def conbill(self,driver,id):
        self.findId(driver,id).click()
        self.delaytime(1)
        self.delaytime(3,driver)
        #退出
        js="$(\"button:contains('退出')\").last().click()"
        self.delaytime(1)
        self.excutejs(driver,js)
        self.findId(driver,id).click()
        self.delaytime(1)
        self.delaytime(3,driver)
        js="$(\"button:contains('保存')\").last().click()"
        self.delaytime(1)
        self.excutejs(driver,js)

    #费用结算
    def moneyend(self,driver,id):
        self.findId(driver,id).click()
        self.delaytime(1)
        #关闭
        js="$(\"button:contains('关闭')\").last().click()"
        self.delaytime(1)
        self.excutejs(driver,js)
        self.delaytime(1)
        self.findId(driver,id).click()

        #物流公司
        js="$(\"input[id$=edFreightbtype]\").last().attr(\"id\",\"logcomid\")"
        self.delaytime(1)
        self.excutejs(driver,js)
        self.delaytime(1)
        self.doubleclick(driver,"logcomid")

        #-翻页
        self.pagechoice(driver)

        #-进入下级
        js="$(\"button:contains('进入下级')\").click()"
        self.delaytime(1)
        self.excutejs(driver,js)
        self.delaytime(1)


        #-返回上级
        js="$(\"button:contains('返回上级')\").click()"
        self.delaytime(1)
        self.excutejs(driver,js)
        self.delaytime(1)
        #-关闭
        js="$(\"button:contains('关闭')\").last().click()"
        self.excutejs(driver,js)
        self.delaytime(1)

        #-选中
        self.doubleclick(driver,"logcomid")
        self.delaytime(1)
        js2="$(\"button:contains('选中')\").last().click()"
        self.excutejs(driver,js2)
        self.delaytime(1)
        #print "选中1.。。"

        #-查看单位基本信息
        js="$(\"button:contains('查看单位基本信息')\").click()"
        self.excutejs(driver,js)
        self.delaytime(1)

        #--关闭
        js="$(\"button:contains('关闭')\").last().click()"
        self.excutejs(driver,js)
        self.delaytime(1)

        #-选中
        self.excutejs(driver,js2)
        self.delaytime(1)

        #保存关闭
        js="$(\"button:contains('保存并关闭')\").last().click()"
        self.excutejs(driver,js)
        self.delaytime(1)

    #翻页js
    def pagechoice(self,driver,*c):
        #最后一页
        self.delaytime(1)
        an=str(self.getrandnumber())
        bn=str(self.getrandnumber())
        cn=str(self.getrandnumber())
        dn=str(self.getrandnumber())
        if len(c)>0:
            js="$(\"td[class=Pager_lastPage]\").eq("+str(c[0])+").attr(\"id\",\"lastpage"+an+"\")"
            self.excutejs(driver,js)
            #self.delaytime(1)

            #上一页
            js="$(\"td[class=Pager_prevPage]\").eq("+str(c[0])+").attr(\"id\",\"prepage"+bn+"\")"
            self.excutejs(driver,js)
            #self.delaytime(1)

            #下一页
            js="$(\"td[class=Pager_nextPage]\").eq("+str(c[0])+").attr(\"id\",\"nextpage"+cn+"\")"
            self.excutejs(driver,js)
            #第一页
            js="$(\"td[class=Pager_homePage]\").eq("+str(c[0])+").attr(\"id\",\"homepage"+dn+"\")"
            self.excutejs(driver,js)
            self.delaytime(1)

        else:

            js="$(\"td[class=Pager_lastPage]\").last().attr(\"id\",\"lastpage"+an+"\")"
            self.excutejs(driver,js)
            #self.delaytime(1)

            #上一页
            js="$(\"td[class=Pager_prevPage]\").last().attr(\"id\",\"prepage"+bn+"\")"
            self.excutejs(driver,js)
            #self.delaytime(1)

            #下一页
            js="$(\"td[class=Pager_nextPage]\").last().attr(\"id\",\"nextpage"+cn+"\")"
            self.excutejs(driver,js)
            #第一页
            js="$(\"td[class=Pager_homePage]\").last().attr(\"id\",\"homepage"+dn+"\")"
            self.excutejs(driver,js)
            self.delaytime(1)

        self.findId(driver,"lastpage"+an).click()
        self.findId(driver,"prepage"+bn).click()
        self.findId(driver,"nextpage"+cn).click()
        self.findId(driver,"homepage"+dn).click()

    #通用js执行
    def exjscommin(self,driver,con,*c):
        if len(c)>0:
            js="$(\"button:contains('"+con+"')\").first().click()"
        else:
            js="$(\"button:contains('"+con+"')\").last().click()"
        self.delaytime(1)
        self.excutejs(driver,js)
        #self.delaytime(1)

    #经手人、存货仓库、库存商品选择框
    def passpeople(self,driver,id,*c):
        self.doubleclick(driver,id)
        #如果是库存商品选择框，需要翻页
        if len(c)>0:
            self.pagechoice(driver)
        #关闭
        self.exjscommin(driver,"关闭")
        self.doubleclick(driver,id)
        self.delaytime(1)
        #选中
        self.exjscommin(driver,"选中")

    #库存商品选择框
    def cateitemsel(self,driver,dblid,*c):
        self.delaytime(1)
        if len(c)>0:
            self.findId(driver,dblid).click()
        else:
            self.doubleclick(driver,dblid)
        self.delaytime(1)
        #翻页
        self.pagechoice(driver)
        #添加
        self.exjscommin(driver,"添加")

        #-商品图片管理
        js="$(\"div:contains('商品图片管理')\").last().attr(\"id\",\"picmanid\")"
        self.excutejs(driver,js)
        self.delaytime(2)
        self.findId(driver,"picmanid").click()

        #-售价管理
        js="$(\"div:contains('售价管理')\").last().attr(\"id\",\"saleid\")"
        self.excutejs(driver,js)
        self.delaytime(1)
        self.findId(driver,"saleid").click()

        #-基本信息
        js="$(\"div:contains('基本信息')\").last().attr(\"id\",\"baseid\")"
        self.excutejs(driver,js)
        self.delaytime(1)
        self.findId(driver,"baseid").click()

        #-保存并新增
        self.exjscommin(driver,"保存并新增")
        self.accAlert(driver,1)

        #-保存并关闭
        self.exjscommin(driver,"保存并关闭")
        self.accAlert(driver,1)

        #-关闭
        self.exjscommin(driver,"关闭")

        #关闭
        self.exjscommin(driver,"关闭")
        if len(c)>0:
            self.findId(driver,dblid).click()
        else:
            self.doubleclick(driver,dblid)

        #选中
        self.exjscommin(driver,"选中")

        #选中并关闭
        self.exjscommin(driver,"选中并关闭")

    #商品单位/折前单价
    def itemunit(self,driver,dblid):
        self.doubleclick(driver,dblid)
        self.delaytime(1)

        #关闭
        self.exjscommin(driver,"关闭")
        self.doubleclick(driver,dblid)

        #确定
        self.exjscommin(driver,"确定")

    #商品单位
    def itemnums(self,driver,dblid):
        self.doubleclick(driver,dblid)

        #关闭
        self.exjscommin(driver,"取消")
        self.doubleclick(driver,dblid)

        #确定
        self.exjscommin(driver,"确定")

    #往来单位选择框
    def buycompanysel(self,driver,dblid,*c):
        self.doubleclick(driver,dblid)
        if len(c)==0:
            self.exjscommin(driver,"添加")

            #-保存并新增
            self.exjscommin(driver,"保存并新增")
            self.accAlert(driver,1)

            #-保存并关闭
            self.exjscommin(driver,"保存并关闭")
            self.accAlert(driver,1)

            #-关闭
            self.exjscommin(driver,"关闭")

        #-查看单位基本信息
        self.exjscommin(driver,"查看单位基本信息")

        #-关闭
        self.exjscommin(driver,"关闭")

        #-关闭
        self.exjscommin(driver,"关闭")

        self.doubleclick(driver,dblid)

        #翻页
        self.pagechoice(driver)

        #-选中
        self.exjscommin(driver,"选中")

    #业务员选择框、发货仓库
    def peoplesel(self,driver,dblid,*c):
        #print dblid
        self.delaytime(1)
        self.doubleclick(driver,dblid)
        self.delaytime(1)
        self.delaytime(3,driver)
        #关闭
        self.exjscommin(driver,"关闭")

        #添加
        self.doubleclick(driver,dblid)
        self.delaytime(1)
        self.delaytime(2,driver)
        self.exjscommin(driver,"添加")
        self.delaytime(2)
        #-保存并新增
        self.exjscommin(driver,"保存并新增")
        self.accAlert(driver,1)

        #-保存并关闭
        self.exjscommin(driver,"保存并关闭")
        self.accAlert(driver,1)

        #-关闭
        self.exjscommin(driver,"关闭")

        if len(c)>0:
            self.exjscommin(driver,"添加")
            #所属部门
            js="$(\"input[class=ButtonEdit\").last().attr(\"id\",\"departid\")"
            self.delaytime(1)
            self.excutejs(driver,js)
            self.doubleclick(driver,"departid")
            #-关闭
            self.exjscommin(driver,"关闭")
            self.doubleclick(driver,"departid")
            #-选中
            self.exjscommin(driver,"选中")
            self.exjscommin(driver,"关闭")

        #选中
        self.delaytime(1)
        self.exjscommin(driver,"选中")


    #导入商品明细
    def impitemdetail(self,driver,id):
        self.findId(driver,id).click()
        #导入文件
        self.exjscommin(driver,"导入文件")
        self.accAlert(driver,1)
        self.delaytime(1)
        #取消
        self.exjscommin(driver,"取消")

    #发货信息
    def sendinfo(self,driver,id,*c):
        self.findId(driver,id).click()
        #-关闭
        self.exjscommin(driver,"关闭")
        self.findId(driver,id).click()

        #快捷选择
        self.delaytime(1)
        self.excutejs(driver,c[0])
        self.doubleclick(driver,c[1])

        #-新增
        self.exjscommin(driver,"新增")

        #--保存并关闭
        self.exjscommin(driver,"保存并关闭")
        self.exjscommin(driver,"确定")
        #--关闭
        self.exjscommin(driver,"关闭")

        #-修改
        self.exjscommin(driver,"修改")
        #--保存并关闭
        self.exjscommin(driver,"保存并关闭")
        self.exjscommin(driver,"修改")
        #--关闭
        self.exjscommin(driver,"关闭")

        #-删除
        self.exjscommin(driver,"删除")
        self.delaytime(1)
        self.accAlert(driver,0)

        #-选中
        self.exjscommin(driver,"选中")

        #确定
        self.exjscommin(driver,"确定")

    #商品套餐选择
    def itempacksel(self,driver,id):
        self.findId(driver,id).click()
        #关闭
        self.exjscommin(driver,"关闭")
        self.findId(driver,id).click()

        #添加
        self.exjscommin(driver,"添加")

        #-保存
        js="$(\"button:contains('保存')\").eq(1).click()"
        self.excutejs(driver,js)
        self.exjscommin(driver,"确定")

        #-保存并继续
        self.exjscommin(driver,"保存并继续")
        self.exjscommin(driver,"确定")

        #-退出
        self.exjscommin(driver,"退出")

        #选中
        self.exjscommin(driver,"选中")
        self.exjscommin(driver,"确定")

    #运费结算
    def freghtend(self,driver,id):
        self.findId(driver,id).click()
        #关闭
        self.exjscommin(driver,"关闭")
        self.findId(driver,id).click()

        #保存并关闭
        #支付账户
        self.delaytime(1)
        js="$(\"input[id$=edFreightatype]\").last().attr(\"id\",\"fremonid\")"
        self.excutejs(driver,js)
        self.doubleclick(driver,"fremonid")
        self.exjscommin(driver,"关闭")
        self.doubleclick(driver,"fremonid")
        self.exjscommin(driver,"选中")

        #物流公司
        js="$(\"input[id$=edFreightbtype]\").last().attr(\"id\",\"frecomid\")"
        self.excutejs(driver,js)
        self.nebecompany(driver,"frecomid")

    #有上下级的往来单位选择框
    def nebecompany(self,driver,dblid,*c):
        self.doubleclick(driver,dblid)
        self.delaytime(3,driver)
        if len(c)>0:
            self.delaytime(1)
            self.excutejs(driver,c[0])
            self.delaytime(1)
            self.findId(driver,"allbankacc").click()

        #-翻页
        if len(c)==0:
            self.delaytime(1)
            self.pagechoice(driver)

        #-进入下级
        js="$(\"button:contains('进入下级')\").click()"
        self.delaytime(1)
        self.excutejs(driver,js)

        if len(c)>0:
            self.pagechoice(driver)


        #-返回上级
        js="$(\"button:contains('返回上级')\").click()"
        self.delaytime(1)
        self.excutejs(driver,js)
        #-关闭
        js="$(\"button:contains('关闭')\").last().click()"
        self.delaytime(1)
        self.excutejs(driver,js)

        #-选中
        self.doubleclick(driver,dblid)
        self.delaytime(3,driver)
        if len(c)>0:
            self.delaytime(1)
            self.excutejs(driver,c[0])
            self.delaytime(1)
            self.findId(driver,"allbankacc").click()


        js2="$(\"button:contains('选中')\").last().click()"
        self.delaytime(1)
        self.excutejs(driver,js2)
        #print "选中1.。。"

        if len(c)==0:
            #-查看单位基本信息
            js="$(\"button:contains('查看单位基本信息')\").click()"
            self.excutejs(driver,js)
            self.delaytime(1)

            #--关闭
            js="$(\"button:contains('关闭')\").last().click()"
            self.excutejs(driver,js)

            #-选中
            self.exjscommin(driver,"选中")

            #保存关闭
            js="$(\"button:contains('保存并关闭')\").last().click()"
            self.excutejs(driver,js)
        else:
            #-选中
            self.exjscommin(driver,"选中")

    #保存|退出 保存单据、存入草稿、废弃退出
    def savedraftexit(self,driver,saexid,itnaid,itemid,*c):

        if len(c)>0:
            a="选中"
        else:
            a="选中并关闭"
        self.delaytime(1)
        self.findId(driver,saexid).click()
        self.delaytime(1)
        self.exjscommin(driver,"保存单据")
        self.delaytime(1)
        self.findXpath(driver,itnaid).click()
        self.doubleclick(driver,itemid)
        self.delaytime(1)
        if len(c)>0:
            if c[0]==10:
                self.exjscommin(driver,a)
                self.exjscommin(driver,a)
        self.exjscommin(driver,a)
        self.findId(driver,saexid).click()
        self.delaytime(1)
        self.exjscommin(driver,"存入草稿")

        self.findXpath(driver,itnaid).click()
        self.doubleclick(driver,itemid)
        self.delaytime(1)
        if len(c)>0:
            if c[0]==10:
                self.exjscommin(driver,a)
                self.exjscommin(driver,a)
        self.exjscommin(driver,a)
        self.delaytime(1,driver)
        self.findId(driver,saexid).click()
        self.delaytime(1)
        self.exjscommin(driver,"废弃退出")

    #配置>>
    def contype(self,driver,configid,*c):
        for a in c:
            self.findId(driver,configid).click()
            self.delaytime(3,driver)
            #print a
            self.excutejs(driver,a)
            #退出
            js="$(\"button:contains('退出')\").last().click()"
            self.delaytime(1)
            self.excutejs(driver,js)
            self.findId(driver,configid).click()
            self.delaytime(1)
            self.excutejs(driver,a)
            js="$(\"button:contains('保存')\").last().click()"
            self.delaytime(1)
            self.excutejs(driver,js)
            self.accAlert(driver,1)

    #经手人
    def passpeoplesel(self,driver,dblid):
        self.doubleclick(driver,dblid)
        self.delaytime(1)
        #关闭
        self.exjscommin(driver,"关闭")
        self.doubleclick(driver,dblid)
        self.delaytime(2)
        self.exjscommin(driver,"选中")


    #生产模板
    def promoudle(self,driver,id):
        self.findId(driver,id).click()
        #退出
        self.exjscommin(driver,"退出")
        self.findId(driver,id).click()
        #新增
        self.exjscommin(driver,"新增")

        #-生产模板-配料单
        #-关闭
        self.exjscommin(driver,"关闭")
        self.exjscommin(driver,"新增")

        #-模板名称
        jsmodulename="var a=$(\"input[id$=fullname]\").attr(\"id\");$(\"input[id$=fullname]\").val(a+'"+str(self.getrandnumber())+"')"
        self.delaytime(1)
        self.excutejs(driver,jsmodulename)

        #-关闭 取消
        self.exjscommin(driver,"关闭")
        self.exjscommin(driver,"取消")

        #-关闭 否
        self.exjscommin(driver,"关闭")
        self.exjscommin(driver,"否")
        self.exjscommin(driver,"新增")

        #-生产商品
        js="var a=$(\"input[id$=fullname]\").attr(\"id\");$(\"input[id$=fullname]\").val(a+'"+str(self.getrandnumber())+"');"+"$(\"input[id$=edPType]\").attr(\"id\",\"additemid\")"
        self.delaytime(1)
        self.excutejs(driver,js)
        self.passpeople(driver,"additemid",1)


        #-商品名称
        js=""+"$(\"input[id$=fullname]\").attr(\"id\",\"testid\");"
        self.delaytime(1)
        self.excutejs(driver,js)
        itxpath=self.findId(driver,"testid").get_attribute("value")
        itxpath=itxpath[:10]
        #print itxpath

        itempath1="//*[@id=\""+itxpath+"grid\"]/div[2]/table/tbody/tr[1]/td[3]"
        #print itempath1
        self.findXpath(driver,itempath1).click()
        item1=itxpath+"grid_pfullname"
        self.doubleclick(driver,item1)

        itemname1="$(\"div[class=GridBodyCellText]:contains('M001')\").last().attr(\"id\",\"itemadd1id\")"
        self.delaytime(1)
        self.excutejs(driver,itemname1)
        self.findId(driver,"itemadd1id").click()
        self.exjscommin(driver,"选中并关闭")


        #-配套数量
        itemqty1="//*[@id=\""+itxpath+"grid\"]/div[2]/table/tbody/tr[1]/td[9]"
        self.findXpath(driver,itemqty1).click()
        self.findId(driver,itxpath+"grid_produreqty").send_keys("1")

        itempath2="//*[@id=\""+itxpath+"grid\"]/div[2]/table/tbody/tr[2]/td[3]"
        self.findXpath(driver,itempath2).click()
        self.doubleclick(driver,item1)

        itemname2="$(\"div[class=GridBodyCellText]:contains('555')\").last().attr(\"id\",\"itemadd2id\")"
        self.delaytime(1)
        self.excutejs(driver,itemname2)
        self.findId(driver,"itemadd2id").click()
        self.exjscommin(driver,"选中并关闭")

        itemqty2="//*[@id=\""+itxpath+"grid\"]/div[2]/table/tbody/tr[2]/td[9]"
        self.findXpath(driver,itemqty2).click()
        self.findId(driver,itxpath+"grid_produreqty").send_keys("1")


        #-打印
        #保存
        self.exjscommin(driver,"保存")

        #-关闭 是
        self.exjscommin(driver,"新增")
        js="$(\"input[id$=fullname]\").attr(\"value\",\"testadd proasse module quit"+str(self.getrandnumber())+"\")"
        self.delaytime(1)
        self.excutejs(driver,js)

        js="$(\"input[id$=edPType]\").attr(\"id\",\"additemid\")"
        self.delaytime(1)
        self.excutejs(driver,js)
        self.doubleclick(driver,"additemid")
        self.exjscommin(driver,"选中")

        self.findXpath(driver,itempath1).click()
        self.doubleclick(driver,item1)
        self.delaytime(1)
        self.exjscommin(driver,"选中并关闭")
        self.findXpath(driver,itemqty1).click()
        self.findId(driver,itxpath+"grid_produreqty").send_keys("1")

        self.exjscommin(driver,"关闭")
        self.exjscommin(driver,"是")

        #修改
        self.exjscommin(driver,"修改")
        self.exjscommin(driver,"关闭")
        self.exjscommin(driver,"修改")
        self.exjscommin(driver,"保存")

    #筛选
    def selectit(self,driver,*c):
        jssel="$(\"span:contains('筛选')\").click()"
        self.delaytime(1)
        self.excutejs(driver,jssel)
        self.exjscommin(driver,"取消")
        self.excutejs(driver,jssel)
        self.excutejs(driver,c[0])
        self.delaytime(1)
        self.doubleclick(driver,c[1])
        self.delaytime(1)
        self.excutejs(driver,c[2])
        self.delaytime(1)
        self.findId(driver,c[3]).click()
        self.excutejs(driver,c[4])
        self.exjscommin(driver,"筛选")

    #2种js 取消确定
    def twojsxomm(self,driver,id,*c):
        self.findId(driver,id).click()

    #会员
    def menbersel(self,driver,id):
        self.findId(driver,id).click()
        self.exjscommin(driver,"关闭")
        self.findId(driver,id).click()
        self.exjscommin(driver,"查看会员基本信息")

        self.exjscommin(driver,"积分储值明细")
        self.exjscommin(driver,"单据明细")
        self.exjscommin(driver,"退出")

        self.exjscommin(driver,"积分消费明细")
        self.exjscommin(driver,"单据明细")
        self.exjscommin(driver,"退出")

        self.exjscommin(driver,"取消")
        self.exjscommin(driver,"选中")

    #序列号商品入库
    def seriesiteminto(self,driver,itemsel,itemone):
        self.doubleclick(driver,itemsel)
        js="$(\"div[class=GridBodyCellText]:contains('Series')\").last().attr(\"id\",\"seitemid\")"
        self.delaytime(1)
        self.excutejs(driver,js)
        self.findId(driver,"seitemid").click()
        self.exjscommin(driver,"选中并关闭")
        self.exjscommin(driver,"关闭")

        self.findXpath(driver,itemone).click()
        self.doubleclick(driver,itemsel)

        self.delaytime(1)
        self.excutejs(driver,js)
        self.findId(driver,"seitemid").click()
        self.exjscommin(driver,"选中并关闭")

        itemser=self.getrandnumber()
        f=open(r'C:\workspace\nufeeb.button\instock\instockortherseries','w')
        f.write(itemser)
        f.close()

        js="$(\"input[id$=snnoTxt]\").val('"+itemser+"')"
        self.delaytime(1)
        self.excutejs(driver,js)
        self.exjscommin(driver,"添加",1)
        self.exjscommin(driver,"删除当前行")
        self.exjscommin(driver,"添加",1)
        self.exjscommin(driver,"删除全部")


        self.exjscommin(driver,"导入")
        self.exjscommin(driver,"导入文件")
        self.accAlert(driver,1)
        self.exjscommin(driver,"取消")


        js="$(\"input[id$=snnostartTxt]\").val('"+itemser+"')"
        self.delaytime(1)
        self.excutejs(driver,js)
        self.exjscommin(driver,"批量添加")
        self.exjscommin(driver,"完成")

    #序列号商品出库
    def seriesitemout(self,driver,itemid,itnaid,*c):
        self.doubleclick(driver,itemid)
        js="$(\"div[class=GridBodyCellText]:contains('Series')\").last().attr(\"id\",\"seitemid\")"
        self.delaytime(1)
        self.excutejs(driver,js)
        self.findId(driver,"seitemid").click()
        self.exjscommin(driver,"选中并关闭")
        self.exjscommin(driver,"关闭")

        self.findXpath(driver,itnaid).click()
        self.doubleclick(driver,itemid)
        self.exjscommin(driver,"选中并关闭")

        self.exjscommin(driver,"选择")
        self.exjscommin(driver,"选中")
        self.exjscommin(driver,"删除当前行")


        itemser=self.getrandnumber()
        self.exjscommin(driver,"选择")
        js="$(\"input[id$=edFilterStr]\").val('222')"
        js2="$(\"div[id$=btnFilter]\").last().click()"
        self.delaytime(1)
        self.excutejs(driver,js)
        self.excutejs(driver,js2)
        self.exjscommin(driver,"全部")

        js="$(\"input[id$=snnoTxt]\").val('"+itemser+"')"
        self.delaytime(1)
        self.excutejs(driver,js)
        self.exjscommin(driver,"添加",1)
        self.exjscommin(driver,"删除全部")

        self.exjscommin(driver,"导入")
        self.exjscommin(driver,"导入文件")
        self.accAlert(driver,1)
        self.exjscommin(driver,"取消")

        if len(c)>0:
            js="$(\"input[id$=snnostartTxt]\").val('"+c[0]+"')"
            self.delaytime(1)
            self.excutejs(driver,js)
            self.exjscommin(driver,"批量添加")
            self.exjscommin(driver,"完成")

        else:
            js="$(\"input[id$=snnostartTxt]\").val('"+itemser+"')"
            self.delaytime(1)
            self.excutejs(driver,js)
            self.delaytime(1)
            js2="$(\"input[id$=snnobaseTxt]\").val('test')"
            self.excutejs(driver,js2)
            self.exjscommin(driver,"批量添加")
            self.exjscommin(driver,"删除全部")
            self.exjscommin(driver,"选择")
            self.exjscommin(driver,"选中")
            self.exjscommin(driver,"选中")
            self.exjscommin(driver,"完成")

    #商品套餐的
    def skupagesalman(self,driver,*c):
        if len(c)==0:
            #-商品图片管理
            js="$(\"div:contains('商品图片管理')\").last().attr(\"id\",\"picmanid\")"
            self.delaytime(1)
            self.excutejs(driver,js)
            self.findId(driver,"picmanid").click()

        #-售价管理
        js="$(\"div:contains('售价管理')\").last().attr(\"id\",\"saleid\")"
        self.delaytime(1)
        self.excutejs(driver,js)
        self.findId(driver,"saleid").click()

        #-基本信息
        js="$(\"div:contains('基本信息')\").last().attr(\"id\",\"baseid\")"
        self.delaytime(1)
        self.excutejs(driver,js)
        self.delaytime(1)
        self.findId(driver,"baseid").click()


    #科目选择框
    def subselect(self,driver,dblid):
        self.delaytime(1)
        self.doubleclick(driver,dblid)
        self.exjscommin(driver,"关闭")
        self.doubleclick(driver,dblid)
        self.exjscommin(driver,"进入下级")
        self.exjscommin(driver,"返回上级")
        self.exjscommin(driver,"选中")
        self.exjscommin(driver,"选中")
        self.exjscommin(driver,"选中")

    #查询条件
    def conditonsel(self,driver,conid):
        self.findId(driver,conid).click()
        self.pagechoice(driver)
        self.exjscommin(driver,"关闭")
        self.findId(driver,conid).click()
        self.exjscommin(driver,"查看单位基本信息")
        self.exjscommin(driver,"关闭")
        self.exjscommin(driver,"返回上级")
        self.exjscommin(driver,"进入下级")
        self.exjscommin(driver,"选择一类")
        self.findId(driver,conid).click()
        self.exjscommin(driver,"选中")
        self.exjscommin(driver,"选中")

    #刷新
    def refreshbutton(self,driver):
        js="$(\"span:contains('刷新')\").last().click()"
        self.delaytime(1)
        self.excutejs(driver,js)

    #筛选
    def selectbycon(self,driver,condition,*c):
        js1="$(\"input[id$=edColumns]\").attr(\"id\",\"selid\")"
        js2="$(\"div:contains('"+condition+"')\").last().attr(\"id\",\"seitid\")"
        js3="$(\"input[id$=edValue]\").attr(\"value\",\"a1x\")"
        if len(c)>0:
            js3="$(\"input[id$=edValue]\").attr(\"value\",\""+c[0]+"\")"
        self.selectit(driver,js1,"selid",js2,"seitid",js3)

    #MenuCaption 选项
    def classmen(self,driver,condition):
        js="$(\"td[class=MenuCaption]:contains('"+condition+"')\").last().click()"
        self.delaytime(1)
        self.excutejs(driver,js)

    #往来对账
    def checkacccom(self,driver,id):
        self.findId(driver,id).click()
        self.delaytime(1)
        self.exjscommin(driver,"关闭")
        self.findId(driver,id).click()
        self.exjscommin(driver,"确定")
        self.exjscommin(driver,"查看凭证")
        self.exjscommin(driver,"退出")
        self.exjscommin(driver,"组号设置")
        self.exjscommin(driver,"退出")
        self.exjscommin(driver,"组号设置")
        js="$(\"input[id$=edWldzGroup]\").val('3')"
        self.delaytime(1)
        self.excutejs(driver,js)
        self.exjscommin(driver,"确定")
        #网页发布
        js="$(\"input[id$=zeroShowType]\").last().attr(\"id\",\"noviewid\")"
        self.delaytime(1)
        self.excutejs(driver,js)
        self.doubleclick(driver,"noviewid")
        js="$(\"div:contains('不显示红冲单据')\").last().attr(\"id\",\"viewid\")"
        self.delaytime(1)
        self.excutejs(driver,js)
        self.findId(driver,"viewid").click()
        self.exjscommin(driver,"网页发布")
        self.delaytime(3,driver)
        self.exjscommin(driver,"取消")
        self.exjscommin(driver,"网页发布")
        self.exjscommin(driver,"对账发布")
        self.exjscommin(driver,"关闭")

        self.exjscommin(driver,"网页发布")
        self.exjscommin(driver,"对账发布")
        js="$(\"input[id$=checksendMail]\").click()"
        self.delaytime(1)
        self.excutejs(driver,js)
        self.exjscommin(driver,"发送邮件")
        self.accAlert(driver,1)

        self.exjscommin(driver,"网页发布")
        self.exjscommin(driver,"对账发布")
        js="$(\"input[id$=checksendMail]\").click()"
        self.delaytime(1)
        self.excutejs(driver,js)
        self.exjscommin(driver,"关闭")


        #发布管理
        self.exjscommin(driver,"发布管理")
        self.delaytime(1)
        self.exjscommin(driver,"删除")
        self.accAlert(driver,1)
        self.exjscommin(driver,"关闭")

        self.pagechoice(driver)
        self.exjscommin(driver,"退出")

    #往来单位
    def classbtype(self,driver,dblid):
        self.doubleclick(driver,dblid)
        self.pagechoice(driver)
        self.exjscommin(driver,"查看单位基本信息")
        self.exjscommin(driver,"关闭")
        self.exjscommin(driver,"关闭")
        self.doubleclick(driver,dblid)
        self.exjscommin(driver,"选中")
        self.doubleclick(driver,dblid)
        self.exjscommin(driver,"选择一类")


    #有上下级的往来单位选择框
    def nebecompany2(self,driver,dblid,*c):
        self.doubleclick(driver,dblid)
        if len(c)>0:
            self.delaytime(1)
            self.excutejs(driver,c[0])
            self.delaytime(1)
            self.findId(driver,"allbankacc").click()

        #-翻页
        if len(c)==0:
            self.pagechoice(driver)

        #-进入下级
        js="$(\"button:contains('进入下级')\").click()"
        self.excutejs(driver,js)

        if len(c)>0:
            self.pagechoice(driver)


        #-返回上级
        js="$(\"button:contains('返回上级')\").click()"
        self.excutejs(driver,js)
        #-关闭
        js="$(\"button:contains('关闭')\").last().click()"
        self.excutejs(driver,js)

        #-选中
        self.doubleclick(driver,dblid)
        if len(c)>0:
            self.delaytime(1)
            self.excutejs(driver,c[0])
            self.delaytime(1)
            self.findId(driver,"allbankacc").click()

        self.delaytime(1)
        js2="$(\"button:contains('选中')\").last().click()"
        self.excutejs(driver,js2)
        #print "选中1.。。"

        if len(c)==0:
            #-查看单位基本信息
            js="$(\"button:contains('查看单位基本信息')\").click()"
            self.excutejs(driver,js)
            self.delaytime(1)

            #--关闭
            js="$(\"button:contains('关闭')\").last().click()"
            self.excutejs(driver,js)

            #-选中
            self.exjscommin(driver,"选中")

            #选中
            self.exjscommin(driver,"选中")
        else:
            #-选中
            self.exjscommin(driver,"选中")

    #执行js后click()
    def afterjsclick(self,driver,js,id):
        self.delaytime(1)
        self.excutejs(driver,js)
        self.findId(driver,id).click()



    #查看单位基本信息
    def viewcombaseinfo(self,driver,id):
        self.doubleclick(driver,id)
        self.exjscommin(driver,"查看单位基本信息")
        self.exjscommin(driver,"关闭")
        self.pagechoice(driver)
        self.exjscommin(driver,"关闭")
        self.doubleclick(driver,id)
        self.exjscommin(driver,"选中")

    #关闭×
    def closexx(self,driver):
        js="$(\"div[style*=closeButton]\").click()"
        self.delaytime(1)
        self.excutejs(driver,js)


    #input元素 结尾id固定的,div进行选择
    def inputid(self,driver,id,divname,*c):
        if len(c)==0:
            js="$(\"input[id$="+id+"]\").last().attr(\"id\",\""+id+"\")"
            self.delaytime(1)
            self.excutejs(driver,js)
            self.doubleclick(driver,id)
        tempid=self.getrandnumber(1)
        self.delaytime(1)
        js="$(\"div:contains('"+divname+"')\").last().attr(\"id\",\"abc"+str(tempid[0])+"\")"
        self.delaytime(1)
        self.excutejs(driver,js)
        self.findId(driver,"abc"+str(tempid[0])).click()


    #element contains
    def elementcontains(self,driver,el,con,giveid):
        js="$(\""+el+":contains('"+con+"')\").last().attr(\"id\",\""+giveid+"\")"
        self.delaytime(1)
        self.excutejs(driver,js)

    #element id 赋值
    def elementvalue(self,driver,el,id,value):
        js="$(\""+el+"[id$="+id+"]\").last().val('"+value+"')"
        self.delaytime(1)
        self.excutejs(driver,js)

    def lableclick(self,driver,forid):
        js="$(\"label[for$="+forid+"]\").click()"
        self.delaytime(1)
        self.excutejs(driver,js)

    #js取input val内容
    def jsinputgetval(self,*c):
        #c[0] driver; c[1] id; c[2] jsid
        js="var a=$(\"input[id$="+c[2]+"]\").last().val();$(\"input[id$="+c[2]+"]\").attr(\"temp\",a)"
        self.delaytime(1)
        self.excutejs(c[0],js)
        val=self.findId(c[0],c[1]).get_attribute("temp")
        return val

    #数据库取订单主表数据
    def getmysqldlyndxOrder(self,number,summary):
        cur=self.mysqlopen()
        datas=[]
        sqls=[]
        #往来单位
        sql="SELECT FullName FROM btype WHERE id=(SELECT btypeid FROM dlyndxOrder  WHERE number='"+number+"' AND summary='"+summary+"')"
        sqls.append(sql)
        #经手人
        sql="SELECT FullName FROM employee WHERE id=(SELECT etypeid FROM dlyndxOrder  WHERE number='"+number+"' AND summary='"+summary+"')"
        sqls.append(sql)
        #仓库
        sql="SELECT FullName FROM stock WHERE id=(SELECT ktypeid FROM dlyndxOrder  WHERE number='"+number+"' AND summary='"+summary+"')"
        sqls.append(sql)

        for sql in sqls:
            cur.execute(sql)
            self.delaytime(1)
            data=cur.fetchone()
            datas.append(data[0])

        sql1="SELECT DATE,summary,COMMENT,ToDate,OrderOver,UserOver,AuditOver,createType,number,Total FROM dlyndxOrder WHERE number='"+number+"' AND Summary='"+summary+"'"
        cur.execute(sql1)
        data=cur.fetchone()
        for k in data:
           datas.append(k)
        cur.close()

        return datas

    #数据库取订单里商品数据
    def getmysqlitems(self,number,summary):
        cur=self.mysqlopen()
        datas=[]
        sql=(
            "SELECT ptypeid,assQty,assdpPrice,dpTotal,discount,asstpPrice,tpTotal,tax,taxTotal,assprice,total,COMMENT,toQty,Qty"
             " FROM bakdlyorder "
             " WHERE vchcode=(SELECT vchcode FROM dlyndxOrder WHERE  number='"+number+"'AND summary='"+summary+"')"
        )
        res=cur.execute(sql)
        data=cur.fetchmany(res)
        for k in data:
            temp=[]
            sql="SELECT UserCode,FullName,Unit1,recPrice1,Name FROM ptype WHERE id='"+str(k[0])+"'"
            cur.execute(sql)
            itheader=cur.fetchone()
            for n in itheader:
                temp.append(n)
            for m in k:
                temp.append(m)
            del temp[5]
            datas.append(temp)
        return datas


    #知道了
    def know(self,driver):
        js="$(\"span:contains('知道了')\").last().click()"
        self.delaytime(1)
        self.excutejs(driver,js)



