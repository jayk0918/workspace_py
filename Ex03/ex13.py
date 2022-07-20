def plus(a, b):
    sum = a + b
    return sum


result = plus(3, 7)
print(result)

'''
result = plus(3, '한글')
print(result)
'''

print('===' * 40)


def my_function():
    print('yellow')


my_function()
print(type(my_function()))


def noMsg():
    pass


print(noMsg())

print('===' * 40)


def sum_and_mul(a, b):
    sum = a + b
    mul = a * b
    return sum, mul


num1, num2 = sum_and_mul(3, 7)
print(num1)
print(num2)

result = sum_and_mul(3, 7)
print(result, type(result))
print(result[0])
print(result[1])

print('===' * 40)


def plusPrint(a=100, b=100):
    print('a=%d, b=%d, 합은 %d' % (a, b, a + b))


plusPrint(2, 7)
plusPrint(7)
# plusPrint(,7)
plusPrint(b=70)
plusPrint(a=2, b=8)

print('===' * 40)


def sum_many(*data):
    data = (1, 2, 3, 4, 5)
    sum = 0
    for num in data:
        sum = sum + num

    return sum


print(sum_many(1, 2, 3, 4, 5, 6, 7, 8, 9))

print('===' * 40)


def sum_mul(mode, *args):
    if mode == 'sum':
        result = 0
        for i in args:
            result = result + i
    elif mode == 'mul':
        result = 1
        for i in args:
            result = result * i
    else:
        result = '오류'

    return result

print(sum_mul("sum", 1, 2))
print(sum_mul("mul", 6, 7, 8, 9))

print('===' * 40)

def addPerson(*hp, **kwargs):
    print(hp)
    print(kwargs)

addPerson('010-222-3333', name = '돌리', age = 22)
addPerson('010-222-3333', '010-888-9999', name = '도트', age = 22)
