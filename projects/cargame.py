firstin=raw_input(">")
started=False
while True:
    
    if firstin=="start":
        if started:
            print("car already startrd")
        else:
            started=True
            print("car startrd")
    elif firstin=="stop":
        if started:
            started=False
            print("car stopped")
        else:
            print("car is stopped already")
    elif firstin=="help":
        print("start,stop,quit")
    elif firstin=="quit":
        break
    firstin=raw_input(">")


