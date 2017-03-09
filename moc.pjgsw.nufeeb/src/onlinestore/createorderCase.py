#*-* coding:UTF-8 *-*
'''
Created on 2016��4��21��

@author: xsx
'''
import unittest
from common import  browserClass
from common import  baseClass
import traceback
import time
from selenium.webdriver.common.keys import Keys  #需要引入keys包
base=baseClass.base()
browser=browserClass.browser()
class createTest(unittest.TestCase):


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
        #切换到自义定流程
        btn=".//*[@id='$3327be68$linkButton1']"
        browser.findXpath(self.driver,btn)
        '''
       
        
        module=".//*[@id='$80d499b2$ManagerMenuBar3']/div"
        modulename=".//*[@id='$80d499b2$ManagerMenuBar3_14']/td[3]"
        browser.openModule2(self.driver, module, modulename)
        
        
        pass


    def tearDown(self):
        print "test over"
        #self.driver.close()
        pass


    def testCreateorder(self):
        u'''网上下载订单'''
        morebtn=".//*[@id='$dea0a8b3$button10']"
        downorder=".//*[@id='$dea0a8b3$synTrade0']/td[3]"
        browser.openModule2(self.driver, morebtn, downorder)
              
        begin=9
        end=13
        shop='微店一号'
               
        okbtn=".//*[@id='$8bee40ab$btnOk']"
        cancelbtn=".//*[@id='$8bee40ab$button1']"      
          
        try:
            str1='html/body/div['
            str2=']/table/tbody/tr[2]/td/div' 
            btn1="/html/body/table[8]/tbody/tr[2]/td/div/div/div/table/tbody/tr[3]/td[2]/table/tbody/tr/td[2]/div/div"
            a=browser.getdtnamicElement(self.driver, str1, str2, btn1, shop, begin, end)                     
            try:
                for n in range(1,4):
                    time.sleep(1)
                    btn2="/html/body/table[8]/tbody/tr[2]/td/div/div/div/table/tbody/tr[3]/td[4]/table/tbody/tr/td[2]/div/div"
                    base.findXpath(self.driver,btn2).click()
                    time.sleep(1)
                    xpath2='html/body/div['+str(a+1)+']/table/tbody/tr['+str(n)+']/td/div' 
                    #print base.findXpath(self.driver,xpath2).text
                    base.findXpath(self.driver,xpath2).click()
                    print(u"获取状态"+str(n)+"元素成功")
                    base.findXpath(self.driver,okbtn).click() 
                    time.sleep(10)
            except:
                print(u"获取订单状态失败")
                print(traceback.format_exc()) 
                                   
            try:
                base.findXpath(self.driver,cancelbtn).click()
                #base.accalert(self.driver)
                time.sleep(2)
                        
            except:
                print(u"下载成功，查询失败")
                print(traceback.format_exc())                                        
        
        except:
            print(u"订单创建失败")
            print(traceback.format_exc())
            
        print ('testover')
        
        pass
    
    def testSubmitorder(self):
        u'''原始订单页面提交订单'''
        submit=".//*[@id='$dea0a8b3$button9']"
        all=".//*[@id='$dea0a8b3$quickStatus']/table/tbody/tr[1]/td/div"
        browser.findXpath(self.driver,all).click()
        try:
            #判断一共要提交几次          
            str1=".//*[@id='$dea0a8b3$c_grid_Audit']/div[2]/table/tbody/tr["
            str2="]/td[4]/div"
            n=browser.getlines(self.driver, str1, str2)
            
            #提交成功确认按钮
            okbtn="html/body/table[7]/tbody/tr[2]/td/div/table/tbody/tr/td/table/tbody/tr[2]/td/button"
            #继续按钮
            contin=".//*[@id='$1c0ec6ae$canadd']"
            #提示框内消息
            winbtn=".//*[@id='$1c0ec6ae$grid']/div[2]/table/tbody/tr/td[3]/div"
            #关闭按钮
            winclose=".//*[@id='$1c0ec6ae$btnClose']" 
            
            trueorfalse=".//*[@id='$1c0ec6ae$grid']/div[2]/table/tbody/tr[2]/td[3]/div"   
                    
            #进行提交
            
            for i in range(1,n):
                checkbtn=".//*[@id='$dea0a8b3$c_grid_Audit']/div[2]/table/tbody/tr["+str(i)+"]/td[2]/input"
                checkbtn2=".//*[@id='$dea0a8b3$c_grid_Audit']/div[2]/table/tbody/tr["+str(i-1)+"]/td[2]/input"
                #处理状态
                subcon=".//*[@id='$dea0a8b3$c_grid_Audit']/div[2]/table/tbody/tr["+str(i)+"]/td[5]/div"
                subtext=browser.findXpath(self.driver,subcon).text
                #提醒是关闭的订单，只有一个提醒
                flash=".//*[@id='$dea0a8b3$c_grid_Audit']/div[2]/table/tbody/tr["+str(i)+"]/td[3]/div/font"
                #是否选中
                con=browser.elementisexist(self.driver,trueorfalse)
                #选中该行并进行提交
                browser.findXpath(self.driver,checkbtn).click()
                browser.findXpath(self.driver,submit).click()  
                
                if con==True:
                    browser.findXpath(self.driver,winclose).click()  
                    time.sleep(2)
                    browser.findXpath(self.driver,checkbtn2).click()
                if subtext=='未提交':                    
                    #判断是否有提醒
                    #有提醒
                    if browser.elementisexist(self.driver, flash)==True:
                        try:
                            #如果是交易关闭的订单
                            flashtext=browser.findXpath(self.driver,flash).text
                            #winbtn=".//*[@id='$1c0ec6ae$grid']/div[2]/table/tbody/tr/td[3]/div"
                            if flashtext==u"闭":
                                if browser.findXpath(self.driver,winbtn).text==u'过滤交易关闭的订单':
                                    browser.findXpath(self.driver,winclose).click() 
                                    print "次订单已经关闭，测试成功"
                                else:
                                    print "此订单提示是闭，但弹出窗口提示不正常，测试失败,弹出框信息为:"+browser.findXpath(self.driver,winbtn).text
                                    
                        except:
                            print(u"原始订单页面关闭交易订单提交失败")
                            print(traceback.format_exc())
                            
                        try:    
                            #如果是未支付的订单
                            flashtext=browser.findXpath(self.driver,flash).text
                            #winbtn=".//*[@id='$1c0ec6ae$grid']/div[2]/table/tbody/tr/td[3]/div"
                            if flashtext==u"未付":
                                if browser.findXpath(self.driver,winbtn).text==u'未付款的订单':
                                    browser.findXpath(self.driver,contin).click() 
                                    browser.findXpath(self.driver, okbtn).click()
                                    print "次订单是未支付订单，测试成功"
                                else:
                                    print "此订单提示是未付，但弹出窗口提示不正常，测试失败"
                                    print  browser.findXpath(self.driver,winbtn).text
                        except:
                            print(u"原始订单页面未支付订单提交失败")
                            print(traceback.format_exc())
                        
                        try:    
                            #如果是商品未对应的订单,谷歌浏览器不支持
                            flashtext=browser.findXpath(self.driver,flash).text
                            #winbtn=".//*[@id='$1c0ec6ae$grid']/div[2]/table/tbody/tr/td[3]/div"
                            if flashtext==u"未对":
                                time.sleep(5)
                                #browser.findXpath(self.driver,all).send_keys(Keys.ENTER)
                                if browser.findXpath(self.driver,winbtn).text==u'过滤未对应本地商品的订单':
                                    browser.findXpath(self.driver,winclose).click() 
                                    print "次订单是未未对应订单，测试成功"
                                else:
                                    print "此订单提示是未对，但弹出窗口提示不正常，测试失败"
                                    print  browser.findXpath(self.driver,winbtn).text
                        except:
                            print(u"原始订单页面未对应订单处理失败")
                            print(traceback.format_exc())   
                            
                        #如果是退款中的订单
                        try:
                            flashtext=browser.findXpath(self.driver,flash).text
                            if flashtext==u'退':
                                browser.findXpath(self.driver,contin).click() 
                                browser.findXpath(self.driver, okbtn).click()
                                print u"退款中订单提交发货成功"
                        except :
                            print(u"原始订单页面退款中订单提交失败")
                            print(traceback.format_exc())
                    #没有提醒，可以直接提交发货
                    if browser.elementisexist(self.driver, flash)==False:    
                        try:
                            #正常提交
                            
                            browser.findXpath(self.driver, okbtn).click()
                        except:
                            print(u"原始订单页面订单未提交订单失败")
                            print(traceback.format_exc())

                elif subtext=='已提交发货':
                    try:
                        
                        if browser.findXpath(self.driver,winbtn).text=='过滤已提交发货的订单':
                            browser.findXpath(self.driver,winclose).click()
                            print "该订单提交发货，测试成功"
                        else:
                            print "该订单提交发货，提示框信息显示失败，测试失败"
                    except:
                        print(u"原始订单页面订单提交发货失败")
                        print(traceback.format_exc())
                        
                else :
                    print "测试用例不含处理状态，请添加"
                    print subtext
                time.sleep(2)
                browser.findXpath(self.driver,checkbtn).click()
            
        except:
            print(u"原始订单页面订单提交失败")
            print(traceback.format_exc())
        
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()