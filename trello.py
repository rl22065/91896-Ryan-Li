import easygui

userExit = False 
newlist = []
idList = []
pageNum = 1

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

def search():
    
    userChoice = easygui.buttonbox("Where would you like to search: ",
                             choices=["Tasks", "Members"])
    if userChoice == "Tasks":
        title = "title"
        dict = tasks
    elif userChoice == "Members":
        title = "name"
        dict = members

    query = easygui.enterbox(f"Please enter your query")
    for id in dict:
        if query in dict[id][title].lower():
            newlist.append(dict[id][title])
            if id not in idList:
                idList.append(id)
    if newlist == []:
        easygui.msgbox("No results found, are you sure \
you typed everything in correctly?")
    else:
        detailed = easygui.buttonbox(f"results: {newlist}", 
        choices=["Detailed View", "Exit"])
        if detailed == "Detailed View":
            for result in idList:
                if fancyOutput(dict, result, title) == "next":
                    pass
                else:
                    break
        else:
            pass


def updateTask():
    pass

def report():
    pass

def fancyOutput(dict, primaryKey, title):
    output = [f"{dict[primaryKey][title]}"]
    

    for key, value in dict[primaryKey].items():
        output.append(f"{key}: {value}")
        
    choice = easygui.buttonbox("\n".join(output), 
                        title=f"{1} of {len(idList)}",
                        choices=["Next", "Exit"])
    if choice == "Next":
        return "next"
    elif choice is None or choice == "Exit":
        return "exit"
        

    

def newTask():
    pass


while userExit != True:
    menu = easygui.choicebox("What would you like to do: ", 
                             choices=["Search", "Update Task",
                                       "Report", "New Task"])
    if menu == "Search":
        newlist = []
        idList = []
        pageNum = 1
        search()


    elif menu == "Update Task":
        updateTask()

    elif menu == "Report":
        report()

    elif menu == "New Task":
        newTask()

    elif menu is None:
        break