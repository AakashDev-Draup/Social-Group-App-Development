from view.user import Userapi
from view.group import Groupapi, editgroupapi
from view.post import postapi
from view.comment import commentapi


def initialize_routes(api):
    api.add_resource(Userapi, '/api/User')
    api.add_resource(Groupapi, '/api/Group')
    api.add_resource(editgroupapi, '/api/Group/<id>')
    api.add_resource(postapi, '/api/Group/<id>/post')
    api.add_resource(commentapi, '/api/post/<id>/comment')

