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

li = [1,2,'sdhf',3]
li1=[]
for i in li:
    li1.append(i)
print(li1,end =' ')
<<<<<<< HEAD
print(st)

print("hello world")
=======
print(st)
>>>>>>> cd521b2d9adffe19717cddc32fe29e5a02204b44
