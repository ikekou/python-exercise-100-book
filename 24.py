import math

s = input('input > ')

l = len(s)
r = ''
r = s[:l//2] + '@' + s[math.ceil(l/2):]

print(r)