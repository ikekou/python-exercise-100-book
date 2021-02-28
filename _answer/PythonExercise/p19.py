vowels = ['a', 'i', 'u', 'e', 'o']

word = input('文字列を入力してください > ')

new_word = ''
for s in word:
    if s in vowels:
        continue
    new_word += s

print(f'作成した文字列 : {new_word}')
