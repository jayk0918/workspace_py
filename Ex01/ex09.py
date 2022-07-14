s = ''
str1 = 'hello world'
str2 = "안녕 세상"
print(type(s), type(str1), type(str2), sep=",")
print(isinstance(str2, str))

print(2, 4, 6, sep="!")

print("==="*40)

s01 = 'aaa'
s02 = 'aaa'

print(id(s01))
print(id(s02))

s01 = 'aaaa'
s02 = 'cccc'
print(id(s01))
print(id(s02))

print("==="*40)

str = "돌리\n도트"
str2 = """ABCDEFG abcdef
가나다라마 123456789"""
print(str)
print(str2)

print("==="*40)

print("hello\nworld\nbut\n'no welcome'")

print("==="*40)

print("hello world\rbut 'no welcome'")



