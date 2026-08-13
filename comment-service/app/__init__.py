from flask import Flask
from .database import db, init_db
from .urls import register_routes

def create_app():
    app = Flask(__name__)
    init_db(app)
    
    with app.app_context():
        db.create_all()
    
    register_routes(app)
    return app