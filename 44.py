# l = [1,2,3,'4',5]
l = [1,2,3,4,5]

if len([i for i in l if isinstance(i,str)]):
    print('str')
else:
    print('not str')