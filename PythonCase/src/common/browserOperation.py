#-*- coding:UTF-8 -*-
from selenium import webdriver
import time

import traceback
import baseinfo
'''
Created on 2016��4��5��

@author: xsx
'''

def startBrowser(browserType):
    try:
        if browserType.upper()=='CHROME':
            driver=webdriver.Chrome()
        elif browserType.upper()=='IE':
            driver=webdriver.Ie()
        elif browserType.upper()=='FIREFOX' or browserType.upper()=='FF':
            driver=webdriver.Firefox()
        return driver
    except:
        print(u'浏览器启动失败')
        return driver
        
def loginUser(driver,name,user,pwd,login):
    try:
        driver.find_element_by_id(name).clear()
        driver.find_element_by_id(name).send_keys(u"测试网店桂")
        driver.find_element_by_id(user).clear()
        driver.find_element_by_id(user).send_keys(u"网店")
        driver.find_element_by_id(pwd).clear()
        driver.find_element_by_id(pwd).send_keys("grasp121#")
        driver.find_element_by_id(login).click()
 
        return driver
    except:
        print(traceback.format_exc())
        print(u"登录元素定位失败")
        return driver


def openModule2(driver,module,modulename):
    try:
        driver.find_element_by_xpath(module).click()
        driver.find_element_by_xpath(modulename).click()
    except :
        print(u"2级模块定位失败")
        print(traceback.format_exc())    
    
    
def openModule3(driver,module,modulename,moduledetail):
    try:
        time.sleep(2) 
        driver.find_element_by_xpath(module).click() 
        time.sleep(3) 
        driver.find_element_by_xpath(modulename).click()
        driver.find_element_by_xpath(moduledetail).click()
    except :
        print(u"3级模块定位失败")
        print(traceback.format_exc())


def openModule4(driver,module,modulename,moduledetail,modulenade):
    try:
        driver.find_element_by_xpath(module).click()
        driver.find_element_by_xpath(modulename).click()
        driver.find_element_by_xpath(moduledetail).click()
        driver.find_element_by_xpath(modulenade).click()
    except :
        print(u"4级模块定位失败")
        print(traceback.format_exc())


def accreditErp(driver,acc):
    try:
        driver.find_element_by_xpath(acc).click()
    except:
        print(u"1级模块定位失败")
        print(traceback.format_exc())    

        
def acccomfirm(driver,loginname,password,loginbtn,acc):
    try:
        driver.find_element_by_id(loginname).clear()
        driver.find_element_by_id(loginname).send_keys("18080107102")
        driver.find_element_by_id(password).clear()
        driver.find_element_by_id(password).send_keys("sdfasdf*-")
        driver.find_element_by_id(loginbtn).click()
        driver.find_element_by_xpath(acc).click()
        time.sleep(5)
    except:
        print(u"可授权页面授权失败")
        print(traceback.format_exc())
        
#检索网店动态元素        
def selectshop(driver,shop,begin,end,btn):            
    try:
        for a in range(begin,end):                      
            driver.find_element_by_xpath(btn).click()
            #driver.find_element_by_xpath("html/body/table[3]/tbody/tr[2]/td[4]/table/tbody/tr/td[2]/div/div[2]/div[2]/div/table[2]/tbody/tr[2]/td[2]/table/tbody/tr/td[2]/div/table/tbody/tr[2]/td[2]/table/tbody/tr[1]/td[2]/table/tbody/tr/td[2]/div/div").click()
            xpath='/html/body/div['+str(a)+']/table/tbody/tr[9]/td/div'
            baseinfo.elementisexist(driver,xpath)
            print xpath
            if baseinfo.elementisexist(driver,xpath)==True:
                if driver.find_element_by_xpath(xpath).text==str(shop):
                    print driver.find_element_by_xpath(xpath).text
                    driver.find_element_by_xpath(xpath).click()
                    break

    except:
        print(u"定位网店搜索元素失败")
        print(traceback.format_exc())
        
        
        
        
        
        