s = 'This is the python exercise.'

l = [v for v in s.split() if 't' not in v]
print(l)

s2 = ' '.join(l)
print(f's2 : {s2}')