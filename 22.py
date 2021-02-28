s = input('input 1 > ')
s2 = input('input 2 > ')
result = ''

# for i in s:
    # for j in s2:
        # if i == j:
            # result += i

for ch in s:
    if ch in s2 and not ch in result:
        result += ch

print(result)