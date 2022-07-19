'''
aList = ['개', '돼지', '호랑이']

for name in aList:
    print(name)
'''

friendList = [('둘리', 10), ('마이콜', 20), ('도우넛', 30)]

for person in friendList:
    print('이름 : {0}, 나이 : {1}'.format(person[0], person[1]))


print('===' * 40)

for name, age in friendList:
    print('이름 : %s, 나이 : %d' %(name, age))

print('===' * 40)

for i in range(0, 2):
    name = friendList[i][0]
    age = friendList[i][1]
    print('이름 : %s, 나이 : %d' % (name, age))
