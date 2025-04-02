import json
import csv

def load_and_display_tasks(filename):
    with open(filename, 'r') as file:
        tasks = json.load(file)
    
    print("\nCurrent Tasks:")
    print("ID | Task Name          | Completed | Priority")
    print("-" * 45)
    for task in tasks:
        print(f"{task['id']:2} | {task['task']:<18} | {str(task['completed']):<9} | {task['priority']}")
    return tasks

def calculate_task_stats(tasks):
    total_tasks = len(tasks)
    completed_tasks = sum(1 for task in tasks if task['completed'])
    pending_tasks = total_tasks - completed_tasks
    avg_priority = sum(task['priority'] for task in tasks) / total_tasks if total_tasks > 0 else 0
    
    print("\nTask Statistics:")
    print(f"Total Tasks: {total_tasks}")
    print(f"Completed Tasks: {completed_tasks}")
    print(f"Pending Tasks: {pending_tasks}")
    print(f"Average Priority: {avg_priority:.2f}")
    return total_tasks, completed_tasks, pending_tasks, avg_priority

def save_tasks(filename, tasks):
    with open(filename, 'w') as file:
        json.dump(tasks, file, indent=4)

def json_to_csv(json_filename, csv_filename):
    with open(json_filename, 'r') as json_file:
        tasks = json.load(json_file)
    
    with open(csv_filename, 'w', newline='') as csv_file:
        fieldnames = ['ID', 'Task', 'Completed', 'Priority']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        
        writer.writeheader()
        for task in tasks:
            writer.writerow({
                'ID': task['id'],
                'Task': task['task'],
                'Completed': task['completed'],
                'Priority': task['priority']
            })
def main():
    tasks = load_and_display_tasks(r'C:\Users\user\Downloads\Python\pythonhomeworks\lesson-9\homework\tasks.json')
 
    calculate_task_stats(tasks)
    
    for task in tasks:
        if task['id'] == 1:
            task['completed'] = True
            print("\nModified task 1 to completed")
    
    save_tasks('tasks.json', tasks)
    
    json_to_csv('tasks.json', 'tasks.csv')
    print("\nTasks have been converted to tasks.csv")

if __name__ == "__main__":
    main()