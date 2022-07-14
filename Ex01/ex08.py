#확장 연산자
x = 2
x += 5

print(x)

x -=3

print(x)

x**=3

print(x)

print("==="*40)


# 관계 연산자

print(1 > 3)
print(2 < 4)
print(4 <= 5)
print(4 >= 5)
print(6 == 9)
print(6 != 9)

print("==="*40)

a= 6
print(0 < a < 10)
print(0 < a and a < 10)

print("==="*40)

a = 10
b = 20
c = a
d = 10
print(a == b)
print(a is b)
print(a is c)

print("==="*40)

print(id(a))
print(id(b))
print(id(c))
print(id(d))

print("==="*40)

# 논리 연산자
print(True and True)
print(True and False)
print(False and False)
print(True or True)
print(True or False)
print(False or False)
print(not True)
print(not False)

print("==="*40)

print(abs(-3)) # 절대값
print(int(3.1415)) # 정수형
print(float(3)) # 실수형
print(complex(3)) # 복소수형
print(pow(2, 10)) # 승수계산
