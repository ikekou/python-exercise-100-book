# import re

# s = input('input > ')

# matched = re.match(r'[A-Z]',s[0])

# # print(matched)

# if matched:
#     print(s[0] + s)
# else:
#     print(s[0].upper() + s[1:])

s = input('input > ')

if s[0].islower():
    s2 = s[0].upper() + s[1:]
else:
    s2 = s * 2

print(s2)