l = ['1',2,'3',4.0,'5',6,'7',8.0,'9',10]

l2 = []
for i in l:
    if isinstance(i,int):
        l2.append(i)
print(l2)