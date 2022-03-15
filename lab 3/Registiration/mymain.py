from register import *
from login import *



print ("..........Hello kind user.............")
print(".........please login to connect..........")


def main() :
    print ("please login or Register (for login press l) and (for Register press r)")
    x= input ("Enter here :")
    if x=="l" or x=="r" :
        if x=="l" :
            return login()
        else :
            return register()

    else :
        main()

main()
