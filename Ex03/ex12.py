count = 0
result = 0
while count <= 10:
    result += count
    count += 1

print(result)

i = 0
while True:
    i += 1
    if i % 6 == 0 and i % 14 == 0:
        break

print(i)
