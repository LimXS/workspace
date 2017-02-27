#*-* coding:UTF-8 *-*
'''
Created on 2016��4��21��

@author: xsx
'''
import unittest
from selenium import webdriver
from common import  browserClass
from common import  baseClass
import traceback
import time
from selenium.webdriver.common.keys import Keys  #需要引入keys包
base=baseClass.base()
browser=browserClass.browser()


        
driver=webdriver.Chrome()
browser.set_up(driver)
browser.openModule2(driver,".//*[@id='$80d499b2$ManagerMenuBar3']/div",".//*[@id='$80d499b2$ManagerMenuBar3_15']/td[3]")
browser.openModule2(driver,".//*[@id='$dea0a8b3$button8']",".//*[@id='$dea0a8b3$synTrade0']/td[3]")
browser.findXpath(driver,"/html/body/table[7]/tbody/tr[2]/td/div/div/div/table/tbody/tr[3]/td[2]/table/tbody/tr/td[2]/div/div").click()
js1="$(\"div[class=Border]\").css(\"display\",\"block\");$(\"div[class=Border]\").css(\"visibility\",\"visible\");"
js2="$(\"div:contains(\'明丽客\')\").eq(1).attr(\"id\",\"testid222\")"
driver.execute_script(js2)
time.sleep(2)
#driver.execute_script(js1)
#js3="$(\"#testid222\").click()"
#driver.execute_script(js3)
browser.findId(driver,"testid222").click()
print "over"