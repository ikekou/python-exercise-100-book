print('********')
print('選択肢 : {0: \'グー\', 1: \'チョキ\', 2: ')
print('********')

a = int(input('自分が出す手を入力してください（整数：0, 1, 2）'))

import random
import math

b = math.floor(random.random() * 3)

l = ['グー','チョキ','パー']
print(f'コンピューターの出した手 : {l[b]}')
print(f'自分の出した手 : {l[a]}')

r = ''
if a == b:
    r = '引き分け'
elif (a==0 and b==1) or (a==1 and b==2) or (a==2 and b==0):
    r = '勝ち'
else:
    r = '負け'

print(f'結果 : {r}')