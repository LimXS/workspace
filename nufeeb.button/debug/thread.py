# -*- coding: utf-8 -*-
'''
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
'''
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
    senddata=[]
    today = datetime.date.today()
    today=today.strftime('%Y-%m-%d')
    for k in range(n):
        nskdata=(
        {"bill":{"date":"2016-12-27","draft":False,"displaynumber":"","number":"TEST-JHD20161227-"+rannum+str(k),"inputno":"2605638079543105363",
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
    return senddata

def sendandcompare(senddata,headers):
    today = datetime.date.today()
    today=today.strftime('%Y-%m-%d')
    #制单
    stockurlsave="http://dba.wsgjp.com.cn/Beefun/Beefun.Bill.StockOrderBill.ajax/Save"
    pageorderdata=browser.requestpost(stockurlsave,senddata,headers,1)
    print pageorderdata
    vchcode=browser.datatrunjson2(pageorderdata)
    vchcode=vchcode["vchcode"]
    print vchcode
    browser.delaytime(1)
    #查询
    url="http://dba.wsgjp.com.cn/Carpa.Web/Carpa.Web.Script.DataService.ajax/GetPagerData"
    datas={"pagerId":"$609e9e2b$grid_pager1","queryParams":{"vchType":7,"xTypeid":"","isComplete":"1","isAudit":0,"isExport":"-1","dlytype":-1},"orders":None,"filter":None,"first":0,"count":100}
    pageorderdata=browser.requestpost(url,datas,headers,1)
    print pageorderdata
    browser.delaytime(1)

    #审核
    urlskcheck="http://dba.wsgjp.com.cn/Beefun/Beefun.Carrier.OrderManager.ajax/UpdateAuditOver"
    #headers={'cookie':nskcookie,"Content-Type": "application/json"}
    inskcheckdata={"vchcode":vchcode,"auditType":1,"auditResult":{"auditremark":"","auditresult":1}}
    pageorderdata=browser.requestpost(urlskcheck,inskcheckdata,headers,1)
    print pageorderdata
    browser.delaytime(1)
    #进货入库
    intoskurl="http://dba.wsgjp.com.cn/Beefun/Beefun.Bill.StockBill.ajax/Save"
    inskdata=(
    {"bill":{"vchtype":34,"ischecked":False,"invoicetag":False,"fromordercode":0,"wmsorder":False,"atypeid":None,"atypetypeid":None,"afullname":None,
             "atypetotal":0,"preference":0,"jtotal":0,"jremain":0,"settletype":2,"settleaccounts":[],"gatheringdlys":[],"fc_settletotal":0,
             "fc_preference":0,"freightbtypeid":0,"freightbfullname":None,"freightatypeid":None,"freightafullname":"","freightatypetypeid":None,
             "freightatypetotal":0,"freightfee":0,"freightfee_remain":0,"freightfee_buyerpay":0,"freightbillno":"","freightfeeshare":0,
             "freightfee_needshare":False,"freightfeesharetype":0,"fc_freightfeeshare":0,"fc_freightfee":0,"fc_freightsettletotal":0,
             "fc_freightfeeremain":0,"expense":0,"expenseshare":0,"expense_needshare":False,"fc_expense":0,"fc_expenseshare":0,
             "details":[{"ordercode":"227739963728236540","orderdlycode":"227739963728236699","dlyorder":"227739963728236699","createtype":0,
                         "platdlyorder":0,"ptypeid":"869585272784951","ptypecode":"a1x","ischecked":"1","ptypestandard":"","ptypetype":"",
                         "ptypearea":"","pfullname":"002 无编码修改_Ax","pname":"002","pic_url":"http://wd.geilicdn.com/vshop520219391-1459218328272-4913776.png?w=480&h=0",
                         "modifiedtime":today,"assqty":1,"asstoqty":0,"ptypeunit":"个","discount":1,"pstatus":0,"assprice":13.6,"assdpprice":13.6,
                         "asstpprice":13.6,"tax":0,"total":13.6,"dptotal":13.6,"tptotal":13.6,"taxtotal":0,"qty":1,"maxqty":1,"price":13.6,"dpprice":13.6,"tpprice":13.6,
                         "unit":1,"unitrate":1,"pcomment":"","comment":"TEST-20161227-004;","dlysale_suiteid":0,"ptypesuiteid":0,"ptypesuiteqty":0,"prop1name":"",
                         "prop2name":"","prop3name":"","prop1":0,"prop2":0,"prop3":0,"prop1_enabled":False,"prop2_enabled":False,"prop3_enabled":False,"fullbarcode":None,
                         "position":None,"snenabled":0,"protectdays":None,"ptypeweight":0,"producedate":None,"expirationdate":None,"batchno":"","retailprice":29.5,
                         "brandname":None,"isonlinesend":0,"urate0":"","urate1":"","urate2":"","ptypeweightall":0,"costshare":0,"oneweight":0,"temp_ucode":"a1x"}],
             "type":0,"ktypeid":"2605638079543104740","kfullname":"主仓库","ktypeid2":0,"kfullname2":None,"deliverytype":0,"date":"2016-12-27","btypeid":
                 "2605638088187950285","total":13.6,"etypeid":"2605638088210451192","deptid":0,"number":"TESTJH-"+vchcode,"summary":"原摘要：222222222222",
             "comment":"原说明：222222222222","currencyid":0,"exchangerate":0,"postid":0,"eshopid":0,"inputno":"2605638079543105363","postno":0,
             "billtype":0,"dlytype":0,"createtype":0,"auditstate":0,"profileid":0,"vchcode":0,"period":0,"draft":True,"redword":False,"redold":False,
             "redoldcode":0,"postindex":0,"overtime":today,"printtimes":0,"__checkindex":0,"__result":None,"__checknumber":False,
             "displaynumber":"","assistant":None,"bfullname":"t5123443","efullname":"001","dfullname":None,"inputfullname":"xsx","postfullname":None,
             "loadovertime":None,"btypearea":None,"btypeperson":None,"btypephone":None,"btypetelandaddress":None,"btypebank":None,"btypetaxnumber":None,
             "btypebankaccount":None,"currencyname":None,"btypetax":0,"custominfo1":None,"custominfo2":None,"custominfo3":None,"fc_total":0,
             "projectsid":0,
            "projectname":None,"profitlayout":None,"ffullname":"","ftypeid":0}}
    )
    pageorderdata=browser.requestpost(intoskurl,inskdata,headers,1)
    print pageorderdata
    browser.delaytime(1)
    #退货
    reinkurl="http://dba.wsgjp.com.cn/Beefun/Beefun.Bill.StockBackBill.ajax/Save"
    reinkdata=(
        {"bill":{"vchtype":6,"ischecked":False,"invoicetag":False,"gatheringdlys":[],"atypeid":None,"atypetypeid":None,"afullname":None,"atypetotal":0,
             "preference":0,"jtotal":0,"jremain":0,"settletype":1,"settleaccounts":[],"fc_settletotal":0,"fc_preference":0,
             "details":[{"prop1":0,"prop1name":"","prop2":0,"prop2name":"","prop3":0,"prop3name":"","pic_url":"http://wd.geilicdn.com/vshop520219391-1459218328272-4913776.png?w=480&h=0",
                         "ptypeid":"869585272784951","pfullname":"002 无编码修改_Ax","pname":"002","ptypecode":"a1x","brandname":"","temp_ucode":"a1x",
                         "temp_ucode_flag":True,"ptypeunit":"个","unit":"1","unitrate":1,"ptypestandard":"","ptypetype":"","ptypearea":"","snenabled":0,
                         "ptypeweight":0,"oneweight":0,"batchno":None,"producedate":None,"expirationdate":None,"position":None,"pstatus":0,"comment":"",
                         "prop1_enabled":False,"prop2_enabled":False,"prop3_enabled":False,"fullbarcode":"","retailprice":29.5,"ptypeweightall":0,"tax":0,
                         "showstockqty":232,"assdpprice":13.6,"discount":1,"assqty":1,"price":13.6,"dpprice":13.6,"qty":1,"dptotal":13.6,"asstpprice":13.6,
                         "tpprice":13.6,"tptotal":13.6,"taxtotal":0,"assprice":13.6,"total":13.6,"mallfee":0,"urate0":"","urate1":"","urate2":""}],"type":0,
             "ktypeid":"2605638079543104740","kfullname":"主仓库","ktypeid2":0,"kfullname2":None,"deliverytype":0,"date":"2016-12-27",
             "btypeid":"2605638079543104347","total":13.6,"etypeid":"2605638088210451192","deptid":"2605638088426904000","number":"TESTJT-"+vchcode,
             "summary":"","comment":"","currencyid":0,"exchangerate":0,"postid":0,"eshopid":0,"inputno":"2605638079543105363","postno":0,"billtype":0,
             "dlytype":0,"createtype":0,"auditstate":0,"profileid":0,"vchcode":0,"period":0,"draft":True,"redword":False,"redold":False,"redoldcode":0,
             "postindex":0,"overtime":today,"printtimes":0,"__checkindex":0,"__result":None,"__checknumber":False,
             "displaynumber":"","assistant":None,"bfullname":"网店客户","efullname":"001","dfullname":"xxx","inputfullname":"xsx","postfullname":None,
             "loadovertime":None,"btypearea":None,"btypeperson":None,"btypephone":None,"btypetelandaddress":None,"btypebank":None,"btypetaxnumber":None,
             "btypebankaccount":None,"currencyname":None,"btypetax":0,"custominfo1":None,"custominfo2":None,"custominfo3":None,"fc_total":0,"projectsid":0,
             "projectname":None,"profitlayout":None,"~/Selector/BTypeSelector.gspx":"00002","customerreceiver":None,"customerreceivermobile":None,
             "customerreceiverphone":None,"customerreceiverzipcode":None,"customerreceiverprovince":None,"customerreceivercity":None,
             "customerreceiverdistrict":None,"customerreceiveraddress":None,"deliveryinfoid":0,"deliveryinfotext":"",
             "~/Selector/ETypeSelector.gspx":"00001","~/Selector/KTypeSelector.gspx":"00001","~/Selector/DepartmentSelector.gspx":"00001","ftypeid":0}}
        )
    pageorderdata=browser.requestpost(reinkurl,reinkdata,headers,1)
    print pageorderdata
    browser.delaytime(2)
    #销售
    newsaleurl="http://dba.wsgjp.com.cn/Beefun/Beefun.Bill.SaleOrderBill.ajax/Save"
    nsaldata=(
        {"bill":{"date":"2016-12-27","draft":False,"displaynumber":"","number":"TESTSHD-"+vchcode,"inputno":"2605638079543105363",
             "inputfullname":"xsx","redword":False,"redold":False,"billtype":0,"ktypeid":"2605638079543104740","kfullname":"主仓库",
             "btypetax":0,"todate":today,"isneedinvoice":False,"currencyid":0,"btypeid":"2605638079543104347",
             "bfullname":"网店客户","etypeid":"2605638088210451192","efullname":"001","summary":"","comment":"",
             "details":[{"prop1":0,"prop1name":"","prop2":0,"prop2name":"","prop3":0,"prop3name":"","pic_url":"http://wd.geilicdn.com/vshop520219391-1459218328272-4913776.png?w=480&h=0",
                         "ptypeid":"869585272784951","pfullname":"002 无编码修改_Ax","pname":"002","ptypecode":"a1x","brandname":"","temp_ucode":"a1x",
                         "temp_ucode_flag":True,"ptypeunit":"个","unit":"1","unitrate":1,"ptypestandard":"","ptypetype":"","ptypearea":"","snenabled":0,
                         "ptypeweight":0,"oneweight":0,"batchno":None,"producedate":None,"expirationdate":None,"position":None,"pstatus":0,"comment":"",
                         "prop1_enabled":False,"prop2_enabled":False,"prop3_enabled":False,"fullbarcode":"","retailprice":29.5,"ptypeweightall":0,"tax":0,
                         "showstockqty":229,"assdpprice":30,"discount":1,"assqty":1,"price":30,"dpprice":30,"qty":1,"dptotal":30,"asstpprice":30,"tpprice":30,
                         "tptotal":30,"taxtotal":0,"assprice":30,"total":30,"mallfee":0,"urate0":"","urate1":"","urate2":""}],"isover":False,
             "../Selector/BTypeSelector.gspx":"00002","customerreceiver":None,"customerreceivermobile":None,"customerreceiverphone":None,
             "customerreceiverzipcode":None,"customerreceiverprovince":None,"customerreceivercity":None,"customerreceiverdistrict":None,
             "customerreceiveraddress":None,"deliveryinfoid":0,"deliveryinfotext":"","../Selector/ETypeSelector.gspx":"00001","deptid":0,
             "dfullname":"","../Selector/KTypeSelector.gspx":"00001","total":30,"ftypeid":0}}
    )
    #pageorderdata=browser.requestpost(newsaleurl,nsaldata,headers,1)
    pageorderdata=browser.requestpost(newsaleurl,nsaldata,headers,1)
    print pageorderdata
    vchcode=browser.datatrunjson2(pageorderdata)
    vchcode=vchcode["vchcode"]
    print vchcode
    browser.delaytime(1)
    #审核
    slcheckurl="http://dba.wsgjp.com.cn/Beefun/Beefun.Carrier.OrderManager.ajax/UpdateAuditOver"
    slcheckdata={"vchcode":vchcode,"auditType":1,"auditResult":{"auditremark":"","auditresult":1}}
    pageorderdata=browser.requestpost(slcheckurl,slcheckdata,headers,1)
    print pageorderdata
    browser.delaytime(1)
    #出库
    slurl="http://dba.wsgjp.com.cn/Beefun/Beefun.Bill.SaleBill.ajax/Save"
    sldata=(
        {"bill":{"vchtype":11,"collectionondelivery":False,"collectiontotal":0,"fc_collectiontotal":0,"customerfreightfee":0,"mallfee":0,"taxfee":0,
             "fc_mallfee":0,"fc_customerfreightfee":0,"fc_taxfee":0,"repairid":0,"storeid":0,"posid":0,"integralexchange":0,"integralamount":0,
             "vipcardamount":0,"bonuspoints":0,"customershopaccount":None,"payaccount":None,"dlyretail":0,"ischecked":False,"invoicetag":False,
             "eshopname":None,"eshoptype":0,"freighttype":0,"isonlinesend":0,"atypeid":None,"atypetypeid":None,"afullname":None,"atypetotal":0,
             "preference":0,"jtotal":0,"jremain":0,"settletype":1,"settleaccounts":[],"gatheringdlys":[],"fc_settletotal":0,"fc_preference":0,
             "freightbtypeid":0,"freightbfullname":None,"freightatypeid":None,"freightafullname":"","freightatypetypeid":None,"freightatypetotal":0,
             "freightfee":0,"freightfee_remain":0,"freightfee_buyerpay":0,"freightbillno":"","freightfeeshare":0,"freightfee_needshare":False,
             "freightfeesharetype":0,"fc_freightfeeshare":0,"fc_freightfee":0,"fc_freightsettletotal":0,"fc_freightfeeremain":0,"vipcardid":0,
             "vipdiscount":0,"custominfo1":None,"custominfo2":None,"custominfo3":None,
             "details":[{"ordercode":"227739964638662744","orderdlycode":"227739964638662986","dlyorder":"227739964638662986","createtype":0,
                         "platdlyorder":0,"ptypeid":"869585272784951","ptypecode":"a1x","ischecked":"1","ptypestandard":"","ptypetype":"",
                         "ptypearea":"","pfullname":"002 无编码修改_Ax","pname":"002","pic_url":"http://wd.geilicdn.com/vshop520219391-1459218328272-4913776.png?w=480&h=0",
                         "modifiedtime":today,"assqty":1,"asstoqty":0,"ptypeunit":"个","discount":1,"pstatus":0,"assprice":30,"assdpprice":30,
                         "asstpprice":30,"tax":0,"total":30,"dptotal":30,"tptotal":30,"taxtotal":0,"qty":1,"maxqty":1,"price":30,"dpprice":30,"tpprice":30,"unit":1,
                         "unitrate":1,"pcomment":"","comment":"SHD-20161227-001;","dlysale_suiteid":0,"ptypesuiteid":0,"ptypesuiteqty":0,"prop1name":"",
                         "prop2name":"","prop3name":"","prop1":0,"prop2":0,"prop3":0,"prop1_enabled":False,"prop2_enabled":False,"prop3_enabled":False,
                         "fullbarcode":None,"position":None,"snenabled":0,"protectdays":0,"ptypeweight":0,"producedate":None,"expirationdate":None,
                         "batchno":"","retailprice":29.5,"brandname":None,"isonlinesend":0,"urate0":"","urate1":"","urate2":"","ptypeweightall":0,"oneweight":0,
                         "temp_ucode":"a1x"}],"type":0,"ktypeid":"2605638079543104740","kfullname":"主仓库","ktypeid2":0,"kfullname2":None,"deliverytype":0,
             "date":"2016-12-27","btypeid":"2605638079543104347","total":30,"etypeid":"2605638088210451192","deptid":0,"number":"TESTSHD-"+vchcode,
             "summary":"原摘要：销售订货【002 无编码修改_Ax】等给【网店客户】:001","comment":"订单编号：SHD-20161227-001；","currencyid":0,
             "exchangerate":0,"postid":0,"eshopid":0,"inputno":"2605638079543105363","postno":0,"billtype":0,"dlytype":0,"createtype":0,
             "auditstate":0,"profileid":0,"vchcode":0,"period":0,"draft":True,"redword":False,"redold":False,"redoldcode":0,"postindex":0,
             "overtime":today,"printtimes":0,"__checkindex":0,"__result":None,"__checknumber":False,"displaynumber":"",
             "assistant":None,"bfullname":"网店客户","efullname":"001","dfullname":None,"inputfullname":"xsx","postfullname":None,"loadovertime":None,
             "btypearea":None,"btypeperson":None,"btypephone":None,"btypetelandaddress":None,"btypebank":None,"btypetaxnumber":None,"btypebankaccount":None,
             "currencyname":None,"btypetax":0,"fc_total":0,"projectsid":0,"projectname":None,"profitlayout":None,"ffullname":"","ftypeid":0}}
    )
    pageorderdata=browser.requestpost(slurl,sldata,headers,1)
    print pageorderdata
    browser.delaytime(1)
    #退货
    salreurl="http://dba.wsgjp.com.cn/Beefun/Beefun.Bill.SaleBackBill.ajax/Save"
    salredata=(
        {"bill":{"vchtype":45,"mallfee":0,"fc_mallfee":0,"taxfee":0,"fc_taxfee":0,"ischecked":False,"invoicetag":False,"dlyretail":0,"payaccount":None,
             "vipcardamount":0,"bonuspoints":0,"storeid":0,"posid":0,"atypeid":None,"atypetypeid":None,"afullname":None,"atypetotal":0,"preference":0,
             "jtotal":0,"jremain":0,"settletype":2,"settleaccounts":[],"gatheringdlys":[],"fc_settletotal":0,"fc_preference":0,"vipcardid":0,"vipdiscount":0,
             "details":[{"prop1":0,"prop1name":"","prop2":0,"prop2name":"","prop3":0,"prop3name":"","pic_url":"http://wd.geilicdn.com/vshop520219391-1459218328272-4913776.png?w=480&h=0",
                        "ptypeid":"869585272784951","pfullname":"002 无编码修改_Ax","pname":"002","ptypecode":"a1x","brandname":"","temp_ucode":"a1x",
                        "temp_ucode_flag":True,"ptypeunit":"个","unit":"1","unitrate":1,"ptypestandard":"","ptypetype":"","ptypearea":"",
                        "snenabled":0,"ptypeweight":0,"oneweight":0,"batchno":None,"producedate":None,"expirationdate":None,"position":None,
                        "pstatus":0,"comment":"","prop1_enabled":False,"prop2_enabled":False,"prop3_enabled":False,"fullbarcode":"","retailprice":29.5,
                        "ptypeweightall":0,"tax":0,"showstockqty":227,"assdpprice":30,"discount":1,"assqty":1,"price":30,"dpprice":30,"qty":1,
                        "dptotal":30,"asstpprice":30,"tpprice":30,"tptotal":30,"taxtotal":0,"assprice":30,"total":30,"mallfee":0,"urate0":"",
                        "urate1":"","urate2":""}],"type":0,"ktypeid":"2605638079543104740","kfullname":"主仓库","ktypeid2":0,"kfullname2":None,
             "deliverytype":0,"date":"2016-12-27","btypeid":"2605638079543104347","total":30,"etypeid":"2605638088210451192",
             "deptid":"2605638088426904000","number":"TESTXT-"+vchcode,"summary":"","comment":"","currencyid":0,"exchangerate":0,"postid":0,
             "eshopid":0,"inputno":"2605638079543105363","postno":0,"billtype":0,"dlytype":0,"createtype":0,"auditstate":0,"profileid":0,
             "vchcode":0,"period":0,"draft":True,"redword":False,"redold":False,"redoldcode":0,"postindex":0,"overtime":today,
             "printtimes":0,"__checkindex":0,"__result":None,"__checknumber":False,"displaynumber":"","assistant":None,"bfullname":"网店客户",
             "efullname":"001","dfullname":"xxx","inputfullname":"xsx","postfullname":None,"loadovertime":None,"btypearea":None,"btypeperson":None,
             "btypephone":None,"btypetelandaddress":None,"btypebank":None,"btypetaxnumber":None,"btypebankaccount":None,"currencyname":None,
             "btypetax":0,"custominfo1":None,"custominfo2":None,"custominfo3":None,"fc_total":0,"projectsid":0,"projectname":None,"profitlayout":None,
             "../Selector/BTypeSelector.gspx":"00002","customerreceiver":None,"customerreceivermobile":None,"customerreceiverphone":None,
             "customerreceiverzipcode":None,"customerreceiverprovince":None,"customerreceivercity":None,"customerreceiverdistrict":None,
             "customerreceiveraddress":None,"deliveryinfoid":0,"deliveryinfotext":"","../Selector/ETypeSelector.gspx":"00001",
             "~/Selector/DepartmentSelector.gspx":"00001","../Selector/KTypeSelector.gspx":"00001","ftypeid":0}}
        )
    pageorderdata=browser.requestpost(salreurl,salredata,headers,1)
    print pageorderdata

    browser.delaytime(1)

    #单据中心
    notecenurl="http://dba.wsgjp.com.cn/Carpa.Web/Carpa.Web.Script.DataService.ajax/GetPagerData"
    notdata={"pagerId":"$c3e1bf43$grid_pager1","queryParams":{"vchtype":"","beginDate":"2016-12-20","endDate":"2016-12-30","redwordType":0,"dlyType":0},"orders":None,"filter":None,"first":0,"count":5000}
    f=open(r"D:\cookies\cennote.txt")
    nskcookie=f.read()
    #print nskcookie
    headers={'cookie':nskcookie,"Content-Type": "application/json"}
    pageorderdata=browser.requestpost(notecenurl,notdata,headers,1)
    print "单据中心...."
    print pageorderdata







def main():

    f=open(r"D:\cookies\stocksave.txt")
    nskcookie=f.read()
    #print nskcookie
    headers={'cookie':nskcookie,"Content-Type": "application/json"}

    senddata=createorderdata(10000)
    #n=0
    print len(senddata)
    num_of_threads = 100
    _st = time.time()
    wm = workerManger(num_of_threads)
    print num_of_threads


    for i in senddata:
        wm.add_job(sendandcompare,i,headers)
        #wm.get_result(printer,resault_list)
    wm.start()
    wm.wait_for_complete()

    print 'result Queue\'s length == %d '% wm.resultQueue.qsize()
    '''
    while wm.resultQueue.qsize():
        a=wm.resultQueue.get()
        for i in a :
            print i
    '''
    print time.time() - _st

if __name__ == '__main__':
  main()




