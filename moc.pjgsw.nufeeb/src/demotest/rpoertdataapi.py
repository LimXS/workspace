#*-* coding:UTF-8 *-*

import  xml.dom.minidom
import time
import json
import re
import requests
from common import browserClass


browser=browserClass.browser()
driver=browser.startBrowser('chrome')
browser.set_up(driver)
