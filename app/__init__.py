# app/__init__.py
from flask import Flask
from app.config import Config
from app.extensions import db, bcrypt, jwt, mail
from flask_migrate import Migrate

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicializar extensiones
    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)
    mail.init_app(app)
    Migrate(app, db)
    
     # Inicializar Flask-Admin
    from app.admin import init_admin
    init_admin(app)

    @app.route("/")
    def home():
        return {"message": "API ON FIRE TONIGHT"}, 200

    return app
