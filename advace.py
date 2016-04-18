#!/usr/bin/env python

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [cc for cc in L1 if isinstance(cc, str) ]

print L2

def triangles():
        i = 1
        l = [1]
        yield l
        while i < 100:
                ll = []
                i = i+1
                n = 0
                j = 0
                for value in l:
                        ll.insert(j,n+value)
                        j = j + 1
                        n = value
                j = j + 1
                ll.insert(j,n)
                yield ll
                l = ll

#triangles()
n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break
