#!/usr/bin/python3
'''FLASK ENVIRONNEMENT'''


from flask import Flask, jsonify, request


app = Flask(__name__)
users = {}


@app.route("/")
def hello_world():
    return "<p>Welcome to the Flask API!</p>"


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


@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    new_user = data.get('username')

    if new:
        users[new_user] = data
        return jsonify({"message": "User added", "user": data}), 201
    else:
        return jsonify({"error": "Username is required"}), 400


if __name__ == "__main__":
    app.run()
