from flask import Flask

from configuration.config import initialize_db
from flask_restful import Api
from urls.url import initialize_routes
app = Flask(__name__)
api = Api(app)

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/Social-Group'
}

initialize_db(app)
initialize_routes(api)


app.run(debug=True)


