#-*- coding:UTF-8 -*-
'''
Created on 2016��4��5��

@author: xsx
'''

import unittest
from common import browserOperation
from common import baseinfo
import time
import traceback
import os
import  xml.dom.minidom
import re

class orderSearchtest(unittest.TestCase):


    def setUp(self):
        self.driver=browserOperation.startBrowser('chrome')
        self.driver.get("http://71.wsgjp.com.cn")
        self.driver.maximize_window()
        self.name='$8a3327cd$corpName'
        self.user='$8a3327cd$userName'
        self.pwd='$8a3327cd$pwdEdit'
        self.login='$8a3327cd$btnLogin'
        browserOperation.loginUser(self.driver,self.name ,self.user,self.pwd,self.login)
        self.driver.implicitly_wait(30)
        
        module=".//*[@id='$a453b9d8$mnuRoot3']/div"
        ordermodule=".//*[@id='$a453b9d8$mnuRoot3_2']/td[3]"
        ordername=".//*[@id='$a453b9d8$mnuRoot3_2_1']/td[3]"
        browserOperation.openModule3(self.driver, module, ordermodule, ordername)
        
        pass


    def tearDown(self):
        print('test over')
        self.driver.close()
        
        pass
    


    def testCreatesearchorder(self):
        u'''检索订单查询页面并提取数据'''    
        #选择日期
        searchbtn=".//*[@id='$2fbb1d58$button5']"
        '''
        enddate=".//*[@id='$2fbb1d58$edEndDate']"
        begindate=".//*[@id='$2fbb1d58$edBeginDate']"
        
        n=3
        end=self.driver.find_element_by_xpath(enddate).get_attribute("title")
        
        newdate=baseinfo.timeoperate(end,n)
        self.driver.find_element_by_xpath(begindate).clear()
        self.driver.find_element_by_xpath(begindate).send_keys(newdate)
        browserOperation.accreditErp(self.driver,searchbtn)
        '''
        #选择网店
        shop='18080107102'
        
        btn=".//*[@id='$2fbb1d58$bLeft']/table/tbody/tr[2]/td[2]/table/tbody/tr[1]/td[2]/table/tbody/tr/td[2]/div/div"
        begin=37
        end=60
        browserOperation.selectshop(self.driver,shop,begin,end,btn)   
        browserOperation.accreditErp(self.driver,searchbtn)
        print("网店设置完成")
        #将检索数据写入到列表和文件
        path='D:\search.txt'
        methon1='a+'
        methon2='w'
        str1='\n'
        str2=';'
        searchpath="$2fbb1d58$c_grid"
        time=59
        data=''
        baseinfo.writefilemethon(self.driver, path, data,methon2, data)   
        try:    
            orderlist=baseinfo.extractdata(self.driver,searchpath,time)
            for a in orderlist:
                for b in a:
                    baseinfo.writefilemethon(self.driver, path, b, methon1, str2)
                baseinfo.writefileonly(self.driver, path, methon1, str1)
        except:
            print(u"将订单列表写入到文件失败")
            print(traceback.format_exc())
        #time.sleep(5)
        pass
 
    def testSearchcompare(self):
        u'''对比订单查询页面数据'''
        '''
        os.system("D:\workspace\PythonCase\src\demo\compare.py")
        '''
        #读取xml文件
        #进行一次提取,订单总数
        dom = xml.dom.minidom.parse('D:/apiordertotal420.xml')
        root = dom.documentElement
        bb = root.getElementsByTagName('responseData')

        b1=bb[0]
        c=b1.firstChild.data
        ff=[]

        resault=re.findall(":(.*?),",c)
        #resault1=re.findall("\"img\":\"(.+?)\"",c)

        for n in range(0,(len(resault)-3)/22):
            ff.append(resault[(2+n*22):(2+(n+1)*22)])
        '''
        print len(ff)
        for n in range(0,len(ff)):
        print ff[n][4]

        #读取ERP创建订单前台数据
        fil=open('D:\createorder.txt','r')
        createlis=[]
        for small in fil.readlines():
            createlis.append(small.split(';'))

       for j in range(0,len(createlis)):
           print createlis[j][0]
       print len(createlis)

      '''
    
        #订单详情list,xml一次性提取分别放入列表中            


        domc = xml.dom.minidom.parse('D:/apiorderdetail420.xml')
        rootc = domc.documentElement
        detail = rootc.getElementsByTagName('responseData')

        aa=[]

        for m in range(0,len(detail)):
            detail1=detail[m]
            cc=detail1.firstChild.data
            #print c
            resault=re.findall(":(.*?),",cc)
            #resault1=re.findall("\"img\":\"(.+?)\"",c)
            aa.append(resault)
            #aa.append(resault1)
        #print aa


        #读取txt文件


        #读取ERP订单查询前台数据
        f=open('D:\search.txt','r')
        deatillis=[]
        for small in f.readlines():
            deatillis.append(small.split(';'))

        #print deatillis
        #print len(aa)
        #订单查询比对

        for k in range(0,len(deatillis)):
            #print "detail(txt):"+deatillis[k][8]
            for v in range(0,len(aa)):
                #print "aa(txt):"+aa[v][9]
                if deatillis[k][8]==aa[v][9]:
                    #下单时间
                    if deatillis[k][1].strip(' ')!=aa[v][58]:
                        print "订单号为："+deatillis[k][8]
                        print "订单页面查询下单时间："+deatillis[k][1]
                        print "api接口返回的数据为add_time："+aa[v][58]
                        print "下单时间，接口和页面数据不同\n"

                    #收货人
                    if deatillis[k][2]!=aa[v][37]:
                        print "订单号为："+deatillis[k][8]
                        print "订单页面查询收货人："+deatillis[k][2]
                        print "api接口返回的数据为name："+aa[v][37]
                        print "收货人，接口和页面数据不同\n"
                    #买家账号
                    if deatillis[k][3]!=aa[v][3]:
                        print "订单号为："+deatillis[k][8]
                        print "订单页面查询的买家账号："+deatillis[k][3]
                        print "api接口返回的数据buyer_id："+aa[v][3]
                        print "收货人，接口和页面数据不同(接口返回就是0)\n"
            
                    #付款时间
                    if deatillis[k][4].strip(' ')!=aa[v][26]:
                        #print len(deatillis[k][4])
                        #print len(aa[v][26])
                        print "订单号为："+deatillis[k][8]
                        print "订单页面查询的付款时间："+deatillis[k][4]
                        print "api接口返回的数据pay_time："+aa[v][26]
                        print "接口和页面数据不同\n"
                
                    #退款状态
                    if deatillis[k][11]!="正常" and (aa[v][22]=="unpay" or aa[v][22]=="pay" or aa[v][22]=="ship"or aa[v][22]=="accept"or aa[v][22]=="finish" or aa[v][22]=="close"):
                        print "订单号为："+deatillis[k][8]
                        print "订单页面查询的退款状态："+deatillis[k][11]
                        print "api接口返回的数据status："+aa[v][22]
                        print "接口和页面数据不同\n"
                
                    #留言    
                    if deatillis[k][19]=='' and (deatillis[k][20]!='' or deatillis[k][21]!=''):
                        print "订单号为："+deatillis[k][8]
                        print "有买家或者卖家留言，留言却无标记\n"
                    if deatillis[k][19]!='' and (deatillis[k][20]=='' or deatillis[k][21]==''):
                        print "订单号为："+deatillis[k][8]
                        print "没有有买家或者卖家留言，留言却有标记\n"

                    #买家留言
                    if deatillis[k][20].strip(' ')!=aa[v][19]:
                        print "订单号为："+deatillis[k][8]
                        print "订单页面查询的买家留言："+deatillis[k][20]
                        print "api接口返回的数据note："+aa[v][19]
                        print "接口和页面数据不同\n"
                    

  
                    #卖家留言
                    if deatillis[k][21].strip(' ')!=aa[v][7]:
                        print "订单号为："+deatillis[k][8]
                        print "订单页面查询的卖家留言："+deatillis[k][21]
                        print "api接口返回的数据express_note："+aa[v][7]
                        print "接口和页面数据不同\n"


                    #货到付款
                    if deatillis[k][23]=='' and deatillis[k][11]=="货到付款" :
                        print "货到付款订单却无标记\n"
                    if deatillis[k][23]!=' ' and deatillis[k][11]!="货到付款":
                        print "不是货到付款订单却有标记\n"
            
            
                    #金额
                    money=float(deatillis[k][24])
                    moneyw=str("%.2f"%money) 
                    if moneyw!=aa[v][49]:
                        print "订单号为："+deatillis[k][8]
                        print "订单页面查询的金额："+moneyw
                        print "api接口返回的数据total_price："+aa[v][49]
                        print "接口和页面数据不同\n"

                    #订单原金额
            
                    if deatillis[k][25]!=deatillis[k][24]+deatillis[k][26]:
                        print "订单号为："+deatillis[k][8]
                        print "订单页面查询的订单原金额："+deatillis[k][25]
                        print "订单页面查询的金额："+deatillis[k][24]
                        print "订单页面查询的优惠："+deatillis[k][26]
                        print "金额+优惠=原单\n"

            
                    #优惠金额
                    apidis=float(aa[v][27])
                    apidisw=str("%.2f"%apidis)
                    #print apidisw
                    dis=float(deatillis[k][26])
                    disw=str("%.2f"%dis) 
                    if str(disw)!=str(apidisw):
                        print "订单号为："+deatillis[k][8]
                        print "订单页面查询的优惠金额："+str(disw)
                        print "api接口返回的数据discount_amount ："+str(apidisw)
                        print "接口和页面数据不同\n"
            
                    
                    #省份
                    if deatillis[k][28].strip(' ')!=(aa[v][38]+str("省")):
                        print "订单号为："+deatillis[k][8]
                        print "订单页面查询的省份："+deatillis[k][28]
                        print "api接口返回的数据province ："+aa[v][38]
                        print "接口和页面数据不同\n"
                    #物流公司
                    if deatillis[k][29].strip(" ")!='' and aa[v][10]=="null":
                        print "订单号为："+deatillis[k][8]
                        print "订单页面查询的物流公司："+deatillis[k][29]
                        print "api接口返回的数据express："+aa[v][10]
                        print "接口和页面数据不同\n"
                    if deatillis[k][29].strip(" ")=='' and aa[v][10]!="null":
                        print "订单号为："+deatillis[k][8]
                        print "订单页面查询的物流公司："+deatillis[k][29]
                        print "api接口返回的数据express："+aa[v][10]
                        print "接口和页面数据不同\n"    
                    if deatillis[k][29].strip(" ")!='' and aa[v][10]!="null":
                        if deatillis[k][29].strip(' ')!=aa[v][10]:
                            print "订单号为："+deatillis[k][8]
                            print "订单页面查询的物流公司："+deatillis[k][29]
                            print "api接口返回的数据express："+aa[v][10]
                            print "接口和页面数据不同\n"
            
                    #物流单号
                    if deatillis[k][30].strip(' ')!='' and aa[v][62]=="null":
                        print "订单号为："+deatillis[k][8]
                        print "订单页面查询的单号："+deatillis[k][30]
                        print "api接口返回的数据express_no ："+aa[v][62]
                        print "接口和页面数据不同\n"
                
                    if deatillis[k][30].strip(" ")=='' and aa[v][10]!="null":
                        print "订单号为："+deatillis[k][8]
                        print "订单页面查询的物流公司："+deatillis[k][30]
                        print "api接口返回的数据express："+aa[v][10]
                        print "接口和页面数据不同\n" 
                    if deatillis[k][30].strip(" ")!='' and aa[v][10]!="null":         
                        if deatillis[k][30].strip(' ')!=aa[v][62]:
                            print "订单号为："+deatillis[k][8]
                            print "订单页面查询的单号："+deatillis[k][30]
                            print "api接口返回的数据express_no ："+aa[v][62]
                            print "接口和页面数据不同\n"
            
                    #发货日期
                    if deatillis[k][31].strip(' ')!='' and aa[v][13]=="null":
                        print "订单号为："+deatillis[k][8]
                        print "订单页面查询的省份："+deatillis[k][30]
                        print "api接口返回的数据send_time ："+aa[v][13]
                        print "接口和页面数据不同\n"
                    if deatillis[k][31].strip(' ')=='' and aa[v][13]!="null":
                        print "订单号为："+deatillis[k][8]
                        print "订单页面查询的省份："+deatillis[k][30]
                        print "api接口返回的数据send_time ："+aa[v][13]
                        print "接口和页面数据不同\n"
                    if deatillis[k][31].strip(' ')!='' and aa[v][13]!="null":               
                        if deatillis[k][31].strip(' ')!=aa[v][13]:
                            print "订单号为："+deatillis[k][8]
                            print "订单页面查询的省份："+deatillis[k][31]
                            print "api接口返回的数据send_time ："+aa[v][13]
                            print "接口和页面数据不同\n"
                    
                    #网店名称
                    if deatillis[k][34].strip(' ')!=aa[v][1]:
                        print "订单号为："+deatillis[k][8]
                        print "订单页面查询的网店名称："+deatillis[k][34]
                        print "api接口返回的数据dseller_name："+aa[v][1]
                        print "接口和页面数据不同\n"
                            
                    #订单来源
                    if deatillis[k][37]!="微店":
                        print "订单来源出错"+deatillis[k][37]
                    
                    #交易状态
                    if deatillis[k][44].strip(' ')=="等待付款订单" and aa[v][22]!="unpay":
                        print "订单号为："+deatillis[k][8]
                        print "订单页面查询的网店名称："+deatillis[k][44]
                        print "api接口返回的数据status："+aa[v][22]
                        print "接口和页面数据不同\n"        
                    
                    if deatillis[k][44].strip(' ')=="已付款订单" and aa[v][22]!="pay":
                        print "订单号为："+deatillis[k][8]
                        print "订单页面查询的网店名称："+deatillis[k][44]
                        print "api接口返回的数据status："+aa[v][22]
                        print "接口和页面数据不同\n"         
                    if deatillis[k][44].strip(' ')=="交易成功" and aa[v][22]!="finish":
                        print "订单号为："+deatillis[k][8]
                        print "订单页面查询的网店名称："+deatillis[k][44]
                        print "api接口返回的数据status："+aa[v][22]
                        print "接口和页面数据不同\n" 
                    if deatillis[k][44].strip(' ')=='':
                        print "订单号为："+deatillis[k][8]
                        print "订单页面查询的网店名称："+deatillis[k][44]
                        print "api接口返回的数据status："+aa[v][22]
                        print "接口和页面数据不同\n" 
                    if deatillis[k][44].strip(' ')=='未知' and aa[v][22]!="":
                        print "订单号为："+deatillis[k][8]
                        print "订单页面查询的网店名称："+deatillis[k][44]
                        print "api接口返回的数据status："+aa[v][22]
                        print "接口和页面数据不同\n"       
                    
                    #买家运费
                    con=float(deatillis[k][45])
                    conw=str("%.2f"%con) 
                    if conw!=aa[v][24]:
                        print "订单号为："+deatillis[k][8]
                        print "订单页面查询的买家运费："+conw
                        print "api接口返回的数据express_fee_num："+aa[v][24]
                        print "接口和页面数据不同\n"     
                     
                    '''         
                    #单据摘要
                    if deatillis[k][49]!=aa[v][24]:
                        print "订单号为："+deatillis[k][8]
                        print "订单页面查询的买家运费："+deatillis[k][49]
                        print "api接口返回的数据express_fee_num："+aa[v][24]
                        print "接口和页面数据不同\n" 
                    '''        
                    #收货地址
                    if deatillis[k][50].strip(' ')!=aa[v][35].strip(' '):
                        print "订单号为："+deatillis[k][8]
                        print "订单页面查询的收货地址："+deatillis[k][50]
                        print "api接口返回的数据address："+aa[v][35]
                        print "接口和页面数据不同\n"          
                    
        print "接口未返回交易成功时间，重量，称重异常，称重状态，验货状态，经手人，旗帜，包含手工日志"
        print "erp:单据编号，是否同步，处理状态，退款状态目前只有正常，物流方式仓库，锁定说明，发货备注，配货员，验货员，发货员，物流单打印，配货单打印，物流成本，订单类型，锁定状态"
        print "暂时未处理：收货人联系方式"


        pass
   
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    #unittest.main(defaultTest='suite')
    unittest.main()
