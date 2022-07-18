print("리스트 기본")

testList = [1, 2, 'python']
print(testList)
print(testList[0])

print(testList[-1])
print(testList[-2])

tList = testList[1:3]
print(tList)
print(testList[1:3])

print(tList*2)
print(len(tList + [3, 4, 5]))
print(len(tList))

print("python" in tList)
print("dolly" in tList)
print(3 in tList)

print("===" * 40)

a = ['apple', 'banana', 10, 20]
a[2] = a[2] + 20
print(a)

print("===" * 40)

cList = [1, 12, 123, 1234]
cList[0:2] = []
print(cList)

print("===" * 40)

dList = [1, 12, 123, 1234]
dList[0:1] = 'a'
print(dList)
dList[4:] = [12345]
print(dList)
dList[:0] = [12, -1, 0]
print(dList)

print("===" * 40)

b = [1, 123, 1000, 12, 1000]
print(b)

#b.insert(5,[1,2,3])
#print(b)
print(len(b))
print(b.count(1000))

b.reverse()
print(b)

b.sort()
print(b)

print(b.index(1000)) # 여러 개의 같은 값이면 맨 앞 값을 표시
