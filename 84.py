l = [1,0,[],(2,3),'AA','',False,3]

cnt = 0
cnt2 = 0
for i in l:
    if i:
        cnt+=1
    if bool(i):
        cnt2+=1

print(cnt,cnt2)