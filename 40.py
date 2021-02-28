l = [1,'22',3,'444',0.0,'5']

# min,max=float('inf'),0
# for i in l:
#     if isinstance(i,int):
#         if min>i:
#             min=i
#         if max<i:
#             max=i
# print(min,max)

l2 = [v for v in l if isinstance(v,int)]

print(min(l2))
print(max(l2))