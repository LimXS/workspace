#*-* coding:UTF-8 *-*

import re
import requests
import json
from mengdian import gettokenmeng
from common import base
basec=base.baseCommon()
#获取单个订单
'''
f=open(r'D:\api\mengtoken.txt','r')
token=f.read()
'''
token=gettokenmeng.getmengToken()
print "token:"+token
apiurl='https://open.mengdian.com/api/mname/WE_MALL/cname/orderFullInfoGetHighly?accesstoken='+token
id="81604271101345416"

payload={"order_no":id}
apires=requests.post(apiurl,data=json.dumps(payload))
apidata=json.loads(apires.text)

print apidata['data']


print apidata["data"]["pay_time"]
print apidata["data"]["remark"]
#print apidata["data"]["order_details"][0]
print apidata["data"]["order_details"][0]["price"]
print apidata["data"]["receiver_region"]["province"]
print apidata["data"]["receiver_region"]["city"]
print apidata["data"]["receiver_region"]["district"]
print apidata["data"]["receiver_region"]["address"]
t=[]
a=apidata["data"]["receiver_region"]["province"].strip()
b=apidata["data"]["receiver_region"]["city"].strip()
c=apidata["data"]["receiver_region"]["district"].strip()
d=apidata["data"]["receiver_region"]["address"].strip()
f=a+b+c+d
'''
t.append(a)
t.append(b)
t.append(c)
t.append(d)
f=''.join(t)
print f.strip('\n')
'''
print f
print type(apidata["data"]["delivery_amount"])


print apidata["data"]["pay_status"]
print apidata["data"]["order_details"][0]["return_id"]
print apidata["data"]["order_details"][0]["return_qty"]
print apidata["data"]["order_details"][0]["return_type"]
print apidata["data"]["order_details"][0]["return_status"]
print type(apidata["data"]["order_details"][0]["return_status"])
print apidata["data"]["carrier_name"]
print apidata["data"]["express_no"]
print "api接口返回的数据order_status："+str(apidata["data"]["order_status"])+"(0:全部；1：交易中；2：交易成功；3：交易关闭)\n"


'''
#店铺信息
apiurl3='https://open.mengdian.com/api/mname/WE_MALL/cname/shopGet?accesstoken='+token


payload3={"include_intro":False}
apires3=requests.post(apiurl3,data=json.dumps(payload3))
apidata3=json.loads(apires3.text)

print apidata3['data']['shop_name']



#获取订单列表 取订单总数
timelist=basec.getTime()
start=timelist[1]
end=timelist[0]

apiurl2='https://open.mengdian.com/api/mname/WE_MALL/cname/orderGetHighly?accesstoken='+token
#payload2={"order_status":None,"pay_status":None,"delivery_status":None,"page_size":20,"page_no":1,"create_begin_time":start,"create_end_time":end}
payload2={"order_status":None,"pay_status":None,"delivery_status":None,"page_size":20,"page_no":1}
apires2=requests.post(apiurl2,data=json.dumps(payload2))
print apires2.text
apidata2=json.loads(apires2.text)
print apidata2["data"]["row_count"]
'''