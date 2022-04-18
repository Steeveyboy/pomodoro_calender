import json, datetime
from flask import Flask, request, Response, session


ex = {"id":0, "name":"First Task", "periods":4, "periodsComplete":0, "description":"This is task 1 description. Its not too long", "dueDate": datetime.datetime(2022,3,13,23,56).isoformat()}
ex2 = {"id":1, "name":"Second Task", "periods":2, "periodsComplete":0, "description":"Task 2 is fairly long, probably a few lines \n, might have a list: \n\t eggs \n\t bacon \n\t toast \n\t jus egg salad bacon cheese berger salad days peanute butter chocolate chocolate lorem epsum is too difficult to look up", "dueDate": datetime.datetime(2022,3,21,23,59).isoformat()}

taskList = [ex, ex2]
app = Flask(__name__)

@app.route("/init")
def landing():
    res = Response()
    res.set_data(json.dumps({"tasks":taskList}))
    res.headers["Access-Control-Allow-Origin"] = "http://localhost:8080"
    return res

@app.route("/addtask", methods=["POST"])
def addtask():
    taskList.append(json.loads(request.get_data()))
    print(len(taskList))
    res = Response()
    res.headers["Access-Control-Allow-Origin"] = "http://localhost:8080"
    return res

@app.route("/updatetasks", methods=["POST"])
def updateTasks():
    print(json.loads(request.get_data())['tasks'])
    taskList.clear()
    taskList.extend(json.loads(request.get_data())['tasks'])
    res = Response()
    res.headers["Access-Control-Allow-Origin"] = "http://localhost:8080"
    return res
