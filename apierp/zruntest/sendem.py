import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)



from common import base

bas=base.baseCommon()

To1 = "1206626163@qq.com"
To2="625499968@qq.com"
To3="394264687@qq.com"
To4="2275879116@qq.com"

bas.send_Email(To1)

bas.send_Email(To2)
#bas.send_Email(To3)
#bas.send_Email(To4)
