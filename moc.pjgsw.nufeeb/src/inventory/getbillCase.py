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
f.close()
header={'cookie':cookiestr,"Content-Type": "application/json"}
header2={'cookie':cookiestr,"Content-Type": "application/x-www-form-urlencoded"}

stamp=browser.gettimestamp()


vipinfo=browser.vipinfo(header)
print vipinfo
print vipinfo["itemList"]["rows"]
print vipinfo["itemList"]["rows"][0][7]
