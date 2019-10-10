import random

guess=random.randint(1,5)
x=input('enter your guess')

while x!=guess:
    x=int(input('wrong,,enter your guess'))
else:
    print('you are right')
