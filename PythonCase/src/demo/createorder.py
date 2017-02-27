#-*- coding: UTF-8 -*-

import traceback
from common import browserOperation
import time
from selenium.webdriver.common.action_chains import ActionChains
from common import baseinfo
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


if __name__ == "__main__":
     
        
        driver = browserOperation.startBrowser('chrome')
        driver.implicitly_wait(5)
        driver.get("http://71.wsgjp.com.cn")
        driver.maximize_window()
        browserOperation.loginUser(driver, '$8a3327cd$corpName', '$8a3327cd$userName', '$8a3327cd$pwdEdit', '$8a3327cd$btnLogin')
        
        '''
        module=".//*[@id='$a453b9d8$mnuRoot3']/div"
        ordermodule=".//*[@id='$a453b9d8$mnuRoot3_2']/td[3]"
        ordername=".//*[@id='$a453b9d8$mnuRoot3_2_1']/td[3]"
        browserOperation.openModule3(driver, module, ordermodule, ordername)

        
        js = 'document.querySelectorAll("div")[30].style.display="block";'
        driver.execute_script(js)
        '''

        time.sleep(7)
        module=".//*[@id='$a453b9d8$mnuRoot3']/div"
        ordermodule=".//*[@id='$a453b9d8$mnuRoot3_2']/td[3]"
        ordername=".//*[@id='$a453b9d8$mnuRoot3_2_0']/td[3]"
        browserOperation.openModule3(driver, module, ordermodule, ordername)
        

        orderbtn1=".//*[@id='$8b74f50b$button1']"
        orderbtn2=".//*[@id='$8b74f50b$createTrade0']/td[3]"

        
        
        okbtn=".//*[@id='$9073ce9d$btnOk']"
        cancelbtn=".//*[@id='$9073ce9d$btnCancel']"
        begin=37
        end=70
        shop='18080107102'
        time.sleep(5)
        driver.find_element_by_xpath(orderbtn1).click()
        time.sleep(5)
        driver.find_element_by_xpath(orderbtn2).click()
                
        try:
            for a in range(begin,end):               
                btn1="html/body/table[8]/tbody/tr[2]/td/div/div/table/tbody/tr/td/table/tbody/tr[2]/td[2]/div/table/tbody/tr[3]/td[2]/table/tbody/tr[2]/td[4]/table/tbody/tr[1]/td[2]/table/tbody/tr[2]/td[2]/table/tbody/tr/td[2]/div/div"
                driver.find_element_by_xpath(btn1).click()
                xpath1='html/body/div[' + str(a) + ']/table/tbody/tr[8]/td/div' 
                print xpath1  
                baseinfo.elementisexist(driver,xpath1)                                
                if baseinfo.elementisexist(driver,xpath1)==True:                    
                    if driver.find_element_by_xpath(xpath1).text==str(shop):   
                        print driver.find_element_by_xpath(xpath1).text                                           
                        driver.find_element_by_xpath(".//*[@id='$9073ce9d$edEShop']").click()                      
                        driver.find_element_by_xpath(btn1).click()                     
                        driver.find_element_by_xpath(xpath1).click()
                        break             
            try:
                for n in range(1,4):
                    btn2="html/body/table[8]/tbody/tr[2]/td/div/div/table/tbody/tr/td/table/tbody/tr[2]/td[2]/div/table/tbody/tr[3]/td[2]/table/tbody/tr[2]/td[4]/table/tbody/tr[1]/td[2]/table/tbody/tr[2]/td[4]/table/tbody/tr/td[2]/div/div"
                    driver.find_element_by_xpath(btn2).click()
                    xpath2='html/body/div[' + str(a+1) + ']/table/tbody/tr['+str(n)+']/td/div'
                    print driver.find_element_by_xpath(xpath2).text
                    driver.implicitly_wait(5)
                    driver.find_element_by_xpath(xpath2).click()
                    print(u"获取状态"+str(n)+"元素成功")
                    driver.find_element_by_xpath(okbtn).click() 
                    time.sleep(30)           
                try:
                    driver.find_element_by_xpath(cancelbtn).click()
                    baseinfo.accalert(driver)
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
            
        print ('testover')
        
        
'''        
        try:
            time.sleep(3)
            driver.find_element_by_xpath(orderbtn1).click()   
            time.sleep(3)             
            driver.find_element_by_xpath(orderbtn2).click()
            try:
                for a in range(begin,end):
                    driver.find_element_by_xpath(btn1).click()
                    xpath1='html/body/div[' + str(a) + ']/table/tbody/tr[8]/td/div'                    
                    baseinfo.elementisexist(driver,xpath1)
                    print ("xpath1:"+xpath1)
                    if baseinfo.elementisexist(driver,xpath1)==True:
                        if driver.find_element_by_xpath(xpath1).text==shop:
                            #print driver.find_element_by_xpath(xpath1).text
                            #driver.find_element_by_xpath(btn1).click()
                            #time.sleep(5)

                            print (u"元素已定位到")       
                                              
                            break                
                
            except:
                print(u"订未找到该元素")
                print(traceback.format_exc())
                
            time.sleep(3)
               
            for n in range(1,4):
                driver.find_element_by_xpath(".//*[@id='$9073ce9d$edEShop']").click()    
                #time.sleep(2)  
                xpath2='html/body/div[' + str(a+1) + ']/table/tbody/tr[' + str(n) + ']/td/div'
                print ("xpath1:"+xpath1)
                print ("xpath2:"+xpath2)
                
                driver.find_element_by_xpath(btn1).click()
                time.sleep(2) 
                print driver.find_element_by_xpath(xpath1).text            
                driver.find_element_by_xpath(xpath1).click() 

                
                driver.find_element_by_xpath(".//*[@id='$9073ce9d$edStatus']").click()    
                driver.find_element_by_xpath(btn2).click()
                time.sleep(5) 
                print driver.find_element_by_xpath(xpath2).text
                driver.find_element_by_xpath(xpath2).click()
                
                
                driver.find_element_by_xpath(okbtn).click()
                time.sleep(60)
                driver.find_element_by_xpath(cancelbtn).click()
                baseinfo.accalert(driver)
                
                driver.find_element_by_xpath(orderbtn1).click()   
                             
                driver.find_element_by_xpath(orderbtn2).click()
                print n
                    
        except:
            print(u"订单创建失败")
            print n
            print(traceback.format_exc())
        
        print("test over")



        
        
        
        
        checkboxfirst=".//*[@id='$8b74f50b$c_grid_Audit']/div[2]/table/tbody/tr[1]/td[2]/input"
        checkboxall=".//*[@id='$8b74f50b$c_grid_Audit_column0']/div/table/tbody/tr/td/input"
        deletebtn=".//*[@id='$8b74f50b$c_delbill']"
        waitecheck=".//*[@id='$8b74f50b$dd_tradestatus_check1']"
        
        #ͳ��7���ڶ�������
        enddate=".//*[@id='$8b74f50b$edEndDate']"
        begindate=".//*[@id='$8b74f50b$edBeginDate']"
        searchbtn=".//*[@id='$8b74f50b$button8']"
        n=7
        end=driver.find_element_by_xpath(enddate).get_attribute("title")
        
        
        
        newdate=baseinfo.timeoperate(end,n)
        driver.find_element_by_xpath(begindate).clear()
        driver.find_element_by_xpath(begindate).send_keys(newdate)
        driver.find_element_by_xpath(waitecheck).click()
        browserOperation.accreditErp(driver,searchbtn)
              
        createtext="html/body/table[12]"
        createbtn=".//*[@id='$8b74f50b$button1']"
        createdown=".//*[@id='$8b74f50b$createTrade0']/td[3]"
        
        driver.find_element_by_xpath(createbtn).click()
        driver.find_element_by_xpath(createdown).click()
        
        driver.find_element_by_xpath(createtext)
        
        
        
        
        
        if baseinfo.elementisexist(driver, checkboxfirst)==True:
            #ѡ������
            
            #ɾ������
            driver.find_element_by_xpath(checkboxall).click()
            
            driver.find_element_by_xpath(deletebtn).click()
            
            time.sleep(5)
            print("�и�Ԫ��")
            
        elif baseinfo.elementisexist(driver, checkboxfirst)==False:     
            print("û�и�Ԫ��")       
            
        
        time.sleep(5)
        '''      
