
## _filename = "task.json"
import json

#### Asve to file 
def save_task_to_file(tasks, filename="tasks.json"): 
    with open(filename, "w") as file: 
        json.dump(tasks, file, indent=4)
    print("Tasks added to file.")    