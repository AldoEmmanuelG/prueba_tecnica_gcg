from flask import Flask, request, jsonify
import re
import json
import os
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

FILE_NAME = "users.json"

# -----------------------
# Cargar datos
# -----------------------
def load_users():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as f:
        return json.load(f)

# -----------------------
# Guardar datos
# -----------------------
def save_users(users):
    with open(FILE_NAME, "w") as f:
        json.dump(users, f, indent=4)

# -----------------------
# Validación de email
# -----------------------
def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)

# -----------------------
# Endpoint
# -----------------------
@app.route('/add-user', methods=['POST'])
def add_user():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Body vacío"}), 400

    name = data.get("name")
    email = data.get("email")

    # Validar campos vacíos
    if not name or not email or name.strip() == "" or email.strip() == "":
        return jsonify({"error": "Campos vacíos"}), 400

    # Validar email
    if not is_valid_email(email):
        return jsonify({"error": "Email inválido"}), 400

    users = load_users()

    # Validar duplicados
    for user in users:
        if user["email"] == email:
            return jsonify({"error": "Usuario ya existe"}), 400

    new_user = {
        "name": name,
        "email": email
    }

    users.append(new_user)
    save_users(users)

    return jsonify({
        "message": "Usuario agregado",
        "user": new_user
    }), 201

@app.route('/users', methods=['GET'])
def get_users():
    users = load_users()
    return jsonify(users), 200
@app.route('/user/<email>', methods=['GET'])
def get_user(email):
    users = load_users()

    for user in users:
        if user["email"] == email:
            return jsonify(user), 200

    return jsonify({"error": "Usuario no encontrado"}), 404
if __name__ == '__main__':
    app.run(debug=True)