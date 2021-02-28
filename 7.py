for i in range(1,31):
    if i%15 == 0:
        print(f'{i} : fizzbuzz')
    elif i%3 == 0:
        print(f'{i} : fizz')
    elif i%5 == 0:
        print(f'{i} : buzz')
    else:
        print(i)
