word1 = input('1つ目の文字列を入力してください > ')
word2 = input('2つ目の文字列を入力してください > ')

r = ''
for ch in word1:
    if ch in word2 and not ch in r:
        r += ch

print(f'重複する文字列 : {r}')
