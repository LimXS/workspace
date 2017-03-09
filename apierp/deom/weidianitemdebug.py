#*-* coding:UTF-8 *-*
from common import base
from common import itemscompare
import unittest
import traceback
import re
import requests
import json
import time

cookie=open(r"E:\cookie.txt","r")
cookie=cookie.read()
url="http://beefun.wsgjp.com/Carpa.Web/Carpa.Web.Script.DataService.ajax/GetPagerData"
headers={'Content-Type': 'application/json; charset=gb2312','cookie':cookie,}
payload={"pagerId":"$19b126ff$gridPType_pager1","queryParams":{"eshopId":"2605638400292508735","ismall":False,"classTypeId":"","platFullname":"","RelationStatus":0,"StockStatus":3,"isShowZeroQty":False,"notShowZeroQty":False,"isRepeatXcode":False,"isGiftSku":False,"isDifrentXcoe":False,"isDifrentSkuXcode":False},"orders":None,"filter":None,"first":0,"count":20}
data=json.dumps(payload)

apidata=requests.post(url=url,data=data,headers=headers)
print apidata.text


f=open(r"C:\workspace\apierp\sp.dat","r")
token=f.read()
print "token:"+token


params={"itemid":"1790451081"}
publics={"method":"vdian.item.get","access_token":token,"version":"1.0","format":"json"}

payload={"param":json.dumps(params),"public":json.dumps(publics)}
url="http://api.vdian.com/api"
apires=requests.post(url,data=payload)
apidata=json.loads(apires.text)
print apidata

print apidata[""]