# -*- coding: utf-8 -*-
'''
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
'''
from common import  loggingClass
import xml.dom.minidom
from PIL import Image
import requests
import re
from bs4 import BeautifulSoup
import time
import datetime
import random
import traceback
import urllib
import Queue
import threading
import json
import hashlib
import random
from common import browserClass
browser=browserClass.browser()
lock=threading.Lock()
class Worker(threading.Thread):
    def __init__(self,tagQueue,resultQueue,**kwds):
        threading.Thread.__init__(self,**kwds)
        self.tagQueue=tagQueue
        self.resultQueue = resultQueue


    def run(self):
        while 1:
            try:
                callable,args,kws=self.tagQueue.get(False)
                res=callable(*args,**kws)
                self.resultQueue.put(res)  # put result
            except Queue.Empty:
                break

class workerManger:
    def __init__(self,num_workers=10):
        self.tagQueue=Queue.Queue()
        self.resultQueue = Queue.Queue()  # 输出结果的队列
        self.workers=[]
        self._recruitThreads(num_workers)

    def _recruitThreads(self, num_workers):
        for i in range(num_workers):
            worker = Worker(self.tagQueue, self.resultQueue)  # 创建工作线程
            self.workers.append(worker)  # 加入到线程队列

    def start(self):
        for w in self.workers:
            w.start()

    def wait_for_complete(self):
        while len(self.workers):
            worker = self.workers.pop()  # 从池中取出一个线程处理请求
            worker.join()
            if worker.isAlive() and not self.tagQueue.empty():
               self.workers.append(worker)  # 重新加入线程池中
        print 'All jobs were complete.'


    def add_job(self, callable, *args, **kwds):
         self.tagQueue.put((callable, args, kwds))  # 向工作队列中加入请求

    def get_result(self, *args, **kwds):
        return self.resultQueue.get(*args, **kwds)

rannum=browser.getrandnumber()
print rannum
#生成url
def createorderdata(n):
    a=["a"]
    senddata=a*n
    '''
    today = datetime.date.today()
    today=today.strftime('%Y-%m-%d')
    for k in range(n):
        nskdata=(
        {"bill":{"date":"2016-12-27","draft":False,"displaynumber":"","number":"TEST2-JHD20161227-"+rannum[:-6]+str(k),"inputno":"2605638079543105363",
                 "inputfullname":"xsx","redword":False,"redold":False,"billtype":0,"ktypeid":"2605638079543104740","kfullname":"主仓库",
                 "btypetax":0,"todate":today,"efullname":"001","currencyid":0,"btypeid":"2605638088187950285",
                 "bfullname":"t5123443","etypeid":"2605638088210451192","summary":"222222222222","comment":"222222222222",
                 "details":[{"prop1":0,"prop1name":"","prop2":0,"prop2name":"","prop3":0,"prop3name":"",
                         "pic_url":"http://wd.geilicdn.com/vshop520219391-1459218328272-4913776.png?w=480&h=0","ptypeid":"869585272784951",
                         "pfullname":"002 无编码修改_Ax","pname":"002","ptypecode":"a1x","brandname":"","temp_ucode":"a1x","temp_ucode_flag":True,
                         "ptypeunit":"个","unit":"1","unitrate":1,"ptypestandard":"","ptypetype":"","ptypearea":"","snenabled":0,"ptypeweight":0,
                         "oneweight":0,"batchno":None,"producedate":None,"expirationdate":None,"position":None,"pstatus":0,"comment":"",
                         "prop1_enabled":False,"prop2_enabled":False,"prop3_enabled":False,"fullbarcode":"","retailprice":29.5,"ptypeweightall":0,
                         "tax":0,"showstockqty":230,"assdpprice":13.6,"discount":1,"assqty":1,"price":13.6,"dpprice":13.6,"qty":1,"dptotal":13.6,
                         "asstpprice":13.6,"tpprice":13.6,"tptotal":13.6,"taxtotal":0,"assprice":13.6,"total":13.6,"mallfee":0,"urate0":"","urate1":"",
                         "urate2":""}],"isover":False,"../Selector/BTypeSelector.gspx":"00003","customerreceiver":None,"customerreceivermobile":None,
             "customerreceiverphone":None,"customerreceiverzipcode":None,"customerreceiverprovince":None,"customerreceivercity":None,
             "customerreceiverdistrict":None,"customerreceiveraddress":None,"deliveryinfoid":0,"deliveryinfotext":"","total":13.6,"ftypeid":0}}
        )
        senddata.append(nskdata)
    '''
    return senddata

def sendandcompare(senddata,headers):
    '''
    lock.acquire()
    #时间操作
    f=open(r'C:\workspace\proxynufeeb.button\temp','r')
    lasttime=f.read()
    f.close()
    nowtime=time.time()
    times=nowtime-float(lasttime)
    if times>4000:
        newcookie()
        f=open(r'C:\workspace\proxynufeeb.button\temp','w')
        f.write(str(nowtime))
        f.close()
    else:
        pass
    lock.release()
    '''
    today = datetime.date.today()
    overday=today+datetime.timedelta(days=-6)

    today=today.strftime('%Y-%m-%d')
    overday=overday.strftime('%Y-%m-%d')
    '''
    f=open(r"D:\cookies\stocksave.txt")
    nskcookie=f.read()
    #print nskcookie
    headers={'cookie':nskcookie,"Content-Type": "application/json"}
    '''
    #零售单
    for vchcode2 in range(0,10000):
        salreurl="http://dba.wsgjp.com.cn/Beefun/Beefun.Bill.Retail.RetailBill.ajax/Save"
        salredata=(
            {"bill":{"date":today,"salebill":1,"number":"LST-20170103-"+str(vchcode2)+browser.getrandnumber(),"inputno":"2605638079543105363",
                     "inputfullname":"xsx","etypeid":"2605638088210451192","efullname":"001","deptid":"2605638088426904000","dfullname":"xxx",
                     "ktypeid":"2605638079543104740","kfullname":"主仓库","btypeid":"2605638079543104347","bfullname":"网店客户",
                     "etypetypeid":"00001","dtypetypeid":"00001","storeid":"870112713973509","storename":"mendiantest2","posid":"870112720699452",
                     "posname":"md2cashd2","vipcardid":0,"vipdiscount":0,
                     "details":[{"prop1":0,"prop1name":"","prop2":0,"prop2name":"","prop3":0, "prop3name":"","ptypeid":"869585272784951",
                                 "pfullname":"002 无编码修改_Ax","ptypecode":"a1x","brandname":None,"pname":"002","temp_ucode":"a1x",
                                 "temp_ucode_flag":True,"ptypeunit":"个","unit":"1","unitrate":1,"ptypestandard":"","ptypetype":"","ptypearea":"",
                                 "snenabled":0,"batchno":None,"producedate":None,"position":None,"pstatus":0,"comment":"","prop1_enabled":False,
                                 "prop2_enabled":False,"prop3_enabled":False,"fullbarcode":"","promovchcode":0,"assdpprice":29.5,"assqty":1,
                                 "discount":1,"tax":0,"price":29.5,"dpprice":29.5,"qty":1,"dptotal":29.5,"asstpprice":29.5,"tpprice":29.5,"tptotal":29.5,
                                 "taxtotal":0,"assprice":29.5,"total":29.5,"mallfee":0,"ptypeweightall":0}],"total":29.5,"preference":0,
                     "atypeid":"2605638079543102554","afullname":"现金","atypetypeid":"0000100003","atypetotal":29.5,"recivetotal01":29.5,
                     "integralexchange":"0","integralamount":0,"vipcardamount":"0","payaccount":"0","settleaccounts":None,"recivemoney":200,
                     "backmoney":170.5}}
        )
        pageorderdata=browser.requestpost(salreurl,salredata,headers,1)
        print pageorderdata

    '''
    #salevchodelist=[]
    for vchcode2 in range(0,10000):
        salreurl="http://dba.wsgjp.com.cn/Beefun/Beefun.Bill.Retail.RetailBill.ajax/GetPos"
        salredata={"storeid":"870112713973509"}
        pageorderdata=browser.requestpost(salreurl,salredata,headers,1)
        print pageorderdata
    '''











def newcookie():
    #central note
    while 1:
        try:
            driver=browser.startBrowser('chrome')
            browser.set_up(driver)
            #browser.set_up(driver)
            #driver.get("http://dba.wsgjp.com.cn/")
            dom = xml.dom.minidom.parse(r'C:\workspace\proxynufeeb.button\frequentlyused\frelocation')
            module=browser.xmlRead(dom,'module',0)
            moduledetail=browser.xmlRead(dom,'moduledetail',1)

            browser.openModule2(driver,module,moduledetail)
            browser.delaytime(1)
            browser.refreshbutton(driver)
            browser.delaytime(1)
            cookies=browser.cookieSave(driver)
            browser.delaytime(1)
            #driver.close()

            f=open(r"D:\cookies\cennote.txt",'w')
            f.write(cookies)
            f.close()
            #driver.close()

            #check
            driver=browser.startBrowser('chrome')
            browser.set_up(driver)

            dom = xml.dom.minidom.parse(r'C:\workspace\proxynufeeb.button\stock\stocklocation')

            modulename=browser.xmlRead(dom,"module",0)
            moduledetail=browser.xmlRead(dom,'moduledetail',1)

            browser.openModule2(driver,modulename,moduledetail)
            browser.delaytime(1)
            browser.refreshbutton(driver)
            browser.delaytime(1)
            cookies=browser.cookieSave(driver)
            browser.delaytime(1)
            #driver.close()

            f=open(r"D:\cookies\stocksave.txt",'w')
            f.write(cookies)
            f.close()
            #driver.close()
            '''
            #报表
            driver=browser.startBrowser('chrome')
            browser.set_up(driver)
            dom = xml.dom.minidom.parse(r'C:\workspace\proxynufeeb.button\reports\reportslocation.xml')
            module=browser.xmlRead(dom,'module',0)
            moduledetail=browser.xmlRead(dom,'moduledetail',1)
            moduledd=browser.xmlRead(dom,'saleadd',3)

            browser.openModule3(driver,module,moduledetail,moduledd)
            browser.exjscommin(driver,"确定")
            browser.delaytime(5)
            browser.refreshbutton(driver)
            browser.delaytime(5)
            cookies=browser.cookieSave(driver)
            browser.delaytime(1)
            #driver.close()

            f=open(r"D:\cookies\salecookie.txt",'w')
            f.write(cookies)
            f.close()

            today = datetime.date.today()
            overday=today+datetime.timedelta(days=-6)

            today=today.strftime('%Y-%m-%d')
            overday=overday.strftime('%Y-%m-%d')

            #报表

            reskdel="http://dba.wsgjp.com.cn/Carpa.Web/Carpa.Web.Script.DataService.ajax/GetPagerData"
            reskdata={"pagerId":"$2c40fc$grid_pager1","queryParams":{"btypeid":None,"etypeid":None,"ktypeid":None,"ptypeid":None,"begin":overday,"end":today,"redold":-1,"vchtype":0,"orderClause":"order by ndx.date,ndx.number","eshopid":0},"orders":None,"filter":None,"first":0,"count":20000}
            f=open(r"D:\cookies\coktemp.txt")
            nskcookie=f.read()
            print nskcookie
            headers={'cookie':nskcookie,"Content-Type": "application/json"}
            pageorderdata=browser.requestpost(reskdel,reskdata,headers,1)
            print pageorderdata

            urlsum="http://dba.wsgjp.com.cn/Carpa.Web/Carpa.Web.Script.DataService.ajax/GetPagerSummary"
            udata={"pagerId":"$2c40fc$grid_pager1"}
            pageorderdata=browser.requestpost(urlsum,udata,headers,1)
            print pageorderdata
            '''

            #关闭
            driver=browser.startBrowser('chrome')
            browser.set_up(driver)

            dom = xml.dom.minidom.parse(r'C:\workspace\proxynufeeb.button\finance\financelocation')
            module=browser.xmlRead(dom,'module',0)
            moduledetail=browser.xmlRead(dom,'moduledetail',1)
            browser.openModule2(driver,module,moduledetail)
            browser.delaytime(1)
            driver.close()
            print "取cookie成功"
            break
        except:
            print "取cookie失败 重新取"
            pass



def main():
    a=random.sample(range(200,2260,1),100)
    '''
    cookstarttime=time.time()
    f=open(r'C:\workspace\proxynufeeb.button\temp','w')
    f.write(str(cookstarttime))
    f.close()
    '''
    #newcookie()

    a=[120,200]
    for num in a:
        f=open(r"D:\cookies\stocksave.txt")
        nskcookie=f.read()
        #print nskcookie
        headers={'cookie':nskcookie,"Content-Type": "application/json"}

        senddata=createorderdata(2000)
        #n=0
        print len(senddata)
        num_of_threads = num
        _st = time.time()
        loggingClass.addlogmes("info","开始-线程个数:",str(num_of_threads))
        wm = workerManger(num_of_threads)
        print num_of_threads


        for i in senddata:
            try:
                wm.add_job(sendandcompare,i,headers)
            except:
                pass
        #wm.get_result(printer,resault_list)
        wm.start()
        wm.wait_for_complete()
        loggingClass.addlogmes("info","结束-线程个数:",str(num_of_threads))
        usetime=time.time() - _st
        loggingClass.addlogmes("info","所用时间:",str(usetime))
        print 'result Queue\'s length == %d '% wm.resultQueue.qsize()
        '''
        while wm.resultQueue.qsize():
            a=wm.resultQueue.get()
            for i in a :
                print i
        '''

        print usetime

if __name__ == '__main__':
  main()




