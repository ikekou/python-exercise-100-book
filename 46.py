l = ['python1','java1',1,'python2','java2',2]

for v in l:
    if 'python' in str(v):
        l.remove(v)

print(l)

# list.removeってどういうメソッドなのか？値を指定しているのか？