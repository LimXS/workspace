#*-* coding:UTF-8 *-*

import  xml.dom.minidom
import time
import json
import re
import requests
from common import browserClass


browser=browserClass.browser()
res=requests.session()
f=open(r"E:\cookie.txt","r")
cookie=f.read()
cookiestr=cookie
f.close()
header={'cookie':cookiestr,"Content-Type": "application/json"}
header2={'cookie':cookiestr,"Content-Type": "application/x-www-form-urlencoded"}
stamp=browser.gettimestamp()
print stamp



print browser.notecentel(header)

#report list
repageid="$75b7249e$grid_pager1"
reurl="http://beefun.wsgjp.com/Carpa.Web/Carpa.Web.Script.DataService.ajax/GetPagerData"
data={"pagerId":repageid,"queryParams":{"mode":"storecode","key":"","begin":stamp[3],"end":stamp[2]},"orders":None,"filter":None,"first":0,"count":100000}
repadetail=browser.pagedetail(reurl,data,header)
print repadetail["itemList"]["rows"]

destore=repadetail["itemList"]["rows"][1]
storeid=destore[2]
print storeid

deurl="http://beefun.wsgjp.com/Beefun/Report/StoreRetailList.gspx"
reiddeda="{\"begin\":\""+stamp[3]+"\",\"end\":\""+stamp[2]+"\",\"storeid\":"+str(storeid)+"}"
dadata={"__Params":reiddeda}
deidtext=browser.pagedetail(deurl,dadata,header2,2)
print deidtext
deid=browser.getpageid(deidtext,1)
print deid
