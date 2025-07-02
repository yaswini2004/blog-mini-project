from flask import Flask
from routes.post_routes import post_bp
from models.post import db

def create_app():
    app = Flask(__name__)
    app.secret_key = 'secret123'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db' 
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)  

    with app.app_context():
        db.create_all()  
    app.register_blueprint(post_bp)

    return app
#app.py in which running all the file using flask
