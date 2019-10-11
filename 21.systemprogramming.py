import os
import platform
#waits for a keystroke without return statement
def getch():
    os.system("bash -c \"read -n 1\"")
print('type any key')
getch()

#different code for different platforms

def plat():
    if(platform.system()=='Windows'):
        print('you are in windows')
    elif(platform.system()=='Linux'):
        print('you are in linux')

plat()