#*-* coding:UTF-8 *-*

import unittest
from common import  browserClass
browser=browserClass.browser()

class loginTest(unittest.TestCase):


    def setUp(self):
        self.driver=browser.startBrowser('chrome')
        self.url="http://beefun.wsgjp.com/"
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(25)
        pass


    def tearDown(self):
        print "test over"
        #self.driver.close()
        pass


    def testcorrectLogin(self):
        u'''登录页面：正确的用户密码'''
        
        name="$1b8bb415$corpName"
        user="$1b8bb415$userName"
        pwd="$1b8bb415$pwdEdit"
        login="$1b8bb415$btnLogin"
        loginname="xsx123456"
        username="xsx"
        password="xsx123456."
        browser.loginUser(self.driver,name ,user,pwd,login,loginname,username,password)
        pass
'''
    def testwrongLogin(self):
        #登录页面，错误的登录数据
        name='$8a3327cd$corpName'
        user='$8a3327cd$userName'
        pwd='$8a3327cd$pwdEdit'
        login='$8a3327cd$btnLogin'
        loginname="xsx123456"
        username="xsx"
        password="xsx123456."
        browser.loginUser(self,self.driver,name ,user,pwd,login,loginname,username,password)
        pass
'''
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()