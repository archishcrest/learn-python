from flask_cqlalchemy import CQLAlchemy
from datetime import datetime
from flask_bcrypt import Bcrypt
from db import db
import uuid

bcrypt = Bcrypt()

class User(db.Model):
    __keyspace__ = 'blog_keyspace'
    __table_name__ = 'users'

    id = db.columns.UUID(default=uuid.uuid4)
    username = db.columns.Text(primary_key=True)
    password_hash = db.columns.Text(required=True)
    created_at = db.columns.DateTime(default=datetime.utcnow)

    def set_password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)
