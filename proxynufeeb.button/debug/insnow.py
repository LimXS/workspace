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




def createorder(num,becode):
    today = datetime.date.today()
    overday=today+datetime.timedelta(days=-1)

    today=today.strftime('%Y-%m-%d')
    overday=overday.strftime('%Y-%m-%d')
    #print overday
    getdatas=[]


    todaytime=datetime.datetime.now()
    overtime=todaytime+datetime.timedelta(days=-1)
    todaytime=todaytime.strftime('%Y-%m-%d %H:%M:%S')
    #print todaytime
    overtime=overtime.strftime('%Y-%m-%d %H:%M:%S')
    #print overtime

    fc=open(r"E:\new.txt")
    item=fc.read()


    etypeids={'1151581351029634':u'（京东）君问手机旗舰店','28455803329945743':'yhhycg','3293278338924174660':u'天机数码店','3293278520339531720':'2',
         '7608004971719290048':u'亚马逊问问店','8080322324297667222':u'拍拍问问店','8489586093684841544':'3','8623847055876651182':'1',
         '8623847055891053928':'4','9584807475043094946':u'供销平台','12184225228657647994':'5','12184225317590870082':'9',
         '12184225317595413496':'8','17440768759282257092':'6','17440768759282258064':u'君问数码官方旗舰店','17440768759282258217':'7'
         }
    #print item
    itemlist=re.findall("values(.*?);",item)

    for a in range(num):
        #网店

        #etypeid=random.choice(etypeids.keys())
        #etypename=etypeids[etypeid]

        etypeid='28455803329945743'
        etypename='yhhycg'

        #商品
        itemnow1=random.choice(itemlist)
        #print itemnow
        itemdata1=re.findall("'(.*?)'",itemnow1)
        #print itemdata[1]

        itemnow2=random.choice(itemlist)
        #print itemnow
        itemdata2=re.findall("'(.*?)'",itemnow2)
        #print itemdata[1]


        listspro=[u"北京",u"上海",u"广州",u"深圳",u"天津",u"四川",u"湖北",u"湖南",u"西藏",u"青海"]
        listcity=[u"北京市",u"上海市",u"广州市",u"深圳市",u"天津市",u"成都",u"武汉",u"西宁",u"拉萨",u"西安"]
        listunit=[u"高新区",u"武侯区",u"中和",u"华阳",u"红牌楼",u"双流区",u"西城区",u"朝阳区"]
        listadd=[u"天府大道",u"武侯大道",u"熊猫大道",u"剑南大道",u"益州大道",u"龙泉",u"三圣乡",u"布达拉宫u",u"克勒青",u"西单"]
        billdata=(
            {"orderEntity":{"atypeid":0,"buyerid":0,"tradeid":becode+browser.getrandnumber()+str(a),"number":None,"payno":"","gatheringvchcode":0,
                        "tradecreatetime":todaytime,"trademodifiedtime":todaytime,"modifiedtime":todaytime,"orderupdatetime":None,"steptradedeliverytime":None,
                        "tradepaiedtime":None,"tradefinishtime":None,"createtype":1,"tradetype":0,"tradestatus":2,"steptradestatus":0,"refundstatus":0,
                        "processstatus":0,"shippingtype":0,"sellerflag":0,"invoicestatus":0,"isneedinvoice":False,"deleted":False,"isptypematchup":False,
                        "tradetotal":float(itemdata2[3])+float(itemdata1[3]),"total":0,"settletotal":0,"paiedtotal":0,"preferentialtotal":0,"mallfee":0,"customerfreightfee":0,
                        "buyerpayment":0,"expressagencyfee":0,"atypetypeid":None,"atypename":None,"btypename":None,"etypename":"乐迪","displaynumber":None,
                        "creatorid":"17440768759282236639","creatorname":"hehe","taxtotal":0,"deliverdeleted":False,"taxamount":0,"financeaudit":0,
                        "clearancetype":0,"taxfee":0,"exceptiontypes":"","gatheringnumber":None,"mallsendtype":0,"storecode":None,"storeorderstatus":0,
                        "refundapplytotal":0,"receivebillid":0,"currencyid":0,"currencyname":"","isreceivebill":False,"ktypeid":"17440768759281675167",
                        "kfullname":None,"downloadsource":0,
                        "eshopsaleorderdetails":[
                            {"selected":True,"id":"28455809166320424","fullname":itemdata1[1],"unit":1,"fullbarcode":None,"unitname":"个","ucode":None,
                             "urate":1,"xcode":"","ptypeid":itemdata1[5],"taobao_cid":0,"supplyinfo":"","bargainprice":0,"mailbargainprice":0,
                             "bondedbargainprice":0,"prop1_enabled":False,"prop2_enabled":False,"prop3_enabled":False, "modifiedtime":overday,"preprice":float(itemdata1[3]),
                             "preprice2":220,"preprice3":230,"retailprice":float(itemdata1[3]),"preprice4":240,"preprice5":250,"preprice6":260,"preprice7":270,
                             "preprice8":280,"preprice9":290,"preprice10":300,"prop1name":"","prop2name":"","prop3name":"","usercode":itemdata1[0],
                             "propnames":"","prop1":0,"prop2":0,"prop3":0,"area":u"成都","standard":"12*25","type":"0125436","name":itemdata1[2],
                             "skuid":"28455809166319530","goodsqty":0,"pic_url":"","comment":"test1"+browser.getrandnumber()+str(a),"protectdays":"0","snenabled":0,"weight":2,"volume":4080,
                             "ptypecode":itemdata1[0],"ptypename":itemdata1[1],"ptypeunit":"个","ptypestandard":"12*25","ptypetype":"0125436",
                             "ptypearea":u"成都","unitrate":1,"assprice":float(itemdata1[3]),"settleprice":float(itemdata1[3]),"assqty":1,"mallfee":0,"total":float(itemdata1[3]),
                             "settletotal":float(itemdata1[3])},
                            {"selected":True,"id":"28455809168684668","fullname":itemdata2[1],"unit":1,"fullbarcode":None,"unitname":"个","ucode":None,
                             "urate":1,"xcode":"","ptypeid":itemdata2[5],"taobao_cid":0,"supplyinfo":"","bargainprice":0,"mailbargainprice":0,
                             "bondedbargainprice":0,"prop1_enabled":False,"prop2_enabled":False,"prop3_enabled":False,"modifiedtime":overday,"preprice":float(itemdata2[3]),
                             "preprice2":220,"preprice3":230,"retailprice":float(itemdata2[3]),"preprice4":240,"preprice5":250,"preprice6":260,"preprice7":270,"preprice8":280,
                             "preprice9":290,"preprice10":300,"prop1name":"","prop2name":"","prop3name":"","usercode":itemdata2[0],"propnames":"","prop1":0,
                             "prop2":0,"prop3":0,"area":u"成都","standard":"12*25","type":"0125436","name":itemdata2[2],"skuid":"28455809168684666","goodsqty":0,
                             "pic_url":"","comment":"test2"+browser.getrandnumber()+str(a),"protectdays":"0","snenabled":0,"weight":2,"volume":4080,"ptypecode":itemdata2[0],
                             "ptypename":itemdata2[1],"ptypeunit":"个","ptypestandard":"12*25","ptypetype":"0125436","ptypearea":u"成都","unitrate":1,"assprice":float(itemdata2[3]),
                             "settleprice":float(itemdata2[3]),
                             "assqty":1,"mallfee":0,"total":float(itemdata2[3]),"settletotal":float(itemdata2[3])}],
                        "eshopbuyer":None,"secrettype":0,"eshoptype":0,"vchcode":0,"profileid":0,
                        "buyermessage":"","sellermemo":"","summary":"ordersummary"+browser.getrandnumber()+str(a),"comment":"ordercomment"+browser.getrandnumber()+str(a),"sellertype":None,"invoicetitle":"","tradefrom":None,
                        "platformfreightname":None,"freightname":None,"freightbillno":None,"eshopid":etypeid,"bshoptype":0,"shoptype":0,
                        "eshopname":etypename,"btypeid":"28455803329961343","etypeid":"3121930940033791","createtime":today,"customerpayaccount":"",
                        "customeremail":"","customershopaccount":"Tcustomer"+browser.getrandnumber()+str(a),"customerreceiver":"TREcustomer"+browser.getrandnumber()+str(a),"customerreceivercountry":u"中国",
                        "customerreceiverprovince":random.choice(listspro),"customerreceivercity":random.choice(listcity),"customerreceiverdistrict":random.choice(listunit),
                        "customerreceiveraddress":random.choice(listadd)+browser.getrandnumber()+str(a)+"号","customerreceiverphone":"1"+browser.getrandnumber(),"customerreceivermobile":"1"+browser.getrandnumber(),"idcard":"",
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
    pageorderdata=browser.requestpost(sendurl,salredata,headers2,1)
    print pageorderdata

def selgreenf3(salredata,):
    pageorderdata=browser.requestpost(sendurl,salredata,headers3,1)
    print pageorderdata

def selgreenf4(salredata,):
    pageorderdata=browser.requestpost(sendurl,salredata,headers4,1)
    print pageorderdata

def selgreenf5(salredata,):
    pageorderdata=browser.requestpost(sendurl,salredata,headers5,1)
    print pageorderdata

def sendpro(num):

    fc=open(r"D:\cookies\eshop6.txt")
    nskcookie=fc.read()
    browser.delaytime(1)
    f2=open(r"D:\cookies\eshop7.txt")
    nskcookie2=f2.read()
    browser.delaytime(1)
    f3=open(r"D:\cookies\eshop8.txt")
    nskcookie3=f3.read()
    browser.delaytime(1)
    f4=open(r"D:\cookies\eshop9.txt")
    nskcookie4=f4.read()
    f5=open(r"D:\cookies\eshop10.txt")
    nskcookie5=f5.read()
    global headers
    global headers2
    global headers3
    global headers4
    global headers5

    global sendurl
    headers={'cookie':nskcookie,"Content-Type": "application/json"}
    headers2={'cookie':nskcookie2,"Content-Type": "application/json"}
    headers3={'cookie':nskcookie3,"Content-Type": "application/json"}
    headers4={'cookie':nskcookie4,"Content-Type": "application/json"}
    headers5={'cookie':nskcookie5,"Content-Type": "application/json"}


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
        sendurl="http://hehe.wsgjp.com.cn/Beefun/Beefun.EShopSale.EShopSaleOrderCreate.ajax/SaveAndAuditSaleOrder"
        senddatas=createorder(1000,"NEW2TEST4CreateOrder")
        data=pool.map(selgreenf,senddatas)
    elif num==1:
        sendurl="http://hehe.wsgjp.com.cn/Beefun/Beefun.EShopSale.EShopSaleOrderCreate.ajax/SaveAndAuditSaleOrder"
        senddatas=createorder(1000,"NEW2TEST4DeCheck")
        data=pool.map(selgreenf2,senddatas)

    elif num==2:
        sendurl="http://hehe.wsgjp.com.cn/Beefun/Beefun.EShopSale.EShopSaleOrderCreate.ajax/SaveAndAuditSaleOrder"
        senddatas=createorder(1000,"NEW2TEST4DePrint")
        data=pool.map(selgreenf3,senddatas)

    elif num==3:
        sendurl="http://hehe.wsgjp.com.cn/Beefun/Beefun.EShopSale.EShopSaleOrderCreate.ajax/SaveAndAuditSaleOrder"
        senddatas=createorder(1000,"NEW2TEST4DeCheckItem")
        data=pool.map(selgreenf4,senddatas)
    else:
        sendurl="http://hehe.wsgjp.com.cn/Beefun/Beefun.EShopSale.EShopSaleOrderCreate.ajax/SaveAndAuditSaleOrder"
        senddatas=createorder(1000,"NEW2TEST4DeSendItem")
        data=pool.map(selgreenf5,senddatas)

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

    p0 = multiprocessing.Process(target = sendpro,args=(0,))
    p0.start()

    p1 = multiprocessing.Process(target = sendpro,args=(1,))
    p1.start()

    p2 = multiprocessing.Process(target = sendpro,args=(2,))
    p2.start()

    p3 = multiprocessing.Process(target = sendpro,args=(3,))
    p3.start()

    p4 = multiprocessing.Process(target = sendpro,args=(4,))
    p4.start()
'''
    p5 = multiprocessing.Process(target = sendpro,args=(4,))
    p5.start()

    p6 = multiprocessing.Process(target = sendpro,args=(5,))
    p6.start()



    #p99 = multiprocessing.Process(target = sendpro,args=(100,))
    #p99.start()
'''


