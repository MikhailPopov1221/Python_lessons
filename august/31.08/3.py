from apscheduler.schedulers.background import BackgroundScheduler
import time

def say():
    print("Работа в фоне")

scheduler = BackgroundScheduler()
scheduler.add_job(say, 'interval', seconds=2)
scheduler.start()

time.sleep(10)
