from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime


def say_hello():
    print("Hello from code, time:", datetime.now().time())
    
def inform():
    print("---INFORMATION---")
    
scheduler = BlockingScheduler()
scheduler.add_job(say_hello, 'interval', seconds=0)
scheduler.add_job(inform, 'interval', seconds=2)
scheduler.start()

print("Hello")


