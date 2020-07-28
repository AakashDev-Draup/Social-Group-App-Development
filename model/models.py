
from configuration.config import db
import datetime


class Role(db.Document):
    name = db.StringField(required=True,unique=True, max_length=50)
    permissions = db.ListField(db.StringField())


class Group(db.Document):

    name = db.StringField(required=True, max_length=50)
    visibility = db.StringField(default='public')
    role_dict = db.DictField()  # fill with {'userid':'roleid'}
    date_created = db.DateTimeField(default=datetime.datetime.now())
    lastactive_dict = db.DictField()    # fill with {'userid':'last active time'}


class Post(db.Document):

    userid = db.ReferenceField('User')
    groupid = db.ReferenceField('Group')
    content = db.StringField(required=True, max_length=160)
    # approval is set to true for now
    approval = db.StringField(Default=True, max_length=10)
    date_created = db.DateTimeField(default=datetime.datetime.now())


class Comment(db.Document):

    userid = db.ReferenceField('User')
    postid = db.ReferenceField('Post')
    content = db.StringField(required=True, max_length=50)
    date_created = db.DateTimeField(default=datetime.datetime.now())


class User(db.Document):

    name = db.StringField(required=True, max_length=30)
    email = db.StringField(required=True)














