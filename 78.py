d = {'b':222,'a':111,'d':444,'c':333}

key_to_get_min_value = min(d.keys(), key= lambda k: d[k])
print(key_to_get_min_value)