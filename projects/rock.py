import random


options=['r','p','s']
userscore=0
computerscore=0

def rps(userscore,computerscore): 

    def check(userscore,computerguess):
        if userguess==computerguess:
            return 0 
        elif userguess=='r' and computerguess=='p':
            return False
        elif userguess=='p' and computerguess=='s':
            return False
        elif userguess=='s' and computerguess=='r':
            return False
        else:
            return True


    computerguess=options[random.randint(0,len(options)-1)]
    userguess=str(input('choose from r,p,s'))

    result=check(userscore,computerguess)

    if result==True:
        userscore+=1
        msg='userscore:{userscore} computerscore:{computerscore}'
        print(msg.format(userscore=userscore,computerscore=computerscore))
        return rps(userscore,computerscore)
    elif result==False:
        computerscore+=1
        msg='userscore:{userscore} computerscore:{computerscore}'
        print(msg.format(userscore=userscore,computerscore=computerscore))
        return rps(userscore,computerscore)
    return rps(userscore,computerscore)

rps(userscore,computerscore)


        