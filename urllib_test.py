#!/usr/bin/env python

from urllib import request

in_url = input("url:")

pretend = input("pretend?(0 or 1):")

if pretend == '1':
        req = request.Request(in_url)
        req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
        url = req
else:
        url = in_url

with request.urlopen(url) as f:
    data = f.read()
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', data.decode('utf-8'))
