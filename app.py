from flask import Flask, render_template, request, jsonify
import json, os

app = Flask(__name__)
DATA_FILE = "todos.json"

def load_todos():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE) as f:
            return json.load(f)
    return []

def save_todos(todos):
    with open(DATA_FILE, "w") as f:
        json.dump(todos, f)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/todos", methods=["GET"])
def get_todos():
    return jsonify(load_todos())

@app.route("/api/todos", methods=["POST"])
def add_todo():
    todos = load_todos()
    data = request.json
    todo = {
        "id": (todos[-1]["id"] + 1) if todos else 1,
        "text": data["text"],
        "done": False
    }
    todos.append(todo)
    save_todos(todos)
    return jsonify(todo), 201

@app.route("/api/todos/<int:todo_id>", methods=["PATCH"])
def toggle_todo(todo_id):
    todos = load_todos()
    for t in todos:
        if t["id"] == todo_id:
            t["done"] = not t["done"]
            save_todos(todos)
            return jsonify(t)
    return jsonify({"error": "Not found"}), 404

@app.route("/api/todos/<int:todo_id>", methods=["DELETE"])
def delete_todo(todo_id):
    todos = load_todos()
    todos = [t for t in todos if t["id"] != todo_id]
    save_todos(todos)
    return jsonify({"ok": True})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)