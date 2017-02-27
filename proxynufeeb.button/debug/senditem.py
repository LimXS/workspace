# -*- coding: utf-8 -*-
'''
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
'''
import requests
import re
from bs4 import BeautifulSoup
import time
import datetime
import random
import traceback
import  MySQLdb
import Queue
import threading
from common import browserClass
browser=browserClass.browser()



today = datetime.date.today()
overday=today+datetime.timedelta(days=-6)
todayda=today.strftime('%Y-%m-%d %H:%M:%S')
overdayda=overday.strftime('%Y-%m-%d %H:%M:%S')

today=today.strftime('%Y-%m-%d')
overday=overday.strftime('%Y-%m-%d')
nran=browser.getrandnumber()

f=open(r"D:\cookies\eshop.txt")
nskcookie=f.read()
#print nskcookie
headers={'cookie':nskcookie,"Content-Type": "application/json"}
browser.delaytime(1)

#根据ptype 的 id 确定商品 ;ptype 的 profileid是账套的商品(ptype_assinfo); 把账套商品弄40个出来；ptype 的 id与ptype_assinfo的ptypeid 一样
'''
ptypeid="870037043076268"
sql="SELECT UserCode,FullName,preprice,pic_url,name FROM ptype WHERE id='"+ptypeid+"'"
conn= MySQLdb.connect(host='172.16.0.96',user='website',passwd='test@2011',db='beefun',port = 4306)
cur = conn.cursor()
sqlreault=cur.execute(sql)
# 使用 fetchone() 方法获取一条数据库。
data = cur.fetchone()
print data
for da in data:
    print da
cur.close()

listspro=["北京","上海","广州","深圳","天津","四川","湖北","湖南","西藏","青海"]
listcity=["北京市","上海市","广州市","深圳市","天津市","成都","武汉","西宁","拉萨","西安"]
listunit=["高新区","武侯区","中和","华阳","红牌楼","双流区","西城区","朝阳区"]
listadd=["天府大道","武侯大道","熊猫大道","剑南大道","益州大道","龙泉","三圣乡","布达拉宫","克勒青","西单"]





#提交 eshop_saleorder vchcode  SELECT * FROM eshop_saleorder WHERE tradeid="Today-20170106681570294"
urlcheck="http://dba.wsgjp.com.cn/Beefun/Beefun.EShopSale.EShopSaleOrderList.ajax/AuditBills"
billdata={"ids":["227740050840516254","227740050840127484"]}
pageorderdata=browser.requestpost(urlcheck,billdata,headers,1)
print pageorderdata


#审核 eshop_deliverbill vchcode  SELECT * FROM eshop_deliverbill WHERE tradeid="Today-20170106677607025"
urlcheck="http://dba.wsgjp.com.cn/Beefun/Beefun.EShopDeliver.EShopDeliverList.ajax/SubmitAudit"
billdata={"vchcodes":["227740050847261432","227740050847261429"],"isForceAudit":False}

pageorderdata=browser.requestpost(urlcheck,billdata,headers,1)
print pageorderdata



#打印
urlprint="http://dba.wsgjp.com.cn/Beefun/Beefun.EShopDeliver.EShopDeliverList.ajax/SubmitPrint"
billdata={"vchcodes":["227740050847261432","227740050847261429"]}

pageorderdata=browser.requestpost(urlprint,billdata,headers,1)
print pageorderdata

#验货
urlcheckitem="http://dba.wsgjp.com.cn/Beefun/Beefun.EShopDeliver.BatchList.ajax/DoCheck"
billdata={"vchcodes":["227740050847261432","227740050847261429"]}

pageorderdata=browser.requestpost(urlcheckitem,billdata,headers,1)
print pageorderdata


#发货
#vchcodes eshop_deliverbill vchcodes
ursend="http://dba.wsgjp.com.cn/Beefun/Beefun.EShopDeliver.BatchList.ajax/BatchSendGoods"
billdata={"vchcodes":["227740050847261432","227740050847261429"],"onlineOrder":False,"sendTime":"2017-01-06 11:22:50"}

pageorderdata=browser.requestpost(ursend,billdata,headers,1)
print pageorderdata

'''


ursend="http://dba.wsgjp.com.cn/Carpa.Web/Carpa.Web.Script.DataService.ajax/GetPagerData"
billdata={"pagerId":"$c5e778c0$batchGrid_pager1","queryParams":{"begin":overday,"end":today},"orders":None,"filter":None,"first":0,"count":12}


pageorderdata=browser.requestpost(ursend,billdata,headers,1)
print pageorderdata





