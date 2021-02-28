d={'a':111,'b':222,'c':333}
l = ['b','c','d','a']

# for i in d:
#     if i in l:
#         print(i)

for i in l:
    print(d.get(i))
        