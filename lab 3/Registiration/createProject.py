import re
dateRegex = re.compile(r'^\d{4}\-(0[1-9]|1[012])\-(0[1-9]|[12][0-9]|3[01])$')




def validateTitle():
    p = input(f"please enter project name: ")
    if p.isalnum():
        return p

    else:
        return validateTitle()


def validateDetails():
    d = input(f"please enter project Details: ")
    if d.isalnum():
        return d

    else:
        return validateDetails()


def validateTarget():
    t = input("Enter Target :  ")
    if t.isdigit():
        return t

    else:
        return validateTarget()




def validateStartDate():
    while True:
        startdate = input("Enter satart date : ")
        if re.fullmatch(dateRegex, startdate):
            return startdate

def validateEndDate():
        Enddate = input("Enter End date : ")

        if re.fullmatch(dateRegex, Enddate):
           return Enddate


def insertProjects (info):
    with open ("projects.txt","a") as projectsfile:
        data=info.strip("\n")
        data=f"{data}\n"
        projectsfile.write(data)


def create (email):
    title = validateTitle()
    details = validateDetails()
    totaltarget= validateTarget()
    startdate = validateStartDate()
    EndDate= validateEndDate()

    info = [title, details, totaltarget,startdate,EndDate,email]
    projectInfo = ":".join(info)
    insertProjects(projectInfo)



