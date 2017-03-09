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
from selenium.webdriver.common.keys import Keys
class ordercreateandcheckTest(unittest.TestCase):


    def setUp(self):
        self.driver=browserOperation.startBrowser('chrome')
        self.driver.get("http://71.wsgjp.com.cn")
        self.driver.maximize_window()
        self.name='$8a3327cd$corpName'
        self.user='$8a3327cd$userName'
        self.pwd='$8a3327cd$pwdEdit'
        self.login='$8a3327cd$btnLogin'
        browserOperation.loginUser(self.driver,self.name ,self.user,self.pwd,self.login)
        time.sleep(7)
        module=".//*[@id='$a453b9d8$mnuRoot3']/div"
        ordermodule=".//*[@id='$a453b9d8$mnuRoot3_2']/td[3]"
        ordername=".//*[@id='$a453b9d8$mnuRoot3_2_0']/td[3]"
        browserOperation.openModule3(self.driver, module, ordermodule, ordername)
        pass


    def tearDown(self):
        print('test over')
        self.driver.close()
        time.sleep(5)
        pass


    def testCreateorder(self):
        u'''下载订单'''
        orderbtn1=".//*[@id='$8b74f50b$button1']"
        orderbtn2=".//*[@id='$8b74f50b$createTrade0']/td[3]"

        
       
        okbtn=".//*[@id='$9073ce9d$btnOk']"
        cancelbtn=".//*[@id='$9073ce9d$btnCancel']"
        begin=38
        end=70
        shop='18080107102'
        time.sleep(5)
        self.driver.find_element_by_xpath(orderbtn1).click()
        time.sleep(5)
        self.driver.find_element_by_xpath(orderbtn2).click()
        time.sleep(3)   
        
        try:
            for a in range(begin,end):               
                btn1="/html/body/table[8]/tbody/tr[2]/td/div/div/table/tbody/tr/td/table/tbody/tr[2]/td[2]/div/table/tbody/tr[3]/td[2]/table/tbody/tr[2]/td[4]/table/tbody/tr[1]/td[2]/table/tbody/tr[2]/td[2]/table/tbody/tr/td[2]/div/div"     
                self.driver.find_element_by_xpath(btn1).click()
                xpath1='html/body/div[' + str(a) + ']/table/tbody/tr[8]/td/div' 
                print xpath1  
                baseinfo.elementisexist(self.driver,xpath1)                                
                if baseinfo.elementisexist(self.driver,xpath1)==True:                    
                    if self.driver.find_element_by_xpath(xpath1).text==str(shop):   
                        print self.driver.find_element_by_xpath(xpath1).text                                           
                        self.driver.find_element_by_xpath(".//*[@id='$9073ce9d$edEShop']").click()                      
                        self.driver.find_element_by_xpath(btn1).click()                     
                        self.driver.find_element_by_xpath(xpath1).click()
                        break             
            try:
                for n in range(1,4):
                    btn2="html/body/table[8]/tbody/tr[2]/td/div/div/table/tbody/tr/td/table/tbody/tr[2]/td[2]/div/table/tbody/tr[3]/td[2]/table/tbody/tr[2]/td[4]/table/tbody/tr[1]/td[2]/table/tbody/tr[2]/td[4]/table/tbody/tr/td[2]/div/div"
                    self.driver.find_element_by_xpath(btn2).click()
                    xpath2='html/body/div[' + str(a+1) + ']/table/tbody/tr['+str(n)+']/td/div'
                    print self.driver.find_element_by_xpath(xpath2).text
                    self.driver.implicitly_wait(5)
                    self.driver.find_element_by_xpath(xpath2).click()
                    print(u"获取状态"+str(n)+"元素成功")
                    self.driver.find_element_by_xpath(okbtn).click() 
                    time.sleep(15)           
                try:
                    self.driver.find_element_by_xpath(cancelbtn).click()
                    baseinfo.accalert(self.driver)
                    time.sleep(10)
                        
                except:
                    print(u"保存失败")
                    print(traceback.format_exc())

            except:
                print(u"获取状态"+str(n)+"元素失败")
                print(traceback.format_exc())                           
        
        
        except:
            print(u"订单创建失败")
            print(traceback.format_exc())
        
        pass
    
    def testOrdercheck(self):
        u'''审核订单'''
        #进行审核
        checkbtn=".//*[@id='$8b74f50b$button6']"
        checkthisbtn=".//*[@id='$8b74f50b$auditTrade1']/td[3]"
        ordernum=".//*[@id='$e0a78471$grid_column0']/div"
        falsereason=".//*[@id='$e0a78471$grid_column1']/div"
        deal=".//*[@id='$e0a78471$grid_column2']/div"
        alertclose=".//*[@id='$e0a78471$btnClose']"
        nomatch=".//*[@id='$e0a78471$grid']/div[2]/table/tbody/tr/td[3]/div "
        checkokbtn=".//*[@id='$b452a789$button1']"
        checkfailclose=".//*[@id='$65495eb2$btnClose']"

        selectpeople=".//*[@id='$33ce728a$btnSelect']"
        enter=".//*[@id='$b452a789$edTarget']"
        try:
            for times in range(1,100):
                title=".//*[@id='$8b74f50b$c_grid_Audit']/div[2]/table/tbody/tr["+str(times)+"]/td[3]/div"
                if baseinfo.elementisexist(self.driver,title)==False:
                    break
        except:
            print(u"获取行数失败")
            print(traceback.format_exc()) 
                
        #flagxpath=".//*[@id='$8b74f50b$c_grid_Audit']/div[2]/table/tbody/tr[1]/td[3]/div"
        #flagtext=self.driver.find_element_by_xpath(flagxpath).text
        nowlines=times-1
        m=1
        
        for n in range(1,times):
            
            #totalxpath=".//*[@id='$8b74f50b$c_grid_Audit']/div[2]/table/tbody/tr["+str(n)+"]/td[3]/div"
            lock=".//*[@id='$8b74f50b$c_grid_Audit']/div[2]/table/tbody/tr["+str(m)+"]/td[41]/div"   
            check=".//*[@id='$8b74f50b$c_grid_Audit']/div[2]/table/tbody/tr["+str(m)+"]/td[2]/input" 
            people=".//*[@id='$8b74f50b$c_grid_Audit']/div[2]/table/tbody/tr["+str(m)+"]/td[35]/div"       
            checkall=".//*[@id='$8b74f50b$c_grid_Audit_column0']/div/table/tbody/tr/td/input"
            try:
                time.sleep(2)
                self.driver.find_element_by_xpath(checkall).click()
                time.sleep(5)
                self.driver.find_element_by_xpath(checkall).click()              
                self.driver.find_element_by_xpath(check).click()
                time.sleep(5)    
                self.driver.find_element_by_xpath(checkbtn).click()
                self.driver.implicitly_wait(5)
                self.driver.find_element_by_xpath(checkthisbtn).click()
                print ("本次执行第m列:"+str(m))
            except:
                print(u"打开审核小窗口失败")
                print(traceback.format_exc())
                
            try:
                if self.driver.find_element_by_xpath(lock).text==' ':
                    print ('此订单未锁定')
                    if baseinfo.elementisexist(self.driver,alertclose)==True:
                        dd=self.driver.find_element_by_xpath(nomatch).text
                        if dd==u'订单与本地商品未对应':
                            print(u"次订单未锁定，审核时商品未对应，测试成功")
                            self.driver.find_element_by_xpath(alertclose).click()                      
                        else :
                            print(u"次订单未锁定，应该出现审核时商品未对应，测试失败")
                            self.driver.find_element_by_xpath(alertclose).click()
                     
                    
                    elif  baseinfo.elementisexist(self.driver,enter)==True:
                        print("此订单已对应，可以进行审核")
                        time.sleep(5)
                        if self.driver.find_element_by_xpath(people).text==' ':
                            self.driver.find_element_by_xpath(enter).send_keys(Keys.ENTER)
                            self.driver.find_element_by_xpath(selectpeople).click()
                            self.driver.find_element_by_xpath(checkokbtn).click()
                    
                            if baseinfo.elementisexist(self.driver,checkfailclose)==True:
                                self.driver.find_element_by_xpath(checkfailclose).click()
                                #failcheckreason=".//*[@id='$e0a78471$grid']/div[2]/table/tbody/tr/td[3]"                
                                print "审核失败，可能是因为库存不足"
                                #print driver.find_element_by_xpath(failcheckreason).text
                                self.driver.find_element_by_xpath(alertclose).click()
                       
                    
                        
                elif self.driver.find_element_by_xpath(lock).text!='' :
                    print("此订单已锁定")
                    '''
                    aa=self.driver.find_element_by_xpath(ordernum).text
                    bb=self.driver.find_element_by_xpath(falsereason).text
                    cc=self.driver.find_element_by_xpath(deal).text
                    '''
                    self.driver.find_element_by_xpath(alertclose).click()
            except:
                    print(u"订单审核出错")
                    print(traceback.format_exc())
                
            try:
                for lines in range(1,10):
                    totalnow=".//*[@id='$8b74f50b$c_grid_Audit']/div[2]/table/tbody/tr["+str(lines)+"]/td[3]/div"
                    if baseinfo.elementisexist(self.driver,totalnow)==False:
                        break
                afterlines=lines-1
                if nowlines==afterlines:
                    m=m+1            
                nowlines=afterlines
            except:
                print(u"取列数失败")
                print(traceback.format_exc())

                    
                       
        print 'test over3'   
        pass
   
    def testWritedate(self):
        u'''提取订单创建页面数据'''
        path='D:\createorder.txt'
        methon1='a+'
        methon2='w'
        str1='\n'
        str2=';'
        data=''
        searchpath="$8b74f50b$c_grid_Audit"
        times=45
        
        unpay="//*[@id='$8b74f50b$dd_tradestatus_check1']"
        time.sleep(5)
        self.driver.find_element_by_xpath(unpay).click()
        
        time.sleep(2)
        serachcheck=".//*[@id='$8b74f50b$button8']"
        self.driver.find_element_by_xpath(serachcheck).click()
        
        baseinfo.writefilemethon(self.driver, path, data, methon2, data)   
        try:    
            createlist=baseinfo.extractdata(self.driver,searchpath,times)
            
            for a in createlist:
                for b in a:
                    baseinfo.writefilemethon(self.driver, path, b, methon1, str2)
                baseinfo.writefileonly(self.driver, path, methon1, str1)
            
        except:
            print(u"将订单列表写入到文件失败")
            print(traceback.format_exc())
        pass


    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()