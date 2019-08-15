course="python's for beginners"
course='python for "beginners"'
course='''hello student's"how are you"'''
#prints first element
print(course[0])
#print second from last
print(course[-2])
# print 0-4 
print(course[0:5])
#print from3 to end
print(course[3:])
# print from start to 10
print(course[:10])
#clones a string
another=course[:]
print(another[1:-1])

print(len(another))
#change to upper
print(another.upper())
#change to lower
print(another.lower())
#find returnd the index of character
print(another.find("a"))
print(another.find("how"))
#in returns a boolean value based on the results
print("how" in another)
#replace replaces a character with another
print(another.replace("s","h"))
