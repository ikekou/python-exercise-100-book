l = [1,3,2,3,4,6,5,8,7]

for i,v in enumerate(l):
    if i%3==0 and int(v)%3==0:
        l.pop(i)
print(l)
