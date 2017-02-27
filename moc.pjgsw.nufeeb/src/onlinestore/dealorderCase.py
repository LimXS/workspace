#*-* coding:UTF-8 *-*

import unittest

import traceback
import time
import re
import random
import string
import requests
import json

from common import  browserClass
browser=browserClass.browser()

class dealTest(unittest.TestCase):


    def setUp(self):
        
        self.driver=browser.startBrowser('chrome')
        self.url="http://beefun.wsgjp.com/"
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        
        name="$1b8bb415$corpName"
        user="$1b8bb415$userName"
        pwd="$1b8bb415$pwdEdit"
        login="$1b8bb415$btnLogin"
        loginname="xsx123456"
        username="xsx"
        password="xsx123456."
        browser.loginUser(self.driver,name ,user,pwd,login,loginname,username,password)
        
        '''
        #base.accAlert(self.driver, 1)
        
        curpage_url = self.driver.current_url  
        print curpage_url 
        '''
        #get the session cookie  
        cookie = [item["name"] + "=" + item["value"] for item in self.driver.get_cookies()]  
        #print cookie  
  
        self.cookiestr = ';'.join(item for item in cookie)  
        
        
        #print self.cookiestr 
        
        '''
        #切换到自义定流程
        btn=".//*[@id='$3327be68$linkButton1']"
        browser.findXpath(self.driver,btn).click()
        '''
        module=".//*[@id='$80d499b2$ManagerMenuBar3']/div"
        modulename=".//*[@id='$80d499b2$ManagerMenuBar3_4']/td[3]"
        
        browser.openModule2(self.driver, module, modulename)
        
        #选择全部订单
        '''
        selectall=".//*[@id='$4f87816c$quickquery']/div/table[1]/tbody/tr/td[2]/div"
        browser.findXpath(self.driver,selectall).click()
        '''
        pass


    def tearDown(self):
        print "test over"
        #self.driver.close()
        pass

    def testsendItems(self):
        u'''进行发货'''
        all=".//*[@id='$390deff7$quickquery']/div/table[1]/tbody/tr/td[2]/div"
        submit=".//*[@id='$390deff7$button22']"
        browser.findXpath(self.driver,all).click()
        
        #判断一共要提交几次          
        str1=".//*[@id='$390deff7$deliverMainGrid']/div[2]/table/tbody/tr["
        str2="]/td[5]/div"
        n=browser.getlines(self.driver, str1, str2)
                     
        #弹出框继续按钮
        coun=".//*[@id='$640f9fd5$button1']"
        #弹出框取消按钮
        cancel=".//*[@id='$640f9fd5$btnCancel']"
                     
        #弹出框第一行提示信息
        firstsumm=".//*[@id='$640f9fd5$grid']/div[2]/table/tbody/tr[1]/td[3]/div"
                       
        #弹出框第二行
        secoundsumm=".//*[@id='$640f9fd5$grid']/div[2]/table/tbody/tr[2]/td[3]/div"
            #提交发货后确认
        comfirm=".//*[@id='$a58c31c7$button1']"
            
        #一次一次进行提交
        for i in range(1,n):
            #订单id
            idxpath=".//*[@id='$390deff7$deliverMainGrid']/div[2]/table/tbody/tr["+str(i)+"]/td[5]/div"
            id=browser.findXpath(self.driver,idxpath).text
            #提交按钮             
            submitcheck=".//*[@id='$390deff7$deliverMainGrid']/div[2]/table/tbody/tr["+str(i)+"]/td[2]/input"
            submitcheck2=".//*[@id='$390deff7$deliverMainGrid']/div[2]/table/tbody/tr["+str(i-1)+"]/td[2]/input"
            #是否截停
            iscut=".//*[@id='$390deff7$deliverMainGrid']/div[2]/table/tbody/tr["+str(i)+"]/td[43]/div"
            cuttext=browser.findXpath(self.driver,iscut).text
            #取物流公司
            expressxpath=".//*[@id='$390deff7$deliverMainGrid']/div[2]/table/tbody/tr["+str(i)+"]/td[27]/div"
            express=browser.findXpath(self.driver, expressxpath).text.strip()
            #取物流单号
            expressnoxpath=".//*[@id='$390deff7$deliverMainGrid']/div[2]/table/tbody/tr["+str(i)+"]/td[28]/div"
            expressno=browser.findXpath(self.driver, expressnoxpath).text.strip()
                
            browser.findXpath(self.driver, submitcheck).click()
            browser.findXpath(self.driver, submit).click()
            '''   
            if browser.elementisexist(self.driver,secoundsumm)==True:
                browser.findXpath(self.driver, cancel).click()
                browser.findXpath(self.driver, submitcheck2).click()
            '''        
            #没有被截停的订单    
            if cuttext.strip()=='':
                if expressno!=''and express=='':
                    print id+":没有物流公司确有单号，逻辑错误"
                 
                try:    
                    #没有填写物流公司
                    if express=='':
                        
                        if browser.findXpath(self.driver, firstsumm).text=="未填写物流公司被过滤！":
                            browser.findXpath(self.driver, cancel).click()
                            print id+":订单未填写物流信息，测试成功"
                            #填上物流公司
                            express=".//*[@id='$390deff7$deliverMainGrid']/div[2]/table/tbody/tr["+str(i)+"]/td[27]/div"
                            browser.findXpath(self.driver,express).click()
                            time.sleep(2)
                            allexpress=".//*[@id='$390deff7$deliverMainGrid_freightbtypeid']"
                            browser.findXpath(self.driver,allexpress).send_keys(u"圆通速递")
                            time.sleep(2)
                            #定位动态元素
                            '''
                            flag="圆通速递"
                            st1="/html/body/div["
                            st2="]/table/tbody/tr[2]/td/div"
                            begin=7
                            end=6
                            btn=".//*[@id='$390deff7$deliverMainGrid']/div[2]/table/tbody/tr[1]/td[27]/table/tbody/tr/td[2]/div/div"
                            '''
                            btn=".//*[@id='$390deff7$deliverMainGrid']/div[2]/table/tbody/tr[1]/td[27]/table/tbody/tr/td[2]/div/div"
                            for n in range(9,16):
                                expath="html/body/div["+str(n)+"]/table/tbody/tr[2]/td/div"
                                if browser.elementisexist(self.driver,expath)==True:
                                    if browser.findXpath(self.driver,expath).text=="圆通速递":
                                        browser.findXpath(self.driver,expath).click()
                                        break
                        
                            time.sleep(1)
                            browser.findXpath(self.driver, submitcheck).click()
                            browser.findXpath(self.driver, submit).click()
                              
                        else:
                            print id+":未填写物流信息，提示框确没提示"
                    #没有填写物流单号
                    if expressno=='':
                        if browser.findXpath(self.driver, firstsumm).text.strip()=="未填写物流单号被过滤！":
                            browser.findXpath(self.driver, cancel).click()
                            print id+":该订单未填写物流单号，测试成功"
                            time.sleep(1)
                            #填上物流单号
                            xpath="//*[@id='$390deff7$deliverMainGrid_freightbillno']"
                            '''    
                            js = 'document.getElementById("$390deff7$deliverMainGrid_freightbillno").style.visibility="visible";'
                            self.driver.execute_script(js)
                            browser.findXpath(self.driver,xpath).send_keys(a)
                            '''
                            no=".//*[@id='$390deff7$deliverMainGrid']/div[2]/table/tbody/tr["+str(i)+"]/td[28]/div"
                            browser.findXpath(self.driver,no).click()
                            time.sleep(1)
                            a=string.join(random.sample(['0','1','2','3','4','5','6','7','8','9','7','8','9'], 12)).replace(" ","")
                            browser.findXpath(self.driver,xpath).send_keys(a)
                            time.sleep(1)
                            browser.findXpath(self.driver,submit).click()
                            time.sleep(1)
                        else:
                            print id+":未填写物流单号，提示框确没提示"
                
                except:
                    print(u"操作物流公司失败,测试失败")
                    print(traceback.format_exc()) 
                    
                try:
                    #有物流公司和单号进行发货
                    payxpath=".//*[@id='$390deff7$deliverMainGrid']/div[2]/table/tbody/tr["+str(i)+"]/td[11]/div"
                    #如果是已付款订单
                    if browser.findXpath(self.driver, payxpath).text.strip()!='':
                        #调用接口看订单是否已发货
                        f=open('E:\wei\sp.dat','r')
                        token=f.read()
                        print "token:"+token
                        
                        params={"order_id":id}
                        publics={"method":"vdian.order.get","access_token":token,"version":"1.0","format":"json"}
                        
                        payload={"param":json.dumps(params),"public":json.dumps(publics)}
                        url="http://api.vdian.com/api"
                        res=requests.post(url,data=payload)
                        
                        b=res.text
                        st=re.findall("status\":\"(.*?)\"",b)
                        for a in st:
                            orderstatus=a
                        print id+":"+orderstatus
                        #res=requests.get(url)
                        #url="http://api.vdian.com/api?param={"order_id":"18571688"}&public={"method":"vdian.order.get","access_token":"c5be93f3f2774f01c63a9c999d625a29","version":"1.0","format":"json"}"
                        ifsend="#.//*[@id='$695f1103$grid']/div[2]/table/tbody/tr/td[2]/div"
                        browser.findXpath(self.driver, comfirm).click()
                        #如果没有发过货
                        if orderstatus=='pay':
                            if browser.elementisexist(self.driver,ifsend)==False:
                                print id+":该订单填写了物流信息并且已经付款，发货成功,测试通过"
                            else:
                                print id+":该订单填写了物流信息并且已经付款，发货失败,测试不通过"
                                print orderstatus
                        #如果之前就发过货
                        else :
                            info=browser.findXpath(self.driver, ifsend).text
                            print id+":此为接口之间返回的信息，该订单之前已经发过货"
                            print info
                            print orderstatus
                    #如果是未付款订单
                    elif browser.findXpath(self.driver, payxpath).text.strip()=='':
                        #print "test:"+browser.findXpath(self.driver, firstsumm).text.strip()
                        if browser.findXpath(self.driver, firstsumm).text.strip()=='订单的交易状态为：未付款,点击继续将继续发货！':
                            browser.findXpath(self.driver, cancel).click()
                            #browser.findXpath(self.driver, comfirm).click()
                            print id+":该订单填写了物流信息但未付款，发货失败,测试通过"
                        else:
                            print id+":该订单填写了物流信息但未付款，发货失败,对话框提示信息不符合，测试不通过"
                    else :
                        print u"无提示信息，测试失败"
                except:
                    print(u"该订单填写了物流信息，发货失败,测试失败")
                    print(traceback.format_exc())
                    
            elif cuttext.strip()!='':
                browser.findXpath(self.driver, cancel).click()
                print id+":该订单被截停，发货失败，测试成功"
                
                    
            else:
                print u"改订单状态未知"
                print cuttext
                        
            browser.findXpath(self.driver, submitcheck).click()
      

    def testgetandcompareData(self):
        u'''将接口数据和页面数据进行对比'''
        try:
            #获取订单页面数据并放入列表
            aa='http://beefun.wsgjp.com/EShopDeliver/EShopDeliverList.gspx?caption=%B6%A9%B5%A5%B4%A6%C0%ED&tag=SimpleProcessStatus'
            headers = {'cookie':self.cookiestr,'Content-Type': 'application/json'}  

            #取页面数据
            b=browser.handleorderRead(self.driver,aa, headers)
            
            #从第5个开始，最后9个不要
            resaultpage=re.findall("(?<=tradeid).*?(?=tradeid)",b)           
            lisorder=[]
            lis=[]

            flag=0
            for sigle in resaultpage:
                if flag>=5 and flag<=(len(resaultpage)-9):
                    lisorder.append(sigle)
                flag=flag+1
            #print len(lisorder)
            #print lisorder[1]
            for a in lisorder:
                #print a
                result=re.compile("\"")
                z=result.sub('',a) 
                #print len(z)
                #print z
                c=re.findall(":(.*?),",z)
                lis.append(c)
    
            print len(lis)
            #print lis[1][0],lis[2][0]
        except:
            print(u"抓取页面数据失败")
            print(traceback.format_exc())
        
        #读取接口数据    
        path='D:/apiorderdetail.xml'
        tagname='responseData'
        aa=browser.apixmlRead(self.driver, path, tagname)

        #根据订单号进行比较
        flag=0
        try:
            for k in range(0,len(lis)):
                #print lis[k][0]
                if flag%2==1:
                    for v in range(0,len(aa)):
                        if lis[flag][0]==aa[v][9]:
                            #进行比较
                            
                            #买家姓名
                            
                            #买家账号
                            
                            #电话号码
                            
                            #手机号码
                            
                            
                            #付款时间
                            #提取页面时间戳
                            if lis[flag-1][8].strip()!='' and aa[v][26].strip()!='':
                                timestr=re.findall("\((.*?)\)",lis[flag-1][8])
                                dst = '.'.join(timestr)
                                timeint=int(dst)/1000
                                #转换接口时间为时间戳
                                timeArray = time.strptime(aa[v][26], "%Y-%m-%d %H:%M:%S")
                                timeStamp = int(time.mktime(timeArray))
                            
                                if timeint!=timeStamp:
                                    print u"订单编号："+lis[flag-1][0]
                                    print u"接口返回付款时间pay_time："+timeStamp
                                    print u"页面付款时间："+timeint
                                else:
                                    print "\n"
                            elif lis[flag-1][8].strip()=='null' and aa[v][26].strip()=='':
                                print "\n"
                            else:
                                print u"订单编号："+lis[flag-1][0]
                                print u"接口返回付款时间pay_time："+aa[v][26]
                                print u"页面付款时间："+lis[flag-1][8]+"\n"
                            #卖家备注
                            if aa[v][7].strip()!=lis[flag-1][6].strip():
                                print u"订单编号："+lis[flag-1][0]
                                print u"接口返回卖家备注express_note："+aa[v][7]
                                print u"页面卖家备注："+lis[flag-1][6]+"\n"
                            #买家备留言
                            if aa[v][19].strip()!=lis[flag-1][5].strip():
                                print u"订单编号："+lis[flag-1][0]
                                print u"接口返回买家留言note："+aa[v][19]
                                print u"页面买家留言："+lis[flag-1][5]+"\n"
                                
                            #订单金额
                            money=float(lis[flag-1][17])
                            moneyw=str("%.2f"%money) 
                            if moneyw!=aa[v][30]:
                                print u"订单号为："+lis[flag-1][0]
                                print u"订单页面金额："+moneyw
                                print u"api接口返回的数据price："+aa[v][30]+"\n"
                            
                            
                            #订单优惠金额    
                            
                            a1=float(aa[v][41])
                            a2=float(aa[v][30])
                            cc=a1-a2
                            apidis=float(cc)
                            apidisw=str("%.2f"%apidis)
                            #print apidisw
                            dis=float(lis[flag-1][18])
                            disw=str("%.2f"%dis) 
                            if str(disw)!=str(apidisw):
                                print u"订单号为："+lis[flag-1][0]
                                print u"订单页面查询的优惠金额："+str(disw)
                                print u"api接口返回的数据discount_amount ："+str(apidisw)+"\n"
                                
                            #金额
                            mytotal=float(lis[flag-1][19])
                            total=str("%.2f"%mytotal)
                            com=dis+money
                            comtr=str("%.2f"%com)
                            if total!=comtr:
                                print u"订单号为："+lis[flag-1][0]
                                print u"订单页面优惠金额："+str(dis)
                                print u"订单页面订单金额 ："+str(moneyw)
                                print u"订单页面金娥："+str(comtr)+"\n"
                                
                            #省份
                            if  (aa[v][38]+str("省"))!=lis[flag-1][52].strip(' '):
                                print u"订单号为："+lis[flag-1][0]
                                print u"页面省份："+lis[flag-1][52]
                                print u"api接口返回的数据province ："+aa[v][38]+"\n"
                                
                            #物流公司
                            if aa[v][10]=='null' and lis[flag-1][70].strip(' ')!='null':
                                print u"订单号为："+lis[flag-1][0]
                                print u"订单页面查询的物流公司："+lis[flag-1][70]
                                print u"api接口返回的数据express："+aa[v][10]+"\n"
                                
                            elif lis[flag-1][70].strip(' ')!=str(aa[v][10]):
                                print u"订单号为："+lis[flag-1][0]
                                print u"订单页面物流公司："+lis[flag-1][70]
                                print u"api接口返回的数据express："+aa[v][10]+"\n"
                                
                            #物流单号
                            if aa[v][62]=='null' and lis[flag-1][4].strip(' ')!='':
                                print u"订单号为："+lis[flag-1][0]
                                print u"订单页面查询的物流单号："+lis[flag-1][4]
                                print u"api接口返回的数据express_no："+aa[v][62]+"\n"
                            if lis[flag-1][4].strip(' ')!='' and aa[v][62]!='null':
                                if lis[flag-1][4].strip(' ')!=aa[v][62]:
                                    print u"订单号为："+lis[flag-1][0]
                                    print u"订单页面物流单号："+lis[flag-1][4]
                                    print u"api接口返回的数据express_no："+aa[v][62]+"\n"
                            if lis[flag-1][4].strip(' ')=='' and   aa[v][62]!='null':
                                print u"订单号为："+lis[flag-1][0]
                                print u"订单页面物流单号："+lis[flag-1][4]
                                print u"api接口返回的数据express_no："+aa[v][62]+"\n"
                                
                            #网店名称
                            if aa[v][1]!= lis[flag-1][68].strip(' '):
                                print u"订单号为："+lis[flag-1][0]
                                print u"订单页面查询的网店名称："+lis[flag-1][68]
                                print u"api接口返回的数据dseller_name："+aa[v][1]+"\n"
                                
                            #退款状态为正常
                            if lis[flag-1][61].strip(' ')=='0' and (aa[v][57]!='null}' or aa[v][56]!='{buyer_refund_fee:null'):
                                print u"订单号为："+lis[flag-1][0]
                                print u"api接口buyer_refund_fee:"+aa[v][56]
                                print u"api接口refund_time:"+aa[v][57]
                                print u"订单页面："+lis[flag-1][61]+"\n"
                            
                            #交易状态
                            if lis[flag-1][25]==('1' or '2'or '3'or '4'or '5'):
                                if aa[v][22]=='unpay' and lis[flag-1][25]!='1':
                                    print u"订单号为："+lis[flag-1][0]
                                    print u"订单页面交易状态："+lis[flag-1][25]+u"(1:未付款订单;2:已付款订单;3:已发货订单;4:交易成功订单;5:交易关闭订单;6:部分发货)"
                                    print u"api接口返回的数据status："+aa[v][22]+"\n"
                                
                                if aa[v][22]=='pay' and lis[flag-1][25]!='2':
                                    print u"订单号为："+lis[flag-1][0]
                                    print u"订单页面交易状态："+lis[flag-1][25]+u"(1:未付款订单;2:已付款订单;3:已发货订单;4:交易成功订单;5:交易关闭订单;6:部分发货)"
                                    print u"api接口返回的数据status："+aa[v][22]+"\n"
                                
                                if aa[v][22]=='ship' and lis[flag-1][25]!='3':
                                    print u"订单号为："+lis[flag-1][0]
                                    print u"订单页面交易状态："+lis[flag-1][25]+u"(1:未付款订单;2:已付款订单;3:已发货订单;4:交易成功订单;5:交易关闭订单;6:部分发货)"
                                    print u"api接口返回的数据status："+aa[v][22]+"\n"
                                    
                                if aa[v][22]=='close' and lis[flag-1][25]!='5':
                                    print u"订单号为："+lis[flag-1][0]
                                    print u"订单页面交易状态："+lis[flag-1][25]+u"(1:未付款订单;2:已付款订单;3:已发货订单;4:交易成功订单;5:交易关闭订单;6:部分发货)"
                                    print u"api接口返回的数据status："+aa[v][22]+"\n"
                                
                                if aa[v][22]=='finish' and lis[flag-1][25]!='4':
                                    print u"订单号为："+lis[flag-1][0]
                                    print u"订单页面交易状态："+lis[flag-1][25]+u"(1:未付款订单;2:已付款订单;3:已发货订单;4:交易成功订单;5:交易关闭订单;6:部分发货)"
                                    print u"api接口返回的数据status："+aa[v][22]+"\n"
                            if lis[flag-1][25]!=('1' or '2'or '3'or '4'or '5'):  
                                print u"订单号为："+lis[flag-1][0]
                                print u"订单页面无此交易状态："+lis[flag-1][25]+u"(1:未付款订单;2:已付款订单;3:已发货订单;4:交易成功订单;5:交易关闭订单;6:部分发货)"
                                print u"api接口返回的数据status："+aa[v][22]+"\n"
                            
                            #买家运费
                            con=float(lis[flag-1][41])
                            conw=str("%.2f"%con) 
                            if conw!=aa[v][24]:
                                print u"订单号为："+lis[flag-1][0]
                                print u"订单页面查询的买家运费："+conw
                                print u"api接口返回的数据express_fee_num："+aa[v][24]
                                print u"接口和页面数据不同\n"
                            #收货地址
                            if lis[flag-1][60].strip(' ')!=aa[v][35].replace(' ','省'):
                                print u"订单号为："+lis[flag-1][0]
                                print u"订单页面收货地址："+lis[flag-1][60]
                                print u"api接口返回的数据address："+aa[v][35]
                                print u"接口和页面数据不同\n"
                            
                            #交易类型
                            if lis[flag-1][69].strip(' ')=='3' and aa[v][11].strip(' ')!=u"货到付款":
                                print u"订单号为："+lis[flag-1][0]
                                print u"订单页面交易类型："+lis[flag-1][69]
                                print u"api接口返回的数据order_type_des："+aa[v][11]
                                print u"接口和页面数据不同\n"
                                
                            if  (aa[v][11].strip(' ')==u"担保交易" or aa[v][11].strip(' ')==u"直接交易" ) and lis[flag-1][69].strip(' ')!='0' :
                                print u"订单号为："+lis[flag-1][0]
                                print u"订单页面交易类型："+lis[flag-1][69]
                                print u"api接口返回的数据order_type_des："+aa[v][11]
                                print u"接口和页面数据不同\n"
                                
                            if lis[flag-1][69].strip(' ')!=('0'or '3'):
                                print u"订单号为："+lis[flag-1][0]
                                print u"订单页面交易类型："+lis[flag-1][69]
                                print u"api接口返回的数据order_type_des："+aa[v][11]
                                print u"无此交易类型\n"
                            #创建方式  
                flag=flag+1
                            
        except:
            print(u"订单数据比较失败")
            print(traceback.format_exc())
        #print("下载时间，")
        pass

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()