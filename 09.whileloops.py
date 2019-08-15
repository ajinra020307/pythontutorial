x=1
while x<=20:
    print("*" * x)
    x+=1

cguess=3
i=1
while i<=3:
    uguess=input("guess")
    if uguess==cguess:
        print("you guessed it")
    i+=1
else:
    print("loop runned without any break")
