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
import MySQLdb
import random
import gevent.pool
import gevent.monkey

gevent.monkey.patch_all()
from common import browserClass
browser=browserClass.browser()

#coding: utf-8
import multiprocessing
import time

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


def createorder(num):
    today = datetime.date.today()
    #overday=today+datetime.timedelta(days=-6)

    today=today.strftime('%Y-%m-%d')
    getdatas=[]
    for a in range(num):
        #ptypeid给一个list 随机选...
        ptypeid="870037043076268"
        sql="SELECT UserCode,FullName,preprice,pic_url,name FROM ptype WHERE id='"+ptypeid+"'"
        conn= MySQLdb.connect(host='172.16.0.96',user='website',passwd='test@2011',db='beefun',port = 4306)
        cur = conn.cursor()
        sqlreault=cur.execute(sql)
        # 使用 fetchone() 方法获取一条数据库。
        data = cur.fetchone()
        '''
        print data
        for da in data:
            print da
        '''
        cur.close()
        listspro=["北京","上海","广州","深圳","天津","四川","湖北","湖南","西藏","青海"]
        listcity=["北京市","上海市","广州市","深圳市","天津市","成都","武汉","西宁","拉萨","西安"]
        listunit=["高新区","武侯区","中和","华阳","红牌楼","双流区","西城区","朝阳区"]
        listadd=["天府大道","武侯大道","熊猫大道","剑南大道","益州大道","龙泉","三圣乡","布达拉宫","克勒青","西单"]
        billdata=(
        {"orderEntity":{"atypeid":0,"buyerid":0,"tradeid":"A2Today-20170106"+browser.getrandnumber()+str(a),"number":None,"payno":"","gatheringvchcode":0,
                    "tradecreatetime":today,"trademodifiedtime":today,"modifiedtime":today,"orderupdatetime":None,"steptradedeliverytime":None,
                    "tradepaiedtime":None,"tradefinishtime":None,"createtype":1,"tradetype":0,"tradestatus":2,"steptradestatus":0,"refundstatus":0,
                    "processstatus":0,"shippingtype":0,"sellerflag":0,"invoicestatus":0,"isneedinvoice":False,"deleted":False,"isptypematchup":False,
                    "tradetotal":134.4,"total":0,"settletotal":0,"paiedtotal":0,"preferentialtotal":0,"mallfee":0,"customerfreightfee":0,
                    "buyerpayment":0,"expressagencyfee":0,"atypetypeid":None,"atypename":None,"btypename":None,"etypename":None,"displaynumber":None,
                    "creatorid":"2605637371041214558","creatorname":"毕方","taxtotal":0,"deliverdeleted":False,"taxamount":0,"financeaudit":0,
                    "clearancetype":0,"taxfee":0,"exceptiontypes":"","gatheringnumber":None,"mallsendtype":0,"storecode":None,"storeorderstatus":0,
                    "refundapplytotal":0,"receivebillid":0,"currencyid":0,"isreceivebill":False,"ktypeid":"2605637371178862817","kfullname":None,
                    "downloadsource":0,
                    "eshopsaleorderdetails":[{"selected":True,"id":"870037042886185","fullname":"13卷 泡沫布双面胶带 泡沫海绵胶 强胶带袋广告胶粘胶条双面胶_宽12mm\\13卷\\每卷约3.5米",
                                                  "unit":1,"fullbarcode":"123456789","unitname":"","ucode":None,"urate":1,"xcode":"S-1235A","ptypeid":"870037042905880",
                                                  "taobao_cid":0,"supplyinfo":"","bargainprice":0,"mailbargainprice":0,"bondedbargainprice":0,"prop1_enabled":False,
                                                  "prop2_enabled":False,"prop3_enabled":False,"modifiedtime":today,"preprice":16.8,"preprice2":0,
                                                  "preprice3":0,"retailprice":16.8,"preprice4":0,"preprice5":0,"preprice6":0,"preprice7":0,"preprice8":0,"preprice9":0,
                                                  "preprice10":0,"prop1name":"","prop2name":"","prop3name":"","usercode":"S-1235A","propnames":"","prop1":0,"prop2":0,
                                                  "prop3":0,"area":"","standard":"","type":"","name":"13卷","skuid":"870037042886184","goodsqty":460,"pic_url":"https://img.alicdn.com/bao/uploaded/i2/TB1Ec5hMVXXXXa7XVXXXXXXXXXX_!!0-item_pic.jpg",
                                                  "comment":"","protectdays":"300","snenabled":0,"weight":0,"volume":0,"ptypecode":"S-1235A","ptypename":"13卷 泡沫布双面胶带 泡沫海绵胶 强胶带袋广告胶粘胶条双面胶_宽12mm\\13卷\\每卷约3.5米",
                                                  "ptypeunit":"","ptypestandard":"","ptypetype":"","ptypearea":"","unitrate":1,"assprice":16.8,"settleprice":16.8,"assqty":3,"mallfee":0,
                                                  "total":50.4,"settletotal":50.4,"comboid":0},
                                             {"selected":True,"id":"870037042898457","fullname":data[1],"unit":1,
                                              "fullbarcode":None,"unitname":"","ucode":None,"urate":1,"xcode":data[0],"ptypeid":ptypeid,"taobao_cid":0,"supplyinfo":"",
                                              "bargainprice":0,"mailbargainprice":0,"bondedbargainprice":0,"prop1_enabled":False,"prop2_enabled":False,"prop3_enabled":False,
                                              "modifiedtime":today,"preprice":float(data[2]),"preprice2":0,"preprice3":0,"retailprice":float(data[2]),"preprice4":0,"preprice5":0,
                                              "preprice6":0,"preprice7":0,"preprice8":0,"preprice9":0,"preprice10":0,"prop1name":"","prop2name":"","prop3name":"","usercode":data[0],
                                              "propnames":"","prop1":0,"prop2":0,"prop3":0,"area":"","standard":"","type":"","name":data[4],"skuid":"870037042898456","goodsqty":242,
                                              "pic_url":data[3],"comment":"","protectdays":"360",
                                              "snenabled":0,"weight":0,"volume":0,"ptypecode":data[0],"ptypename":data[1],"ptypeunit":"",
                                              "ptypestandard":"","ptypetype":"","ptypearea":"","unitrate":1,"assprice":float(data[2]),"settleprice":float(data[2]),"assqty":1,"mallfee":0,"total":float(data[2]),
                                              "settletotal":float(data[2]),"comboid":0}],
                    "eshopbuyer":None,"secrettype":0,"eshoptype":0,"vchcode":0,"profileid":0,"buyermessage":"","sellermemo":"",
                    "summary":None,"comment":None,"sellertype":None,"invoicetitle":"","tradefrom":None,"platformfreightname":None,"freightname":None,"freightbillno":None,
                    "eshopid":"2605638027863255550","bshoptype":0,"shoptype":0,"eshopname":"yhhycg","btypeid":"2605638027863256597","etypeid":0,
                    "createtime":"2017-01-05","customerpayaccount":"","customeremail":"","customershopaccount":"Tcustomer"+browser.getrandnumber(),"customerreceiver":"shouhuoren",
                    "customerreceivercountry":"中国","customerreceiverprovince":random.choice(listspro),"customerreceivercity":random.choice(listcity),"customerreceiverdistrict":random.choice(listunit),
                    "customerreceiveraddress":random.choice(listadd)+browser.getrandnumber()+"号","customerreceiverphone":"","customerreceivermobile":"1"+browser.getrandnumber(),"idcard":"",
                    "customerreceiverarea":"","customeralladdress":"","customerreceiverzipcode":"","di":"","ai":"","ri":"","pi":"","pai":"","mi":"","ici":"",
                    "FullbarCode":""},"mode":"New","isSumbimt":False}
        )
        getdatas.append(billdata)
    return getdatas

def subtocheck(num):
    today = datetime.date.today()
    #overday=today+datetime.timedelta(days=-6)
    today=today.strftime('%Y-%m-%d')
    getdatas=[]
    sql="SELECT vchcode FROM eshop_saleorder WHERE tradeid LIKE 'AToday%'"
    conn= MySQLdb.connect(host='172.16.0.96',user='website',passwd='test@2011',db='beefun',port = 4306)
    cur = conn.cursor()
    res=cur.execute(sql)
    data=cur.fetchmany(res)
    for k in data:
        print k[0]
        billdata={"ids":[str(k[0])]}
        getdatas.append(billdata)
    return getdatas


def selgreenf(salredata,):
    pageorderdata=browser.requestpost(sendurl,salredata,headers,1)
    print pageorderdata

def selgreenf2(salredata,):
    pageorderdata=browser.requestpost(sendurl,salredata,headers,1)
    print pageorderdata



def selgreenf3(salredata,):

    pageorderdata=browser.requestpost(sendurl,salredata,headers2,1)
    #nowsub=json.dumps(salredata)
    print
    trid=salredata["orderEntity"]["tradeid"]
    sql="SELECT vchcode FROM eshop_saleorder  WHERE tradeid='"+trid+"'"
    conn= MySQLdb.connect(host='172.16.0.96',user='website',passwd='test@2011',db='beefun',port = 4306)
    cur = conn.cursor()
    sqlreault=cur.execute(sql)
    # 使用 fetchone() 方法获取一条数据库。
    data = cur.fetchone()
    suburl="http://dba.wsgjp.com.cn/Beefun/Beefun.EShopSale.EShopSaleOrderList.ajax/AuditBills"
    data={"ids":[str(data[0])]}
    pageorderdata=browser.requestpost(suburl,data,headers2,1)
    print pageorderdata

def selgreenf4(salredata,):

    pageorderdata=browser.requestpost(sendurl,salredata,headers3,1)
    #nowsub=json.dumps(salredata)
    print
    trid=salredata["orderEntity"]["tradeid"]
    sql="SELECT vchcode FROM eshop_saleorder  WHERE tradeid='"+trid+"'"
    conn= MySQLdb.connect(host='172.16.0.96',user='website',passwd='test@2011',db='beefun',port = 4306)
    cur = conn.cursor()
    sqlreault=cur.execute(sql)
    # 使用 fetchone() 方法获取一条数据库。
    data = cur.fetchone()
    suburl="http://dba.wsgjp.com.cn/Beefun/Beefun.EShopSale.EShopSaleOrderList.ajax/AuditBills"
    data={"ids":[str(data[0])]}
    pageorderdata=browser.requestpost(suburl,data,headers,1)
    print pageorderdata

def sendpro(num):

    fc=open(r"D:\cookies\eshop.txt")
    nskcookie=fc.read()
    browser.delaytime(1)
    f2=open(r"D:\cookies\eshop2.txt")
    nskcookie2=f2.read()
    browser.delaytime(1)
    f3=open(r"D:\cookies\eshop3.txt")
    nskcookie3=f3.read()
    browser.delaytime(1)
    global headers
    global headers2
    global headers3

    global sendurl
    headers={'cookie':nskcookie,"Content-Type": "application/json"}
    headers2={'cookie':nskcookie2,"Content-Type": "application/json"}
    headers3={'cookie':nskcookie3,"Content-Type": "application/json"}


    global headslist
    headslist=[]
    headslist.append(headers)

    '''
    for n in range(0,5):
        fc=open(r"D:\cookies\eshop"+str(n)+".txt")
        nskcookie=fc.read()
        header={'cookie':nskcookie,"Content-Type": "application/json"}
        headslist.append(header)
    '''
    #headers2={'cookie':nskcookie2,"Content-Type": "application/json"}
    pool = gevent.pool.Pool(25)
    if num==0:
        sendurl="http://dba.wsgjp.com.cn/Beefun/Beefun.EShopSale.EShopSaleOrderCreate.ajax/SaveAndAuditSaleOrder"
        senddatas=createorder(1000)
        data=pool.map(selgreenf,senddatas)
    elif num==1:
        sendurl="http://dba.wsgjp.com.cn/Beefun/Beefun.EShopSale.EShopSaleOrderCreate.ajax/SaveAndAuditSaleOrder"
        senddatas=createorder(30000)
        data=pool.map(selgreenf3,senddatas)

    elif num==2:
        sendurl="http://dba.wsgjp.com.cn/Beefun/Beefun.EShopSale.EShopSaleOrderCreate.ajax/SaveAndAuditSaleOrder"
        senddatas=createorder(30000)
        data=pool.map(selgreenf4,senddatas)
    else:
        sendurl="http://dba.wsgjp.com.cn/Beefun/Beefun.EShopSale.EShopSaleOrderList.ajax/AuditBills"
        senddatas=subtocheck(1000)
        data=pool.map(selgreenf2,senddatas)

    '''
    elif num==2:
        sendurl="http://dba.wsgjp.com.cn/Beefun/Beefun.Bill.StockOverflowBill.ajax/Save"
        senddatas=selgreenf2(1000)
    elif num==3:
        sendurl="http://dba.wsgjp.com.cn/Beefun/Beefun.Bill.GatheringBill.ajax/SaveBill"
        senddatas=selgreenf2(1000)
    elif num==4:
        sendurl="http://dba.wsgjp.com.cn/Beefun/Beefun.Bill.PaymentBill.ajax/SaveBill"
        senddatas=selgreenf2(1000)
    elif num==5:
        sendurl="http://dba.wsgjp.com.cn/Beefun/Beefun.Bill.PaymentBill.ajax/SaveDraftBill"
        senddatas=selgreenf2(1000)

    elif num==6:
        sendurl="http://dba.wsgjp.com.cn/Beefun/Beefun.Bill.SaleBill.ajax/Save"
        senddatas=selgreenf2(1000)
    elif num==7:
        sendurl="http://dba.wsgjp.com.cn/Beefun/Beefun.Bill.SaleBackBill.ajax/Save"
        senddatas=selgreenf2(1000)
    elif num==8:
        sendurl="http://dba.wsgjp.com.cn/Beefun/Beefun.Bill.StockBill.ajax/Save"
        senddatas=selgreenf2(1000)
    elif num==9:
        sendurl="http://dba.wsgjp.com.cn/Beefun/Beefun.Bill.StockBackBill.ajax/Save"
        senddatas=selgreenf2(1000)

    else:
        sendurl="http://dba.wsgjp.com.cn/Carpa.Web/Carpa.Web.Script.DataService.ajax/GetPagerData"
        senddatas=selgreenf2(1000)
'''


if __name__ == "__main__":
    #pool = multiprocessing.Pool(processes = 3)
    #f=open(r"D:\cookies\stocksave.txt")
    #nskcookie=f.read()
    #print nskcookie
    #global headers
    #global salreurl
    #headers={'cookie':nskcookie,"Content-Type": "application/json"}
    #salreurl="http://dba.wsgjp.com.cn/Beefun/Beefun.Bill.StockOrderBill.ajax/Save"
    #newcookie()

    #p0 = multiprocessing.Process(target = sendpro,args=(0,))
    #p0.start()

    p1 = multiprocessing.Process(target = sendpro,args=(1,))
    p1.start()

    p2 = multiprocessing.Process(target = sendpro,args=(2,))
    p2.start()
    '''
    p3 = multiprocessing.Process(target = sendpro,args=(2,))
    p3.start()
    p4 = multiprocessing.Process(target = sendpro,args=(3,))
    p4.start()

    p5 = multiprocessing.Process(target = sendpro,args=(4,))
    p5.start()

    p6 = multiprocessing.Process(target = sendpro,args=(5,))
    p6.start()

    p7 = multiprocessing.Process(target = sendpro,args=(6,))
    p7.start()

    p8 = multiprocessing.Process(target = sendpro,args=(7,))
    p8.start()

    p9 = multiprocessing.Process(target = sendpro,args=(8,))
    p9.start()


    p10 = multiprocessing.Process(target = sendpro,args=(9,))
    p10.start()

    #p99 = multiprocessing.Process(target = sendpro,args=(100,))
    #p99.start()
'''


