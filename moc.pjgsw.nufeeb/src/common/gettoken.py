#*-* coding:UTF-8 *-*
from selenium import webdriver
import re
import requests
import ssl
'''
driver=webdriver.Firefox()
driver.get("https://api.vdian.com/oauth2/authorize?appkey=630426&redirect_uri=http://eshopgateway.mygjp.com&response_type=code&state=123")
driver.find_element_by_id("tele").send_keys("18080107102")
driver.find_element_by_id("password").send_keys("sdfasdf*-")
driver.find_element_by_id("J_LoginBtn").click()
driver.find_element_by_xpath(".//*[@id='outer']/div/div[2]/form/div/div[2]/div/p/input[1]").click()
pageurl=driver.current_url
print pageurl
code=re.findall("code=(.*?)$",pageurl)
print code[0]

url2="https://api.vdian.com/oauth2/access_token?appkey=630426&secret=97da203603c1df312d741b6e3acc3e71&code="+code[0]+"&grant_type=authorization_code"
resp=requests.get(url2).text
print resp
token=re.findall("access_token\":\"(.*?)\"",resp)
print token[0]

'''
url="https://api.vdian.com/login"
data={"country":"86","phone":"18080107102","password":"sdfasdf*-","appkey":"630426","redirect_uri":"http://eshopgateway.mygjp.com","response_type":"code","state":"123"}
res=requests.post(url,data=data)
coo=res.cookies
cookie=re.findall("ta=(.*?) ",str(coo))
print cookie[0]

url2="https://api.vdian.com/oauth2/commit"
data2={"appkey":"630426","userid":"520219391","agreement":"1","response_type":"code","ticket":cookie[0],"state":"123","redirect_uri":"http://eshopgateway.mygjp.com"}
res2=requests.post(url2,data=data2)
print res2.url
pageurl=res2.url
code=re.findall("code=(.*?)$",pageurl)
print code[0]

url3="https://api.vdian.com/oauth2/access_token?appkey=630426&secret=97da203603c1df312d741b6e3acc3e71&code="+code[0]+"&grant_type=authorization_code"
resp=requests.get(url3).text
print resp
token=re.findall("access_token\":\"(.*?)\"",resp)
print token[0]

f=open("E:\wei\sp.dat","w")
f.write(token[0])
f.close()
