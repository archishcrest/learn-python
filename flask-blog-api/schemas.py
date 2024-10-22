from marshmallow import Schema, fields

class BlogPostSchema(Schema):
    id = fields.UUID(dump_only=True)
    title = fields.Str(required=True)
    content = fields.Str(required=True)
    author = fields.Str(required=False)
    slug = fields.Str(required=False)
    created_at = fields.DateTime(dump_only=True)


class UserSchema(Schema):
    id = fields.UUID(dump_only=True)
    username = fields.Str(required=True)
    password = fields.Str(load_only=True, required=True)  # Hide password from output