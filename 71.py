d={'a':111,'b':222,'c':333}

# r = {}
# for i,k in enumerate(d):
#     v = d[k]
#     if v > 150:
#         r.update({k:v})

r = {k:v for k,v in d.items() if v > 150}

print(r)