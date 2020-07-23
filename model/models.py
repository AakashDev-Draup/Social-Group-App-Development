
from configuration.config import db


class Permissions(db.Document):
    # id
    name = db.StringField(required=True, unique=True)


# this class is for scalability
class Roles(db.Document):
    # id
    name = db.StringField(required=True, unique=True, default='member')
    permission = db.ListField(db.ReferenceField('Permissions'), reverse_delete_rule=db.PULL)      # list of permissions ids


class groupuser(db.EmbeddedDocument):
    userid = db.ReferenceField('User')          # reverse delete rule not supported
    roleid = db.ReferenceField('Roles')


class Group(db.Document):
    # id
    name = db.StringField(required=True, max_length=50)
    visibility = db.StringField(default='public')
    # users = db.DictField()    # all the users in group {'userid':'roleid'}
    users = db.ListField(db.EmbeddedDocumentField('groupuser'))



class Post(db.Document):
    # id
    userid = db.ReferenceField('User')      # cascade not used because if user deleted posts are not deleted
    groupid = db.ReferenceField('Group')
    content = db.StringField(required=True, max_length=160)
    # approval is set to true for now
    approval = db.StringField(Default=True, max_length=10)


class Comment(db.Document):
    # id
    userid = db.ReferenceField('User')
    postid = db.ReferenceField('Post')
    content = db.StringField(required=True, max_length=50)

# one to many relation 1 user can have lot of comments and posts


class User(db.Document):
    # id
    name = db.StringField(required=True, max_length=30)
    email = db.StringField(required=True)
    # this can be left for now
    # groups = db.ListField(db.StringField('Group', reverse_delete_rule=db.PULL))
    posts = db.ListField(db.ReferenceField('Post', reverse_delete_rule=db.PULL))      # ids of post created by the user
    comments = db.ListField(db.ReferenceField('Comment', reverse_delete_rule=db.PULL))














