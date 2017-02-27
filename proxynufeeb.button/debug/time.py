# -*- coding: utf-8 -*-
import re
aa="abcdefg"
print aa[-2:]

f=open(r"E:\\testdata\\TEST4DeCheckItem.txt",'r')
k=f.read()
print k
m=re.findall('\'(.*?)\'\);',k)
print m
print m[0][:-20]

ff=open(r"D:\\hehe\\testdata\\TEST4DeCheckItemvc.txt",'w')
ff.write('')
ffc=open(r"D:\\hehe\\testdata\\TEST4DeCheckItemvc.txt",'w+')

ff2=open(r"D:\\hehe\\testdata\\TEST4DeCheckItemid.txt",'w')
ff2.write('')
ffc2=open(r"D:\\hehe\\testdata\\TEST4DeCheckItemid.txt",'w+')
for a in m :
    ffc.write(a[-17:])
    ffc.write('\n')
    print a[-17:]
    ffc2.write(a[:-20])
    ffc2.write('\n')

print len(m)
