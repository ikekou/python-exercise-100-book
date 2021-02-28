l = [0,'1',3,2,'4',5,'7']

l2 = [i for i,v in enumerate(l) if i == int(v)]

print(l2)