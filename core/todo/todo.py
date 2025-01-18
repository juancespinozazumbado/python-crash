
# tasks = [
#         {"id": 1, "title": "Learn Python", "isCompleted": False}, 
#         {"id": 2, "title": "Learn golang", "isComplited": True }, 
#         {"id": 1, "title": "Learn Python", "isCompleted": False}, 
#         {"id": 2, "title": "Learn golang", "isComplited": True }, 
#         {"id": 1, "title": "Learn Python", "isCompleted": False}, 
#         {"id": 2, "title": "Learn golang", "isComplited": True }, 
# ]

###### Display menu
def diaplay_menu(): 
    print("\nTo-Do List manager")
    print("1. Add Task")
    print("2. View Task")
    print("3. Uspdate Task")
    print("4. Mark Task as Complete")
    print("5. Delete Task")
    print("6. Exit")

### Add a new task to array    
def add_task(tasks):
    title = input("Enter task title: ...")
    task_id = len(tasks) + 1 ### len() returns array length 
    tasks.append({"id": task_id, "title": title, "isComplited": False})
    print(f"Tas '{title}' added.") ## string interpolation whit ' and {val} 
   
##### Print all task info        
def view_task(tasks):
    if not tasks: 
        print("not have tasks yet")
        return
    for task in  tasks: 
        status = "complete" if task["isComplited"] else "Incomplete" ## ternary conditional variable = option1 if <condition> else option2
        print(f"{task['id']}: {task['title']} [{status}]")
        
