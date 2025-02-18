#!/usr/bin/python3
"""
the programme will develop a simple API with flask
"""

from flask import Flask, jsonify, request


app = Flask(__name__)
users = {}


@app.route("/")
def home():
    return "Welcome to the Flask API!"


@app.route("/data")
def GU():
    return jsonify(list(users.keys()))


@app.route('/status')
def stat():
    return "OK"


@app.route('/users/<username>')
def search_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    new = data.get('username')

    if new:
        users[new] = data
        return jsonify({"message": "User added", "user": data}), 201
    else:
        return jsonify({"error": "Username is required"}), 400


if __name__ == "__main__":
    app.run()