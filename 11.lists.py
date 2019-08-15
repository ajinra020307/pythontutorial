a=[4,5,3,3]

#to acess individualvalues
print(a[3])
#print ffrom 1 to end
print(a[1:])
#print 1 t0 3
print(a[1:4])
#changin an array value
a[3]=44


#calculating sum
lis=[34,89,89]
sum=0
for char in lis:
    sum+=char
print(sum)

#find largest number in an array
max=0
for char in a:
    if char>max:
        max=char

print(max)

#two dimensional list

aa=[[1,2,3],[4,5,6],[7,89,9]]
#access values from array
print(aa[0][2])

#looping two dimensional array
for row in aa:
    for num in row:
        print(num)

#array properties and methods
k=[1,4,4,5,6]
#adding a value to end of an array
k.append(7)
print(k)
#adding value to any index of an array
k.insert(2,444) #insert(indexno,value)
print(k)
#removing a value from an array
k.remove(444)
print(k)
#remove all values in an array
k.clear()
print(k)