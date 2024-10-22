from cassandra.cqlengine import columns
from db import db
from datetime import datetime
import uuid

class RevokedToken(db.Model):

	__keyspace__ = 'blog_keyspace'
	__table_name__ = 'revoke_token'
	id = db.columns.UUID(primary_key=True, default=uuid.uuid4)
	jti = db.columns.Text(required=True)
	user_id = db.columns.UUID(required=True)
	created_at = db.columns.DateTime(default=datetime.utcnow)

	def __repr__(self):
		return f"<RevokedToken(jti={self.jti})>"
