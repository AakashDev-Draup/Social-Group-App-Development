from view.user import Userapi
from view.group import Groupapi, addtogroupapi,removegroupapi
from view.post import postapi
from view.comment import commentapi
from auth.auth import roleapi


def initialize_routes(api):
    api.add_resource(roleapi, '/api/role/<id>')  # create role and assign permission, id is special key here
    api.add_resource(Userapi, '/api/User')                      # create user
    api.add_resource(Groupapi, '/api/<id>/Group')               # create group with user id
    api.add_resource(addtogroupapi, '/api/addtogroup/<id>')       # add user to the group
    api.add_resource(removegroupapi, '/api/removefromgroup/<id>')   # Remove user from the group
    api.add_resource(postapi, '/api/Group/<id>/post')               # add post
    api.add_resource(commentapi, '/api/<gid>/<pid>/comment')        # add comment

