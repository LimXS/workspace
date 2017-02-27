#*-* coding:UTF-8 *-*
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)


from common import baseClass


bas=baseClass.base()
To1="1206626163@qq.com"
To2="625499968@qq.com"
To3="1344875134@qq.com"


bas.sendemail(To1)
bas.sendemail(To2)
#bas.sendemail(To3)