
from socialgroupmain.configuration.config import schedule_tasks,api,app
from datetime import datetime
from socialgroupmain.scheduler_tasks.del_inactive_users import inactive_users
from socialgroupmain.scheduler_tasks.daily_feed import dailyfeed




"""these are commented to prevent from execution in trial runs
    Remove the comment tag and feed the desired frequency and interval for the run"""

"""The tasks which need to occur frequently at set intervals are performed using the schedule_tasks function
    The description of arguments for the schedule_tasks function is as follows:
    1. The first argument is time for first execution
    2. Function to be assigned in scheduler
    3. frequency i.e. interval after which the function runs again in seconds
    4. No of repetitions None means repeat forever"""


# today_mid = datetime.combine(date.today(), datetime.min.time()) + timedelta(hours=24)
# schedule_tasks(today_mid,dailyfeed,86400,None)

# schedule_tasks(today_mid,inactive_users,86400*2,None)



