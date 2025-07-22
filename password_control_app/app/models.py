from app import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    last_password_hash = db.Column(db.String(200), nullable=True)

    def set_password(self, password):
        self.last_password_hash = self.password_hash
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def is_reusing_old_password(self, password):
        return self.last_password_hash and check_password_hash(self.last_password_hash, password)
