from flask import Flask

# Create the Flask app instance
app = Flask(__name__)

# Import routes after creating the app to avoid circular imports
from app.routes import *
from app.health import *
