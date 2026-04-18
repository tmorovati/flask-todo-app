from task import Task
import csv
import os

class ToDoList: 
    def __init__(self, filename = "tasks.csv"):
        self.task_list = []
        self.filename = filename
        self.load_from_csv()
    
    def add_task(self , task):
           self.task_list.append(task)
           self.save_as_csv()
       
    def remove_task(self, task_name):
        self.task_list = [task for task in self.task_list if task.name != task_name]    
        self.save_as_csv()
    
    def show_tasks(self):
        return [(task.name, task.description, task.rank) for task in self.task_list]
    
    def save_as_csv(self):
        import csv 
        with open(self.filename, "w", newline = "", encoding="utf-8") as f: 
            writer = csv.writer(f)
            writer.writerow(["name", "description", "rank"])
            for task in self.task_list:
                writer.writerow([task.name, task.description, task.rank])
        

    def load_from_csv(self):
        if not os.path.exists(self.filename):
            return

        with open(self.filename, "r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                task = Task(row["name"], row["description"], row["rank"])
                self.task_list.append(task)
    