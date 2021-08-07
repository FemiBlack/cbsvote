from flask import Flask
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from database.db import initialize_db
from flask_restful import Api
from flask_mail import Mail, Message
from resources.routes import initialize_routes
from resources.errors import errors

import os
import uuid
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__, static_folder='../client/dist/', static_url_path='/')
app.config.from_object(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
DATABASE_URL = os.environ.get('DATABASE_URI')
app.config['MONGODB_SETTINGS'] = {'host':  DATABASE_URL}

api = Api(app, errors=errors)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)
app.config['MAIL_SERVER'] = os.environ.get('MAIL_SERVER')
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('SENDGRID_API_KEY')
app.config['MAIL_USE_TLS'] = False
# app.config['MAIL_USE_SSL'] = True
app.config['MAIL_DEFAULT_SENDER'] = os.environ.get('MAIL_DEFAULT_SENDER')
mail = Mail(app)

initialize_db(app)
initialize_routes(api)

CORS(app, resources={r'/*': {'origins': '*'}})
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
def index():
    return app.send_static_file('index.html')


if __name__ == '__main__':
    app.run(port=(os.getenv('PORT') if os.getenv('PORT') else 8000), debug=False)
