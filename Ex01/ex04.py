a = 101
print(a, type(a))
print(isinstance(a, int))

#2진수 8진수 16진수 표현 가능 -> 선언하지 않을 경우 10진수로 연산
b = 0b101 #2진수
c = 0o101 #8진수
d = 0x101 #16진수

print (b, c, d)
print (b + c + d)

#10진수 -> 2진수, 8진수, 16진수
print(bin(5))
print(oct(8))
print(hex(257))

e = 2**1024
print(type(e))
print(e)