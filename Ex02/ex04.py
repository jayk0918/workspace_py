#set

a = {1,2,3}
print(a, type(a))
print(len(a))
print(2 in a)
print(2 not in a)


a.add(4)
print(a)

a.add(1) # 중복값 -> 적용 X
print(a)

#a.remove(3)
a.discard(3)

#a.remove(100)
a.discard(100) # 해당 값이 없어도 에러는 발생 X
print(a)

a.update({1, 1000, 2, 6}) # 중복값 적용 무시
print(a)

s1 = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
s2 = set([10, 20, 30])

print(type(s1), type(s2))

# 합집합
#s3 = s1.union(s2)
s3 = s1|s2
print(s3)

# 교집합
#s4 = s1.intersection(s2)
s4 = s1 & s2
print(s4)

# 차집합
#s5 = s1.difference(s2)
s5 = s1 - s2
print(s5)