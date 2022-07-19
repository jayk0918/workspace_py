for x in range(10):
    print(x, end="")

print('')
print("===" * 40)

for x in range(0, 10, 2):
    print(x, end="")

print('')
print("===" * 40)

for x in range(5, -6, -1):
    print(x, end="")

print("===" * 40)

print('단을 입력하세요 : ', end='')

num = int(input())

for i in range(1, 10):
    print('{0} * {1} = {2}'.format(num, i, num*i))


