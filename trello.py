import easygui

userExit = False 
newlist = []

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
    
    input = (easygui.choicebox("Where would you like to search: ",
                             choices=["Tasks", "Members"])).lower
    if input == "tasks":
        title = "title"
        dict = tasks

    elif input == "members":
        title = "name"
        dict = members
    collectInput()    
    for id in dict:
        if collectInput in dict[id][title].lower():
            newlist.append(dict[id][title])
    easygui.msgbox(f"results: {newlist}" )

def updateTask():
    pass

def report():
    pass

def output():
    pass

def newTask():
    pass

def collectInput():
    search = easygui.enterbox((f"Please enter your query")).lower
    return search

while userExit != True:
    menu = easygui.choicebox("What would you like to do: ", 
                             choices=["Search", "Update Task",
                                       "Report", "New Task"])
    if menu == "Search":
        search()

    elif menu == "Update Task":
        updateTask()

    elif menu == "Report":
        report()

    elif menu == "New Task":
        newTask()

    elif menu is None:
        break