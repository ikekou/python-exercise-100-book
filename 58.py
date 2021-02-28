t = (1,[2,3],'4',(5,6,7),(None,),(9,10))

r = []
for v in t:
    if isinstance(v,tuple):
        r.append(v)
    elif isinstance(v,list):
        r.append(tuple(v))
    else:
        r.append((v,))
print(tuple(r))