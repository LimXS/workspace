#*-* coding:UTF-8 *-*
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)


import unittest

from weidian import orderweiCase
from weidian import itemsweiCase

from mengdian import itemsmengCase
from mengdian import ordermengCase

from rerendian import orderrenrenCase
from rerendian import itemsrenrenCase

from youzan import  itemsyouzanCase
from youzan import  orderyouzanCase


from mushroomstreet import itemsmushroomCase
from mushroomstreet import ordermushroomCase

print "OK"
