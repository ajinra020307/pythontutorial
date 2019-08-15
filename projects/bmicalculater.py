def calculatebmi():
    h=int(input("enter height in cms,eg:176:"))
    w=int(input("enter weight in kgs,eg:66:"))
    hh=h*h
    bmi=w/hh
    print("your bmi is ", bmi)

calculatebmi()
