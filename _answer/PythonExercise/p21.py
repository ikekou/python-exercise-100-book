word = input('文字列を入力してください > ')

if word[0].islower():
    word = word[0].upper() + word[1:]
elif word[0].isupper():
    word = word*2

print(f'変換後の文字列 : {word}')
