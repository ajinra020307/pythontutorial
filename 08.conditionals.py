x=20
y=30

if x>20:
    print("x is greater than 20")
elif x<20:
    print("x is less than 20")
else:
    print("x is equal to 20")

if x>10 and y>10:
    print("x and y greater than 10")
elif x<10 or y<10:
    print("x or y lesser than 10")
else:
    print("x and y are not in same range")

name="ajin"

if len(name)>6:
    print("good")
elif len(name)<6:
    print("name must be 6 character")

weight=int(input("enter your weight? "))
unit=raw_input("L for lbs or k for kg")
if unit=="l":
    print(weight*30)
else:
    print(weight*1.6)
