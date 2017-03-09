#*-* coding:UTF-8 *-*

import  xml.dom.minidom
import time
import json
import re
import requests
from common import browserClass
import datetime
import time

browser=browserClass.browser()



a="1472745600000"
b=browser.handlestampdays(a,0)
print b


a="1472784843000"
b=browser.handlestampdays(a,-1)
print b