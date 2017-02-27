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
def getsubdata3():
    datas=[]

    #审核
    fc=open(r"E:\vchcode.txt")
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
    random.shuffle(datas)
    return datas
f3=open(r"D:\cookies\eshop7.txt")
nskcookie3=f3.read()
browser.delaytime(1)

headers3={'cookie':nskcookie3,"Content-Type": "application/x-www-form-urlencoded"}
k=getsubdata3()
deurl="http://hehe.wsgjp.com.cn/Beefun/TaskForm.gspx?title=%u63D0%u4EA4"
for da in k:
    pageorderdata=browser.requestpost(deurl,da,headers3)
    print pageorderdata
    browser.delaytime(7)