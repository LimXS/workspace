#*-* coding:UTF-8 *-*

import  xml.dom.minidom
import time
import json
import re
import requests

f=open(r"E:\cookie.txt","r")
cookie=f.read()

#单据中心
url="http://beefun.wsgjp.com.cn/Carpa.Web/Carpa.Web.Script.DataService.ajax/GetPagerData"
header={'cookie':cookie,"Content-Type": "application/json"}
data={"pagerId":"$c3e1bf43$grid_pager1","queryParams":None,"orders":None,"filter":None,"first":0,"count":100}
page=requests.post(url,headers=header,data=json.dumps(data))
#print page.text
page=page.text
page=page.replace("false","\"False\"")
#print page
#放字典，每一条一个位置
pagedic=json.loads(page)
Vchtype=pagedic["itemList"][0]["vchtypeid"]
Vchcode= pagedic["itemList"][0]["vchcode"]

urlnotedatail="http://beefun.wsgjp.com.cn/Beefun/Bill/StockBackBill.gspx"
data2={"Vchtype":Vchtype,"Vchcode":Vchcode,"Mode":"read"}
pagedetail=requests.post(url,headers=header,data=json.dumps(data))

print "note detail........."

pagedetail=pagedetail.text
print pagedetail
pagedetail=pagedetail.replace("false","\"False\"")
pagedetail=json.loads(pagedetail)

print pagedetail