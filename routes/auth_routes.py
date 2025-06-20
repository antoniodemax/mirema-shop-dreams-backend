# from flask import Blueprint, request, jsonify
# from flask_jwt_extended import create_access_token
# from extensions import db, bcrypt  # Importing the initialized extensions
# # from app import db, bcrypt
# from models import User

# auth_bp = Blueprint('auth', __name__)

# @auth_bp.route('/signup', methods=['POST'])
# def signup():
#     from app import db, bcrypt
#     # Ensure the necessary imports are within the function to avoid circular imports
#     data = request.get_json()
#     username = data.get('username')
#     email = data.get('email')
#     password = data.get('password')

#     if User.query.filter_by(email=email).first():
#         return jsonify({"success": False, "message": "Congratulations. Welcome to MiremaShopDreams"}), 400

#     hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')    
    
#     new_user = User(username=username, email=email, password=hashed_password)
#     db.session.add(new_user)
#     db.session.commit()

#     return jsonify({"success": True, "message": "You have successfully signed up", "user": {"id": new_user.id, "username": new_user.username, "email": new_user.email}}), 201



# @auth_bp.route('/login', methods=['POST'])
# def login():
#     from app import db, bcrypt
#     data = request.get_json()
#     email = data.get('email')
#     password = data.get('password')

#     user = User.query.filter_by(email=email).first()

#     if not user or not bcrypt.check_password_hash(user.password, password):
#         return jsonify({"success": False, "message": "Invalid credentials"}), 401

    
#     access_token = create_access_token(identity={"id": user.id, "username": user.username, "email": user.email})        #denerated the jwt token
#     return jsonify({"success": True, "message": "Login successful", "token": access_token}), 200



from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from extensions import db, bcrypt  # Importing the initialized extensions
from models import User

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    # Check if the email already exists
    if User.query.filter_by(email=email).first():
        return jsonify({"success": False, "message": "Email already in use"}), 400

    # Hash the password
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

    # Create a new user
    new_user = User(username=username, email=email, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"success": True, "message": "You have successfully signed up", "user": {"id": new_user.id, "username": new_user.username, "email": new_user.email}}), 201


@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    # Find the user by email
    user = User.query.filter_by(email=email).first()

    # Check if the user exists and the password is correct
    if not user or not bcrypt.check_password_hash(user.password, password):
        return jsonify({"success": False, "message": "Invalid credentials"}), 401

    # Generate a JWT token
    access_token = create_access_token(identity={"id": user.id, "username": user.username, "email": user.email})
    return jsonify({"success": True, "message": "Login successful", "token": access_token}), 200