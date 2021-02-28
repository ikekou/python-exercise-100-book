t = (1,'2',3,'4',5)

# m = map(str,t)
# for i in m:
#     print(i)

str_t = (str(v) for v in t)
c = int(''.join(str_t))
print(c)