d = {'A': 111, 'B': 222, 'C': 333}
new_d = {key:value for key, value in d.items() if value > 150}
print(f'絞り込みをかけた辞書 : {new_d}')
