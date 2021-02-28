word = input('文字列を入力してください > ')

d = {}
for s in word:
    if s in d.keys():
        d[s] += 1
    else:
        d[s] = 1
print(d)
