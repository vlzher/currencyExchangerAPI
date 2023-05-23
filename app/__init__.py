from dotenv import load_dotenv
from flask import Flask
from app.routes import routes_bp
import os

app = Flask(__name__)
app.register_blueprint(routes_bp)
load_dotenv()

app.debug = True
if os.environ.get('ENV') == 'dev':
    app.debug = True


