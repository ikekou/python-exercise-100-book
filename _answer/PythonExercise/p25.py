word1 = input('1つ目の英単語を入力してください > ')
word2 = input('2つ目の英単語を入力してください > ')
word3 = input('3つ目の英単語を入力してください > ')

words = [word1, word2, word3]

words.sort()
sord_words = ', '.join(words)
print(f'並び替えた英単語 : {sord_words}')
