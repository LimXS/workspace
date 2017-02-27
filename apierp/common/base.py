#*-* coding:UTF-8 *-*
from selenium import webdriver
import requests
import re
import traceback
import datetime
import time
import  xml.dom.minidom
import MySQLdb

import email.MIMEMultipart# import MIMEMultipart
import email.MIMEText# import MIMEText
import email.MIMEBase# import MIMEBase
import os
import smtplib
import mimetypes




class baseCommon():
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

    #读取接口xml文件
    def apixmlRead(self,driver,path,tagname):
        try:
            #取出接口数据并放入列表
            domc = xml.dom.minidom.parse(path)
            rootc = domc.documentElement
            detail = rootc.getElementsByTagName(tagname)
            aa=[]

            for m in range(0,len(detail)):
                detail1=detail[m]
                cc=detail1.firstChild.data
                #print c
                resaultapi=re.findall(":(.*?),",cc)
                #resault1=re.findall("\"img\":\"(.+?)\"",c)
                aa.append(resaultapi)
            return aa
        except:
            print("获取接口数据失败")
            print(traceback.format_exc())

    #读取页面数据，get方法
    def handleorderRead(self,driver,url,headers):
        try:
            req = requests.get(url,headers = headers)
            b=req.text
            #print b
            return b
        except:
            print("get取页面数据失败")
            print(traceback.format_exc())

    #读取页面数据，post方法
    def orderRead(self,driver,url,data,headers):
        try:
            req = requests.post(url,data=data,headers = headers)
            b=req.text
            print b
            return b

        except:
            print("post取页面数据失败")
            print(traceback.format_exc())

    #cookie保存
    def cookieSave(self,driver):
        try:
            #get the session cookie
            cookie = [item["name"] + "=" + item["value"] for item in self.driver.get_cookies()]
            #print cookie

            cookiestr = ';'.join(item for item in cookie)
            return cookiestr
        except:
            print("保存cookie失败")
            print(traceback.format_exc())

    #登录毕方
    def loginUser(self,driver,name,user,pwd,login,logname,username,password):
        try:
            self.findId(driver,name).clear()
            self.findId(driver,name).send_keys(logname)
            self.findId(driver,user).clear()
            self.findId(driver,user).send_keys(username)
            self.findId(driver,pwd).clear()
            self.findId(driver,pwd).send_keys(password)
            self.findId(driver,login).click()

            return driver
        except:
            print(traceback.format_exc())
            print(u"登录失败")
            return driver


    def set_up(self,driver):

        url="http://beefun.wsgjp.com/"
        driver.get(url)
        driver.maximize_window()
        driver.implicitly_wait(10)

        name="$1b8bb415$corpName"
        user="$1b8bb415$userName"
        pwd="$1b8bb415$pwdEdit"
        login="$1b8bb415$btnLogin"
        loginname="xsx123456"
        username="xsx"
        password="grasp147."
        self.loginUser(driver,name ,user,pwd,login,loginname,username,password)

    #启动浏览器
    def startBrowser(self,browserType):
        try:
            if browserType.upper()=='CHROME':
                driver=webdriver.Chrome()
            elif browserType.upper()=='IE':
                driver=webdriver.Ie()
            elif browserType.upper()=='FIREFOX' or browserType.upper()=='FF':
                driver=webdriver.Firefox()
            return driver
        except:
            print(u'启动浏览器失败')
            return driver

    #读取页面数据，get方法
    def handleorderRead(self,driver,url,headers):
        try:
            req = requests.get(url,headers = headers)
            b=req.text
            print b
            return b
        except:
            print("get取页面数据失败")
            print(traceback.format_exc())

    #读取页面数据，post方法
    def postRead(self,driver,url,data,headers):
        try:
            req = requests.post(url,data=data,headers = headers)
            b=req.text
            print b
            return b

        except:
            print(u"post取页面数据失败")
            print(traceback.format_exc())


    def erpOrder(self,b):
        #从第5个开始，最后9个不要
            resaultpage=re.findall("(?<=tradeid).*?(?=tradeid)",b)
            lisorder=[]
            lis=[]

            flag=0
            for sigle in resaultpage:
                if flag>=4 and flag<=(len(resaultpage)-9):
                    lisorder.append(sigle)
                flag=flag+1
            #print len(lisorder)
            #print lisorder[1]
            for a in lisorder:
                #print a
                result=re.compile("\"")
                z=result.sub('',a)
                #print len(z)
                #print z
                c=re.findall(":(.*?),",z)
                lis.append(c)

            print len(lis)
            #print lis[1][0],lis[2][0]
            return  lis


    def erpItems(self,res):
        try:
            '''
            itemsno=re.findall("itemCount\":(.*?)}",res)
            itemexist=int(itemsno[0])
            print "itemscount:"+str(itemexist)
           '''
            before=re.findall("itemList\":(.*?)itemCount",res)

            print "before...................."
            print len(before)
            print before[0]

            itemlist=re.findall("id(.*?)ptypeurl",before[0])
            print "itemlist................."
            print len(itemlist)
            return itemlist

        except:
            print(u"抓取页面数据失败")
            print(traceback.format_exc())

    def erpmengpageItems(self,itemlist):
        try:
            itemlis=re.compile("\"")
            resault=itemlis.sub('',itemlist)
            iresault=re.findall(":(.*?),",resault)

            return iresault

        except:
            print(u"萌店取面数据放进List失败")
            print(traceback.format_exc())

    def getTime(self):
        timelist=[]
        end=datetime.datetime.now()
        endtime=end.strftime("%Y-%m-%d %H:%M:%S")
        print endtime
        timelist.append(endtime)
        #先获得时间数组格式的日期
        start=(datetime.datetime.now()-datetime.timedelta(days=1))
        #转换为其他字符串格式:
        starttime = start.strftime("%Y-%m-%d %H:%M:%S")
        print starttime
        timelist.append(starttime)
        return timelist


    def gettoken(self,sql):
        conn= MySQLdb.connect(host='172.16.0.96',user='website',passwd='test@2011',db='beefun',port = 4306)
        cur = conn.cursor()
        aa=cur.execute(sql)
        #print aa
        row=cur.fetchone()
        print row[0]
        info = cur.fetchmany(aa)
        '''
        print cur.fetchone()
        print cur.scroll(0,'absolute')

        for i in info:
            print i
        '''
        cur.close()
        conn.commit()
        conn.close()
        token= row[0]
        return token

    def gettokeneach(self,sql):
        conn= MySQLdb.connect(host='172.16.0.96',user='website',passwd='test@2011',db='beefun',port = 4306)
        cur = conn.cursor()
        aa=cur.execute(sql)

        info = cur.fetchmany(aa)
        '''
        print cur.fetchone()
        print cur.scroll(0,'absolute')

        for i in info:
            print i
        '''
        cur.close()
        conn.commit()
        conn.close()
        return info

    #发送邮件
    def send_Email(self,address):
        timeStamp=time.time()
        timeArray = time.localtime(timeStamp)
        otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S" , timeArray)

        From = "xusxue@grasp.com.cn"
        To1 = "1206626163@qq.com"
        To2="625499968@qq.com"
        To3="394264687@qq.com"
        To4="2275879116@qq.com"
        file_name = "D:/apiresault.html"#附件名
        host='61.139.77.221'
        server = smtplib.SMTP(host,25)
        server.login("xusxue@grasp.com.cn","abcd+123456789") #仅smtp服务器需要验证时

        # 构造MIMEMultipart对象做为根容器
        main_msg = email.MIMEMultipart.MIMEMultipart()

        # 构造MIMEText对象做为邮件显示内容并附加到根容器
        text_msg = email.MIMEText.MIMEText(u"网店接口，请下载后查看，预览显示不完全",_charset="utf-8")
        main_msg.attach(text_msg)

        #构造MIMEBase对象做为文件附件内容并附加到根容器
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
        main_msg['From'] =From
        main_msg['To'] = address
        main_msg['Subject'] = "beenfun report"+otherStyleTime
        main_msg['Date'] = email.Utils.formatdate( )

        # 得到格式化后的完整文本
        fullText = main_msg.as_string( )

        # 用smtp发送邮件
        try:
            server.sendmail(From, address, fullText)
            #server.sendmail(From, To2, fullText)
            #server.sendmail(From, To3, fullText)
            #server.sendmail(From, To4, fullText)
        finally:
            server.quit()

