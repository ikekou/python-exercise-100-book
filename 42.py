l = [1,2,3,3]

# for i in l:
#     for j in l:
#         if i == j:
#             print('juhuku')
#             break
#     else:
#         continue
#     break

if len(set(l)) < len(l):
    print('juhuku')
else:
    print('not juhuku')