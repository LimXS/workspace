#*-* coding:UTF-8 *-*

import  xml.dom.minidom
import time
from common import browserClass
browser=browserClass.browser()

driver=browser.startBrowser('chrome')
browser.set_up(driver)

dom = xml.dom.minidom.parse(r'D:\workspace\moc.pjgsw.nufeeb\src\data\basedata')

module='moudle'
modulename=browser.xmlRead(driver,dom,module,2)
moduledetail=browser.xmlRead(driver,dom,'page',2)

browser.openModule2(driver,modulename,moduledetail)