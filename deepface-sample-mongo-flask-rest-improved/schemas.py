from marshmallow import Schema, fields, validate, ValidationError

def allowed_file(filename):
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def validate_file(file):
    if file is None:
        raise ValidationError("No file provided.")
    if not allowed_file(file.filename):
        raise ValidationError("Invalid file type. Only .png, .jpg and .jpeg are allowed.")

class AddFaceSchema(Schema):
    name = fields.String(required=True, validate=validate.Length(min=1))
    file = fields.Method(required=True, deserialize='load_file', validate=validate_file)

    def load_file(self, value):
        return value
