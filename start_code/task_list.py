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

finsihed_tasks = yes_tasks(tasks)

print(finsihed_tasks)
