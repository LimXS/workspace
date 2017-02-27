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

def changes(a,b):
    #list 分段函数,a:数据[(1),(2)]b:长度
    k=[]
    for i in xrange(0,len(a),b):
        k.append(a[i:i+b])
    return k

def createorderdata():
    sendata=[]
    #打印
    fc=open(r"E:\sp.txt")
    item=fc.read().strip()
    all=re.findall("values\('(.*?)'",item)


    #print len(all)
    for a in all:
        billdata1={"vchcodes":[a]}
        billdata2="{\"type\":1,\"param\":[\""+a+"\"]}"
        billdata3={"__Params":billdata2}
        billdata=[]
        billdata.append(billdata1)
        billdata.append(billdata3)
        sendata.append(billdata)
    '''
    temp=changes(all,10)

    for gro in temp[:-1]:
        #print "gro........."
        #print gro
        billdata=[]
        #print "vchcodes........."
        billdata1={"vchcodes":[gro[0],gro[1],gro[2],gro[3],gro[4],gro[5],gro[6],gro[7],gro[8],gro[9]]}
        billdata2="{\"type\":1,\"param\":[\""+gro[0]+"\",\""+gro[1]+"\",\""+gro[2]+"\",\""+gro[3]+"\",\""+gro[4]+"\",\""+gro[5]+"\",\""+gro[6]+"\",\""+gro[7]+"\",\""+gro[8]+"\",\""+gro[9]+"\"]}"
        billdata3={"__Params":billdata2}
        billdata.append(billdata1)
        billdata.append(billdata3)
        #print billdata
        sendata.append(billdata)
    '''
    random.shuffle(sendata)
    return sendata


def selgreenf(sendurl,headers,salredata,):
    pageorderdata=browser.requestpost(sendurl,salredata,headers,1)
    browser.delaytime(3)
    print pageorderdata

def selgreenf2(sendurl,headers,salredata,):
    #pageorderdata=browser.requestpost("http://hehe.wsgjp.com.cn/Beefun/Beefun.EShopSale.EShopSaleOrderList.ajax/GetUnRelationPtype",salredata[0],headers[0],1)
    #print pageorderdata
    print "salredata.."
    print salredata[1]
    pageorderdata2=browser.requestpost(sendurl,salredata[1],headers[1])
    browser.delaytime(3)
    print pageorderdata2

def main():
    #newcookie()
    a=[3]
    for num in a:
        fc=open(r"D:\cookies\eshop6.txt")
        nskcookie=fc.read()
        #print nskcookie
        header1={'cookie':nskcookie,"Content-Type": "application/json"}
        header2={'cookie':nskcookie,"Content-Type": "application/x-www-form-urlencoded"}
        headers=[]
        headers.append(header1)
        headers.append(header2)
        senddata=createorderdata()
        #n=0
        print len(senddata)
        num_of_threads = num

        loggingClass.addlogmes("info","开始-线程个数:",str(num_of_threads))
        wm = workerManger(num_of_threads)
        print num_of_threads
        deurl="http://hehe.wsgjp.com.cn/Beefun/TaskForm.gspx?title=%u63D0%u4EA4"
        for i in senddata:
            try:
                wm.add_job(selgreenf2,deurl,headers,i)
            except:
                pass
        #wm.get_result(printer,resault_list)
        wm.start()
        wm.wait_for_complete()
        loggingClass.addlogmes("info","结束-线程个数:",str(num_of_threads))

        print 'result Queue\'s length == %d '% wm.resultQueue.qsize()
        '''
        while wm.resultQueue.qsize():
            a=wm.resultQueue.get()
            for i in a :
                print i
        '''


if __name__ == '__main__':
  main()




