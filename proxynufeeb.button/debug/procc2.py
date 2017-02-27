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

            f=open(r"D:\cookies\cennote2.txt",'w')
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

            f=open(r"D:\cookies\stocksave2.txt",'w')
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


#进货订单数据
def greenget(num):
    today = datetime.date.today()
    #overday=today+datetime.timedelta(days=-6)

    today=today.strftime('%Y-%m-%d')
    getdatas=[]
    for a in range(0,num):
        #stockurlsave="http://dba.wsgjp.com.cn/Beefun/Beefun.Bill.StockOrderBill.ajax/Save"
        nskdata=(
        {"bill":{"date":"2017-01-04","draft":False,"displaynumber":"","number":"TJHD-20170104"+browser.getrandnumber()+str(a),"inputno":"2605637371041214558",
                 "inputfullname":"毕方","redword":False,"redold":False,"billtype":0,"ktypeid":"2605637371178862817","kfullname":"主仓库",
                 "btypetax":0,"todate":today,"efullname":"丁超","currencyid":0,"btypeid":"2605637371041213604",
                 "bfullname":"网店客户","etypeid":"869735145061843","summary":"","comment":"",
                 "details":[{"prop1":0,"prop1name":"","prop2":0,"prop2name":"","prop3":0,"prop3name":"","pic_url":"https://img.alicdn.com/bao/uploaded/i1/T1WlXHFlFgXXXXXXXX_!!0-item_pic.jpg",
                             "ptypeid":"870037142332159","pfullname":"得力803封箱器 胶带切割器打包切割器 金属封箱胶带打包切割","pname":"得力80","ptypecode":"803",
                             "brandname":"","temp_ucode":"803","temp_ucode_flag":True,"ptypeunit":"","unit":"1","unitrate":1,"ptypestandard":"","ptypetype":"",
                             "ptypearea":"","snenabled":0,"ptypeweight":0,"oneweight":0,"batchno":None,"producedate":None,"expirationdate":None,"position":None,
                             "pstatus":0,"comment":"","prop1_enabled":False,"prop2_enabled":False,"prop3_enabled":False,"fullbarcode":"","retailprice":28,
                             "ptypeweightall":0,"tax":0,"showstockqty":1000026.89,"assdpprice":325,"discount":1,"assqty":1,"price":325,"dpprice":325,"qty":1,
                             "dptotal":325,"asstpprice":325,"tpprice":325,"tptotal":325,"taxtotal":0,"assprice":325,"total":325,"mallfee":0,"urate0":"","urate1":"",
                             "urate2":""}],"isover":False,"../Selector/BTypeSelector.gspx":"00002","customerreceiver":None,"customerreceivermobile":None,
                 "customerreceiverphone":None,"customerreceiverzipcode":None,"customerreceiverprovince":None,"customerreceivercity":None,
                 "customerreceiverdistrict":None,"customerreceiveraddress":None,"deliveryinfoid":0,"deliveryinfotext":"","total":325,"ftypeid":0}}
            )
        getdatas.append(nskdata)

    return getdatas

#零售单数据
def lsdatas(num):
    today = datetime.date.today()
    #overday=today+datetime.timedelta(days=-6)

    today=today.strftime('%Y-%m-%d')
    getdatas=[]
    for a in range(0,num):

        nskdata=(
        {"bill":{"date":today,"salebill":1,"number":"TLS-20170104"+browser.getrandnumber()+str(a),"inputno":"2605637371041214558",
                 "inputfullname":"毕方", "etypeid":"2605638028977887647","efullname":"李四","deptid":"2605638028997505217","dfullname":"开发部",
                 "ktypeid":"2605637371178862817","kfullname":"主仓库","btypeid":"2605637371041213604","bfullname":"网店客户","etypetypeid":"00003",
                 "dtypetypeid":"00002","vipcardid":0,"vipdiscount":0,
                 "details":[{"prop1":0,"prop1name":"","prop2":0,"prop2name":"","prop3":0, "prop3name":"","ptypeid":"870037142332159",
                             "pfullname":"得力803封箱器 胶带切割器打包切割器 金属封箱胶带打包切割","ptypecode":"803","brandname":None,"pname":"得力80",
                             "temp_ucode":"803","temp_ucode_flag":True,"ptypeunit":"","unit":"1","unitrate":1,"ptypestandard":"","ptypetype":"",
                             "ptypearea":"","snenabled":0,"batchno":None,"producedate":None,"position":None,"pstatus":0,"comment":"",
                             "prop1_enabled":False,"prop2_enabled":False,"prop3_enabled":False,"fullbarcode":"","promovchcode":0,"assdpprice":28,
                             "assqty":1,"discount":1,"tax":0,"price":28,"dpprice":28,"qty":1,"dptotal":28,"asstpprice":28,"tpprice":28,"tptotal":28,
                             "taxtotal":0,"assprice":28,"total":28,"mallfee":0,"ptypeweightall":0},
                            {"prop1":0,"prop1name":"","prop2":0,"prop2name":"","prop3":0,"prop3name":"","ptypeid":"870037142359478",
                             "pfullname":"得力7696速写本专业素描绘画本A4专业美术用纸 297*210mm_单本","ptypecode":"7696","brandname":None,
                             "pname":"得力76","temp_ucode":"7696","temp_ucode_flag":True,"ptypeunit":"","unit":"1","unitrate":1,"ptypestandard":"",
                             "ptypetype":"","ptypearea":"","snenabled":0,"batchno":None,"producedate":None,"position":None,"pstatus":0,"comment":"",
                             "protectdays":250,"prop1_enabled":False,"prop2_enabled":False,"prop3_enabled":False,"fullbarcode":"987654321",
                             "promovchcode":0,"assdpprice":12.9,"assqty":1,"discount":1,"tax":0,"price":12.9,"dpprice":12.9,"qty":1,"dptotal":12.9,
                             "asstpprice":12.9,"tpprice":12.9,"tptotal":12.9,"taxtotal":0,"assprice":12.9,"total":12.9,"mallfee":0,"ptypeweightall":0}],
                 "storeid":None,"posid":None,"total":40.9,"preference":0.9,"atypeid":"2605637371041211671","afullname":"现金","atypetypeid":"0000100003",
                 "atypetotal":40,"recivetotal01":40,"integralexchange":"0","integralamount":0,"vipcardamount":"0","payaccount":"0","settleaccounts":None,
                 "recivemoney":100,"backmoney":60}}
            )
        getdatas.append(nskdata)

    return getdatas

#报溢单数据
def stockover(num):
    today = datetime.date.today()
    overday=today+datetime.timedelta(days=-6)

    today=today.strftime('%Y-%m-%d')
    overday=overday.strftime('%Y-%m-%d')
    getdatas=[]
    for a in range(0,num):

        nskdata=(
        {"billEntity":{"vchtype":14,
                       "details":[{"prop1":0,"prop1name":"","prop2":0,"prop2name":"","prop3":0,"prop3name":"","pic_url":"https://img.alicdn.com/bao/uploaded/i2/TB13QtNKpXXXXbOXFXXXXXXXXXX_!!0-item_pic.jpg",
                                   "ptypeid":"870037142370015","pfullname":"日本 百乐 BLLH20C/百乐  水笔/中性笔/财务笔 彩色_黑色0.4mm","pname":"日本 百",
                                   "ptypecode":"BLLH20C4-B-CHN","brandname":"","temp_ucode":"BLLH20C4-B-CHN","temp_ucode_flag":True,"ptypeunit":"",
                                   "unit":"1","unitrate":1,"ptypestandard":"","ptypetype":"","ptypearea":"","snenabled":0,"ptypeweight":0,"oneweight":0,"batchno":None,
                                   "producedate":None,"expirationdate":None,"position":None,"pstatus":0,"comment":"","prop1_enabled":False,"prop2_enabled":False,
                                   "prop3_enabled":False,"retailprice":28,"ptypeweightall":0,"assqty":1,"qty":1,"urate0":"","urate1":"","urate2":""}],"type":0,
                       "ktypeid":"2605637371178862817","kfullname":"主仓库","ktypeid2":0,"kfullname2":None,"deliverytype":0,"date":"2017-01-04","btypeid":None,
                       "total":0,"etypeid":"869735145061843","deptid":"2605638028997505217","number":"TBY-20170104"+browser.getrandnumber()+str(a),"summary":"","comment":"","currencyid":0,
                       "exchangerate":0,"postid":0,"eshopid":0,"inputno":"2605637371041214558","postno":0,"billtype":0,"dlytype":0,"createtype":0,"auditstate":0,
                       "profileid":0,"vchcode":0,"period":0,"draft":True,"redword":False,"redold":False,"redoldcode":0,"postindex":0,
                       "overtime":overday,"printtimes":0,"__checkindex":0,"__result":None,"__checknumber":False,"displaynumber":"","assistant":None,"bfullname":None,
                       "efullname":"丁超","dfullname":"开发部","inputfullname":"毕方","postfullname":None,"loadovertime":None,"btypearea":None,"btypeperson":None,
                       "btypephone":None,"btypetelandaddress":None,"btypebank":None,"btypetaxnumber":None,"btypebankaccount":None,"currencyname":None,"btypetax":0,
                       "custominfo1":None,"custominfo2":None,"custominfo3":None,"fc_total":0,"projectsid":0,"projectname":None,"profitlayout":None,
                       "../Selector/ETypeSelector.gspx":"00008","~/Selector/DepartmentSelector.gspx":"00002","../Selector/KTypeSelector.gspx":"00002","ftypeid":0}}
            )
        getdatas.append(nskdata)

    return getdatas

#收款单
def remoney(num):
    today = datetime.date.today()
    overday=today+datetime.timedelta(days=-6)

    today=today.strftime('%Y-%m-%d')
    overday=overday.strftime('%Y-%m-%d')
    getdatas=[]
    for a in range(0,num):

        nskdata=(
        {"bill":{"date":"2017-01-04","draft":True,"number":"TSK-20170104"+browser.getrandnumber()+str(a),"displaynumber":"",
                 "assistant":{"checketype":True,"inioverdate":"2016-08-24","serverdate":"2017-01-04"},"total":1,"inputno":"2605637371041214558",
                 "inputfullname":"毕方","currencyid":0,"btypeid":"2605637371041213575","bfullname":"申通e物流","etypeid":"869735145061843",
                 "efullname":"丁超","deptid":"2605638028997505217","dfullname":"开发部","summary":"","comment":"",
                 "details":[{"usercode":"0141","fullname":"建设银行","atypeid":"2605637371041211673","atypetypeid":"000010000400001","currencyid":0,
                             "comment":"","total":1}],"gatheringdlys":[],"querynumber":"","querysummary":"","vchtype":4,"paytotal":None,"atypeid":None,
                 "atypetypeid":None}}
        )
        getdatas.append(nskdata)

    return getdatas

#付款单
def givemoney(num):
    today = datetime.date.today()
    overday=today+datetime.timedelta(days=-6)

    today=today.strftime('%Y-%m-%d')
    overday=overday.strftime('%Y-%m-%d')
    getdatas=[]
    for a in range(0,num):

        nskdata=(
        {"bill":{"vchtype":66,"fc_settletotal":0,"fc_preference":0,"fromordercode":None,"atypeid":None,"atypetypeid":None,"afullname":None,
                 "atypetotal":0,"jtotal":0,"jremain":0,"preference":0,"settletype":2,"settleaccounts":[],"gatheringdlys":[],"paytotal":None,
                 "details":[{"usercode":"101","fullname":"现金","atypeid":"2605637371041211671","atypetypeid":"0000100003","currencyid":0,
                             "comment":"","total":1}],"date":"2017-01-04","btypeid":"2605637371041213575","total":1,"etypeid":"869735145061843",
                 "deptid":"2605638028997505217","number":"TFK-20170104"+browser.getrandnumber()+str(a),"summary":"","comment":"","currencyid":"0","exchangerate":0,"postid":0,
                 "eshopid":0,"inputno":"2605637371041214558","postno":0,"billtype":0,"dlytype":0,"createtype":0,"auditstate":0,"profileid":0,
                 "vchcode":0,"period":0,"draft":True,"redword":False,"redold":False,"redoldcode":0,"postindex":0,"overtime":overday,
                 "printtimes":0,"__checkindex":0,"__result":None,"__checknumber":False,"displaynumber":"",
                 "assistant":{"checketype":True,"inioverdate":"2016-08-24","serverdate":"2017-01-04"},"bfullname":"申通e物流","efullname":"丁超",
                 "dfullname":"开发部","inputfullname":"毕方","postfullname":None,"loadovertime":None,"btypearea":None,"btypeperson":None,
                 "btypephone":None,"btypetelandaddress":None,"btypebank":None,"btypetaxnumber":None,"btypebankaccount":None,"currencyname":None,
                 "btypetax":0,"custominfo1":None,"custominfo2":None,"custominfo3":None,"fc_total":0,"projectsid":0,"projectname":None,
                 "profitlayout":None,"querynumber":"","querysummary":""}}
        )
        getdatas.append(nskdata)

    return getdatas

#销售出库
def saleout(num):
    today = datetime.date.today()
    overday=today+datetime.timedelta(days=-6)

    today=today.strftime('%Y-%m-%d')
    overday=overday.strftime('%Y-%m-%d')
    getdatas=[]
    for a in range(0,num):

        nskdata=(
        {"bill":{"vchtype":11,"collectionondelivery":False,"collectiontotal":0,"fc_collectiontotal":0,"customerfreightfee":0,"mallfee":0,"taxfee":0,
                 "fc_mallfee":0,"fc_customerfreightfee":0,"fc_taxfee":0,"repairid":0,"storeid":0,"posid":0,"integralexchange":0,"integralamount":0,
                 "vipcardamount":0,"bonuspoints":0,"customershopaccount":None,"payaccount":None,"dlyretail":0,"ischecked":False,"invoicetag":False,
                 "eshopname":None,"eshoptype":0,"freighttype":0,"isonlinesend":0,"atypeid":None,"atypetypeid":None,"afullname":None,"atypetotal":0,
                 "preference":0,"jtotal":0,"jremain":0,"settletype":1,"settleaccounts":[],"gatheringdlys":[],"fc_settletotal":0,"fc_preference":0,
                 "freightbtypeid":0,"freightbfullname":None,"freightatypeid":None,"freightafullname":"","freightatypetypeid":None,"freightatypetotal":0,
                 "freightfee":0,"freightfee_remain":0,"freightfee_buyerpay":0,"freightbillno":"","freightfeeshare":0,"freightfee_needshare":False,
                 "freightfeesharetype":0,"fc_freightfeeshare":0,"fc_freightfee":0,"fc_freightsettletotal":0,"fc_freightfeeremain":0,"vipcardid":0,"vipdiscount":0,
                 "custominfo1":None,"custominfo2":None,"custominfo3":None,
                 "details":[{"prop1":0,"prop1name":"","prop2":0,"prop2name":"","prop3":0,"prop3name":"","pic_url":"https://img.alicdn.com/bao/uploaded/i1/T1WlXHFlFgXXXXXXXX_!!0-item_pic.jpg",
                             "ptypeid":"870037142332159","pfullname":"得力803封箱器 胶带切割器打包切割器 金属封箱胶带打包切割","pname":"得力80","ptypecode":"803",
                             "brandname":"","temp_ucode":"803","temp_ucode_flag":True,"ptypeunit":"","unit":"1","unitrate":1,"ptypestandard":"","ptypetype":"",
                             "ptypearea":"","snenabled":0,"ptypeweight":0,"oneweight":0,"batchno":None,"producedate":None,"expirationdate":None,"position":None,
                             "pstatus":0,"comment":"","prop1_enabled":False,"prop2_enabled":False,"prop3_enabled":False,"fullbarcode":"","retailprice":28,
                             "ptypeweightall":0,"tax":0,"showstockqty":999738.89,"promovchcode":0,"assdpprice":3652,"discount":1,"assqty":1,"price":3652,
                             "dpprice":3652,"qty":1,"dptotal":3652,"asstpprice":3652,"tpprice":3652,"tptotal":3652,"taxtotal":0,"assprice":3652,"total":3652,
                             "mallfee":0,"urate0":"","urate1":"","urate2":"","ordercode":0,"orderdlycode":0}],"type":0,"ktypeid":"2605637371178862817",
                 "kfullname":"主仓库","ktypeid2":0,"kfullname2":None,"deliverytype":0,"date":"2017-01-04","btypeid":"2605637371041213604","total":3652,
                 "etypeid":"869735145061843","deptid":0,"number":"TXS-20170104"+browser.getrandnumber()+str(a),"summary":"","comment":"","currencyid":0,"exchangerate":0,"postid":0,
                 "eshopid":0,"inputno":"2605637371041214558","postno":0,"billtype":0,"dlytype":0,"createtype":0,"auditstate":0,"profileid":0,"vchcode":0,
                 "period":0,"draft":True,"redword":False,"redold":False,"redoldcode":0,"postindex":0,"overtime":overday,"printtimes":0,
                 "__checkindex":0,"__result":None,"__checknumber":False,"displaynumber":"","assistant":None,"bfullname":"网店客户","efullname":"丁超",
                 "dfullname":None,"inputfullname":"毕方","postfullname":None,"loadovertime":None,"btypearea":"","btypeperson":None,"btypephone":None,
                 "btypetelandaddress":None,"btypebank":None,"btypetaxnumber":None,"btypebankaccount":None,"currencyname":None,"btypetax":0,"fc_total":0,
                 "projectsid":0,"projectname":None,"profitlayout":None,"../Selector/BTypeSelector.gspx":"00002","btelandaddress":"","bperson":"","bphone":"",
                 "../Selector/ETypeSelector.gspx":"00008","../Selector/KTypeSelector.gspx":"00002","ftypeid":0}}
        )
        getdatas.append(nskdata)

    return getdatas

#销售退货
def salereturn(num):
    today = datetime.date.today()
    overday=today+datetime.timedelta(days=-6)

    today=today.strftime('%Y-%m-%d')
    overday=overday.strftime('%Y-%m-%d')
    getdatas=[]
    for a in range(0,num):

        nskdata=(
        {"bill":{"vchtype":45,"mallfee":0,"fc_mallfee":0,"taxfee":0,"fc_taxfee":0,"ischecked":False,"invoicetag":False,"dlyretail":0,"payaccount":None,
                 "vipcardamount":0,"bonuspoints":0,"storeid":0,"posid":0,"atypeid":None,"atypetypeid":None,"afullname":None,"atypetotal":0,"preference":0,
                 "jtotal":0,"jremain":0,"settletype":2,"settleaccounts":[],"gatheringdlys":[],"fc_settletotal":0,"fc_preference":0,"vipcardid":0,
                 "vipdiscount":0,"details":[{"prop1":0,"prop1name":"","prop2":0,"prop2name":"","prop3":0,"prop3name":"","pic_url":"https://img.alicdn.com/bao/uploaded/i1/T1WlXHFlFgXXXXXXXX_!!0-item_pic.jpg",
                                             "ptypeid":"870037142332159","pfullname":"得力803封箱器 胶带切割器打包切割器 金属封箱胶带打包切割","pname":"得力80",
                                             "ptypecode":"803","brandname":"","temp_ucode":"803","temp_ucode_flag":True,"ptypeunit":"","unit":"1","unitrate":1,
                                             "ptypestandard":"","ptypetype":"","ptypearea":"","snenabled":0,"ptypeweight":0,"oneweight":0,"batchno":None,
                                             "producedate":None,"expirationdate":None,"position":None,"pstatus":0,"comment":"","prop1_enabled":False,
                                             "prop2_enabled":False,"prop3_enabled":False,"fullbarcode":"","retailprice":28,"ptypeweightall":0,"tax":0,
                                             "showstockqty":999737.89,"assdpprice":3652,"discount":1,"assqty":1,"price":3652,"dpprice":3652,"qty":1,"dptotal":3652,
                                             "asstpprice":3652,"tpprice":3652,"tptotal":3652,"taxtotal":0,"assprice":3652,"total":3652,"mallfee":0,"urate0":"",
                                             "urate1":"","urate2":""}],"type":0,"ktypeid":"2605637371178862817","kfullname":"主仓库","ktypeid2":0,
                 "kfullname2":None,"deliverytype":0,"date":"2017-01-04","btypeid":"2605637371041213604","total":3652,"etypeid":"869735145061843","deptid":0,
                 "number":"TXT-20170104"+browser.getrandnumber()+str(a),"summary":"","comment":"","currencyid":0,"exchangerate":0,"postid":0,"eshopid":0,"inputno":"2605637371041214558",
                 "postno":0,"billtype":0,"dlytype":0,"createtype":0,"auditstate":0,"profileid":0,"vchcode":0,"period":0,"draft":True,"redword":False,"redold":False,
                 "redoldcode":0,"postindex":0,"overtime":overday,"printtimes":0,"__checkindex":0,"__result":None,"__checknumber":False,
                 "displaynumber":"","assistant":None,"bfullname":"网店客户","efullname":"丁超","dfullname":None,"inputfullname":"毕方","postfullname":None,
                 "loadovertime":None,"btypearea":None,"btypeperson":None,"btypephone":None,"btypetelandaddress":None,"btypebank":None,"btypetaxnumber":None,
                 "btypebankaccount":None,"currencyname":None,"btypetax":0,"custominfo1":None,"custominfo2":None,"custominfo3":None,"fc_total":0,"projectsid":0,
                 "projectname":None,"profitlayout":None,"../Selector/BTypeSelector.gspx":"00002","customerreceiver":None,"customerreceivermobile":None,
                 "customerreceiverphone":None,"customerreceiverzipcode":None,"customerreceiverprovince":None,"customerreceivercity":None,
                 "customerreceiverdistrict":None,"customerreceiveraddress":None,"deliveryinfoid":0,"deliveryinfotext":"","../Selector/ETypeSelector.gspx":"00008",
                 "../Selector/KTypeSelector.gspx":"00002","ftypeid":0}}
        )
        getdatas.append(nskdata)

    return getdatas


#进货入库
def stockinto(num):
    today = datetime.date.today()
    overday=today+datetime.timedelta(days=-6)

    today=today.strftime('%Y-%m-%d')
    overday=overday.strftime('%Y-%m-%d')
    getdatas=[]
    for a in range(0,num):

        nskdata=(
        {"bill":{"vchtype":34,"ischecked":False,"invoicetag":False,"fromordercode":0,"wmsorder":False,"atypeid":None,"atypetypeid":None,
                 "afullname":None,"atypetotal":0,"preference":0,"jtotal":0,"jremain":0,"settletype":2,"settleaccounts":[],"gatheringdlys":[],
                 "fc_settletotal":0,"fc_preference":0,"freightbtypeid":0,"freightbfullname":None,"freightatypeid":None,"freightafullname":"",
                 "freightatypetypeid":None,"freightatypetotal":0,"freightfee":0,"freightfee_remain":0,"freightfee_buyerpay":0,"freightbillno":"",
                 "freightfeeshare":0,"freightfee_needshare":False,"freightfeesharetype":0,"fc_freightfeeshare":0,"fc_freightfee":0,
                 "fc_freightsettletotal":0,"fc_freightfeeremain":0,"expense":0,"expenseshare":0,"expense_needshare":False,"fc_expense":0,
                 "fc_expenseshare":0,
                 "details":[{"prop1":0,"prop1name":"","prop2":0,"prop2name":"","prop3":0,"prop3name":"","pic_url":"https://img.alicdn.com/bao/uploaded/i2/TB13QtNKpXXXXbOXFXXXXXXXXXX_!!0-item_pic.jpg",
                             "ptypeid":"870037142380645","pfullname":"日本 百乐 BLLH20C/百乐  水笔/中性笔/财务笔 彩色_黑色0.5mm","pname":"日本 百",
                             "ptypecode":"BLLH20C5-B-CHN","brandname":"","temp_ucode":"BLLH20C5-B-CHN","temp_ucode_flag":True,"ptypeunit":"","unit":"1",
                             "unitrate":1,"ptypestandard":"","ptypetype":"","ptypearea":"","snenabled":0,"ptypeweight":0,"oneweight":0,"batchno":None,
                             "producedate":None,"expirationdate":None,"position":None,"pstatus":0,"comment":"","prop1_enabled":False,"prop2_enabled":False,
                             "prop3_enabled":False,"fullbarcode":"","retailprice":28,"ptypeweightall":0,"tax":1.22,"showstockqty":31,"assdpprice":15,
                             "discount":0.85,"assqty":1,"price":12.9056,"dpprice":15,"qty":1,"dptotal":15,"asstpprice":12.75,"tpprice":12.75,"tptotal":12.75,
                             "taxtotal":0.16,"assprice":12.9056,"total":12.91,"mallfee":0,"urate0":"","urate1":"","urate2":"","ordercode":0,"orderdlycode":0}],
                 "type":0,"ktypeid":"2605637371178862817","kfullname":"主仓库","ktypeid2":0,"kfullname2":None,"deliverytype":0,"date":"2017-01-04",
                 "btypeid":"2605637371041213604","total":12.91,"etypeid":"869735145061843","deptid":0,"number":"TJH-20170104"+browser.getrandnumber()+str(a),"summary":"","comment":"",
                 "currencyid":0,"exchangerate":0,"postid":0,"eshopid":0,"inputno":"2605637371041214558","postno":0,"billtype":0,"dlytype":0,"createtype":0,
                 "auditstate":0,"profileid":0,"vchcode":0,"period":0,"draft":True,"redword":False,"redold":False,"redoldcode":0,"postindex":0,
                 "overtime":today,"printtimes":0,"__checkindex":0,"__result":None,"__checknumber":False,"displaynumber":"",
                 "assistant":None,"bfullname":"网店客户","efullname":"丁超","dfullname":None,"inputfullname":"毕方","postfullname":None,"loadovertime":None,
                 "btypearea":None,"btypeperson":None,"btypephone":None,"btypetelandaddress":None,"btypebank":None,"btypetaxnumber":None,"btypebankaccount":None,
                 "currencyname":None,"btypetax":0,"custominfo1":None,"custominfo2":None,"custominfo3":None,"fc_total":0,"projectsid":0,"projectname":None,
                 "profitlayout":None,"wmsOrder":False,"~/Selector/BTypeSelector.gspx":"00002","customerreceiver":None,"customerreceivermobile":None,
                 "customerreceiverphone":None,"customerreceiverzipcode":None,"customerreceiverprovince":None,"customerreceivercity":None,
                 "customerreceiverdistrict":None,"customerreceiveraddress":None,"deliveryinfoid":0,"deliveryinfotext":"",
                 "~/Selector/ETypeSelector.gspx":"00008","~/Selector/KTypeSelector.gspx":"00002","ftypeid":0}}
        )
        getdatas.append(nskdata)

    return getdatas

#进货退货
def stockreturn(num):
    today = datetime.date.today()
    overday=today+datetime.timedelta(days=-6)

    today=today.strftime('%Y-%m-%d')
    overday=overday.strftime('%Y-%m-%d')
    getdatas=[]
    for a in range(0,num):

        nskdata=(
        {"bill":{"vchtype":6,"ischecked":False,"invoicetag":False,"fromordercode":0,"wmsorder":False,"atypeid":None,"atypetypeid":None,
                 "afullname":None,"atypetotal":0,"preference":0,"jtotal":0,"jremain":0,"settletype":2,"settleaccounts":[],"gatheringdlys":[],
                 "fc_settletotal":0,"fc_preference":0,"freightbtypeid":0,"freightbfullname":None,"freightatypeid":None,"freightafullname":"",
                 "freightatypetypeid":None,"freightatypetotal":0,"freightfee":0,"freightfee_remain":0,"freightfee_buyerpay":0,"freightbillno":"",
                 "freightfeeshare":0,"freightfee_needshare":False,"freightfeesharetype":0,"fc_freightfeeshare":0,"fc_freightfee":0,
                 "fc_freightsettletotal":0,"fc_freightfeeremain":0,"expense":0,"expenseshare":0,"expense_needshare":False,"fc_expense":0,
                 "fc_expenseshare":0,
                 "details":[{"prop1":0,"prop1name":"","prop2":0,"prop2name":"","prop3":0,"prop3name":"","pic_url":"https://img.alicdn.com/bao/uploaded/i2/TB13QtNKpXXXXbOXFXXXXXXXXXX_!!0-item_pic.jpg",
                             "ptypeid":"870037142380645","pfullname":"日本 百乐 BLLH20C/百乐  水笔/中性笔/财务笔 彩色_黑色0.5mm","pname":"日本 百",
                             "ptypecode":"BLLH20C5-B-CHN","brandname":"","temp_ucode":"BLLH20C5-B-CHN","temp_ucode_flag":True,"ptypeunit":"","unit":"1",
                             "unitrate":1,"ptypestandard":"","ptypetype":"","ptypearea":"","snenabled":0,"ptypeweight":0,"oneweight":0,"batchno":None,
                             "producedate":None,"expirationdate":None,"position":None,"pstatus":0,"comment":"","prop1_enabled":False,"prop2_enabled":False,
                             "prop3_enabled":False,"fullbarcode":"","retailprice":28,"ptypeweightall":0,"tax":1.22,"showstockqty":31,"assdpprice":15,
                             "discount":0.85,"assqty":1,"price":12.9056,"dpprice":15,"qty":1,"dptotal":15,"asstpprice":12.75,"tpprice":12.75,"tptotal":12.75,
                             "taxtotal":0.16,"assprice":12.9056,"total":12.91,"mallfee":0,"urate0":"","urate1":"","urate2":"","ordercode":0,"orderdlycode":0}],
                 "type":0,"ktypeid":"2605637371178862817","kfullname":"主仓库","ktypeid2":0,"kfullname2":None,"deliverytype":0,"date":"2017-01-04",
                 "btypeid":"2605637371041213604","total":12.91,"etypeid":"869735145061843","deptid":0,"number":"TJT-20170104"+browser.getrandnumber()+str(a),"summary":"","comment":"",
                 "currencyid":0,"exchangerate":0,"postid":0,"eshopid":0,"inputno":"2605637371041214558","postno":0,"billtype":0,"dlytype":0,"createtype":0,
                 "auditstate":0,"profileid":0,"vchcode":0,"period":0,"draft":True,"redword":False,"redold":False,"redoldcode":0,"postindex":0,
                 "overtime":today,"printtimes":0,"__checkindex":0,"__result":None,"__checknumber":False,"displaynumber":"",
                 "assistant":None,"bfullname":"网店客户","efullname":"丁超","dfullname":None,"inputfullname":"毕方","postfullname":None,"loadovertime":None,
                 "btypearea":None,"btypeperson":None,"btypephone":None,"btypetelandaddress":None,"btypebank":None,"btypetaxnumber":None,"btypebankaccount":None,
                 "currencyname":None,"btypetax":0,"custominfo1":None,"custominfo2":None,"custominfo3":None,"fc_total":0,"projectsid":0,"projectname":None,
                 "profitlayout":None,"wmsOrder":False,"~/Selector/BTypeSelector.gspx":"00002","customerreceiver":None,"customerreceivermobile":None,
                 "customerreceiverphone":None,"customerreceiverzipcode":None,"customerreceiverprovince":None,"customerreceivercity":None,
                 "customerreceiverdistrict":None,"customerreceiveraddress":None,"deliveryinfoid":0,"deliveryinfotext":"",
                 "~/Selector/ETypeSelector.gspx":"00008","~/Selector/KTypeSelector.gspx":"00002","ftypeid":0}}
        )
        getdatas.append(nskdata)

    return getdatas




#查询
def seledatas(num):
    getdatas=[]
    notdata={"pagerId":"$c3e1bf43$grid_pager1","queryParams":{"vchtype":"","beginDate":"2016-12-20","endDate":"2017-01-30","redwordType":0,"dlyType":0},"orders":None,"filter":None,"first":0,"count":50000}
    getdatas=[notdata]*num


    return getdatas

def greenf2(salredata,):
    pageorderdata=browser.requestpost(sendurl,salredata,headers,1)
    print pageorderdata
    #k=browser.datatrunjson2(pageorderdata)
    #print k["Message"]
def selgreenf2(salredata,):
    pageorderdata=browser.requestpost(sendurl,salredata,headers2,1)
    print pageorderdata

def sendpro(num):

    fc=open(r"D:\cookies\stocksave2.txt")
    nskcookie=fc.read()
    f2=open(r"D:\cookies\cennote2.txt")
    nskcookie2=f2.read()
    global headers
    global headers2
    global sendurl
    headers={'cookie':nskcookie,"Content-Type": "application/json"}
    headers2={'cookie':nskcookie2,"Content-Type": "application/json"}
    pool = gevent.pool.Pool(25)
    if num==0:
        sendurl="http://dba.wsgjp.com.cn/Beefun/Beefun.Bill.StockOrderBill.ajax/Save"
        senddatas=greenget(1000)
    elif num==1:
        sendurl="http://dba.wsgjp.com.cn/Beefun/Beefun.Bill.Retail.RetailBill.ajax/Save"
        senddatas=lsdatas(1000)
    elif num==2:
        sendurl="http://dba.wsgjp.com.cn/Beefun/Beefun.Bill.StockOverflowBill.ajax/Save"
        senddatas=stockover(1000)
    elif num==3:
        sendurl="http://dba.wsgjp.com.cn/Beefun/Beefun.Bill.GatheringBill.ajax/SaveBill"
        senddatas=remoney(1000)
    elif num==4:
        sendurl="http://dba.wsgjp.com.cn/Beefun/Beefun.Bill.PaymentBill.ajax/SaveBill"
        senddatas=givemoney(1000)
    elif num==5:
        sendurl="http://dba.wsgjp.com.cn/Beefun/Beefun.Bill.PaymentBill.ajax/SaveDraftBill"
        senddatas=givemoney(1000)

    elif num==6:
        sendurl="http://dba.wsgjp.com.cn/Beefun/Beefun.Bill.SaleBill.ajax/Save"
        senddatas=saleout(1000)
    elif num==7:
        sendurl="http://dba.wsgjp.com.cn/Beefun/Beefun.Bill.SaleBackBill.ajax/Save"
        senddatas=salereturn(1000)
    elif num==8:
        sendurl="http://dba.wsgjp.com.cn/Beefun/Beefun.Bill.StockBill.ajax/Save"
        senddatas=stockinto(1000)
    elif num==9:
        sendurl="http://dba.wsgjp.com.cn/Beefun/Beefun.Bill.StockBackBill.ajax/Save"
        senddatas=stockreturn(1000)

    else:
        sendurl="http://dba.wsgjp.com.cn/Carpa.Web/Carpa.Web.Script.DataService.ajax/GetPagerData"
        senddatas=seledatas(1000)

    if num==100:
        data=pool.map(selgreenf2,senddatas)
    else:
        data=pool.map(greenf2,senddatas)

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

    p1 = multiprocessing.Process(target = sendpro,args=(0,))
    p1.start()
    p2 = multiprocessing.Process(target = sendpro,args=(1,))
    p2.start()
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



