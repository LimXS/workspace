#*-* coding:UTF-8 *-*

import zipfile
import time
import datetime
import traceback
import sys
import random
reload(sys)
sys.setdefaultencoding( "utf-8" )
import unittest
import email.MIMEMultipart# import MIMEMultipart
import email.MIMEText# import MIMEText
import email.MIMEBase# import MIMEBase
import os
import shutil

import smtplib
import mimetypes
import json
from selenium.webdriver.common.action_chains import ActionChains
import requests
import MySQLdb

class base(unittest.TestCase):
    '''
    classdocs
    '''
    def __init__(self):

        pass

    '''定位单个元素封装'''
    def findId(self,driver,eid):
        f = driver.find_element_by_id(eid)
        return f
    
    def findName(self,driver,name):
        f = driver.find_element_by_name(name)
        return f
    
    def findClassName(self,driver,name):
        f = driver.find_element_by_class_name(name)
        return f
    
    def findTagName(self,driver,name):
        f = driver.find_element_by_tag_name(name)
        return f
    
    def findLinkText(self,driver,text):
        f = driver.find_element_by_link_text(text)
        return f
    
    def findPLinkText(self,driver,text):
        f = driver.find_element_by_partial_link_text(text)
        return f
    
    def findXpath(self,driver,xpath):
        f = driver.find_element_by_xpath(xpath)
        return f
    
    def findCss(self,driver,css):
        f = driver.find_element_by_css_selector(css)
        return f

    def sendKeys(self,driver,xpath,key):
        f=self.findXpath(driver,xpath).send_keys(key)
        return f

    #读写文件
    def writeFilemethon(self,driver,filepath,data,methon,stri):
        try:
        
            f=open(filepath,methon)
            f.write(stri)
            f.write(data)
            f.close()  
        except:
            print(u"文件操作失败")
            print(traceback.format_exc())              
    
    def writeFileonly(self,driver,filepath,methon,stri):
        try:
        
            f=open(filepath,methon)
            f.write(stri)
            f.close()  
        except:
            print(u"文件操作失败")
            print(traceback.format_exc())              

    def handleFile(self,driver,filepath,methon,flag,stri):
        try:
            f=open(filepath,methon)
            if flag==0:
                f.write(stri)
                f.close()
            if flag==1:
                a=f.readlines()
                f.close()
                return a
        except:
            print(u"文件操作失败")
            print(traceback.format_exc())
    #确认框处理
    def accAlert(self,driver,state):

        self.delaytime(1)
        driver.implicitly_wait(5)
        alert=driver.switch_to_alert()
        #driver.implicitly_wait(5)
        time.sleep(5)
        #接收警告信息
        if state==1:
            alert.accept()
        #取消
        else:
            alert.dismiss()

    #时间处理        
    def timeOperate(self,begin,n):
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

    #浏览器切换
    def browserChange(self,driver):
        try:
            now_handle=driver.current_window_handle
            all_handles=driver.window_handles
            for handle in all_handles:
                if handle != now_handle:
                    driver.switch_to_window(handle)
        except:
            print(u"切换浏览器窗口失败")
            print(traceback.format_exc())
            
            
    #读取接口xml文件
    def xmlRead(self,domc,tagname,n):
        try:
            #取出接口数据并放入列表
           # domc = xml.dom.minidom.parse(path)
            rootc = domc.documentElement
            detail = rootc.getElementsByTagName(tagname)
            b=detail[n]
            return b.firstChild.data
        except:
            print("获取xml数据失败")
            print(traceback.format_exc())

    def xmlChange(self,domc,tagname,n):
        try:
            #取出接口数据并放入列表
           # domc = xml.dom.minidom.parse(path)
            rootc = domc.documentElement
            detail = rootc.getElementsByTagName(tagname)
            b=detail[n]
            return b.firstChild.data
        except:
            print("获取xml数据失败")
            print(traceback.format_exc())
         
    #读取页面数据，get方法
    def requestget(self,url,headers):
        try:
            req = requests.get(url,headers = headers)  
            b=req.text
            #print b
            return b
        except:
            print("get取页面数据失败")
            print(traceback.format_exc()) 
             
    #读取页面数据，post方法
    def requestpost(self,url,data,headers,*c):
        try:
            if len(c)>0:
                req = requests.post(url,data=json.dumps(data),headers = headers)
            else:
                req = requests.post(url,data=data,headers = headers)
            b=req.text
            #print b
            return b
        except:
            print("post取页面数据失败")
            print(traceback.format_exc()) 
         
    #cookie保存
    def cookieSave(self,driver):
        try:
            #get the session cookie  
            cookie = [item["name"] + "=" + item["value"] for item in driver.get_cookies()]
            #print cookie  
  
            cookiestr = ';'.join(item for item in cookie) 
            return cookiestr
        except:
            print("保存cookie失败")
            print(traceback.format_exc()) 
            

    #发送邮件
    def sendemail(self,address,*c):
        timeStamp=time.time()
        timeArray = time.localtime(timeStamp)
        otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S" , timeArray)

        From = "xusxue@grasp.com.cn"
        #To = "1206626163@qq.com"
        file_name = "D:/beefunresault.html"#附件名
        if len(c)>0:
            file_name = "D:/beefunbutton.zip"#附件名
        host='61.139.77.221'
        server = smtplib.SMTP(host,25)
        server.login("xusxue@grasp.com.cn","abcd+123456789") #仅smtp服务器需要验证时

        # 构造MIMEMultipart对象做为根容器
        main_msg = email.MIMEMultipart.MIMEMultipart()

        # 构造MIMEText对象做为邮件显示内容并附加到根容器
        if len(c)>0:
            text_msg = email.MIMEText.MIMEText(u"点击图片截图，请预览",_charset="utf-8")
        else:
            text_msg = email.MIMEText.MIMEText(u"进销存页面点击报告，请下载后查看",_charset="utf-8")
        main_msg.attach(text_msg)

        # 构造MIMEBase对象做为文件附件内容并附加到根容器
        ctype,encoding = mimetypes.guess_type(file_name)
        if ctype is None or encoding is not None:
            ctype='application/octet-stream'
        maintype,subtype = ctype.split('/',1)
        file_msg=email.MIMEImage.MIMEImage(open(file_name,'rb').read(),subtype)
        print ctype,encoding

        ## 设置附件头
        basename = os.path.basename(file_name)
        file_msg.add_header('Content-Disposition','attachment', filename = basename)#修改邮件头
        main_msg.attach(file_msg)

        # 设置根容器属性
        main_msg['From'] = From
        main_msg['To'] = address
        main_msg['Subject'] = "beenfun report"+otherStyleTime
        main_msg['Date'] = email.Utils.formatdate( )

        # 得到格式化后的完整文本
        fullText = main_msg.as_string( )

        # 用smtp发送邮件
        try:
            server.sendmail(From, address, fullText)
        finally:
            server.quit()

    #时间操作
    def gettimestamp(self,*c):
        #今天和其他前时间戳
        stamp=[]
        if len(c)>0:
            if c[0]==100:
                today = datetime.date.today()
                today=today+datetime.timedelta(days=c[1])
                overday=today+datetime.timedelta(days=c[2])
            else:
                today = datetime.date.today()
                today=today+datetime.timedelta(days=1)
                overday=today+datetime.timedelta(days=-6)
        else:
            today = datetime.date.today()
            overday=today+datetime.timedelta(days=-6)

        todayda=today.strftime('%Y-%m-%d %H:%M:%S')
        overdayda=overday.strftime('%Y-%m-%d %H:%M:%S')

        today=today.strftime('%Y-%m-%d')
        overday=overday.strftime('%Y-%m-%d')

        timeArray1 = time.strptime(todayda, "%Y-%m-%d %H:%M:%S")
        timeArray2 = time.strptime(overdayda, "%Y-%m-%d %H:%M:%S")

        tostamp=int(time.mktime(timeArray1))
        overstamp=int(time.mktime(timeArray2))

        stamp.append(tostamp)
        stamp.append(overstamp)
        stamp.append(today)
        stamp.append(overday)

        return stamp

    #时间戳转换为日期
    def handlestamp(self,data):
        dateArray = datetime.datetime.utcfromtimestamp(float(data)/1000)
        threeDayAgo = dateArray+datetime.timedelta(days = 1)
        otherStyleTime = threeDayAgo.strftime("%Y-%m-%d")
        return otherStyleTime

    #时间戳转换为日期
    def handlestampdays(self,data,day):
        dateArray = datetime.datetime.utcfromtimestamp(float(data)/1000)
        threeDayAgo = dateArray+datetime.timedelta(days = day)
        otherStyleTime = threeDayAgo.strftime("%Y-%m-%d")
        return otherStyleTime

    #时间戳转换为日期
    def handlestampdaysevery(self,data,day):
        dateArray = datetime.datetime.utcfromtimestamp(float(data))
        threeDayAgo = dateArray+datetime.timedelta(days = day)
        otherStyleTime = threeDayAgo.strftime("%Y-%m-%d %H:%M:%S")
        return otherStyleTime


    def doubleclick(self,driver,element,*c):
        #定位到要双击的元素
        if len(c)>0:
            qqq =self.findXpath(driver,element)
        else:
           qqq =self.findId(driver,element)
        #对定位到的元素执行鼠标双击操作
        ActionChains(driver).double_click(qqq).perform()


     #压缩
    def zip_dir(self,dirname,zipfilename):
        filelist = []
        if os.path.isfile(dirname):
            filelist.append(dirname)
        else :
            for root, dirs, files in os.walk(dirname):
                for name in files:
                    filelist.append(os.path.join(root, name))

        zf = zipfile.ZipFile(zipfilename, "w", zipfile.zlib.DEFLATED)
        for tar in filelist:
            arcname = tar[len(dirname):]
            #print arcname
            zf.write(tar,arcname)
        zf.close()

    #删除文件夹并重新创建
    def deleteandmkdir(self):
        shutil.rmtree(r"D:\screentestpic")
        #print "delete"
        time.sleep(1)
        os.mkdir(r"D:\screentestpic")

    #获取文件大小
    def getdirsize(self,path):
        size = 0L
        for root , dirs, files in os.walk(path, True):
            size += sum([os.path.getsize(os.path.join(root, name)) for name in files])
            #目录下文件大小累加
        return size

    #button click
    def buttonclick(self,driver):
        js="$(\"button:contains('确定')\").click()"
        driver.execute_script(js)

    def excutejs(self,driver,js):
        driver.execute_script(js)
        self.delaytime(1)

    def delaytime(self,n,*c):
        if len(c)>0:
            c[0].implicitly_wait(n)
        else:
            time.sleep(n)


    def getrandnumber(self,*c):
        if len(c)>0:
            return random.sample(range(1,1000000,1),c[0])
        else:
            return str(random.randint(100000000, 1000000000))

    #mysql查询多条sql,结果只有一条且只取一个字段
    def mysqlsqls(self,*sqls):
        cur=self.mysqlopen()
        datas=[]
        for sql in sqls:
            cur.execute(sql)
            data=cur.fetchone()
            datas.append(data[0])
        return datas


    #打开数据库
    def mysqlopen(self):
        conn= MySQLdb.connect(host='172.16.0.96',user='website',passwd='test@2011',db='beefun', charset="utf8",port = 4306)
        cur = conn.cursor()
        return cur

    #数据库查询操作
    def mysqlselect(self,sql,*c):
        conn= MySQLdb.connect(host='172.16.0.96',user='website',passwd='test@2011',db='beefun',port = 4306)
        cur = conn.cursor()
        sqlreault=cur.execute(sql)
        # 使用 fetchone() 方法获取一条数据库。
        data = cur.fetchone()
        #游标定位到第n+1个
        #cur.scroll(n,'absolute')
        data=data[0]
        if len(c)>0:
            data=cur.fetchmany(sqlreault)
        cur.close()
        return data

    #字符串转小数
    def strconfloat(self,data):
        k=("%.4f" % float(str(data)))
        return k




