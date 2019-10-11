numbers=[]
def createnumlist(array):
    for num in range(0,101):
        if num%2==0:
            array.append(num)


createnumlist(numbers)
print(len(numbers))
usernumber=int(input('Enter a number between 0 and 100'))

def search(userinput,array):
    print(array)
    if len(array)>1:
        halfnum=len(array)//2
        firstarray=array[:halfnum]
        secondarray=array[halfnum:]
        if(userinput in firstarray):
            return search(userinput,firstarray)
        elif(userinput in secondarray):
            return search(userinput,secondarray)
        else:
            print('not found')

search(usernumber,numbers)