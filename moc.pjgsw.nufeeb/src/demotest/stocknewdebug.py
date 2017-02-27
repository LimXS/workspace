#*-* coding:UTF-8 *-*

import  xml.dom.minidom
import time
from common import browserClass
browser=browserClass.browser()

driver=browser.startBrowser('chrome')
browser.set_up(driver)

dom = xml.dom.minidom.parse(r'D:\workspace\moc.pjgsw.nufeeb\src\data\basedata')

module='moudle'
modulename=browser.xmlRead(driver,dom,module,0)
moduledetail=browser.xmlRead(driver,dom,'page',0)

browser.openModule2(driver,modulename,moduledetail)

no="//*[@id='$eb57a3e$edNumber']"
no='html/body/table[4]/tbody/tr/td[2]/div/div[2]/div[2]/div/div[1]/table/tbody/tr/td[6]/div/table/tbody/tr/td[6]'
time.sleep(3)

js='document.getElementById("$eb57a3e$edNumber").style.color="blue";'
driver.execute_script(js)

#js='document.getElementById("$eb57a3e$edNumber").control.get_text();'
js="var code=document.getElementById('$eb57a3e$edNumber').value;$eb57a3e$edNumber.setAttribute('value',code);"
driver.execute_script(js)
time.sleep(2)
#print browser.findXpath(driver,no)
aa=browser.findId(driver,"$eb57a3e$edNumber").get_attribute("value")
print aa
print "over................."
'''
js2="var code=document.getElementById('$eb57a3e$edNumber').value;var text=document.createTextNode(code);$eb57a3e$edNumber.appendChild(text);"
driver.execute_script(js2)
aa=browser.findId(driver,"$eb57a3e$edNumber").text
print aa
'''
time.sleep(3)





xpath=".//*[@id='$eb57a3e$grid']/div[2]/table/tbody/tr[1]/td[2]"
browser.findXpath(driver,xpath).click()
xpath2=".//*[@id='$eb57a3e$grid']/div[2]/table/tbody/tr[1]/td[2]/table/tbody/tr/td[2]/div/div"
browser.findXpath(driver,xpath2).click()

time.sleep(2)
input1="//*[@id='$84d24c7e$grid']/div[2]/table/tbody/tr[1]/td[2]/input"
browser.findXpath(driver,input1).click()
choicein=".//*[@id='$84d24c7e$btnKeepSelect']"
browser.findXpath(driver,choicein).click()

time.sleep(2)
input2="//*[@id='$84d24c7e$grid']/div[2]/table/tbody/tr[2]/td[2]/input"
browser.findXpath(driver,input2).click()
choiceandclose=".//*[@id='$84d24c7e$btnSelect']"
browser.findXpath(driver,choiceandclose).click()
#time.sleep(3)
num1=".//*[@id='$eb57a3e$grid']/div[2]/table/tbody/tr[1]/td[20]/div"
'''
js='document.getElementById("$eb57a3e$grid_assqty").style.visibility="visible";'
driver.execute_script(js)
'''
browser.findXpath(driver,"//*[@id='$eb57a3e$grid']/div[2]/table/tbody/tr[1]/td[20]").click()
browser.findXpath(driver,"//*[@id='$eb57a3e$grid_assqty']").send_keys("2")
#time.sleep(3)
num2=".//*[@id='$eb57a3e$grid']/div[2]/table/tbody/tr[2]/td[20]/div"
browser.findXpath(driver,num2).click()
browser.findXpath(driver,"//*[@id='$eb57a3e$grid_assqty']").send_keys("2")

money=".//*[@id='$eb57a3e$grid']/div[2]/table/tbody/tr[1]/td[22]/div"
browser.findXpath(driver,money).click()
browser.findXpath(driver,".//*[@id='$eb57a3e$grid_assdpprice']").send_keys("3")

money2=".//*[@id='$eb57a3e$grid']/div[2]/table/tbody/tr[2]/td[22]/div"
browser.findXpath(driver,money2).click()
browser.findXpath(driver,".//*[@id='$eb57a3e$grid_assdpprice']").send_keys("3")

