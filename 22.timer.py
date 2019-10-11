from threading import Timer
def prin():
    print('i will print after 4sec')

x=Timer(2.0,prin,args = None, kwargs = None)
Timer.start(x)
#to cancel a timer
#Timer.cancel(x)




    