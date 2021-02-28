w1 = input('input 1 > ')
w2 = input('input 2 > ')
w3 = input('input 3 > ')

words = [w1,w2,w3]

words.sort()
result = ', '.join(words)
print(result)