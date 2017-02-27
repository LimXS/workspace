# -*- coding: utf-8 -*-
import random
f=open(r"D:\testdata\TEST1DeCheckItemid.dat",'r')
k=f.readlines()
g=open(r"D:\testdatarand\TEST1DeCheckItemid.dat",'w+')
random.shuffle(k)
for a in k:
    g.write(a)








[\"{checksubdata_11}\",\"{checksubdata_12}\",\"{checksubdata_13}\",\"{checksubdata_14}\",\"{checksubdata_15}\",\"{checksubdata_16}\",\"{checksubdata_17}\",\"{checksubdata_18}\",\"{checksubdata_19}\",\"{checksubdata_20}\"]