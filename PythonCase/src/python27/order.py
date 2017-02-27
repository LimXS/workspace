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

class orderTest(unittest.TestCase):


    def setUp(self):
        self.driver=browserOperation.startBrowser('firefox')
        self.driver.get("http://71.wsgjp.com.cn")
        self.driver.maximize_window()
        self.name='$8a3327cd$corpName'
        self.user='$8a3327cd$userName'
        self.pwd='$8a3327cd$pwdEdit'
        self.login='$8a3327cd$btnLogin'
        browserOperation.loginUser(self.driver,self.name ,self.user,self.pwd,self.login)
        self.driver.implicitly_wait(30)
        pass


    def tearDown(self):
        print('test over')
        self.driver.close()
        
        pass
    
    def testAccredit(self):
        u'''进行授权'''
        time.sleep(3)
        modulename=".//*[@id='$a453b9d8$mnuRoot11']/div"
        moduledetail=".//*[@id='$a453b9d8$mnuRoot11_4']/td[3]"
        modulenade=".//*[@id='$a453b9d8$mnuRoot11_4_1']/td[3]"
        ass=".//*[@id='$f554ba1$grid']/div[2]/table/tbody/tr[8]/td[8]/div/a/font"
        browserOperation.openModule3(self.driver, modulename, moduledetail, modulenade)
        self.driver.implicitly_wait(30)
        browserOperation.accreditErp(self.driver,ass)
        baseinfo.accalert(self.driver)
        baseinfo.browserchange(self.driver)
        loginname="tele"
        password="password"
        loginbtn="J_LoginBtn"
        acc=".//*[@id='outer']/div/div[2]/form/div/div[2]/div/p/input[1]"
        self.driver.implicitly_wait(30)
        if baseinfo.elementisexist(self.driver, acc)==True:
            browserOperation.accreditErp(self.driver,acc)
        elif baseinfo.elementisexist(self.driver, acc)==False:            
            browserOperation.acccomfirm(self.driver, loginname, password, loginbtn,acc)
        
        pass
'''
    def testCreateorder(self):
        
        module=".//*[@id='$a453b9d8$mnuRoot3']/div"
        ordermodule=".//*[@id='$a453b9d8$mnuRoot3_2']/td[3]"
        ordername=".//*[@id='$a453b9d8$mnuRoot3_2_0']/td[3]"
        browserOperation.openModule3(self.driver, module, ordermodule, ordername)
        #参数
        checkboxfirst=".//*[@id='$8b74f50b$c_grid_Audit']/div[2]/table/tbody/tr[1]/td[2]/input"
        checkboxall=".//*[@id='$8b74f50b$c_grid_Audit_column0']/div/table/tbody/tr/td/input"
        deletebtn=".//*[@id='$8b74f50b$c_delbill']"
        waitecheck=".//*[@id='$8b74f50b$dd_tradestatus_check1']"
        
        #统计7日内订单总数
        enddate=".//*[@id='$8b74f50b$edEndDate']"
        begindate=".//*[@id='$8b74f50b$edBeginDate']"
        searchbtn=".//*[@id='$8b74f50b$button8']"
        n=7
        end=self.driver.find_element_by_xpath(enddate).get_attribute("title")
        
        #设置日期并进行检索 
        newdate=baseinfo.timeoperate(end,n)
        self.driver.find_element_by_xpath(begindate).clear()
        self.driver.find_element_by_xpath(begindate).send_keys(newdate)
        self.driver.find_element_by_xpath(waitecheck).click()
        browserOperation.accreditErp(self.driver,searchbtn)
        try:
            
            if baseinfo.elementisexist(self.driver, checkboxfirst)==True:
                #删除操作
                self.driver.find_element_by_xpath(checkboxall).click()                
                #删除所有订单，之后再重新下载
                #self.driver.find_element_by_xpath(deletebtn).click()  
                #baseinfo.accalert(self.driver)          
                time.sleep(5)
                print(u"此时已经存在订单")
            
            elif baseinfo.elementisexist(self.driver, checkboxfirst)==False:     
                print(u"此时没有该订单")  
        except:
            print(u"删除订单失败")
            print(traceback.format_exc())
        
        pass
        

    def testSearchorder(self):
        
        module=".//*[@id='$a453b9d8$mnuRoot3']/div"
        ordermodule=".//*[@id='$a453b9d8$mnuRoot3_2']/td[3]"
        ordername=".//*[@id='$a453b9d8$mnuRoot3_2_1']/td[3]"
        browserOperation.openModule3(self.driver, module, ordermodule, ordername)
        
        
        #选择日期
        enddate=".//*[@id='$2fbb1d58$edEndDate']"
        begindate=".//*[@id='$2fbb1d58$edBeginDate']"
        searchbtn=".//*[@id='$2fbb1d58$button5']"
        n=3
        end=self.driver.find_element_by_xpath(enddate).get_attribute("title")
        
        newdate=baseinfo.timeoperate(end,n)
        self.driver.find_element_by_xpath(begindate).clear()
        self.driver.find_element_by_xpath(begindate).send_keys(newdate)
        browserOperation.accreditErp(self.driver,searchbtn)
        
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
   
    
    def testOutorder(self):
       
        module=".//*[@id='$a453b9d8$mnuRoot3']/div"
        ordermodule=".//*[@id='$a453b9d8$mnuRoot3_2']/td[3]"
        ordername=".//*[@id='$a453b9d8$mnuRoot3_2_8']/td[3]"
        orderdetail=".//*[@id='$a453b9d8$mnuRoot3_2_8_0']/td[3]"
        browserOperation.openModule4(self.driver, module, ordermodule, ordername,orderdetail)
        pass
'''
   
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    #unittest.main(defaultTest='suite')
    unittest.main()

    
    
    
    
    
    
    
    