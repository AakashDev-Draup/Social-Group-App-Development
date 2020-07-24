
from configuration.config import db

# id reminds every class has unique id


class Role(db.Document):
    name = db.StringField(required=True,unique=True, max_length=50)
    permissions = db.ListField(db.StringField())


class Group(db.Document):
    # id
    name = db.StringField(required=True, max_length=50)
    visibility = db.StringField(default='public')
    posts = db.ListField(db.ReferenceField('Post'), reverse_delete_rule=db.PULL)
    users = db.ListField(db.DictField())        # fill with {'userid':'roleid'}


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
    # not required now
    # groups = db.ListField(db.ReferenceField('Group', reverse_delete_rule=db.PULL))
    posts = db.ListField(db.ReferenceField('Post', reverse_delete_rule=db.PULL))      # ids of post created by the user
    comments = db.ListField(db.ReferenceField('Comment', reverse_delete_rule=db.PULL))














