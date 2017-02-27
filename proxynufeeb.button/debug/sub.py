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

def changes2(a,b):
   #list 分段函数,a:数据[(1),(2)]b:长度
   for i in xrange(0,len(a),b):
       yield  a[i:i+b]


def changes(a,b):
    #list 分段函数,a:数据[(1),(2)]b:长度
    k=[]
    for i in xrange(0,len(a),b):
        k.append(a[i:i+b])
    return k


def getsubdata():
    datas=[]

    #审核
    fc=open(r"E:\vccheck2.txt")
    item=fc.read().strip()
    all2=re.findall("values\('(.*?)'",item)

    fc2=open(r"E:\vccheckitem2.txt")
    item=fc2.read().strip()
    all3=re.findall("values\('(.*?)'",item)

    all=list (set(all2)-set(all3))
    #print len(all)
    temp=changes(all,10)
    print len(temp)
    print "temp...."
    print temp
    for gro in temp[:-1]:
        print "gro........."
        print gro
        print "vchcodes........."
        billdata2="{\"type\":1,\"param\":[\""+gro[0]+"\",\""+gro[1]+"\",\""+gro[2]+"\",\""+gro[3]+"\",\""+gro[4]+"\",\""+gro[5]+"\",\""+gro[6]+"\",\""+gro[7]+"\",\""+gro[8]+"\",\""+gro[9]+"\"]}"
        billdata3={"__Params":billdata2}

        print billdata3
        datas.append(billdata3)

    return datas

def getsubdata2():
    datas=[]

    #审核
    fc=open(r"E:\vccheck2.txt")
    item=fc.read().strip()
    all=re.findall("values\('(.*?)'",item)


    #print len(all)
    temp=changes(all,10)
    print len(temp)
    print "temp...."
    print temp
    for gro in temp[:-1]:
        print "gro........."
        print gro
        print "vchcodes........."
        billdata2="{\"type\":1,\"param\":[\""+gro[0]+"\",\""+gro[1]+"\",\""+gro[2]+"\",\""+gro[3]+"\",\""+gro[4]+"\",\""+gro[5]+"\",\""+gro[6]+"\",\""+gro[7]+"\",\""+gro[8]+"\",\""+gro[9]+"\"]}"
        billdata3={"__Params":billdata2}

        print billdata3
        datas.append(billdata3)

    return datas

def getsubdata3():
    datas=[]

    #审核
    fc=open(r"E:\vccheckitem2.txt")
    item=fc.read().strip()
    all=re.findall("values\('(.*?)'",item)


    #print len(all)
    temp=changes(all,10)
    print len(temp)
    print "temp...."
    print temp
    for gro in temp[:-1]:
        print "gro........."
        print gro
        print "vchcodes........."
        billdata2="{\"type\":1,\"param\":[\""+gro[0]+"\",\""+gro[1]+"\",\""+gro[2]+"\",\""+gro[3]+"\",\""+gro[4]+"\",\""+gro[5]+"\",\""+gro[6]+"\",\""+gro[7]+"\",\""+gro[8]+"\",\""+gro[9]+"\"]}"
        billdata3={"__Params":billdata2}

        print billdata3
        datas.append(billdata3)

    return datas

def getsubdata4():
    datas=[]

    #审核
    fc=open(r"E:\vcsenditem2.txt")
    item=fc.read().strip()
    all=re.findall("values\('(.*?)'",item)


    #print len(all)
    temp=changes(all,10)
    print len(temp)
    print "temp...."
    print temp
    for gro in temp[:-1]:
        print "gro........."
        print gro
        print "vchcodes........."
        billdata2="{\"type\":1,\"param\":[\""+gro[0]+"\",\""+gro[1]+"\",\""+gro[2]+"\",\""+gro[3]+"\",\""+gro[4]+"\",\""+gro[5]+"\",\""+gro[6]+"\",\""+gro[7]+"\",\""+gro[8]+"\",\""+gro[9]+"\"]}"
        billdata3={"__Params":billdata2}

        print billdata3
        datas.append(billdata3)

    return datas


def selgreenf(salredata,):
    pageorderdata=browser.requestpost(sendurl,salredata,headers)
    print salredata
    browser.delaytime(20)
    print pageorderdata
def selgreenf2(salredata,):
    pageorderdata=browser.requestpost(sendurl,salredata,headers2)
    print salredata
    browser.delaytime(20)
    print pageorderdata

def selgreenf3(salredata,):
    pageorderdata=browser.requestpost(sendurl,salredata,headers3)
    print salredata
    browser.delaytime(20)
    print pageorderdata

def selgreenf4(salredata,):
    pageorderdata=browser.requestpost(sendurl,salredata,headers4)
    print salredata
    browser.delaytime(20)
    print pageorderdata


def sendpro(num):

    fc=open(r"D:\cookies\eshop10.txt")
    nskcookie=fc.read()
    browser.delaytime(1)
    f2=open(r"D:\cookies\eshop.txt")
    nskcookie2=f2.read()
    browser.delaytime(1)
    f3=open(r"D:\cookies\eshop2.txt")
    nskcookie3=f3.read()
    browser.delaytime(1)
    f4=open(r"D:\cookies\eshop11.txt")
    nskcookie4=f4.read()
    f5=open(r"D:\cookies\eshop10.txt")
    nskcookie5=f5.read()
    global headers
    global headers2
    global headers3
    global headers4
    global headers5

    global sendurl
    headers={'cookie':nskcookie,"Content-Type": "application/x-www-form-urlencoded"}
    headers2={'cookie':nskcookie2,"Content-Type": "application/x-www-form-urlencoded"}
    headers3={'cookie':nskcookie3,"Content-Type": "application/x-www-form-urlencoded"}
    headers4={'cookie':nskcookie4,"Content-Type": "application/x-www-form-urlencoded"}
    headers5={'cookie':nskcookie5,"Content-Type": "application/x-www-form-urlencoded"}


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
    pool = gevent.pool.Pool(1)
    if num==0:
        sendurl="http://hehe.wsgjp.com.cn/Beefun/TaskForm.gspx?title=%u63D0%u4EA4"
        senddatas=getsubdata()
        data=pool.map(selgreenf,senddatas)
    elif num==1:
        sendurl="http://hehe.wsgjp.com.cn/Beefun/TaskForm.gspx?title=%u63D0%u4EA4"
        senddatas=getsubdata2()
        data=pool.map(selgreenf2,senddatas)

    elif num==2:
        sendurl="http://hehe.wsgjp.com.cn/Beefun/TaskForm.gspx?title=%u63D0%u4EA4"
        senddatas=getsubdata3()
        data=pool.map(selgreenf3,senddatas)

    else :
        sendurl="http://hehe.wsgjp.com.cn/Beefun/TaskForm.gspx?title=%u63D0%u4EA4"
        senddatas=getsubdata4()
        data=pool.map(selgreenf4,senddatas)


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
'''
    p4 = multiprocessing.Process(target = sendpro,args=(4,))
    p4.start()

    p5 = multiprocessing.Process(target = sendpro,args=(4,))
    p5.start()

    p6 = multiprocessing.Process(target = sendpro,args=(5,))
    p6.start()


    ######
    p7...............................
    14:08 sub 10

    #p99 = multiprocessing.Process(target = sendpro,args=(100,))
    #p99.start()
'''


