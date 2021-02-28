l = [1,2,3,4,5,6,7,8,9]

# for i in range(0, 9, 3):
#     print(tuple(l[i:i+3]))

r = [tuple(l[i:i+3]) for i in range(0,9,3)]
print(r)