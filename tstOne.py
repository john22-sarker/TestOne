# Tuple
myTuple = (1,2,3,4,5,6,7,8,9)
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
