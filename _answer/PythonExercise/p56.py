t = (1, '2', 3, '4', 5)
str_t = (str(v) for v in t)
converted_int = int(''.join(str_t))
print(f'変換後の数値 : {converted_int}')