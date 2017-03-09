#-*- coding: UTF-8 -*-

import traceback
from common import browserOperation
import time
from selenium.webdriver.common.action_chains import ActionChains
from common import baseinfo
from selenium import webdriver
import urllib2


if __name__ == "__main__":
    try:  
        
        driver = browserOperation.startBrowser('firefox')
        driver.implicitly_wait(5)
        driver.get("http://71.wsgjp.com.cn")
        driver.maximize_window()
        browserOperation.loginUser(driver, '$8a3327cd$corpName', '$8a3327cd$userName', '$8a3327cd$pwdEdit', '$8a3327cd$btnLogin')
        #订单查询
        module=".//*[@id='$a453b9d8$mnuRoot3']/div"
        ordermodule=".//*[@id='$a453b9d8$mnuRoot3_2']/td[3]"
        ordername=".//*[@id='$a453b9d8$mnuRoot3_2_1']/td[3]"
        browserOperation.openModule3(driver, module, ordermodule, ordername)
        
        '''
        js = 'document.querySelectorAll("div")[30].style.display="block";'
        driver.execute_script(js)
        '''
        aa=driver.current_url
        print aa
        request = urllib2.Request(aa)
        response = urllib2.urlopen(request)
        print response.read()
        #defauleWin=driver.current_window_handle()
        #driver.switch_to_frame(driver.find_element_by_xpath("html/body/iframe"))
        #driver.find_element_by_xpath("html/body/div[44]/table/tbody/tr[12]/td").click()
        check=".//*[@id='$2fbb1d58$dd_eshop']"
        shop='18080107102'
        begin=30
        end=60
        #driver.find_element_by_css_selector(".Border>table>tbody>tr>td").click()
        #driver.find_element_by_css_selector(".Border>table>tbody>tr").click()
        #driver.find_element_by_xpath("/html/body/div[38]/table/tbody/tr[12]/td").click()
        ''
        for a in range(begin,end):
            btn=".//*[@id='$2fbb1d58$bLeft']/table/tbody/tr[2]/td[2]/table/tbody/tr[1]/td[2]/table/tbody/tr/td[2]/div/div"
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
        
        #testdata=driver.find_element_by_xpath("//*[@id='$2fbb1d58$c_grid']/div[2]/table/tbody/tr[1]/td[55]/div").text
        #print testdata
        f=open('D:\search.txt','w')
        f.write("写入测试数据")
        f.write("\n")
        f.close()
        for n in range(1,100):
            nformxpath=".//*[@id='$2fbb1d58$c_grid']/div[2]/table/tbody/tr["+str(n)+"]/td[3]/div"
            print nformxpath
            if baseinfo.elementisexist(driver,nformxpath)==False:
                break
        print n 
        print 'test over1'    
                          
        bigrid=[] 
        for row in range(1,n):
            grid=[]
            for line in range(3,59):
                formxpath=".//*[@id='$2fbb1d58$c_grid']/div[2]/table/tbody/tr["+str(row)+"]/td["+str(line)+"]/div"
                baseinfo.elementisexist(driver,formxpath)
                if baseinfo.elementisexist(driver,formxpath)==True:
                    data=driver.find_element_by_xpath(formxpath).text
                    #print data
                    grid.append(data)
                    print grid
                    f=open('D:\search.txt','a')
                    f.write(data)
                    f.write(';')
                    f.close()
            f=open('D:\search.txt','a')
            f.write("\n")
            f.close()
            bigrid.append(grid)
        print 'test over2'   
        
        le=open('D:\search2.txt','w')
        le.write('列表小王子')
        print("\n")
        for a in bigrid:
            for b in a:
                le=open('D:\search2.txt','a')
                le.write(b)
                le.write(';')
            le=open('D:\search2.txt','a')
            le.write('\n')
            le.close()
        print 'test over3'
        
        time.sleep(2222)
        
        

     
     
     
     
        '''
        #订单创建
        module=".//*[@id='$a453b9d8$mnuRoot3']/div"
        ordermodule=".//*[@id='$a453b9d8$mnuRoot3_2']/td[3]"
        ordername=".//*[@id='$a453b9d8$mnuRoot3_2_0']/td[3]"
        browserOperation.openModule3(driver, module, ordermodule, ordername)
        
        #分别下载所有状态下的订单
        #n=2为等待付款的订单，n=3为已付款订单,n=4为已发货订单，n=5为交易成功订单

        orderbtn1=".//*[@id='$8b74f50b$button1']"
        orderbtn2=".//*[@id='$8b74f50b$createTrade0']/td[3]"

        btn1="html/body/table[8]/tbody/tr[2]/td/div/div/table/tbody/tr/td/table/tbody/tr[2]/td[2]/div/table/tbody/tr[3]/td[2]/table/tbody/tr[2]/td[4]/table/tbody/tr[1]/td[2]/table/tbody/tr[2]/td[2]/table/tbody/tr/td[2]/div/div"
        btn2="html/body/table[9]/tbody/tr[2]/td/div/div/table/tbody/tr/td/table/tbody/tr[2]/td[2]/div/table/tbody/tr[3]/td[2]/table/tbody/tr[2]/td[4]/table/tbody/tr[1]/td[2]/table/tbody/tr[2]/td[4]/table/tbody/tr/td[2]/div/div"
        okbtn=".//*[@id='$9073ce9d$btnOk']"
        cancelbtn=".//*[@id='$9073ce9d$btnCancel']"
        try:
            for n in range(1,6):
                driver.find_element_by_xpath(orderbtn1).click()
                driver.find_element_by_xpath(orderbtn2).click()
            try:
                for a in range(begin,end):
                    driver.find_element_by_xpath(btn).click()
                    xpath1='html/body/div[' + str(a) + ']/table/tbody/tr[8]/td/div'
                    xpath2='html/body/div[' + str(a+1) + ']/table/tbody/tr[n]/td/div'
                    baseinfo.elementisexist(driver,xpath)
                    print ("xpath1:"xpath1)
                    print("xpath2:"xpath2)
                    if baseinfo.elementisexist(driver,xpath)==True:
                        if driver.find_element_by_xpath(xpath).text==str(shop):
                            driver.find_element_by_xpath(xpath1).click()
                            driver.find_element_by_xpath(btn2).click()
                            driver.find_element_by_xpath(xpath2).click()
                            break
                time.sleep(10)
                drive.find_element_by_xpath(okbtn).click()
                time.sleep(60)
                drive.find_element_by_xpath(cancelbtn).click()
                baseinfo.accalert(self.driver)
                time.sleep(10)
            except:
                print(u"获取状态"n"元素失败")
                print(traceback.format_exc())

    except:
        print(u"订单创建失败")
        print(traceback.format_exc())
        
        
        
        
        
        checkboxfirst=".//*[@id='$8b74f50b$c_grid_Audit']/div[2]/table/tbody/tr[1]/td[2]/input"
        checkboxall=".//*[@id='$8b74f50b$c_grid_Audit_column0']/div/table/tbody/tr/td/input"
        deletebtn=".//*[@id='$8b74f50b$c_delbill']"
        waitecheck=".//*[@id='$8b74f50b$dd_tradestatus_check1']"
        
        #统计7日内订单总数
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
            #选择日期
            
            #删除操作
            driver.find_element_by_xpath(checkboxall).click()
            
            driver.find_element_by_xpath(deletebtn).click()
            
            time.sleep(5)
            print("有该元素")
            
        elif baseinfo.elementisexist(driver, checkboxfirst)==False:     
            print("没有该元素")       
            
        
        time.sleep(5)
        '''
        
        
        
        

        
    except:
        print(traceback.format_exc())
        print("取值失败")
