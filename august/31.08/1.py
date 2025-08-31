from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime


def say_hello():
    print("Hello from code, time:", datetime.now().time())
    
scheduler = BlockingScheduler()
scheduler.add_job(say_hello, 'interval', seconds=5)
scheduler.start()


