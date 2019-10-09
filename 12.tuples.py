#tuples are similar to arrays but cannot br changed
thistuple = ("apple", "banana", "cherry")
thistuple2=(2,3,4)
print(thistuple)
print(thistuple[2])
print(thistuple[-2])
print(thistuple[0:2])

print('apple' in thistuple)
print(len(thistuple))

#returns a new tuple
print(thistuple+thistuple2)
for value in thistuple:
    print(value)
