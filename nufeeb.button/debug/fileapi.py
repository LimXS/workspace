# -*- coding: utf-8 -*-
import time
import requests
import json
from common import browserClass
browser=browserClass.browser()
f=open('e:src.txt','r')
l=f.read()
print l
headers={'cookie':l}
#cookie='_ati=146267075305; ASP.NET_SessionId=qe5bebuz2cphgb0o01omllql; _umdata=65F7F3A2F63DF0207E2BEE3A391EB24C36974786A7AE62C01730E5CD202421301CEB2174FC2A3B8ECD43AD3E795C914C875265D2A3D8556E4D50D098EE48453E; corpName=%E6%B5%8B%E8%AF%95%E6%AF%95%E6%96%B9%E6%A1%82; userName=%E6%AF%95%E6%96%B9; Beefun.LoginValidation.ValidationHandler.WhiteListHandler=09:53:10 276; BeefunMainOpenMark=2017/3/17%20%u4E0A%u53489%3A53%3A34540; quickDate=4; MDIPageLocation=%7E%252FBeefun%252FBaseInfo2%252FPTypeList.gspx'
'''
url="http://beefun.wsgjp.com/Carpa.Web/Carpa.Web.Script.DataService.ajax/GetPagerData"

#cookie='_ati=146267075305; ASP.NET_SessionId=qe5bebuz2cphgb0o01omllql; _umdata=65F7F3A2F63DF0207E2BEE3A391EB24C36974786A7AE62C01730E5CD202421301CEB2174FC2A3B8ECD43AD3E795C914C875265D2A3D8556E4D50D098EE48453E; corpName=%E6%B5%8B%E8%AF%95%E6%AF%95%E6%96%B9%E6%A1%82; userName=%E6%AF%95%E6%96%B9; Beefun.LoginValidation.ValidationHandler.WhiteListHandler=09:53:10 276; BeefunMainOpenMark=2017/3/17%20%u4E0A%u53489%3A53%3A34540; MDIPageLocation=%7E%252FBeefun%252FBaseInfo2%252FPTypeList.gspx'
print cookie

datas={"pagerId":"$2669e212$grid_pager1","queryParams":{"parid":"1","isfilter":True,"isshowstop":"0","isqtyautoupload":"-1","filtermode":"quickquery","filterstr":""},"orders":None,"filter":None,"first":0,"count":900}
req=requests.post(url=url,headers=headers,data=json.dumps(datas))
print req.text


cookie='_ati=146267075305; ASP.NET_SessionId=qe5bebuz2cphgb0o01omllql; _umdata=65F7F3A2F63DF0207E2BEE3A391EB24C36974786A7AE62C01730E5CD202421301CEB2174FC2A3B8ECD43AD3E795C914C875265D2A3D8556E4D50D098EE48453E; corpName=%E6%B5%8B%E8%AF%95%E6%AF%95%E6%96%B9%E6%A1%82; userName=%E6%AF%95%E6%96%B9; Beefun.LoginValidation.ValidationHandler.WhiteListHandler=09:53:10 276; BeefunMainOpenMark=2017/3/17%20%u4E0A%u53489%3A53%3A34540; quickDate=4; MDIPageLocation=%7E%252FBeefun%252FBaseInfo2%252FPTypeList.gspx'
'''
url="http://beefun.wsgjp.com/Beefun/Beefun.IniPeriod.ImportKtypeIniNew.ajax/SaveFile"
files={'_dataField':(None,'%7B%22ktypeid%22%3A%222605637371178862817%22%2C%22stockid%22%3A%222605637371178862817%22%2C%22kfullname%22%3A%22%u4E3B%u4ED3%u5E93%22%2C%22importertype%22%3A%22jxc%22%7D'),
  'loadfile':('abc.xls',open('D:abc.xls','rb'),'application/vnd.ms-excel')
 }

response=requests.post(url,files=files,headers=headers)
print response.text

time.sleep(2)
url2="http://beefun.wsgjp.com/Beefun/IniPeriod/ImportKtypeIniNewMessage.gspx"
response=requests.get(url2,headers=headers)
print response.text

time.sleep(2)
headers={'cookie':l,"Content-Type":"application/json; charset=UTF-8"}
url3="http://beefun.wsgjp.com/Beefun/Beefun.IniPeriod.ImportKtypeIniNewMessage.ajax/ImportPtype"
response=requests.post(url3,headers=headers)
print response.text
'''
url4="http://beefun.wsgjp.com/Beefun/Beefun.IniPeriod.ImportKtypeIniNewMessage.ajax/ShowMessage"
response=requests.post(url4,headers=headers)
print response.text
'''