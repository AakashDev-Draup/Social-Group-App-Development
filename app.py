from flask import Flask
from datetime import datetime
from scheduler.del_inactive_users import inactive_users
from flask_mail import Mail

from configuration.config import initialize_db
from flask_restful import Api
from urls.url import initialize_routes
from scheduler.scheduler import schedule_tasks
# from scheduler.daily_feed import dailyfeed

app = Flask(__name__)
api = Api(app)
mail = Mail(app)

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/Social-Group'
}

initialize_db(app)
initialize_routes(api)

# these are commented to prevent from execution in trial runs
# firstexec,funcexec,duration(seconds),freq
# schedule_tasks(datetime.now(),inactive_users,60,1)
# today_mid = datetime.combine(date.today(), datetime.min.time())
# schedule_tasks(today_mid,dailyfeed,86400,None)

app.run(debug=True)


