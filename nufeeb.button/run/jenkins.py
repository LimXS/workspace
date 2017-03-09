#*-* coding:UTF-8 *-*

import requests
import os
import sys


curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

urlcookie="http://172.16.0.248:8080/j_acegi_security_check?j_username=xsx&j_password=123456&from=%2Fjob%2Fnufeeb.button%2Fbuild%3Ftoken%3D123456&json=%7B%22j_username%22%3A+%22xsx%22%2C+%22j_password%22%3A+%22123456%22%2C+%22remember_me%22%3A+false%2C+%22from%22%3A+%22%2Fjob%2Fnufeeb.button%2Fbuild%3Ftoken%3D123456%22%7D&Submit=%E7%99%BB%E5%BD%95"
cookietext=requests.get(url=urlcookie)
print cookietext
'''
browser=browserClass.browser()
driver=browser.startBrowser('chrome')
#url="http://172.16.0.248:8080/login?from=%2F"
url="http://172.16.0.248:8080/login?from=%2Fjob%2Fnufeeb.button%2Fbuild%3Ftoken%3D123456"
driver.get(url)
browser.findId(driver,"j_username").send_keys("xsx")

browser.findXpath(driver,"//*[@id='main-panel']/div/form/table/tbody/tr[2]/td[2]/input").send_keys("123456")

browser.findId(driver,"yui-gen1-button").click()
'''