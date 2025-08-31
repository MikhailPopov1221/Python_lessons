from apscheduler.schedulers.background import BackgroundScheduler
import time
from datetime import datetime, timedelta

def say():
    print("Ежедневная задача")

scheduler = BackgroundScheduler()
# scheduler.add_job(say, 'cron', hour=19, minute=3)
scheduler.add_job(
    say, 
    'cron', 
    day_of_week='mon,wen',
    months='1,2',
    hour='8-18/2', 
    minute=0)
scheduler.start()

while True:
    pass
