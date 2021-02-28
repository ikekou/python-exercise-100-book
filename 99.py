import re

l = ['アメリカ','カナダ','スイス','メキシコ','セントルシア','タイ']
l2 = [v for v in l if re.match(r'[サシスセソ]',v)]
print(l2)