#*-* coding:UTF-8 *-*

import  xml.dom.minidom
import time
import json
import re
import requests
from common import browserClass
import datetime
import time


res=requests.session()
f=open(r"E:\cookie.txt","r")
cookie=f.read()
cookiestr=cookie
header={'cookie':cookiestr,"Content-Type": "application/json"}
#单据中心

s=requests.session()
url="http://beefun.wsgjp.com.cn/Carpa.Web/Carpa.Web.Script.DataService.ajax/GetPagerData"

data={"pagerId":"$c3e1bf43$grid_pager1","queryParams":None,"orders":None,"filter":None,"first":0,"count":100}
page=s.post(url,headers=header,data=json.dumps(data))
print page.text
page=page.text
page=page.replace("false","\"False\"")

#print page

pagedic=json.loads(page)


print len(pagedic["itemList"])
print pagedic["itemList"][0]
Vchcode=pagedic["itemList"][0]["vchcode"]
Vchtype=pagedic["itemList"][0]["vchtypeid"]
number=pagedic["itemList"][0]["number"]


print pagedic["itemList"][1]["kfullname"]
print pagedic["itemList"][1]["btypename"]
print pagedic["itemList"][1]["vchtype"]
print u"单据明细（换货）...................."

notedata={"Vchtype":Vchtype,"Vchcode":Vchcode,"Mode":"Read"}

noteurl="http://beefun.wsgjp.com.cn/Beefun/Bill/StockChangeBill.gspx?Vchtype="+str(Vchtype)+"&Vchcode="+str(Vchcode)+"&Mode=Read"
notedetail=requests.get(noteurl,headers=header)

print notedetail.text
#退货
#明细


print "in..........................................."

tempindetails=re.findall("(?<=indetails\":\[).*?(?=outdetails)",notedetail.text)
print len(tempindetails)
print tempindetails
#outdetails=re.findall("(?<=tradeid).*?(?=tradeid)",notedetail.text)
tempindet=re.findall("invoicetotal(.*?)brandname",tempindetails[0])
print len(tempindet)
print tempindet[0]
print tempindet[1]

tempindet=tempindet[0].replace("\"","")
#print noteitem
indetail=re.findall(":(.*?),",tempindet)
print len(indetail)
print indetail

print "out................................"
tempoutdatails=re.findall("(?<=outdetails\":\[)(.*?)brandname\":null\}\]",notedetail.text)
print len(tempoutdatails)
print tempoutdatails
tempoutdet=re.findall("invoicetotal(.*?)brandname",tempoutdatails[0]+"brandname")
print len(tempoutdet)
print tempoutdet[0]
tempoutdet=tempoutdet[0].replace("\"","")
outdetail=re.findall(":(.*?),",tempoutdet)
print len(outdetail)
print outdetail

'''
#qty
print itemdetail[14]
#price
print itemdetail[15]
#total
print itemdetail[16]
'''