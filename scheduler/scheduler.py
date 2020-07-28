from configuration.config import scheduler


def schedule_tasks(firstexec,funcexec,duration,freq):

    scheduler.schedule(
        scheduled_time=firstexec,            # Time for first execution, datetime.min for 00:00
        func=funcexec(),                     # Function to be queued
        args=[],             # Arguments passed into function when executed
        kwargs={},         # Keyword arguments passed into function when executed
        interval=duration,                   # Time before the function is called again, in seconds
        repeat=freq,                     # Repeat this number of times (None means repeat forever)
        meta={}            # Arbitrary pickleable data on the job itself
    )

    # scheduler.schedule(
    #     # scheduled_time=datetime.min, # Time for first execution
    #     scheduled_time=datetime.now(),
    #     func=inactive_users(),  # Function to be queued
    #     args=[],  # Arguments passed into function when executed
    #     kwargs={},  # Keyword arguments passed into function when executed
    #     # interval=172800,                   # Time before the function is called again, in seconds
    #     interval=60,
    #     # repeat=None,                     # Repeat this number of times (None means repeat forever)
    #     repeat=1,
    #     meta={}  # Arbitrary pickleable data on the job itself
    # )

