a = int(input('1つ目の整数を入力してください > '))
b = int(input('2つ目の整数を入力してください > '))

r = a - b
r = -r if r < 0 else r
print(f'計算結果 : {r}')
