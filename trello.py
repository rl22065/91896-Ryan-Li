import easygui

userExit = False 
newList = []
pageNum = 1
catergories = ["title", "description", "assignee", "status", "priority"]
memberList = []
MINPRIORITY = 1
MAXPRIORITY = 3


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
    """Searches through the tasks or members dictionaries based on user input.
    Prompts the user for a query and displays results. The user can choose
    to view detailed information about each result.
    """

    idList = []

    # Easygui buttonbox to choose between searching tasks or members.
    # Changes the title and dict variable based on user choice.
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
    # Easygui enterbox to get the search query from the user.
    # If the user cancels, the function returns.
    # AttributeError is raised if the user cancels the input box.
    try: 
        query = ":3"
        while inputValidation(query, str) != "alg":
            query = easygui.enterbox(f"Please enter your query",
                                        title="Search").lower()
    except AttributeError:
        return
    
    # Append the query to the newList and idList if it matches.
    for taskId in dict:        
        if query in dict[taskId][title].lower():
            newList.append(dict[taskId][title])
            if taskId not in idList:
                idList.append(taskId)
    if inputValidation(newList, list) == "error":
        return
    else:
        # Display the results in a buttonbox, with the option to view. 
        # details or exit.
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
    """Updates a task in the tasks dictionary, prompting the user   
    for the task to update and the field to edit. Uses while loops
    and an input validation function to ensure valid inputs.
    """

    taskList = []
    memberIdList = []

    # Creates the list to iterate through, is created at the start of 
    # the function to ensure it is always up to date.
    for i in members:
        memberIdList.append(i)
        memberList.append(members[i]["name"])
    memberList.append("None")
    for i in tasks:
        if tasks[i]["status"] != "Completed":
            taskList.append(f"{i}: {tasks[i]["title"]}")

    # Easygui choiceboxes to choose which task to edit and its field.
    query = easygui.choicebox("Which task do you want to edit?",
        choices= taskList)
    if query is None:
        return
    field = easygui.choicebox("Which catergory would you like to edit?",
        choices= catergories)
    if field is None:
        return
    # If and elif statements to determine which field to edit
    # and prompt the user for the new value.
    # Uses ":3" as a placeholder and to avoid errors.
    if field in ["title","description"]:
        value = ":3"
        # Uses a while loop to ensure the user inputs a valid value.
        while inputValidation(value, field) != "alg":
            value = easygui.enterbox(f"Please enter the new {field}: ")
    elif field == "assignee":
        value2 = easygui.choicebox("Please assign a new member: ",
        choices=memberList)
        # If the user selects a member, we set the value to their ID.
        # If the user selects "None", we set the value to "None".
        if value2 != "None":
            value = memberIdList[memberList.index(value2)]
        else:
            value = value2
    elif field == "status":
        value = easygui.choicebox("Please assign a status: ",
        choices=["In Progress", "Not Started", "Blocked", "Completed"])
    elif field == "priority":
        value = ":3"
        while inputValidation(value, field) != "alg":
            try:
                value = int(easygui.enterbox("Please assign \
a new priority: "))
            # Value error because we force the user to input an int.
            # This can't be caught by the inputValidation function 
            # so we catch it here and display an error message.
            except ValueError:
                easygui.msgbox(f"{field.upper()} must be an integer!",
                    title="Error !!")
            # Type error because we force the user to input an int.
            # If the user cancels we would get a TypeError.
            # This isn't caught by the inputValidation function as we 
            # can't validate the input before it is entered.
            except TypeError:
                return
    taskId = query.split(":")[0].strip()
    if value != "None" and field == "assignee":
        for i in members:
            # If the task is already assigned to a member, we remove it 
            # from their tasksAssigned list.
            if taskId in members[i]["tasksAssigned"]:
                members[i]["tasksAssigned"].remove(taskId)
        # Then we add the task to the new member's tasksAssigned list.
        members[value]["tasksAssigned"].append(taskId)
    elif value == "Completed":
        # If the task is completed, we remove it from the tasksAssigned 
        # list of the member who was assigned to it.
        for i in members:
            if taskId in members[i]["tasksAssigned"]:
                members[i]["tasksAssigned"].remove(taskId)
    tasks[taskId][field] = value


def addTask(catergories):
    """Adds a new task to the tasks dictionary,
    prompting the user for each field. Uses while loops
    and the input validation function to ensure valid inputs.
    """

    memberIdList = []
    # Creates a list of members to assign the task to.
    for i in members:
        memberList.append(members[i]["name"])
        memberIdList.append(i)
    # Adds "None" to the list to allow for no assignee.
    memberList.append("None")
    newTask = {}
    value = ":3"
    # Iterates through the catergories and prompts the user for each 
    # field. Uses ":3" as a placeholder to avoid errors.
    # Uses the inputValidation function to ensure valid inputs.
    # If the user cancels, the function returns.
    for field in catergories:
        if value != None:
            if field in ["title","description"]:
                value = ":3"
                while inputValidation(value, field) != "alg":                    
                    value = easygui.enterbox(f"Please enter the {field}: ")
            elif field == "assignee":
                value = easygui.choicebox("Please assign the task: ",
                choices=memberList)
                assignee = value
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
                    # Value error because we typecast the user input to
                    # an int this can't be caught by the inputValidation 
                    # function,
                    # so we catch it here and display an error message.
                        easygui.msgbox(f"{field.upper()} must be an integer!",
                            title="Error !!")
                    # If the user cancels we would get a TypeError
                    # so we catch it and return.
                    except TypeError:
                        return
        else:
            return
        newTask[field] = value
    taskId = f"T{len(list(tasks)) + 1}"
    tasks[taskId] = newTask
    # If the assignee is not "None", we add the task to their
    # tasksAssigned list.
    if newTask["assignee"] != "None":
        index = memberList.index(assignee)
        members[memberIdList[index]]["tasksAssigned"].append(taskId)
    easygui.msgbox("New task has been added")
    

def report(pageNum):
    """Displays all the status of the tasks in a report, 
    with the option to view details of each task.
    Starts by displaying the total number of tasks and their statuses.
    The user can choose to view tasks that are blocked, in progress, 
    or not started. Uses the fancyOutput function to display each task's 
    details. If there are no tasks in a category, it displays a message.
    """

    # Creates lists to hold tasks based on their status
    # and a boolean to exit the report loop.
    noBlocked = []
    noInProgress = []
    noNotStarted = []
    noCompleted = []
    reportExit = False
    # Iterates through the tasks dictionary and appends the task title
    # to the appropriate list based on status.
    for taskId in tasks:
        if tasks[taskId]["status"] == "Blocked":
            noBlocked.append(tasks[taskId]["title"])
        elif tasks[taskId]["status"] == "In Progress":
            noInProgress.append(tasks[taskId]["title"])
        elif tasks[taskId]["status"] == "Not Started":
            noNotStarted.append(tasks[taskId]["title"])
        elif tasks[taskId]["status"] == "Completed":
            noCompleted.append(tasks[taskId]["title"])
    while reportExit != True:
        pageNum = 1
        # Displays the total number of tasks and their statuses.
        # Uses easygui buttonbox to allow the user to choose which
        # report to view in more detail.
        choice = easygui.buttonbox(f"Total tasks: {len(tasks)} \n"
                            f"Blocked: {len(noBlocked)} \n"
                            f"In Progress: {len(noInProgress)} \n"
                            f"Not Started: {len(noNotStarted)} \n"
                            f"Completed: {len(noCompleted)} \n",
                            title="Report", choices=["Blocked",
                                                    "In Progress",
                                                    "Not Started",
                                                    "Completed",
                                                    "Exit"])
        # For each status, it checks if the list is empty.
        # If yes, it displays a message saying there are no tasks in 
        # that category if not, it iterates through the list and 
        # displays each task's details using the fancyOutput function.
        if choice == "Blocked":
            if noBlocked == []:
                easygui.msgbox("No tasks are blocked at the moment",
                    title="Report")
            else:
                # Iterates through the given list, then creates a 
                # primary key to tell the fancyOutput function which 
                # tasks to display, using only the name of the task.
                for i in noBlocked:
                    for taskId in tasks:
                        if tasks[taskId]["title"] == i:
                            pk = taskId
                            if fancyOutput(tasks, pk, "title",
                                            pageNum, noBlocked) == "next":
                                pageNum += 1
                                pass
                            else:
                                reportExit = True
                                return  
        elif choice == "In Progress":
            if noInProgress == []:
                easygui.msgbox("No tasks are in progress at the moment",
                    title="Report")
            else:
                for i in noInProgress:
                    for taskId in tasks:
                        if tasks[taskId]["title"] == i:
                            pk = taskId
                            if fancyOutput(tasks, pk, "title",
                                            pageNum, noInProgress) == "next":
                                pageNum += 1
                                pass
                            else:
                                reportExit = True
                                return  
        elif choice == "Not Started": 
            if noNotStarted == []:
                easygui.msgbox("No tasks are not started at the moment",
                    title="Report")
            else:
                for i in noNotStarted:
                    for taskId in tasks:
                        if tasks[taskId]["title"] == i:
                            pk = taskId
                            if fancyOutput(tasks, pk, "title",
                                            pageNum, noNotStarted) == "next":
                                pageNum += 1
                                pass
                            else:
                                reportExit = True
                                return  
        elif choice == "Completed":
            if noCompleted == []:
                easygui.msgbox("No tasks are completed at the moment",
                    title="Report")
            else:
                for i in noCompleted:
                    for taskId in tasks:
                        if tasks[taskId]["title"] == i:
                            pk = taskId
                            if fancyOutput(tasks, pk, "title",
                                            pageNum, noCompleted) == "next":
                                pageNum += 1
                                pass
                            else:
                                reportExit = True
                                return  
        else:
            reportExit = True
            return


def varReset(newList, memberList, pageNum):
    """Resets the variables used in the program to their initial state.
    """

    newList = []
    memberList = []
    pageNum = 1
    return newList, memberList, pageNum


def inputValidation(value, field):
    """Validates the input based on the field type.
    Returns "alg" if the input is valid, "error" if not.
    The two return values are used to determine whether to continue or 
    stop the input loop. "error" can be used to reset the user input in 
    the backend. Displays error messages if the input is invalid.
    """

    # Changes the field type to str if it is title or description.
    if field in ["title", "description"]:
        field = str

    # Uses if and elif statements to check the field type and validate 
    # the input accordingly.
    if field == "priority":
        if value == ":3":
            return "error"        
        elif value == None:
            return "alg"
        # Checks if the value is an integer.
        # If it is an integer, it checks if it is between 
        # 1 and 3. If it is not, it displays an error message and 
        # returns "error".
        elif int(value) < MINPRIORITY or int(value) > MAXPRIORITY:
            easygui.msgbox(f"{field.upper()} must be between 1 and 3!",
                title="Error !!")
            return "error"
        else:
            return "alg"
    # If the field is a list, it checks if the value is empty.
    # If it is, it displays an error message and returns "error".
    # If it is not, it returns "alg" to continue.
    elif field == list:
        if value == []:
            easygui.msgbox("No results found, are you sure \
you typed everything in correctly?",
                title="Error !!")
            return "error"
        else:
            return "alg"
    elif field == str:
        if value == None:
            return "alg"
        # Checks if the value is a string and not empty,
        # if it is, it returns "error".
        elif value.strip() == "":
            easygui.msgbox("Input cannot be empty!",
                title="Error !!")
            return "error"
        # Checks if value is ":3" which is a placeholder,
        # if it is, it returns a silent "error". This can be used to 
        # reset the user input in the backend.
        elif value == ":3":
            return "error"
        else:
            # if the value is valid, it returns "alg" to continue.
            return "alg"


def fullOutput(pageNum):
    """Uses the fancyOutput function to display all tasks in the tasks 
    dictionary. It iterates through the tasks and displays each task's 
    details.
    """

    taskList = []
    # Appends ":3" to the taskList for each task in the dict.
    # This is so the pageNum can be displayed correctly in the 
    # fancyOutput function.
    for taskId in tasks:
        taskList.append(":3")
    # Iterates through the tasks dictionary and uses the fancyOutput 
    # function to display each task's details.
    for taskId in tasks:
        if fancyOutput(tasks, taskId, "title", pageNum, taskList) == "next":
            pageNum +=1
            pass
        else:
            break


def fancyOutput(dict, primaryKey, title, pageNum, list):
    """Formats the output of a task or member in a user-friendly way.
    Returns "next" to continue to the next item or "exit" to stop for 
    use in loops.
    """

    # Creates a list to hold the output, and also appends the title of 
    # the output to the top of the list.
    output = [f"{primaryKey}: {dict[primaryKey][title]}"]
    
    # Iterates through the dictionary and appends each key value pair to 
    # the output list.
    for key, value in dict[primaryKey].items():
        output.append(f"{key}: {value}")
    
    # Uses easygui buttonbox to display one page of output at a time.
    # The user can choose to go to the next page or exit.
    # The pageNum is displayed in the title of the buttonbox.
    choice = easygui.buttonbox("\n".join(output), 
                        title=f"{pageNum} of {len(list)}",
                        choices=["Next", "Exit"])
    if choice == "Next":
        return "next"
    elif choice is None or choice == "Exit":
        return "exit"
        

while userExit != True:
    # Resets the variables at the start of each loop.
    newList, memberList, pageNum = (
        varReset(newList, memberList, pageNum))
    # Uses easygui choicebox to display the main menu and get the user's 
    # choice.
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