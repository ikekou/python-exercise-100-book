d = {'A':111,'B':222,'C':333}
d2 = {'A':111,'B':222,'C':333}

d['D'] = 444

d.update({'D': 444})

print(d)
print(d2)