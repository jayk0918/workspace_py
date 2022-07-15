temp = 23
str = '현재온도는 %d도 입니다.'%temp
print(str)

str2 = '오늘은 %s년 %d월 %d일 입니다.'%('2022', 7, 15)
print(str2)

print('올해 %d살이오'%5)

area = 24.9928
print('원의 넓이 %f'%area)

print('오늘 %10d도 이올시다'%temp)
print('오늘 %-10d도 이올시다'%temp)
print('원의 넓이는 %35.4f 이오'%area)
print('원의 넓이는 %-35.4f 이오'%area)

print('수수료는 %d%%이다'%30)
print("==="*40)

age = 30
print('올해 {0}살이다.'.format(22))
print('올해 {0}살이다.'.format("33"))
print('올해 {0}살이다.'.format(age))

print('오늘은 {0}년 {1}월 {2}일 입니다.'.format("2022", 3, 5))
print('오늘은 {year}년 {month}월 {day}일 입니다.'.format(year = 2022, month = '8', day = 15))
print("==="*40)

print('오늘은 {0:>10}년 {1:<10}월 {2:^10}일 입니다.'.format("2022", 3, 5))