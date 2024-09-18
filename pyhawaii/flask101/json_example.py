from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def hello():
    resp = {"result": "", "method": ""}
    if request.method == "GET":
        resp["result"] = 200
        resp["method"] = "GET"
        resp["mesg"] = "Hello, World!"
        return resp
    elif request.method == "POST":
        resp["result"] = 200
        resp["method"] = "POST"
        resp["mesg"] = "Posted!"
        return resp
