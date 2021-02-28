t = (1,[2,3],'4',(5,6,7),'8',(9,10))

# r=0
# for v in t:
#     if type(v) == tuple:
#         r+=1
# print(r)

t_in_tuple = [v for v in t if isinstance(v,tuple)]
print(len(t_in_tuple))