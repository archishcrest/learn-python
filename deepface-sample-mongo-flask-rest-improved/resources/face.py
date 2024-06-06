from flask.views import MethodView
from flask_smorest import Blueprint, abort
import uuid
import os
from deepface import DeepFace
#from deepface.commons import functions
from db import mongo
#from numpy import asarray
import numpy
from PIL import Image
from io import BytesIO
from flask import Flask, request, jsonify
import PIL
from schemas import AddFaceSchema
from marshmallow import ValidationError

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

blp = Blueprint("Face", "face", description="Add and find Face")

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@blp.route("/add")
class FaceAdd(MethodView):
    def post(self):

        # Manually parse the form data
        file = request.files.get('file')
        name = request.form.get('name')

        # Create a dictionary to validate with Marshmallow schema
        form_data = {
            'name': name,
            'file': file
        }

        schema = AddFaceSchema()
        try:
            result = schema.load(form_data)
            
            savefilename = str(uuid.uuid4()) + '.' + request.files.get('file').filename.split('.')[1]
            path = os.path.join(os.getcwd(), 'images', 'add',savefilename)
            # filepath to save image
            file.save(path)

            model = DeepFace.build_model("ArcFace")
            # img = Image.open(os.path.join(os.getcwd(), 'images', 'add',savefilename))
            # numpydata = numpy.array(PIL.Image.open(path).convert("RGB"))
            # print(path)
            # facial_img = functions.extract_faces(numpydata, target_size = (112, 112),  detector_backend = 'retinaface',enforce_detection = True,  align = True)
            #embedding = model.predict(facial_img)[0]
            embedding = DeepFace.represent(path, model_name="ArcFace")[0]["embedding"]
            #print(embedding)
            mongo.db.deepface.insert_one({"img_path": name, "embedding" : embedding})

            os.remove(path)

            return jsonify({"message": "Face added successfully"}), 201
        except ValidationError as err:
            return jsonify({"errors": err.messages}), 400

        return {"message": "Face added successfully"}, 201
