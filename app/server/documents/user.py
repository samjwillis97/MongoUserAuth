from mongoengine import (
  Document, StringField, EmailField, DynamicDocument
)

class User(DynamicDocument):
  meta = {
    'collection': 'users',
  }
  username: StringField(required=True, unique=True)
  email: EmailField(required=False, unique=True)
  full_name: StringField(required=False)
  hashed_password: StringField(required=True)