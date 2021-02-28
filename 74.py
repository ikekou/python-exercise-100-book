d={'d':444,'a':511,'b':222,'c':333}

r = dict(sorted(d.items(), key=lambda x: x[1]))
print(r)