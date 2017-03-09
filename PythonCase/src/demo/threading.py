# -*- coding: utf-8 -*-
import requests
import re
from bs4 import BeautifulSoup
import time
import datetime
import random
import traceback
import sys
import Queue
import threading


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
            if worker.isAlive() and not self.workQueue.empty():
               self.workers.append(worker)  # 重新加入线程池中
        print 'All jobs were complete.'


    def add_job(self, callable, *args, **kwds):
         self.tagQueue.put((callable, args, kwds))  # 向工作队列中加入请求

    def get_result(self, *args, **kwds):
        return self.resultQueue.get(*args, **kwds)

mutex = threading.Lock()
def add_mutex(func):
    def decor(*args, **kwargs):
        time.sleep(1)
        mutex.acquire()
        func(*args, **kwargs)
        mutex.release()
    return decor


#获取标签
def get_tag(tag_movie):
    res0=requests.get(tag_movie)
    tag_detail=re.findall("tag\">(.*?)<",res0.text)
    return tag_detail
    
#获取类型
def get_typetag(tag_detail):
    movie_type=[]
    for type in tag_detail[0:36]:
        #print type
        movie_type.append(type)
    return movie_type

#爬取类型标签内电影页数

def list_page(type,headers,tag_movie):

        
    #获取每个标签内一共有几页
    try:
        pagehtml=requests.get(tag_movie+type,headers=headers)
        #print "get tag page status:"+str(pagehtml.status_code)
        page=re.findall("total-page=\"(.*?)\">",pagehtml.text)
        page=int(page[0])

            
    except:
        print type
        print str(page)
        print(traceback.format_exc())
        f=open('D:\ip.txt','a+')
        f.write(type)
        f.write(traceback.format_exc())        
        f.write(page)
        f.writr('\n')
        f.close()
    return page


#打印电影简介信息
def movie_summary(url_detail,headers):
    detail=requests.get(url_detail,headers=headers)
    print "get detail movie status:"+str(detail.status_code)
    soup=BeautifulSoup(detail.text)
    c=soup.find_all(attrs={"property":"v:summary"})
    if len(c)>=1:
        print c[0].get_text().strip('\\n')
        print "\n"


#获取每一页电影列表
#@add_mutex
def movie_list(url,headers):
    try:
            #print "get into"
            url_list=requests.get(url,headers=headers)
            print "status:"+str(url_list.status_code)
            #获取每一个电影url
            url_detail=re.findall('nbg\" href=\"(.*?)\"',url_list.text)
            #获取电影名字
            title_list=re.findall("title=\"(.*?)\"",url_list.text)
            #获取每个电影的评分
            scores_list=re.findall('rating_nums\">(.*?)<',url_list.text)
            #获取每个电影评价数
            soup1=BeautifulSoup(url_list.text)
            commit_list=soup1.find_all("span",class_="pl")

            #爬取具体电影信息
            #若电影评分高于8.5分，则进入该电影页面，爬取相关信息
            flag=0
            for scores in scores_list:
                if scores!='':
                    scores=float(scores)
                    if scores>=8.5:
                        #n=n+1
                        sum=movie_summary(url_detail[flag],headers)
                        print title_list[flag]+":"+str(scores)
                        print commit_list[flag].get_text().strip(' ')
                        print sum
                flag=flag+1

       # return url_detail[flag]

    except:
        print(traceback.format_exc())
        f=open('D:\ip.txt','a+')
        f.write(traceback.format_exc())
        f.close()


def main():

    url_requests=[]
    url_head="https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start="

    proxies = {"https": "http://41.118.132.69:4433"}

    #电影标签链接
    tag_movie="https://movie.douban.com/tag/"

    '''
    tag_name=[]
    res0=requests.get(tag_movie)

    #获取标签
    tag_detail=re.findall("tag\">(.*?)<",res0.text)
    '''

    #设置基本参数
    referer='https://movie.douban.com/tag/'

    user_agent=[]
    user_agent.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0)')
    user_agent.append('Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.2)')
    user_agent.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)')
    user_agent.append('Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36')
    headers={"User-Agent":random.choice(user_agent),"Referer":referer}

    tag_detail=get_tag(tag_movie)
    movie_type=get_typetag(tag_detail)
    '''
    urls =[]
    for type in movie_type:
        urls.append(tag_movie+type)
    n=0
    num_of_threads = 10
    _st = time.time()
    wm = workerManger(num_of_threads)
    print num_of_threads
    for i in urls:
        wm.add_job(list_page, i,headers,tag_movie)
        wm.start()
        wm.wait_for_complete()
        print time.time() - _st
    '''
    page_url=[]

    for type in movie_type:
        page=list_page(type,headers,tag_movie)
        #page.append(page)
        for nums in range(0,page):
            page_url.append("https://movie.douban.com/tag/"+type+"?start="+str(nums*20)+"&type=T")

    print len(page_url)
    #n=0
    num_of_threads = 10
    _st = time.time()
    wm = workerManger(num_of_threads)
    print num_of_threads

    for i in page_url:
        wm.add_job(movie_list,i,headers)
    wm.start()
    wm.wait_for_complete()
    print time.time() - _st

if __name__ == '__main__':
  main()
