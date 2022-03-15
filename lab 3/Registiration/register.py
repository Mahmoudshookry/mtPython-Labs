
import re

emailRegex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
#


def validatename (name) :
    n = input (f"please enter your {name}: ")
    if n.isalpha() :
        return n

    else :
        return validatename (name)


def validpass () :
    p = input (f"please enter your password: ")
    if p.isalnum() :

        conf = input(f"please enter your password again : ")
        if conf==p :
            return p
        else :
            print ("you should enter the same pass ")
            validpass()
    else:
        return validpass()

# def validconfirmpass () :
#     p = input (f"please enter your password again")
#     if p.isalnum() :
#         return p
#
#     else :
#         return validpass()


def validphone () :
    phone = input ("Enter your phone number +20:  ")
    if phone.isdigit() :
        return phone

    else :
        return validphone()

# def validmail () :
#     mail = input ("Enter your mail please : ")
#     return mail

def isValidEmail():
    while True:
        email = input("Enter your Email : ")
        if re.fullmatch(emailRegex, email):
            with open("users.txt", "r") as users :
              for x in users :
                  if email!= x.split(":")[0]:
                     return email
                  else :
                    return isValidEmail()


def insert (info):
    with open ("users.txt","a") as usersfile:
        print (info)
        data=info.strip("\n")
        print(data)
        data=f"{data}\n"
        print(data)
        usersfile.write(data)



def register () :
    firstname = validatename("firstname")
    lastname = validatename("lastname")
    password = validpass()
    phonenum = validphone()
    email = isValidEmail()

    print (firstname,lastname,password,phonenum,email)
    info = [email,password,firstname,lastname,phonenum]
    userInfo = ":" .join(info)

    insert(userInfo)
    #return userInfo


