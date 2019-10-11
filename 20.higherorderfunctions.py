#map

a=[1,2,3,4]
squared=list(map(lambda x:x*x,a))
print(squared)


from functools import reduce
#reduce
sum = reduce((lambda x, y: x + y), a) 
print (sum) 

#filter

filtered=list(filter(lambda x:x>2,a))
print(filtered)