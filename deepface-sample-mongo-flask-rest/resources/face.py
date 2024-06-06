from flask import request
from flask_restful import Resource, reqparse
import uuid
import os
from deepface import DeepFace
#from deepface.commons import functions
from db import mongo
#from numpy import asarray
import numpy
from PIL import Image
from io import BytesIO
#from retinaface import RetinaFace
import PIL

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

class FaceResource(Resource):

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('data', type=str, required=True, help='No data provided', location='json')
    
    def post(self):

        # Check the HTTP method and route the request accordingly
        if request.path == '/thirdeye/faceadd':
            return self.faceadd()
        elif request.path == '/thirdeye/facefind':
            return self.facefind()

    def faceadd(self):

        file = request.files['file']
        filecheckname = request.form['filename']
        savefilename = ''

        if file and allowed_file(file.filename):

            savefilename = str(uuid.uuid4()) + '.' + request.files['file'].filename.split('.')[1]
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
            mongo.db.deepface.insert_one({"img_path": filecheckname, "embedding" : embedding})

            os.remove(path)

            return {"message": "Face added successfully"}, 201
        else:
            return jsonify({"message": 'Allowed file types are png, jpg, jpeg'}), 400


###########################################################################


    def facefind(self):
        file = request.files['file']

        if file and allowed_file(file.filename):

            savefilename = str(uuid.uuid4()) + '.' + request.files['file'].filename.split('.')[1]
            path = os.path.join(os.getcwd(), 'images', 'find',savefilename)
            # filepath to save image
            file.save(path)

            target_embedding = embedding = DeepFace.represent(path, model_name="ArcFace")[0]["embedding"]

            query = mongo.db.deepface.aggregate( [
            {
                "$addFields": { 
                    "target_embedding": target_embedding
                }
            }
            , {"$unwind" : { "path" : "$embedding", "includeArrayIndex": "embedding_index"}}
            , {"$unwind" : { "path" : "$target_embedding", "includeArrayIndex": "target_index" }}
            , {
                "$project": {
                    "img_path": 1,
                    "embedding": 1,
                    "target_embedding": 1,
                    "compare": {
                        "$cmp": ['$embedding_index', '$target_index']
                    }
                }
            }
            , {"$match": {"compare": 0}}
            , {
              "$group": {
                "_id": "$img_path",
                "distance": {
                    "$sum": {
                        "$pow": [{
                            "$subtract": ['$embedding', '$target_embedding']
                        }, 2]
                    }
                }
              }
            }
            , { 
                "$project": {
                    "_id": 1
                    #, "distance": 1
                    , "distance": {"$sqrt": "$distance"}
                }
            }, { 
                "$project": {
                    "_id": 1
                    , "distance": 1
                    , "cond": { "$lte": [ "$distance", 4.15 ] }
                }
            }
            , {"$match": {"cond": True}}
            , { "$sort" : { "distance" : 1 } }
            ] )

            my_list = list()
            for i in query:
                my_list.append({'name' : i['_id']})

            os.remove(path)

            return {"message": my_list}, 201
        else:
            return jsonify({"message": 'Allowed file types are png, jpg, jpeg'}), 400

