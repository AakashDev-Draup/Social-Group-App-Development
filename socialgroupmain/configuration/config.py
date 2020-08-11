#~movie-bag/database/db.py

from flask import Flask
from redis import Redis
from rq import Queue
from flask_mail import Mail
from flask_restful import Api
from flask_mongoengine import MongoEngine
from rq_scheduler import Scheduler


app = Flask(__name__)
api = Api(app)
mail = Mail(app)


queue = Queue('test',connection=Redis())


db = MongoEngine()


def initialize_db(app):
    db.init_app(app)


# list_of_job_instances = scheduler.get_jobs()
# for job in list_of_job_instances:
#     print(job)
#     scheduler.cancel(job)

