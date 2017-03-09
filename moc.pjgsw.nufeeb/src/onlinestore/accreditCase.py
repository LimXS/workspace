#-*- coding:UTF-8 -*-
'''

@author: xsx
'''
import unittest
from common import browserClass
from common import baseClass
import traceback
import time
base=baseClass.base()
browser=browserClass.browser()
class accTest(unittest.TestCase):


    def setUp(self):
        self.driver=browser.startBrowser('firefox')
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
        
        module=".//*[@id='$80d499b2$ManagerMenuBar3']/div"
        shopset=".//*[@id='$80d499b2$ManagerMenuBar3_0']/td[3]"
        acc=".//*[@id='$f587eff5$grid']/div[2]/table/tbody/tr[2]/td[9]/div/a/font"
        try:
            browser.openModule3(self.driver, module, shopset,acc)
        except:
            print "点击网店授权失败"
            print(traceback.format_exc())
        pass


    def tearDown(self):
        print "test over"
        #self.driver.close()
        pass


    def testAccrediton(self):
        u'''授权页面进行授权'''                   
        #进行授权
        try:
            state=1
            base.accAlert(self.driver, state)
            base.browserChange(self.driver)
            
            loginname="tele"
            password="password"
            loginbtn="J_LoginBtn"
            acc=".//*[@id='outer']/div/div[2]/form/div/div[2]/div/p/input[1]"
            
            accid="18080107102"
            accpwd="sdfasdf*-"
            
            #closepage=".//*[@id='$523812b6$btnClose']"
            self.driver.implicitly_wait(10)
            if browser.elementisexist(self.driver, acc)==True:
                browser.module1(self.driver,acc)
            elif browser.elementisexist(self.driver, acc)==False:            
                browser.acccomfirm(self.driver, loginname, password, loginbtn,acc,accid,accpwd)
                time.sleep(5)
                self.driver.implicitly_wait(10)
                #base.findXpath(self.driver,closepage).click()
                
            
        except:
            print "授权失败"
            print(traceback.format_exc())

        pass
'''
    def testAccreditoff(self):
        #授权页面取消授权
        #进行授权
        try:
            state=0
            base.accAlert(self.driver, state)
        except:
            print "取消授权失败"
            print(traceback.format_exc())

        pass
'''
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testAccredit']
    unittest.main()