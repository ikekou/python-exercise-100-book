l=['08012034455','09093729682','09030804982','08039175918']

r=[]
for i in l:
    if i[:3]=='080':
        r.append(i)

print(r)