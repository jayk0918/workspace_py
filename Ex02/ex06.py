a = "orange"
b = "banana"
c = "gorilla"

print(a + b + c)
print(a, b, c)
print("orange", "banana", "gorilla")
print("orange", "banana", "gorilla", sep=",")
print("orange", "banana", "gorilla", end="===========") #end="\n"이 기본값인데 변경한 상황
print("orange", "banana", "gorilla", end="\n")

print("==="*40)

print('텍스트 입력')
text = input()
print(text)

print('숫자 입력')
print('입력: ', end = "")
num = input()
print(num)
