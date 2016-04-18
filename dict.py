#!/usr/bin/env python

name = 'dd'
value = 4

d = {"aa":1,"bb":2}
print d,'\n','aa=',d['aa']

d['cc'] = 3

print d,'\n','cc=',d['cc']

d[name]=value

print d,'\n','dd=',d['dd']

if d.get('ee',1) == 1:
        d['ee'] = 5

print d,'\n','ee=',d['ee']

l = [1,]
ll = []
ll.insert(0,1)
ll.insert(1,2)
print ll
ll = []
ll.insert(0,3)
ll.insert(1,4)
print ll
