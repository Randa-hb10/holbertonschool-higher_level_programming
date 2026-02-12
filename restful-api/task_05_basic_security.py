#!/usr/bin/python3
"""
Task 05 - API Security and Authentication Techniques
Basic Auth + JWT + Role-based Access Control (RBAC)
"""

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    jwt_required,
    get_jwt_identity
)

app = Flask(__name__)

# Secret key used for JWT signing (keep it strong in real apps)
app.config["JWT_SECRET_KEY"] = "super-secret-key-change-me"

auth = HTTPBasicAuth()
jwt = JWTManager(app)

# Users stored in memory (dictionary) exactly like required structure
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}


# -----------------------------
# Basic Authentication (HTTPBasicAuth)
# -----------------------------
@auth.verify_password
def verify_password(username, password):
    """Verify provided Basic Auth credentials."""
    user = users.get(username)
    if not user:
        return None
    if check_password_hash(user["password"], password):
        return user
    return None


@auth.error_handler
def basic_auth_error_handler():
    """
    Ensure missing/invalid basic auth returns 401 Unauthorized.
    Body content isn't specified by the task; status code is what matters.
    """
    return jsonify({"error": "Unauthorized"}), 401


@app.route("/basic-protected", methods=["GET"])
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"


# -----------------------------
# JWT Authentication (Flask-JWT-Extended)
# -----------------------------
@app.route("/login", methods=["POST"])
def login():
    """
    Accepts JSON payload with username & password.
    Returns JWT access token if credentials are valid.
    """
    data = request.get_json(silent=True)
    if data is None:
        # Treat invalid/missing JSON as unauthorized-like for this task context
        # (but not required in the expected outputs list)
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"error": "Missing username or password"}), 400

    user = users.get(username)
    if not user or not check_password_hash(user["password"], password):
        return jsonify({"error": "Invalid credentials"}), 401

    # Put identity + role in token payload (identity can be a dict)
    access_token = create_access_token(identity={"username": username, "role": user["role"]})
    return jsonify({"access_token": access_token})


@app.route("/jwt-protected", methods=["GET"])
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted"


@app.route("/admin-only", methods=["GET"])
@jwt_required()
def admin_only():
    identity = get_jwt_identity()
    # identity expected to be dict: {"username": ..., "role": ...}
    role = None
    if isinstance(identity, dict):
        role = identity.get("role")

    if role != "admin":
        return jsonify({"error": "Admin access required"}), 403

    return "Admin Access: Granted"


# -----------------------------
# JWT Error Handlers
# Must return 401 for auth/token problems (per requirement)
# -----------------------------
@jwt.unauthorized_loader
def jwt_missing_token_callback(err):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def jwt_invalid_token_callback(err):
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def jwt_expired_token_callback(jwt_header, jwt_payload):
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def jwt_revoked_token_callback(jwt_header, jwt_payload):
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def jwt_needs_fresh_token_callback(jwt_header, jwt_payload):
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == "__main__":
    app.run()
