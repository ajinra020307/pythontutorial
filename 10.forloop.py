for char in "ajin":
    print(char)
for char in ["ajin","a","aj"]:
    print(char)

#range range(start,end,inc)

for char in range(0,20,1):
    print(char)


#nested loop

for x in range(0,5,1):
    for y in range(0,5,1):
       print(x,y)

#print f
a=[5,2,5,2,2]
for char in a:
    print("x" * char)