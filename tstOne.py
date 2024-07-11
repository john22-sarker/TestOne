# Tuple
myTuple = ('One',2,'three',4,5,6,7,8,9,'ten')
print(type(myTuple))

print(myTuple[:])
x = list(myTuple)
print(type(x))
x.append(0)
myTuple = tuple(x)
print(myTuple)
print(type(myTuple))

# Unpack tuple
(a,b,*c) = myTuple
print(a)
print(c)
print(b)

# Tuple loops
for i in myTuple:
    print(i)

for j in range(len(myTuple)):
    print(myTuple[j])