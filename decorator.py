#!/usr/bin/env python

import functools

def log(text):
        def decorator(func):
        #       @functools.wraps(func)
                print("%s" % (text) )
                def wrapper(*args,**kw):
                        print("begin call:%s" % func.__name__)
                        func(*args,**kw)
                        print("end call:%s" % func.__name__)
                return wrapper
        return decorator

@log("aa")
def now():
        print("time is 2016.4.7")

now()
