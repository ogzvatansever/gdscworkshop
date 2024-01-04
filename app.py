from flask import Flask, request
import sqlite3

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.get("/thread")
def getThread():
    return {
        "message": "Hello World!"
    }, 200

@app.post("/thread")
def createThread():
    con = sqlite3.connect("database.db")
    cur = con.cursor()
    cur.execute("INSERT INTO threads (thread_user, thread_details, thread_created_at, thread_updated_at, thread_likes, thread_rt) VALUES (?,?,?,?,?,?)", tuple(request.json.values()))
    con.commit()
    return {
        "message": "Inserted new thread"
    }, 201
    

@app.put("/thread")
def updateThread():
    pass

@app.delete("/thread")
def deleteThread():
    pass