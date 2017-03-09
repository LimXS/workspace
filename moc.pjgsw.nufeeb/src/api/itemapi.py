import requests
import json
import re

f=open('E:\wei\sp.dat','r')
token=f.read()
print "token:"+token
id="1787478597"
skuid="1787519913"
params={"itemid":skuid}
publics={"method":"vdian.item.get","access_token":token,"version":"1.0","format":"json"}

payload={"param":json.dumps(params),"public":json.dumps(publics)}
url="http://api.vdian.com/api"
apires=requests.post(url,data=payload)
apidata=json.loads(apires.text)
print len(apidata['result']['skus'])