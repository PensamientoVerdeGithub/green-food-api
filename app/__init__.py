from flask import Flask
from flask_cors import CORS
from .config import Config
from .models import db

from .routes.home import home_blueprint
from .routes.ingredientes import ingredientes_blueprint

app = Flask(__name__)

def create_app():
    app.config.from_object(Config)

    db.init_app(app)
    
    CORS(
        app, 
        resources={r"/*": {"origins": ["http://localhost:5173", "http://example.com","https://sissports-front-production.up.railway.app"]}}
    )
    
    app.register_blueprint(home_blueprint)
    app.register_blueprint(ingredientes_blueprint)
    
    return app