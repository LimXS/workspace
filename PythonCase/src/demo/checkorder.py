#-*- coding: UTF-8 -*-

import traceback
from common import browserOperation
import time
from selenium.webdriver.common.action_chains import ActionChains
from common import baseinfo
from selenium import webdriver

from selenium.webdriver.common.keys import Keys

if __name__ == "__main__":
    try:  
        
        driver = browserOperation.startBrowser('chrome')
        driver.implicitly_wait(5)
        driver.get("http://71.wsgjp.com.cn")
        driver.maximize_window()
        browserOperation.loginUser(driver, '$8a3327cd$corpName', '$8a3327cd$userName', '$8a3327cd$pwdEdit', '$8a3327cd$btnLogin')
        #������ѯ
        module=".//*[@id='$a453b9d8$mnuRoot3']/div"
        ordermodule=".//*[@id='$a453b9d8$mnuRoot3_2']/td[3]"
        ordername=".//*[@id='$a453b9d8$mnuRoot3_2_0']/td[3]"
        browserOperation.openModule3(driver, module, ordermodule, ordername)
        
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
        for times in range(1,100):
            title=".//*[@id='$8b74f50b$c_grid_Audit']/div[2]/table/tbody/tr["+str(times)+"]/td[3]/div"
            orderid=".//*[@id='$dea0a8b3$c_grid_Audit']/div[4]/table/tbody/tr["+str(times)+"]/td[4]/div"
            if baseinfo.elementisexist(driver,orderid)==False:
                break
            
        flagxpath=".//*[@id='$8b74f50b$c_grid_Audit']/div[2]/table/tbody/tr[1]/td[3]/div"
        flagtext=driver.find_element_by_xpath(flagxpath).text
        nowlines=times-1
        m=1
        print times
        for n in range(1,times):
            
            #totalxpath=".//*[@id='$8b74f50b$c_grid_Audit']/div[2]/table/tbody/tr["+str(n)+"]/td[3]/div"
            lock=".//*[@id='$8b74f50b$c_grid_Audit']/div[2]/table/tbody/tr["+str(m)+"]/td[41]/div"   
            check=".//*[@id='$8b74f50b$c_grid_Audit']/div[2]/table/tbody/tr["+str(m)+"]/td[2]/input" 
            people=".//*[@id='$8b74f50b$c_grid_Audit']/div[2]/table/tbody/tr["+str(m)+"]/td[35]/div"       
            checkall=".//*[@id='$8b74f50b$c_grid_Audit_column0']/div/table/tbody/tr/td/input"
            
            time.sleep(2)
            driver.find_element_by_xpath(checkall).click()
            time.sleep(5)
            driver.find_element_by_xpath(checkall).click()              
            driver.find_element_by_xpath(check).click()
            time.sleep(5)    
            driver.find_element_by_xpath(checkbtn).click()
            driver.implicitly_wait(5)
            driver.find_element_by_xpath(checkthisbtn).click()
            print ("本次执行第m列:"+str(m))
            if driver.find_element_by_xpath(lock).text==' ':
                print ('此订单未锁定')
                if baseinfo.elementisexist(driver,alertclose)==True:
                    dd=driver.find_element_by_xpath(nomatch).text
                    if dd==u'订单与本地商品未对应':
                        print(u"次订单未锁定，审核时商品未对应，测试成功")
                        driver.find_element_by_xpath(alertclose).click()                      
                    else :
                        print(u"次订单未锁定，应该出现审核时商品未对应，测试失败")
                        driver.find_element_by_xpath(alertclose).click()
                     
                    
                elif  baseinfo.elementisexist(driver,enter)==True:
                    print("此订单已对应，可以进行审核")
                    time.sleep(5)
                    if driver.find_element_by_xpath(people).text==' ':
                        driver.find_element_by_xpath(enter).send_keys(Keys.ENTER)
                        driver.find_element_by_xpath(selectpeople).click()
                        driver.find_element_by_xpath(checkokbtn).click()
                    
                        if baseinfo.elementisexist(driver,checkfailclose)==True:
                            driver.find_element_by_xpath(checkfailclose).click()
                            failcheckreason=".//*[@id='$e0a78471$grid']/div[2]/table/tbody/tr/td[3]"                
                            print "审核失败，可能是因为库存不足"
                            #print driver.find_element_by_xpath(failcheckreason).text
                            driver.find_element_by_xpath(alertclose).click()
                       
                    
                        
            elif driver.find_element_by_xpath(lock).text!='' :
                print("此订单已锁定")
                aa=driver.find_element_by_xpath(ordernum).text
                bb=driver.find_element_by_xpath(falsereason).text
                cc=driver.find_element_by_xpath(deal).text
                driver.find_element_by_xpath(alertclose).click()
            for lines in range(1,10):
                totalnow=".//*[@id='$8b74f50b$c_grid_Audit']/div[2]/table/tbody/tr["+str(lines)+"]/td[3]/div"
                if baseinfo.elementisexist(driver,totalnow)==False:
                    break
            afterlines=lines-1
            if nowlines==afterlines:
                m=m+1            
            nowlines=afterlines
            

                
                       
        print 'test over3'   
    
    except:
        print(traceback.format_exc())


        