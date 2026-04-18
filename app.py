from flask import Flask, render_template, request, redirect, url_for
from todolist import ToDoList
from task import Task

app = Flask(__name__)
todo = ToDoList()

@app.route("/")
def home():
    return render_template("index.html", tasks = todo.task_list)

@app.route("/add", methods = ["POST"])
def add_task():
    name = request.form.get("name", "").strip()
    description = request.form.get("description", "").strip()
    rank = request.form.get("rank", "").strip()
    if name and description and rank:
        task = Task(name, description, rank)
        todo.add_task(task)
    return redirect(url_for("home"))    

@app.route("/delete", methods = ["POST"])
def delete_task():
    name = request.form.get("name", "").strip()
    if name:
        todo.remove_task(name)
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug = True)
    
