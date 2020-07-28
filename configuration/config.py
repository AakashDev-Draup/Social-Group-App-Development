#~movie-bag/database/db.py

from rq import Queue
from flask_mongoengine import MongoEngine
from redis import Redis
from rq_scheduler import Scheduler


scheduler = Scheduler('foo',connection=Redis())     # Get a scheduler for the "default" queue without foo
q = Queue(connection=Redis())


# list_of_job_instances = scheduler.get_jobs()
# for job in list_of_job_instances:
#     print(job)
#     scheduler.cancel(job)

db = MongoEngine()


def initialize_db(app):
    db.init_app(app)