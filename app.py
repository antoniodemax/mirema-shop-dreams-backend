# from flask import Flask
# from extensions import db, bcrypt, jwt  # Importing the initialized extensions
# from routes.auth_routes import auth_bp

# # from flask_sqlalchemy import SQLAlchemy
# # from flask_bcrypt import Bcrypt
# # from flask_jwt_extended import JWTManager

# app = Flask(__name__) # Initialized the  Flask app

# # Configuration for the Flask app
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['JWT_SECRET_KEY'] = 'your_jwt_secret' 

# # Initialized the extensions
# # db = SQLAlchemy(app)
# # bcrypt = Bcrypt(app)
# # jwt = JWTManager(app)
# db.init_app(app)  # Initializing SQLAlchemy
# bcrypt.init_app(app)  # Initializing Bcrypt
# jwt.init_app(app)  # Initializing JWTManager


# # Importing the routes after initializing the app and extensions
# # from routes.auth_routes import auth_bp
# app.register_blueprint(auth_bp, url_prefix='/api/auth')

# if __name__ == '__main__':
#     app.run(debug=True) 
from flask import Flask
from extensions import db, bcrypt, jwt  # Importing the initialized extensions
from flask_migrate import Migrate  # Import Flask-Migrate
from routes.auth_routes import auth_bp

app = Flask(__name__)  # Initialize the Flask app

# Configuration for the Flask app
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret'

# Initialize the extensions
db.init_app(app)
bcrypt.init_app(app)
jwt.init_app(app)

# Initialize Flask-Migrate
migrate = Migrate(app, db)

# Register the auth blueprint
app.register_blueprint(auth_bp, url_prefix='/api/auth')

if __name__ == '__main__':
    app.run(debug=True)