#!/usr/bin/env python
import struct

file = raw_input("the file you want identfy:")

f = open(file,'rb')
s = f.read(30)
print('0-30:',s)

ss = struct.unpack('<ccIIIIIIHH',s)

if ss[0] == 'B' and ss[1] == 'M':
        print 'This is a bmp file! It has ',ss[6],'*', ss[7],', It is color is ',ss[9],'.'
else:
        print 'This is not a bmp file!'

f.close()
