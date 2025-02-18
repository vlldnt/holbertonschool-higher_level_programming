#!/usr/bin/python3
''' Simple flask API with security and basic authentification '''

  
from flask import Flask, jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, create_access_token
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_httpauth import HTTPBasicAuth


app = Flask(__name__)
jwt = JWTManager(app)
auth = HTTPBasicAuth()

users = {
    "user1": {"username": "user1",
              "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1",
               "password": generate_password_hash("password"), "role": "admin"}
}


@auth.verify_password
def verify_password(username, password):
    user = users.get(username)
    if user and check_password_hash(user("password"), password):
        return username
    return None


@app.route("/")
def home():
    return "Welcome to the Flask API!"


@app.route("/login", methods=['POST'])
def login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)


    

@app.route("/basic-protected", methods=['GET'])
def basic_protected():
    return "Basic Auth: Access Granted"


@app.route("/jwt-protected")
def jwt_protected():
    pass


@app.route("/admin-only")
def admin_only():
    pass


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
      return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401

@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    return jsonify({"error": "Token has been revoked"}), 401

@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == '__main__':
    app.run()