#*-* coding:UTF-8 *-*

import re
import requests
import json
from common import base
basec=base.baseCommon()
sql="SELECT token FROM eshop WHERE shopAccount='15608199188'"
token=basec.gettoken(sql)
#print token
print '订单详情'
'''
apiurl2="https://open.koudaitong.com/api/oauthentry?access_token="+token+"&method=kdt.trade.get&tid=E20160513141242009572378"
apires2=requests.get(apiurl2)
print apires2.text
apidata2=json.loads(apires2.text)
'''
id='E20160705094613033774135'
url="https://open.koudaitong.com/api/oauthentry"
payloads={"access_token":token,"method":"kdt.trade.get","tid":id}
apires2=requests.post(url,data=payloads)
print apires2.text
apidata2=json.loads(apires2.text)

print apidata2["response"]["trade"]["orders"]
print len(apidata2["response"]["trade"]["orders"])
print apidata2["response"]["trade"]["orders"][0]
print "api:"+apidata2["response"]["trade"]["orders"][0]['title']
print "api:"+apidata2["response"]["trade"]["orders"][0]['sku_properties_name']

a=apidata2["response"]["trade"]["orders"][0]['sku_properties_name']
apiitemtype=re.findall(":(.*?);",a+';')
de=''
for detail in range(len(apiitemtype)):
    de=de+apiitemtype[detail]+'_'
apiitemtype=de[:-1]
print apiitemtype

print "api:"+str(apidata2["response"]["trade"]["orders"][2])
print "api:"+apidata2["response"]["trade"]["orders"][2]['sku_properties_name']
print "api:"+apidata2["response"]["trade"]["orders"][2]['total_fee']
print apidata2["response"]["trade"]["adjust_fee"]["pay_change"]




'''

print '商品详情'
apiurl='https://open.koudaitong.com/api/oauthentry?access_token=b6f21a5b8ccaa0eeda4a34fefd06ce48feeb1a1b&method=kdt.item.get&num_iid=249451014'
apires=requests.get(apiurl)
print apires.text
apidata=json.loads(apires.text)






'''

