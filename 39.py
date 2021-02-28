l1 = [1,2,3,4,5]
l2 = [10,9,8,7,6]

# r=[]
# for i in range(0,len(l1)):
#     r.append(l1[i]*l2[i])

r = [i*j for i,j in zip(l1,l2)]

print(r)