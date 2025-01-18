from load_from_file import load_tasks_from_file
from todo import add_task, diaplay_menu, view_task
from save_to_file import save_task_to_file


def main(): 
    tasks = load_tasks_from_file()
    while True: 
        diaplay_menu()
        choice = input("Enter your choicve: ")
        if choice == "1": 
            add_task(tasks)
        elif choice =="2": 
            view_task(tasks)
        elif choice == "6": 
            save_task_to_file(tasks)
            print("Exiting....Goodbay!")
            break
        else :
            print("invalida chpice Try again")
            
            
### To start a program use if __name__ == "main": this is the entry point call in python 
        
if __name__ == "__main__":
    main()