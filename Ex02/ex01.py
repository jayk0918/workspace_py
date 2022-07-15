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