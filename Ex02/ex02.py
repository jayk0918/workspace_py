# tuple

t = (1, 2, 3)
#t = 1, 2, 3
#t = tuple([1,2,3])
print(t, type(t))

#i = (1) # 1개짜리는 int로 인식함
i = (1,) #1,로 튜플로 인식시키기 가능
print(i, type(i))

print("==="*40)

t = (1, 2, 'python')
print(t, type(t))

print(t[0], t[1], t[2], t[-1], t[-2])
print(t[1:3])
print(t[:])

ttt = t * 3
print(ttt)

print(t + (3, 4, 5))
print(t)

t = t + (3, 4, 5)
print(t)
print(len(t))

print(20000 in t)

print(t[0] + 1003)

