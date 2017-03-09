#*-* coding:UTF-8 *-*
'''
Created on 2016��4��7��

@author: xsx
'''
import time
import datetime
import traceback

def timeoperate(begin,n):
    try:
        timearray=time.strptime(begin,u"%Y-%m-%d %H:%M:%S")
        timestamp=int(time.mktime(timearray))
        
        datearray=datetime.datetime.utcfromtimestamp(timestamp)
        daysago=datearray-datetime.timedelta(days=n)
        
        newbegin=daysago.strftime("%Y-%m-%d %H:%M:%S")
        return newbegin  
    except:
        print(u"时间设置失败")
        print(traceback.format_exc())   


def browserchange(driver):
    try:
        now_handle=driver.current_window_handle
        all_handles=driver.window_handles
        for handle in all_handles:
            if handle != now_handle:
                driver.switch_to_window(handle)
    except:
        print(u"切换浏览器窗口失败")
        print(traceback.format_exc())
                

def elementisexist(driver,element):
    
    try:
        
        try:
            driver.implicitly_wait(10)
            driver.find_element_by_xpath(element)
            status=True
        except:
            status=False
        return status

    except:
        print(u"判断元素是否存在失败")
        print(traceback.format_exc())
            
   

def accalert(driver):
    try:
        
        time.sleep(10)
        alert=driver.switch_to_alert()
        #接收警告信息
        time.sleep(10)
        alert.accept()
        time.sleep(5)
    except:
        print(u"对话框处理失败")
        print(traceback.format_exc())
        
#订单查询页面获取订单列表        
def extractdata(driver,searchpath,time):
    try:
        for n in range(1,100):
                nformxpath=".//*[@id='" +str(searchpath)+"']/div[2]/table/tbody/tr["+str(n)+"]/td[3]/div"
                print nformxpath
                if elementisexist(driver,nformxpath)==False:
                    break 
        bigrid=[]
        for row in range(1,n):
            grid=[]
            for line in range(3,time):
                formxpath=".//*[@id='" +str(searchpath)+"']/div[2]/table/tbody/tr["+str(row)+"]/td["+str(line)+"]/div"
                elementisexist(driver,formxpath)
                if elementisexist(driver,formxpath)==True:
                    data=driver.find_element_by_xpath(formxpath).text
                    grid.append(data)
                    print grid
                    #print grid
            bigrid.append(grid)
        return bigrid
            
    except:
        print(u"读取订单列表失败")
        print(traceback.format_exc())
        return bigrid
        

def writefilemethon(driver,filepath,data,methon,stri):
    try:
        
        f=open(filepath,methon)
        f.write(stri)
        f.write(data)
        f.close()  
    except:
        print(u"文件操作失败")
        print(traceback.format_exc())              
    
def writefileonly(driver,filepath,methon,stri):
    try:
        
        f=open(filepath,methon)
        f.write(stri)
        f.close()  
    except:
        print(u"文件操作失败")
        print(traceback.format_exc())              
    
        
        