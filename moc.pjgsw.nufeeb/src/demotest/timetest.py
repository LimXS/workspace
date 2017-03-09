#*-* coding:UTF-8 *-*

import  xml.dom.minidom
import time
import json
import re
import requests
from common import browserClass
import datetime
import time

browser=browserClass.browser()
res=requests.session()
f=open(r"E:\cookie.txt","r")
cookie=f.read()
cookiestr=cookie
day=browser.gettimestamp()
header={'cookie':cookiestr,"Content-Type": "application/json"}
header2={'cookie':cookiestr,"Content-Type": "application/x-www-form-urlencoded"}
idurl='http://beefun.wsgjp.com/Beefun/Report/GoodsTransBillQuery.gspx'
dbdurlda="{\"kOutId\":null,\"kfullnameout\":\"全部仓库\",\"kInId\":null,\"kfullnameint\":null,\"eId\":null,\"efullname\":\"全部职员\",\"departtypeid\":null,\"deptname\":null,\"startDate\":\""+str(day[3])+"\",\"endDate\":\""+str(day[2])+"\",\"SaveDate\":false,\"kfullnamein\":\"全部仓库\",\"departname\":\"全部部门\"}"
iddata={"__Params":dbdurlda}
resid=requests.post(url=idurl,headers=header2,data=iddata)
print resid.text
repageid=browser.getpageid(resid)
print repageid

reurl="http://beefun.wsgjp.com/Carpa.Web/Carpa.Web.Script.DataService.ajax/GetPagerData"
reda={"pagerId":repageid,"queryParams":{"level":1,"partypeid":"00000","profileid":0,"startDate":str(day[3]),"endDate":str(day[2]),"kOutId":None,"kInId":None,"eId":None,"kfullnameout":"全部仓库","kfullnamein":"全部仓库","efullname":"全部职员","filterzero":0,"etypetypeid":None,"departtypeid":None,"departname":"全部部门","leveal":1},"orders":None,"filter":None,"first":0,"count":100}
redata=requests.post(url=reurl,data=json.dumps(reda),headers=header)
print redata.text
redatlist=json.loads(redata.text)
print redatlist["itemList"]["rows"]
print len(redatlist["itemList"]["rows"])


data=redatlist["itemList"]["rows"][0]
print data[8]

print "明细报表id...................."
redeurlid="http://beefun.wsgjp.com/Beefun/Report/GoodsTransBillQueryDetails.gspx"
#deidda="{\"ptypeid\":\""+str(data[8])+"\",\"startDate\":\""+str(day[3])+",\"endDate\":\""+str(day[2])+"\",\"pfullname\":\"\",\"kOutId\":null,\"kInId\":null,\"eId\":null,\"etypetypeid\":null,\"departtypeid\":null}"
deidda2="{\"ptypeid\":\""+str(data[8])+"\",\"startDate\":\""+str(day[3])+"\",\"endDate\":\""+str(day[2])+"\",\"pfullname\":\"\",\"kOutId\":null,\"kInId\":null,\"eId\":null,\"etypetypeid\":null,\"departtypeid\":null}"
rededaid={"__Params":deidda2}
resdeid=requests.post(url=redeurlid,headers=header2,data=rededaid)
print resdeid.text
redepageid=browser.getpageid(resdeid)

print redepageid

print "明细报表统计数据...................."
datasum=browser.reportsumdata(redepageid,header)
print datasum

print "报表明细数据...................."
rededaurl="http://beefun.wsgjp.com/Carpa.Web/Carpa.Web.Script.DataService.ajax/GetPagerData"
rededadata={"pagerId":redepageid,"queryParams":None,"orders":None,"filter":None,"first":0,"count":50}
rededata=requests.post(url=rededaurl,data=json.dumps(rededadata),headers=header)
rededatlist=json.loads(rededata.text)
print rededatlist["itemList"]
print rededatlist["itemList"]["rows"][0]
print rededatlist["itemList"]["rows"][0][14]
print rededatlist["itemList"]["rows"][0][15]

print "原始单据........................."
orurl="http://beefun.wsgjp.com/Beefun/Bill/GoodsTransBill.gspx?Vchtype="+str(rededatlist["itemList"]["rows"][0][9])+"&Vchcode="+str(rededatlist["itemList"]["rows"][0][8])+"&Mode=Read"
ordetail=requests.get(orurl,headers=header)
print ordetail.text
#原始单据头
print "原始单据头..................."
orheader=browser.getnotehead(ordetail)
print orheader
print orheader[2]
print orheader[4]
print orheader[43][:10]

print "原始商品数据..................."
ordetotal=re.findall("\"details\":(.*?)freightbtypeid",ordetail.text)
print ordetotal
print len(ordetotal)
orlists=re.findall("outposition(.*?)brandname",ordetotal[0])
print orlists
print len(orlists)
orlist=orlists[0].replace("\"",'')
orlistdata=re.findall(":(.*?),",orlist)
print orlistdata
print len(orlistdata)
print orlistdata[5]
print orlistdata[7]
print orlistdata[60]
print orlistdata[64]