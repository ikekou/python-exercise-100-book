l = [1,2,None,False,'3','4',None,True]

# true_count = 0
# none_count = 0

# for i in l:
#     if i is True:
#         true_count += 1
#     if i is None:
#         none_count += 1

# print(true_count)
# print(none_count)

print(len([v for v in l if v is True or v is None]))