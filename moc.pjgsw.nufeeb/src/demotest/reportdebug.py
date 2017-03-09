#*-* coding:UTF-8 *-*

import  xml.dom.minidom
import time
from common import browserClass
browser=browserClass.browser()

driver=browser.startBrowser('chrome')
'''
browser.set_up(driver)

dom = xml.dom.minidom.parse(r'D:\workspace\moc.pjgsw.nufeeb\src\data\report')
module='module'
module=browser.xmlRead(driver,dom,module,0)
getstock=browser.xmlRead(driver,dom,'getstock',0)
getstockreport=browser.xmlRead(driver,dom,'getstockreport',0)


okinto=browser.xmlRead(driver,dom,'okinto',0)
browser.openModule3(driver,module,getstock,getstockreport)
browser.findXpath(driver,okinto).click()
'''
f=open(r"E:\cookie.txt","w")
cookie=f.read()

url="http://beefun.wsgjp.com/Beefun/Report/PTypeSaleOrderStatistic.gspx?vchtype=stockorder"
headers={'cookie':cookie}

data={"__Params":{"startDate":"2016-06-14","endDate":"2016-06-20","index":0,"btypeid":0}}
a=browser.orderRead(driver,url,data,headers)
print a.text