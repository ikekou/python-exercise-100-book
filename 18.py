s = input('文字列を入力してください')

d = {}
for i in s:
    if i in d.keys():
        d[i] += 1
    else:
        d[i] = 1

print(d)