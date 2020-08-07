# import logging
# try:
#     from cStringIO import StringIO
# except ImportError:
#     from io import StringIO
#
# log_stream = StringIO()
# logging.basicConfig(stream=log_stream, level=logging.INFO)

from pymongo import MongoClient
from pymongo import ASCENDING
import datetime

obj = MongoClient()
datab = obj.my_logs
log_collection = datab.log


log_collection.ensure_index([("timestamp", ASCENDING)])


def log(msg):
    """Log `msg` to MongoDB log"""
    entry = {}
    entry['timestamp'] = datetime.datetime.utcnow()
    entry['msg'] = msg
    log_collection.insert(entry)

log('Log messages like this')