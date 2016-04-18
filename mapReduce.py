#!/usr/bin/env python
def normalize(name):
        return name.title()

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

def is_palindrome(n):
        sn = str(n)
        for i in range(len(sn)/2):
                if sn[i] != sn[len(sn)-i-1]:
                        return False
        return True

output = filter(is_palindrome, range(1, 1000))
print(list(output))
