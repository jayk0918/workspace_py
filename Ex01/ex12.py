s = 'i like Deep Dark Color'

print(s.upper())
print(s.lower())
print(s.swapcase())
print(s.capitalize())
print(s.title())
print(s*3)
print(s+s)

print("==="*40)

s = 'I Like Python I Also Like Java'
print(s.find("Like"))
print(s.find("JS"))
print(s.find("Like",5))

print(s.rfind('Like'))

print(s.index("Also"))

print(s.startswith("I Like"))
print(s.startswith("I"))
print(s.startswith("I Also"))

print(s.endswith("Java"))
print(s.endswith("Like Java"))
print(s.endswith("java"))

print("==="*40)

s = '   dolly and dott  '
print(s)
print(s.strip())
print(s.rstrip())
print(s.lstrip())

s = '<><abc><><defg><><>'
print(s.strip('<>'))

s = '   dolly and dott  '
print(s.replace('dolly', 'patt'))

s = 'king and queen'
print(s.center(60))
print(s.center(60, '-'))
print(s.ljust(60, '-'))
print(s.rjust(60, '-'))

print("==="*40)

print('1234'.isdigit()) # True
print('abcd'.isalpha()) # True
print('12.34'.isdigit()) # False
print('1234'.isalpha()) # False
print('abcd'.isdigit()) # False
print('abcd'.islower()) # True
print('ABCD'.isupper()) # True
print('\n\n'.isspace()) # True
print(' '.isspace()) # True
print(''.isspace()) # False
print('    \t     '.isspace()) # True

print('20'.zfill(10))
print('1234'.zfill(10))




