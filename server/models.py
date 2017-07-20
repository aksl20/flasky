from mongoengine import Document

class User(Document):
    name = StringField(max_length=50)

class Role(Document)
    name = StringField(max_length=50)
