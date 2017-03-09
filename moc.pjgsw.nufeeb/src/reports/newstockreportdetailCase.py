#*-* coding:UTF-8 *-*#*-* coding:UTF-8 *-*

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
header={'cookie':cookiestr,"Content-Type": "application/json"}
header2={"cookie":cookiestr,"Content-Type": "application/x-www-form-urlencoded"}

#报表-批发零售报表-销商品销售统计
print u"报表-批发零售报表-销商品销售统计......................................"
stamp=browser.gettimestamp()
overday=stamp[1]*1000
today=stamp[0]*1000

#页面id
idurl="http://beefun.wsgjp.com/Beefun/Report/ProductsSale.gspx"
b="{\"mode\":\"psale\",\"reporttype\":0,\"querytype\":1,\"StartDate\":\"\/Date("+str(overday)+")\/\",\"EndDate\":\"\/Date("+str(today)+")\/\",\"dlytype\":[0,1,2],\"pTypeid\":null,\"eTypeid\":null,\"kTypeid\":null,\"bTypeid\":null,\"brandid\":null,\"saveDate\":false,\"pId\":null,\"pfullname\":\"\",\"bId\":null,\"bfullname\":\"\",\"eId\":null,\"efullname\":\"\",\"kId\":null,\"kfullname\":\"\",\"brandname\":\"\",\"startDate\":\""+str(stamp[3])+"\",\"endDate\":\""+str(stamp[2])+"\",\"filter\":1,\"leveal\":1}"
#data3={"__Params":"{\"mode\":\"pbuy\",\"reporttype\":0,\"querytype\":0,\"StartDate\":\"\/Date(1469116800000)\/\",\"EndDate\":\"\/Date(1469635200000)\/\",\"dlytype\":[0,1,2],\"pTypeid\":None,\"eTypeid\":None,\"kTypeid\":None,\"bTypeid\":None,\"brandid\":None,\"saveDate\":False,\"pId\":None,\"pfullname\":\"\",\"bId\":None,\"bfullname\":\"\",\"eId\":None,\"efullname\":\"\",\"kId\":None,\"kfullname\":\"\",\"brandname\":\"\",\"startDate\":\"2016-07-22\",\"endDate\":\"2016-07-28\",\"filter\":1,\"leveal\":1}"}
data3={"__Params":b}
idtext=requests.post(url=idurl,data=data3,headers=header2)
print idtext.text
pageid=browser.getpageid(idtext)
print pageid



#报表页面数据


relistsurl="http://beefun.wsgjp.com/Carpa.Web/Carpa.Web.Script.DataService.ajax/GetPagerData"
relistsdata={"pagerId":pageid,"queryParams":{"mode":"psale","pTypeid":None,"bTypeid":None,"eTypeid":None,"kTypeid":None,"dlytype":[0,1,2],"brandid":None,"StartDate":stamp[3],"EndDate":stamp[2],"filter":"3","leveal":1,"querytype":1,"reporttype":0,"pfullname":"","bfullname":"","efullname":"","kfullname":"","brandname":""},"orders":None,"filter":None,"first":0,"count":1000}
reliststext=requests.post(url=relistsurl,data=json.dumps(relistsdata),headers=header)
print "reliststext......................"
#print reliststext.text
relists=browser.reportgetdata(reliststext)
print relists
print len(relists)
listdata=relists[4]
redata=browser.getdetaildata(listdata)
print "redata........."
print redata
print len(redata)

#报表-销售明细账本id

redeurlid="http://beefun.wsgjp.com/Beefun/Report/ProductsSaleDetails.gspx"
reiddeda="{\"mode\":\"psale\",\"pTypeid\":\""+str(redata[4])+"\",\"bTypeid\":null,\"eTypeid\":null,\"kTypeid\":null,\"dlytype\":[0,1,2],\"StartDate\":\""+stamp[3]+"\",\"EndDate\":\""+stamp[2]+"\",\"filter\":0,\"leveal\":1,\"querytype\":1,\"reporttype\":0,\"pfullname\":\"\",\"sonnum\":0,\"bfullname\":\"全部单位\",\"efullname\":\"全部职员\",\"kfullname\":\"全部仓库\",\"isnullflag\":\"1\",\"brandname\":\"全部品牌\"}"
reiddedata={"__Params":reiddeda}
redeidtext=requests.post(url=redeurlid,data=reiddedata,headers=header2)
print "detail page id..................."
depageid=browser.getpageid(redeidtext)
print depageid
print redata[4]

#报表-销售明细账本lists
print "detail lists............................"
redeurl="http://beefun.wsgjp.com/Carpa.Web/Carpa.Web.Script.DataService.ajax/GetPagerData"
rededata={"pagerId":depageid,"queryParams":None,"orders":None,"filter":None,"first":0,"count":1000}
redeliststext=requests.post(url=redeurl,data=json.dumps(rededata),headers=header)
print redeliststext.text
redelists=browser.reportgetdata(redeliststext)
print redelists
print len(redelists)
listdedata=redelists[2]
rededata=browser.getdetaildata(listdedata)
print "rededata........."
print rededata
print len(rededata)
print rededata[3]
print rededata[4]
print rededata[6]
print rededata[8]



print "\n"
#报表-销售明细账本sum
print "detail sum............................"
redesumurl="http://beefun.wsgjp.com/Carpa.Web/Carpa.Web.Script.DataService.ajax/GetPagerSummary"
redesumdata={"pagerId":depageid}
redesumtext=requests.post(url=redesumurl,data=json.dumps(redesumdata),headers=header)
redelistssum=browser.datatrunjson(redesumtext)
print redelistssum


#报表页面统计数据
relistssumurl="http://beefun.wsgjp.com/Carpa.Web/Carpa.Web.Script.DataService.ajax/GetPagerSummary"
relistssumdata={"pagerId":pageid}
relistssumtext=requests.post(url=relistssumurl,data=json.dumps(relistssumdata),headers=header)
print "relistssum........................"
#print relistssumtext.text
relistssum=browser.datatrunjson(relistssumtext)
print relistssum
