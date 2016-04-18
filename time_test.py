#!/usr/bin/env python

from datetime import datetime, timedelta

now = datetime.now()
print(now.strftime('%a %b %d %H:%M:%S'))

time = raw_input("input time:")
ctime = datetime.strptime(time,"%Y-%m-%d %H:%M:%S")
print(ctime)

a = type(ctime)
print a

def totimestamp(dt, epoch=datetime(1970,1,1,0,0,0)):
    td = dt - epoch
    # return td.total_seconds()
    return (td.microseconds + (td.seconds + td.days * 86400) * 10**6) / 10**6


timesp = totimestamp(ctime)
print(timesp)

timesp3 = ctime.timestamp()
print(timesp3)
