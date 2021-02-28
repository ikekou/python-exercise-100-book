import re

s = input('input')

replaced = re.sub(r'[aiueo]','',s)

print(replaced)