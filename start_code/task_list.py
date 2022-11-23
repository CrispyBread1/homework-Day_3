tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]



def no_tasks(list_chores):
    uncompleted_tasks = []
    for task in list_chores:
        if task["completed"] == False:
            uncompleted_tasks.append(task["description"])

    return uncompleted_tasks

def yes_tasks(list_chores):
    completed_tasks = []
    for task in list_chores:
        if task["completed"] == True:
            completed_tasks.append(task["description"])

    return completed_tasks

def list_tasks(list_chores):
    task_descriptions = []
    for task in list_chores:
        task_descriptions.append(task['description'])

    return task_descriptions

def time_taken(list_chores):
    time_lists = []
    time_allowewd = int(input("How long do you have available to complete the task? "))
    for task in list_chores:
        if time_allowewd >= task["time_taken"]:
           time_lists.append(task["description"])

    return time_lists

def search_task(list_chores):
    answer = []
    task = input("Please provide task to get more information ")
    for search in list_chores:
        if task == search["description"]:
            answer = search

    return answer
            
answer = search_task(tasks)

print(answer)








