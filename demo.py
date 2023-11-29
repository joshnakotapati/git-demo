import re
st = "this is string"
x = re.findall('is',st)
y = re.search('/s',st)
z = re.split('/s',st)
print(x)
print(y)
print(z)

s = "testing the string"
print(s.count('t'))
print(s.capitalize())
for i in s:
    if i == 'i':
        continue
        print(s)