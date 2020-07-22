
from configs.config import db


class Permissions(db.Document):
    # id
    name = db.StringField(required=True, unique=True)


# this class is for scalability
class Roles(db.Document):
    # id
    name = db.StringField(required=True, unique=True, default='member')
    permission = db.ListField(db.StringField(), required=True)      # list of permissions ids


class Group(db.Document):
    # id
    name = db.StringField(required=True, max_length=50)
    visibility = db.StringField(default='public')
    users = db.DictField()    # all the users in group {'userid':'roleid'}


class User(db.Document):
    # id
    name = db.StringField(required=True, max_length=30)
    email = db.StringField(required=True, unique=True)
    groups = db.ListField(db.StringField())      # ids of groups user is connected
    posts = db.ListField(db.StringField())      # ids of post created by the user
    commments = db.ListField(db.StringField())      # ids of comments created by the user


class Post(db.Document):
    # id
    userid = db.StringField(required=True)
    groupid = db.StringField(required=True)
    content = db.StringField(required=True, max_length=160)
    approval = db.StringField(Default=False, max_length=20)


class Comment(db.Document):
    # id
    userid = db.StringField(required=True)
    postid = db.StringField(required=True)
    content = db.StringField(required=True, max_length=50)












