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


urlyuanshi="http://dba.wsgjp.com.cn/Beefun/Beefun.EShopSale.EShopSaleOrderCreate.ajax/SaveAndAuditSaleOrder"
billdata=(
    {"orderEntity":{"atypeid":0,"buyerid":0,"tradeid":"AToday-20170106"+browser.getrandnumber(),"number":None,"payno":"","gatheringvchcode":0,
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



pageorderdata=browser.requestpost(urlyuanshi,billdata,headers,1)
print pageorderdata















