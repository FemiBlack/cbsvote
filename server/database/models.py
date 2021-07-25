from .db import db
from flask_bcrypt import generate_password_hash,check_password_hash


class Vote(db.Document):
    name = db.StringField(required=True)
    category = db.StringField(required=True)
    nominee_id = db.StringField(required=True)

class Nominee(db.Document):
    name = db.StringField(required=True)
    category = db.ListField(db.DictField(required=True)) #{'name':'freshest',vote:0}
    reg_no = db.IntField(required=True)
    img = db.StringField()

class User(db.Document):
    email = db.EmailField(required=True, unique=True)
    password = db.StringField(required=True, min_length=6)
    voted_for = db.ListField(db.StringField())

    def hash_password(self):
        self.password = generate_password_hash(self.password).decode('utf8')

    def check_password(self, password):
        return check_password_hash(self.password, password)
