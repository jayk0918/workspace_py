num = input('숫자 입력 : ')
num = int(num)
if num > 0:
    if num % 2 == 0:
        print('짝수')
    else:
        print('홀수')
elif num < 0:
    print('음수')
else:
    print('0')