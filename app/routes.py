from flask import request, render_template
from app import app

txt_path = r".\repeat-responses.txt"

tasks = [{
    'id' : 1,
    'task' : 'Get a job',
    'priority' : 1
},
{
    'id' : 2,
    'task' : 'Get a good night of sleep',
    'priority' : 2
}]

@app.route("/")
def display_homepage():
    return render_template("index.html")


@app.route('/tasks')
def get_tasks():
    t = tasks
    return t

@app.route('/tasks', methods=['POST'])
def add_task():
    if not request.is_json:
        return {'error' : 'Content not a JSON'}, 400
    
    data = request.json
    # check to make sure the data is valid
    required_keys = ["task", "priority"]
    missing_keys = []
    for key in required_keys:
        if key not in data:
            missing_keys.append(key)
    if missing_keys:
        return {"error" : f"Keys: {', '.join(missing_keys)} are missing from request"}, 400
    
    task = data.get('task')
    priority = data.get('priority')

    new_task = {
        "id" : len(tasks) + 1,
        "task" : task,
        "priority" : priority
    }
    tasks.append(new_task)

    return new_task, 201


@app.route('/tasks/<task_id>')
def get_task(task_id):
    t = tasks
    for task in t:
        if task['id'] == int(task_id):
            return task
    return {'error' : f'Unable to find task of id: {task_id}'}, 404












@app.route('/continue', methods=["GET"])
def repeat_form():
    with open(txt_path, 'r+') as f:
        responses = [line.rstrip() for line in f]
    return "<h2>The Story before you began: </h2>" + f"<p>{"<br>".join([i for i in responses])}</p>" + render_template("form.html")

@app.route('/continue', methods =["POST"])
def repeat():
    with open(txt_path, 'r+') as f:
        responses = [line.rstrip() for line in f]
    
    # get user input from the html webpage
    user_input = request.form.get("test_input")
    if user_input == "reset":
        reset_response = """
Once upon a time
there was a small child
with very big dreams.
"""
        responses = ["Once upon a time", "there was a small child","with very big dreams."]
        with open (txt_path, 'w') as f1:
            f1.write(reset_response)
    elif user_input != "":
        responses.append(user_input)
        with open (txt_path, 'a') as f1:
            f1.write(user_input + '\n')
    else:
        responses.append(">No Response<")

    return "<h2>Continue his story:</h2>" + f"<p>{"<br>".join([i for i in responses])}</p>" + render_template("form.html") 