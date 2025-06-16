import easygui

userExit = False 

task = {
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

member = {
    "JSM": {
        "name": "John Smith",
        "email": "john@techvision.com",
        "tasks assigned": ["T1","T2"]
        },
    "JLO": {
        "name": "Jane Love",
        "email": "jane@techvision.com",
        "tasks assigned": ["T4"]
        },
    "BDI": {
        "name": "Bob Dillon",
        "email": "bob@techvision.com",
        "tasks assigned": ["T5"]
        },
    }

def search():
    pass

def updateTask():
    pass

def report():
    pass

def output():
    pass

while userExit != True:
    menu = easygui.choicebox("What would you like to do: ", 
                             choices=["Search", "Update Task", "Report", "New Task"])