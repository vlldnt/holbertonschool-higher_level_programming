#!/usr/bin/python3
'''FLASK ENVIRONNEMENT'''


from flask import Flask, jsonify, request


app = Flask(__name__)
users = {}


@app.route("/")
def hello_world():
    return "Welcome to the Flask API!"


@app.route("/data")
def get_users():
    return jsonify(list(users.keys()))


@app.route("/status")
def status():
    return "OK"


@app.route("/users/<username>")
def username(username):
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=['POST'])
def add_user():
    if not request.json or "username" not in request.json:
        return jsonify({"error": "Username is required"}), 400
    user_data = request.json
    username = user_data["username"]

    users[username] = {
        "username": user_data.get("username"),
        "name": user_data.get("name"),
        "age": user_data.get("age"),
        "city": user_data.get("city")
    }
    return jsonify({"message": "User added", "user": users[username]}), 201


if __name__ == "__main__":
    app.run()
