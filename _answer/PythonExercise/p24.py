word = input('英単語を入力してください > ')
count = 0

for _ in word:
    count += 1

index = count // 2

if count % 2 == 0:
    word = word[:index] + '@' + word[index:]
else:
    word = word[:index] + '@' + word[index+1:]

print(f'変換した英単語 : {word}')
