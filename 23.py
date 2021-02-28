s1 = input('input 1 > ')
s2 = input("input 2 > ")

s1s = s1.split(' ')
s2s = s2.split(' ')

r = []

for i in s1s:
    if i in s2s and not i in r:
        r.append(i)

print(r)