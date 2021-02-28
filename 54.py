l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
new_l = [tuple(l[i:i+3]) for i in range(0, 9, 3)]
# for i in new_l:
#     print('hoge : ' + ' '.join(map(str,list(i))))

for i,row in enumerate(new_l, start=1):
    a,b,c = row
    print(f'row{i} : {a} {b} {c}')