from apscheduler.schedulers.background import BackgroundScheduler
import time
from datetime import datetime, timedelta

def say():
    print("Работа в фоне")

scheduler = BackgroundScheduler()
scheduler.add_job(say, 'date', run_date = datetime.now() + timedelta(seconds=5))
scheduler.start()

while True:
    pass
