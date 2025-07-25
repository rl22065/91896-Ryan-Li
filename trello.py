import easygui

userExit = False 
newList = []
pageNum = 1
catergories = ["title", "description", "assignee", "status", "priority"]
memberList = []

tasks = {
    "T1": {
        "title": "Design Homepage",
        "description": "Create a mockup of the homepage",
        "assignee": "JSM",
        "priority": 3,
        "status": "In Progress"
        },
    "T2": {
        "title": "Implement Login Page",
        "description": "Create the Login page for the website",
        "assignee": "JSM",
        "priority": 3,
        "status": "Blocked"
        },
    "T3": {
        "title": "Fix Navigation Menu",
        "description": "Fix the Navigation menu to be more user-friendly",
        "assignee": "None",
        "priority": 1,
        "status": "Not Started"
        },
    "T4": {
        "title": "Add Payment Processing",
        "description": "Implement payment processing for the website",
        "assignee": "JLO",
        "priority": 2,
        "status": "In Progress"
        },
    "T5": {
        "title": "Create an About Us Page",
        "description": "Create a page with information about the company",
        "assignee": "BDI",
        "priority": 1,
        "status": "Blocked"
        },
    }

members = {
    "JSM": {
        "name": "John Smith",
        "email": "john@techvision.com",
        "tasksAssigned": ["T1","T2"]
        },
    "JLO": {
        "name": "Jane Love",
        "email": "jane@techvision.com",
        "tasksAssigned": ["T4"]
        },
    "BDI": {
        "name": "Bob Dillon",
        "email": "bob@techvision.com",
        "tasksAssigned": ["T5"]
        },
    }


def search(pageNum):
    idList = []
    userChoice = easygui.buttonbox("Where would you like to search: ",
                             choices=["Tasks", "Members"],
                             title="Search")
    if userChoice == "Tasks":
        title = "title"
        dict = tasks
    elif userChoice == "Members":
        title = "name"
        dict = members
    elif userChoice == None:
        return

    query = easygui.enterbox(f"Please enter your query",
                             title="Search").lower()
    if query == None:
        return

    for taskId in dict:        
        if query in dict[taskId][title].lower():
            newList.append(dict[taskId][title])
            if taskId not in idList:
                idList.append(taskId)
    if inputValidation(newList, list) == "error":
        return
    else:
        detailed = easygui.buttonbox(f"Results: {newList}", 
        choices=["Detailed View", "Exit"],
        title=f"Results: {len(newList)} found")
        if detailed == "Detailed View":
            for result in idList:
                if fancyOutput(dict, result, title, pageNum, idList) == "next":
                    pageNum += 1
                    pass
                else:
                    break
        else:
            pass


def updateTask(catergories):
    for i in members:
        memberList.append(members[i]["name"])
    memberList.append("None")
    taskList = []
    for i in tasks:
        taskList.append(f"{i}: {tasks[i]["title"]}")
    query = easygui.choicebox("Which task do you want to edit?",
        choices= taskList)
    field = easygui.choicebox("Which catergory would you like to edit?",
        choices= catergories)
    if field in ["title","description"]:
        value = ":3"
        while inputValidation(value, field) != "alg":                    
            value = easygui.enterbox(f"Please enter the new {field}: ")
    elif field == "assignee":
        value = easygui.choicebox("Please assign a new member: ",
        choices=memberList)
    elif field == "status":
        value = easygui.choicebox("Please assign a status: ",
        choices=["In Progress", "Not Started", "Blocked"])
    elif field == "priority":
        value = ":3"
        while inputValidation(value, field) != "alg":
            try:
                value = int(easygui.enterbox("Please assign \
a new priority: "))
            except ValueError:
                easygui.msgbox(f"{field.upper()} must be an integer!",
                    title="Error !!")
    taskId = query.split(":")[0].strip()
    tasks[taskId][field] = value

    
def addTask(catergories):
    for i in members:
        memberList.append(members[i]["name"])
    memberList.append("None")
    newTask = {}
    value = ":3"
    for field in catergories:
        if value != None:
            if field in ["title","description"]:
                value = ":3"
                while inputValidation(value, field) != "alg":                    
                    value = easygui.enterbox(f"Please enter the {field}: ")
            elif field == "assignee":
                value = easygui.choicebox("Please assign the task: ",
                choices=memberList)
            elif field == "status":
                value = easygui.choicebox("Please assign a status: ",
                choices=["In Progress", "Not Started", "Blocked"])
            elif field == "priority":
                value = ":3"
                while inputValidation(value, field) != "alg":
                    try:
                        value = int(easygui.enterbox("Please assign \
a priority: "))
                    except ValueError:
                        easygui.msgbox(f"{field.upper()} must be an integer!",
                            title="Error !!")
                    except TypeError:
                        return
        else:
            return
        newTask[field] = value
    taskId = f"T{len(list(tasks)) + 1}"
    tasks[taskId] = newTask
    easygui.msgbox("New task has been added")
    

def report(pageNum):
    noBlocked = []
    noInProgress = []
    noNotStarted = []

    for taskId in tasks:
        if tasks[taskId]["status"] == "Blocked":
            noBlocked.append(tasks[taskId]["title"])
        elif tasks[taskId]["status"] == "In Progress":
            noInProgress.append(tasks[taskId]["title"])
        elif tasks[taskId]["status"] == "Not Started":
            noNotStarted.append(tasks[taskId]["title"])
    choice = easygui.buttonbox(f"Total tasks: {len(tasks)} \n"
                        f"Blocked: {len(noBlocked)} \n"
                        f"In Progress: {len(noInProgress)} \n"
                        f"Not Started: {len(noNotStarted)} \n",
                        title="Report", choices=["Blocked",
                                                "In Progress",
                                                "Not Started",
                                                "Exit"])
    if choice == "Blocked":
        if noBlocked == []:
            easygui.msgbox("No tasks are blocked at the moment",
                title="Report")
        else:
            if fancyOutput(tasks, taskId, "title", pageNum, noBlocked) == "next":
                pageNum += 1
                pass
            else:
                return
    elif choice == "In Progress":
        if noInProgress == []:
            easygui.msgbox("No tasks are in progress at the moment",
                title="Report")
        else:
            if fancyOutput(tasks, taskId, "title", pageNum, noInProgress) == "next":
                pageNum += 1
                pass
            else:
                return
    elif choice == "Not Started": 
        if noNotStarted == []:
            easygui.msgbox("No tasks have not been started at the moment",
                title="Report")
        else:
            if fancyOutput(tasks, taskId, "title", pageNum, noNotStarted) == "next":
                pageNum += 1
                pass
            else:  
                return
    else:
        return


def varReset(newList, memberList, pageNum):
    newList = []
    memberList = []
    pageNum = 1
    return newList, memberList, pageNum

def inputValidation(value, field):
    if field in ["title","description"]:
        if value == None:
            return "alg"
        elif value.strip() == "":
            easygui.msgbox(f"{field.upper()} cannot be empty!",
                title="Error !!")
            return "error"
        elif value == ":3":
            return "error"
        else:
            return "alg"
    elif field == "priority":
        if value == ":3":
            return "error"        
        elif value == None:
            return "alg"
        elif not type(value) is int:
            easygui.msgbox(f"{field.upper()} must be an integer!",
                title="Error !!")
            return "error"
        elif int(value) < 0 or int(value) > 3:
            easygui.msgbox(f"{field.upper()} must be between 1 and 3!",
                title="Error !!")
            return "error"
        else:
            return "alg"
    elif field == list:
        if value == []:
            easygui.msgbox("No results found, are you sure \
you typed everything in correctly?",
                title="Error !!")
            return "error"
        else:
            return "alg"





def fullOutput(pageNum):
    taskList = []
    for taskId in tasks:
        taskList.append("")
    for taskId in tasks:
        if fancyOutput(tasks, taskId, "title", pageNum, taskList) == "next":
            pageNum +=1
            pass
        else:
            break

def fancyOutput(dict, primaryKey, title, pageNum, list):
    output = [f"{primaryKey}: {dict[primaryKey][title]}"]
    

    for key, value in dict[primaryKey].items():
        output.append(f"{key}: {value}")
        
    choice = easygui.buttonbox("\n".join(output), 
                        title=f"{pageNum} of {len(list)}",
                        choices=["Next", "Exit"])
    if choice == "Next":
        return "next"
    elif choice is None or choice == "Exit":
        return "exit"
        

while userExit != True:
    newList, memberList, pageNum = (
        varReset(newList, memberList, pageNum))
    menu = easygui.choicebox("What would you like to do: ", 
                             choices=["Search", "Update Task",
                                       "Report", "New Task",
                                       "Task Collection"],
                             title="Menu")
    if menu == "Search":
        search(pageNum)

    elif menu == "Update Task":
        updateTask(catergories)

    elif menu == "Report":
        report(pageNum)

    elif menu == "New Task":
        addTask(catergories)

    elif menu == "Task Collection":
        fullOutput(pageNum)

    elif menu is None:
        break