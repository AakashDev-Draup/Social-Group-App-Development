import string
import random
from socialgroupmain.model.models import User, Group, Post, Comment
from bson import ObjectId
from datetime import datetime
from werkzeug.security import generate_password_hash


def makeuser(n):
    for i in range(n):
        name = str(''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=6)))
        password = generate_password_hash("{name}123".format(name=name))
        email = "{name}@gmail.com".format(name=name)

        User(
            name=name,
            password=password,
            email=email
        ).save()


def makegroup(n):
    for no in range(n):
        access = ['public', 'private']

        name = str(''.join(random.choices(string.ascii_uppercase +
                                          string.digits, k=8)))
        # first member is the admin
        Group(
            name=name,
            visibility=random.choice(access)
            # role_dict={str(userid):'ADMIN'}
        ).save()


def addusergroup():
    from itertools import islice
    users = User.objects
    userlist = []
    roles = ['ADMIN', 'MODERATOR', 'MEMBER']
    for user in users:
        userlist.append(str(user.id))

    dist = [50] * 300
    Inputt = iter(userlist)
    Output = [list(islice(Inputt, ele)) for ele in dist]
    groups = Group.objects
    count = 0
    for group in groups:
        tempdict = {}
        for val in Output[count]:
            tempdict[val] = random.choice(roles)
        group.update(set__role_dict=tempdict)
        count += 1


def addpostcomment():
    groups = Group.objects
    for group in groups:
        tempdict = group.lastactive_dict
        for userid in group.role_dict.keys():
            # use object id for reference fields
            tempdict[userid] = datetime.now()
            name = str(''.join(random.choices(string.ascii_uppercase +
                                              string.digits, k=6)))
            content = "This post has string {name}".format(name=name)
            post = Post(
                userid = ObjectId(userid),
                groupid = ObjectId(group.id),
                content = content

            ).save()
            Comment(
                    userid=ObjectId(userid),
                    postid=post.id,
                    content=content
                    ).save()

        group.update(set__lastactive_dict=tempdict)


# def addcomment():
#     posts = Post.objects
#     for post in posts:
#         name = str(''.join(random.choices(string.ascii_uppercase +
#                                           string.digits, k=6)))
#         content = "my comment is {name}".format(name=name)
#






