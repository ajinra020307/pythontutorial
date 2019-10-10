import random

numbers=[]
allowedoriginal=[]
allowed=[]

def makestructure(array):
    for num in range(0,9):
        array.append([])
        allowed.append(num+1)
        allowedoriginal.append(num+1)

makestructure(numbers)
print(numbers)

def makefirstset(array,allowed,min,max):
    for num in range(min,max):
        for n in range(min,max):
            randomnum=allowed[random.randint(0,len(allowed)-1)]
            allowed.remove(randomnum)
            array[num].append(randomnum)

makefirstset(numbers,allowed,0,3)
print(numbers)
allowed=allowedoriginal[:]

def makesecondset(array,allowed,min,max):
     for num in range(min,max):
        for n in range(min,max):
            randomnum=allowed[random.randint(0,len(allowed)-1)]
            allowed.remove(randomnum)
            array[num].append(randomnum)

makesecondset(numbers,allowed,0,3)
print(numbers)
allowedoriginal=allowedoriginal[:]
