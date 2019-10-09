s={1,2,2,3,2,4}
#add new elements
s.add(5)
print(s)

for value in s:
    print(value)
#adding more elements
s.update([3,2,3,2,2,6,7,8])
print(s)

#removing elements
s.remove(2)
s.discard(2)

#remove last element
s.pop()
#clears the set
s.clear()
#delete the set
del s

s1={1,2}
s2={3,4}

s3=s1.union(s2)
s3.update(s1)
print(s3)