from menu import *
def checkuser(mail,paswo):
    with open ("users.txt") as users :
        data = users.readlines()
        for user in data :
            #print(user)
            # user=user.strip("\n")
            user_info = user.split(":")
            #print(user_info)
            if user_info[0] == mail and user_info[1]==paswo :
                 return True
    return False




def login () :

    email= input ("please enter your mail :  ")
    password = input ("please enter your password : ")

    if checkuser(email,password) :
        print("logged in successfully")
        Menu(email)

    else :
        print ("please enter valid information")
        return login()
