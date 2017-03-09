# -*- coding: utf-8 -*-
import xml
import requests
from common import browserClass
browser=browserClass.browser()
f2=open(r"D:\cookies\eshop.txt")
cookie=f2.read()
headers={'cookie':cookie}
req = requests.get("http://beefun.wsgjp.com/Beefun/EShop2/PTypeRelation2.gspx",headers = headers)
b=req.text
print b