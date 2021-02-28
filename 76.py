l = [
    {
        'id': 10000, 
        'feature': {
            'name': 'Michael', 
            'height': 180.3, 
            'weight': 63.7, 
            'skills': {
                'IT': ['Python', 'Golang', 'SQL'], 
                'Others': ['Chinese', 'Math']
            }
        }
    },
    {
        'id': 10001, 
        'feature': {
            'name': 'Nancy', 
            'height': 156.7, 
            'weight': 39.7, 
            'skills': {
                'IT': ['Java', 'SQL', 'JavaScript'], 
                'Others': ['Accounting']
            }
        }
    }
]

# s1 = l[0]['feature']['skills']
# s2 = l[1]['feature']['skills']

# s1a = [*s1['IT'],*s1['Others']]
# s2a = [*s2['IT'],*s2['Others']]

# for i in s1a:
#     if i in s2a:
#         print(i)

m_skill, n_skill = [d['feature']['skills']['IT'] for d in l]
# print(it_skills)
print(m_skill, n_skill)

c_skill = set(m_skill) & set(n_skill)
print(c_skill)