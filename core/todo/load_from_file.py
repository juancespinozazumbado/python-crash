import json

def load_tasks_from_file(filename="tasks.json"): 
    try: 
        with open(filename, "r") as file: 
            return json.load(file)
    except FileNotFoundError: ## if there's no records in file, return empty array
        return []
    except json.JSONDecodeError:
        # If file exists but has invalid content, return an empty list
        print(f"File {filename} contains invalid JSON. Returning an empty list.")
        return []