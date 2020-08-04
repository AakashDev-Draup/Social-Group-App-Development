#~movie-bag/database/db.py

from flask import Flask
import redis
from rq import Queue
from flask_mail import Mail
from flask_restful import Api
from flask_mongoengine import MongoEngine
from rq_scheduler import Scheduler


app = Flask(__name__)
api = Api(app)
mail = Mail(app)

r = redis.Redis()

scheduler = Scheduler('foo', connection=r)
q = Queue(connection=r)


def schedule_tasks(time_firstexec,func,freq,no_ofexec):

    scheduler.schedule(
        scheduled_time=time_firstexec,            # Time for first execution, datetime.min for 00:00
        func=func(),                     # Function to be queued
        args=[],             # Arguments passed into function when executed
        kwargs={},         # Keyword arguments passed into function when executed
        interval=freq,                   # Time before the function is called again, in seconds
        repeat=no_ofexec,                     # Repeat this number of times (None means repeat forever)
        meta={}            # Arbitrary pickleable data on the job itself
    )


# list_of_job_instances = scheduler.get_jobs()
# for job in list_of_job_instances:
#     print(job)
#     scheduler.cancel(job)

db = MongoEngine()


def initialize_db(app):
    db.init_app(app)