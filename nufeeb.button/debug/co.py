# -*- coding: utf-8 -*-
import xml
from common import browserClass
browser=browserClass.browser()


driver=browser.startBrowser('chrome')
browser.set_up(driver)
#browser.set_up(driver)
#driver.get("http://dba.wsgjp.com.cn/")
dom = xml.dom.minidom.parse(r'C:\workspace\nufeeb.button\frequentlyused\frelocation')
module=browser.xmlRead(dom,'module',0)
moduledetail=browser.xmlRead(dom,'moduledetail',1)

browser.openModule2(driver,module,moduledetail)
cookies=browser.cookieSave(driver)
browser.delaytime(1)
f=open(r"D:\cookies\coktemp.txt",'w')
f.write(cookies)
f.close()

fr=open(r"D:\cookies\coktemp.txt",'r')
nskcoo=fr.read()
print nskcoo
headers={'cookie':nskcoo,"Content-Type": "application/json"}


#单据中心
notecenurl="http://wsgjp.com.cn/Carpa.Web/Carpa.Web.Script.DataService.ajax/GetPagerData"
notdata={"pagerId":"$c3e1bf43$grid_pager1","queryParams":{"vchtype":"","beginDate":"2016-12-20","endDate":"2016-12-28","redwordType":0,"dlyType":0},"orders":None,"filter":None,"first":0,"count":200}

#print nskcookie

pageorderdata=browser.requestpost(notecenurl,notdata,headers,1)
print "单据中心...."
print pageorderdata