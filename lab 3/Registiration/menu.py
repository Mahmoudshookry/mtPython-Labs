from createProject import *
def Menu (email):
    print ("please select from optinos : create     list    edit    delete")
    choose = input("Enter your choice : ")

    if choose == "create":
        create(email)

    if choose == "list":
         list()


    if choose == "edit":
        print(0)

    if choose == "delete":
        projectname= input("please enter project name : ")
        delete(email,projectname)


def list ():
    with open("projects.txt", "r") as projectsfile:
        for x in projectsfile:
            print(x)
mylist=[]
# def delete(email,title):
#     with open("projects.txt", "r") as projectsfile:
#         projects=projectsfile.readlines()
#         for p in projects:
#             lsp=":".join(p)
#             if lsp[0]==title:
#                 if lsp[5]==email:
#                     projects.remove(p)
#                     replaceChanges(projects)
#                     projectsfile.close()
#                 else:
#                   print("hhhhhhhhh")
#             else:
#                 print(f"{title} project doesnt exist")
#         print (mylist)

# def replaceChanges(projects):
#     with open ("projects.txt", "w") as projectsfile:
#         #data=projects.strip("\n")
#         data = projects
#         data=f"{data}\n"
#         projectsfile.write(data)

def delete(email,title):
    #print(email,title)
    with open("projects.txt", "r+") as projectsfile:
        projects=projectsfile.readlines()
        for p in projects:
            print (p)
            lsp = p.split(":")
            z=lsp[5].strip("\n")
            print(lsp)
            if lsp[0] == title and z == email:
                print(1111111111111)

                projects.remove(p)

          #  else:

                 # print("not valid data")
        #projectsfile.close()
        replaceChanges(projects)
        # projectsfile.close()
        #else:
               # print(f"{title} project doesnt exist")
       # print (mylist)

def replaceChanges(projects):

    for x in projects:
        print(x)
        projectInfo=x
       # projectInfo = ":".join(x)
       # print (projectInfo)
        projectInfo = projectInfo.strip("\n")
        projectInfo = f"{projectInfo}\n"

    with open("projects.txt", "w") as projectsfile:

        for y in projects:
           print(y)
           projectsfile.write(y)

    #projectsfile.close()

          #  data = projects.strip("\n")

#        projectsfile.write(projects)
