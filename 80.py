d = {'b':222,'a':111,'d':444,'c':333}

# r = {}

# for k,v in d.items():
#     print(k,v)
#     if v%2==1:
#         continue
#     r[k] = v
# print(r)

# r = {k:v for k,v in d.items() if v%2==0}
# print(r)

d2 = d.copy()
print(d2)

for k,v in d.items():
    if v%2!=0:
        del d2[k]

print(d2)