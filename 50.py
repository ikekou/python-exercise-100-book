l1=[4,6,9,2]
l2=[3,5,7]
l3=[1,9,7]

# r = []
# maxSum = 0
# for l in [l1,l2,l3]:
#     s = 0
#     for i in l:
#         s += i
#     a = s / len(l)
#     if maxSum < a:
#         r = l
#         maxSum = a
# print(r)

l = [l1,l2,l3]

sorted_l = sorted(l,key=lambda v: sum(v) / len(v), reverse=True)
print(sorted_l[0])