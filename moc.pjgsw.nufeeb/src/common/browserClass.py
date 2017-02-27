#*-* coding:UTF-8 *-*
'''
@author: xsx
'''
from selenium import webdriver
import time
import traceback
from baseClass import  base
import requests
import json
import  re
class browser(base):
    '''
    classdocs
    '''

    
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
                driver=webdriver.Chrome()
            elif browserType.upper()=='IE':
                driver=webdriver.Ie()
            elif browserType.upper()=='FIREFOX' or browserType.upper()=='FF':
                driver=webdriver.Firefox()
            return driver
        except:
            print(u'启动浏览器失败')
            return driver
        
        
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
            
            
            
    #获取订单查询页面数据
    def extractdata(self,driver,searchpath,time):
        try:
            for n in range(1,100):
                    nformxpath=".//*[@id='" +str(searchpath)+"']/div[2]/table/tbody/tr["+str(n)+"]/td[3]/div"
                    print nformxpath
                    if self.elementisexist(self,driver,nformxpath)==False:
                        break 
            bigrid=[]
            for row in range(1,n):
                grid=[]
                for line in range(3,time):
                    formxpath=".//*[@id='" +str(searchpath)+"']/div[2]/table/tbody/tr["+str(row)+"]/td["+str(line)+"]/div"
                    self.elementisexist(self,driver,formxpath)
                    if self.elementisexist(self,driver,formxpath)==True:
                        data=base.findXpath(self,driver,formxpath).text
                        grid.append(data)
                        print grid
                        #print grid
                bigrid.append(grid)
            return bigrid
            
        except:
            print(u"获取订单查询数据失败")
            print(traceback.format_exc())
            return bigrid        
    
    
    def openModule2(self,driver,module,modulename):
        try:
            time.sleep(4)
            driver.implicitly_wait(15)
            base.findXpath(self,driver,module).click()
            time.sleep(3)
            base.findXpath(self,driver,modulename).click()
        except :
            print(u"2级页面进入失败")
            print(traceback.format_exc())    
    
    
    def openModule3(self,driver,module,modulename,moduledetail):
        try:
            time.sleep(2) 
            base.findXpath(self,driver,module).click() 
            time.sleep(5)
            base.findXpath(self,driver,modulename).click()
            time.sleep(2)
            base.findXpath(self,driver,moduledetail).click()
        except :
            print(u"3级页面进入失败")
            print(traceback.format_exc())

    
    def openModule4(self,driver,module,modulename,moduledetail,modulenade):
        try:
            base.findXpath(self,driver,module).click()
            base.findXpath(self,driver,modulename).click()
            time.sleep(2)
            base.findXpath(self,driver,moduledetail).click()
            base.findXpath(self,driver,modulenade).click()
        except :
            print(u"4级页面进入失败")
            print(traceback.format_exc())

    #登录毕方
    def loginUser(self,driver,name,user,pwd,login,logname,username,password):
        try:
            base.findId(self,driver,name).clear()
            base.findId(self,driver,name).send_keys(logname)
            base.findId(self,driver,user).clear()
            base.findId(self,driver,user).send_keys(username)
            base.findId(self,driver,pwd).clear()
            base.findId(self,driver,pwd).send_keys(password)
            base.findId(self,driver,login).click()
            time.sleep(2)
 
            return driver
        except:
            print(traceback.format_exc())
            print(u"登录失败")
            return driver
    
    #进行授权
    def acccomfirm(self,driver,loginname,password,loginbtn,acc,accid,accpwd):
        try:
            base.findId(self,driver, loginname).clear()
            base.findId(self,driver, loginname).send_keys(accid)
            base.findId(self,driver, password).clear()
            base.findId(self,driver, password).send_keys(accpwd)
            base.findId(self,driver, loginbtn).click()
            #time.sleep(2)
            base.findXpath(self,driver,acc).click()
            time.sleep(2)
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
                        time.sleep(2)
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
            
            
    def set_up(self,driver):
        
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
        dicmanbe=dicmanbe.replace("true","\"false\"")
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
        time.sleep(2)
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
        time.sleep(2)
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

