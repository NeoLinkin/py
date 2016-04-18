#!/usr/bin/env python

import re

def myMatch():
        t = "16:01:00"
        m = re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', t)
        print(m.group(0))
        print(m.group(1))

l = re.split(r'\s+','a b  c      d')
print(l)


def emailMatch(name):
        re_email = re.compile(r'(.{1,64})@([0-9a-z]{1,32}).([a-z]{2,5})')
        if re_email.match(name):
                print "email is ok"
                ok = re_email.match(name)
                print "name is",ok.group(1)
        else:
                print "not a email"

myMatch()
name = raw_input("your email:")
emailMatch(name)
