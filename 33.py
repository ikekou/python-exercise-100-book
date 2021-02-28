l1 = ['python','ruby','php','javascript']
l2 = ['java','ruby','golang','python','typescript']

r = []

for i in l1:
    for j in l2:
        if i == j and i not in r:
            r.append(i)

print(r)