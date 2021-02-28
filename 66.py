d1 = {'a':111,'b':222,'c':333}
d2 = {'d':444,'e':555}
d3 = {'f':666}

r = {}
for i,k in enumerate(d1):
    r[k] = d1[k]

for i,k in enumerate(d2):
    r[k] = d2[k]

for i,k in enumerate(d3):
    r[k] = d3[k]

print(r)

r2={}
for d in [d1,d2,d3]:
    r2.update(d)
print(r2)