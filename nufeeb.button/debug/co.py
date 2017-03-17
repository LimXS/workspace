
'''
import json
import requests
from common import browserClass


browser=browserClass.browser()
f=open(r'E:/xsx.txt','r')
cookie=f.read()
print cookie
headers={'cookie':cookie,'Content-Type':'multipart/form-data; boundary=----WebKitFormBoundarym7p6dsxjVFUqd7iZ'}
headers={'cookie':cookie,'Content-Type':'multipart/form-data;'}
req = requests.post("http://beefun.wsgjp.com/Beefun/Beefun.IniPeriod.ImportKtypeIniNew.ajax/SaveFile",headers = headers,files = {'file': open(r'C:\Users\xsx\Downloads\abc.xls', 'r')})
b=req.text
print b

url="http://beefun.wsgjp.com/Carpa.Web/Carpa.Web.Script.DataService.ajax/GetPagerData"
headers={'cookie':cookie,'Content-Type':'application/json; charset=UTF-8'}
datas={"pagerId":"$2669e212$grid_pager1","queryParams":{"parid":"1","isfilter":True,"isshowstop":"0","isqtyautoupload":"-1","filtermode":"quickquery","filterstr":""},"orders":None,"filter":None,"first":0,"count":900}
req=requests.post(url=url,header=headers,data=json.dumps(datas))
print req.text



'''