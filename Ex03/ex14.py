x = 1

def function(a):
    global x
    x = 100
    return a + x

print(function(11))
print(x)