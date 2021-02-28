methods = dir(list)
methods2 = [s for s in methods if not '__' in s]
print(methods2)