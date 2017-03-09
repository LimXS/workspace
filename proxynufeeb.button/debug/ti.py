# -*- coding: utf-8 -*-
import time
import datetime
import matplotlib.pyplot as plt
import numpy as np
from pylab import *

'''
#获取横坐标
def getxt(num,evti):
    dts=[]
    dts.append(0)
    now=datetime.datetime.now()
    for a in range(num):
        d1 = now + datetime.timedelta(hours=evti)
        dt1=d1.strftime(\\\"%H:%M:%S\\\")
        dts.append(dt1)
        now=d1
    return dts
print getxt(3,0.5)

#获取纵坐标
def gety(num,sp):
    getys=[]
    now=0
    for k in range(num):
        getys.append(now)
        now+=sp
    return getys
print gety(4,10)


# coding = utf-8
import dateutil, pylab,random
from pylab import *
from datetime import datetime,timedelta

now = datetime.now()
dates = [now + timedelta(hours=i) for i in range(10)]
#values = [random.randint(1, 20) for i in range(10)]
values = [3,2,8,4,5,6,7,8,11,2]
pylab.plot_date(pylab.date2num(dates), values, linestyle='-')
text(17, 277, u'瞬时流量示意')
xtext = xlabel(u'time (s)')
ytext = ylabel(u' (m3)')
ttext = title(u'xx')
grid(True)
setp(ttext, size='large', color='r')
#setp(text, size='medium', name='courier', weight='bold',color='b')
setp(xtext, size='medium', name='courier', weight='bold', color='g')
setp(ytext, size='medium', name='helvetica', weight='light', color='b')
#savefig('simple_plot.png')
savefig('simple_plot')
show()


import numpy as np
import matplotlib.pyplot as plt
from pylab import *

x = np.arange(-5.0, 5.0, 0.02)
y1 = np.sin(x)

plt.figure(1)
plt.subplot(211)
plt.plot(x, y1)
plt.grid(True)

plt.subplot(212)
#设置x轴范围
#设置y轴范围
ylim(-1, 1)
plt.plot(x, y1)

plt.grid(True)
plt.show()
'''
