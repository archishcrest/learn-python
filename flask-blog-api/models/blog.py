from cassandra.cqlengine import columns
from db import db
from datetime import datetime
import uuid

class BlogPost(db.Model):
    __keyspace__ = 'blog_keyspace'
    __table_name__ = 'blog_posts'

    id = db.columns.UUID(primary_key=True, default=uuid.uuid4)
    title = db.columns.Text(required=True)
    content = db.columns.Text(required=True)
    author = db.columns.Text(required=True)
    slug = db.columns.Text(required=False)
    created_at = db.columns.DateTime(default=datetime.utcnow)
