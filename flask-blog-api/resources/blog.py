from flask.views import MethodView
from flask import jsonify
from flask_smorest import Blueprint, abort
from db import db
from models import BlogPost
from schemas import (
    BlogPostSchema
)
from flask_jwt_extended import jwt_required, get_jwt_identity
from uuid import uuid4
from cassandra.cluster import Cluster
from cassandra.cqlengine.query import BatchQuery

blp = Blueprint("Blogs", "blogs", description="Operations on blogs")


@blp.route("/blog")
class Blog(MethodView):

	@jwt_required() 
	@blp.arguments(BlogPostSchema)
	def post(self, blog_data):

		current_user_id = get_jwt_identity()
		new_post = BlogPost(id=uuid4(), author=current_user_id,**blog_data)
		new_post.save()
		return {"message": "Blog created successfully."}, 201


	@blp.response(200, BlogPostSchema(many=True))
	def get(self):
		return BlogPost.objects().all()



@blp.route("/batchblog")
class BatchBlog(MethodView):

	@blp.response(201, BlogPostSchema(many=True))
	def get(self):

		users_data = [
			{'username': 'user1', 'password_hash': 'user1@example.com'},
			{'username': 'user2', 'password_hash': 'user2@example.com'},
		]

		posts_data = [
			{'user_id': uuid4(), 'author': uuid4(), 'title': 'First Post', 'content': 'This is the content of the first post'},
			{'user_id': uuid4(), 'author': uuid4(), 'title': 'Second Post', 'content': 'This is the content of the second post'},
			{'user_id': uuid4(), 'author': uuid4(), 'title': 'Second Post', 'content': 'This is the content of the second post'},
		]

		b = BatchQuery()
		BlogPost.batch(b).create(user_id= uuid4(), author= str(uuid4()), title= 'First Post 1', content= 'This is the content of the first post')
		b.execute()

		# cluster = Cluster()
		# session = cluster.connect()

		# batch = session.batch()

		# for user_data in users_data:
		# 	user_id = uuid4()
		# 	batch.add(User(id=user_id, **user_data))

		# for post_data in posts_data:
		# 	post_data['user_id'] = user_data['user_id']
		# 	batch.add(Post(id=uuid4(), **post_data))

		# session.execute(batch)

		return {"message": "Blog created successfully."}, 201