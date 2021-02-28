l = ['Python','Ruby','PHP','Javascript']

r = l[0]
min_length = len(r)

for i in l:
    if min_length > len(i):
        r = i
        min_length = len(r)

print(r)