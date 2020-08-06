from socialgroupmain import app,api
from socialgroupmain.configuration.config import initialize_db

from socialgroupmain.urls.url import initialize_routes


if __name__ == "__main__":

    app.config['MONGODB_SETTINGS'] = {
        'host': 'mongodb://localhost/Social-Group'
    }

    initialize_db(app)
    initialize_routes(api)

    app.run(debug=True)


