#*-* coding:UTF-8 *-*

import re
import requests
import json
from common import base
import datetime
import datetime
import hashlib
basec=base.baseCommon()


now=datetime.datetime.now()
nowtime=now.strftime("%Y-%m-%d %H:%M:%S")

apiurl="http://api04.weiba04.com/router/rest"

appid="5b11e5f1b3763ba5"
method="weiba.wxrrd.trade.details"
timestamp=nowtime
sql="SELECT token FROM eshop WHERE shopAccount='xmy666'"
token=basec.gettokeneach(sql)
access_token=token[6]
access_token=access_token[0]
print "token:"+access_token

id="E2016070511502597313"

signbefore="access_token="+access_token+"&appid=5b11e5f1b3763ba5&method=weiba.wxrrd.trade.details&order_sn="+id+"&timestamp="+nowtime
#print signbefore
m2 = hashlib.md5()
m2.update(signbefore)
sign= m2.hexdigest().upper()
print sign
payload={"appid":appid,"method":method,"timestamp":nowtime,"access_token":access_token,"sign":sign,"order_sn":id}
apires=requests.post(apiurl,data=payload)
print apires.text
apidata=json.loads(apires.text)
print apidata
print apidata["data"]["goods_amount"]
print apidata["data"]["package"]
print len(apidata["data"]["package"])
print apidata["data"]["order_goods"]
print len(apidata["data"]["order_goods"])
print apidata["data"]["order_goods"][1]
print apidata["data"]["order_goods"][2]["props"]
a=apidata["data"]["order_goods"][2]["props"]
b=a.replace(':',"_")
print b
print apidata["data"]["order_goods"][1]["goods_name"]
print apidata["data"]["order_goods"][1]["quantity"]
print apidata["data"]["order_goods"][1]["pay_price"]
print apidata["data"]["order_goods"][1]["product_sn"]