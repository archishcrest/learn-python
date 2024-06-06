from flask import Flask
from db import init_app
from flask_restful import Api
from resources.face import FaceResource

def create_app():
    app = Flask(__name__)    
    
    api = Api(app)
    init_app(app)

    # Add resources
    api.add_resource(FaceResource, '/deepface/faceadd', endpoint='faceadd')
    api.add_resource(FaceResource, '/deepface/facefind', endpoint='facefind')

    return app
