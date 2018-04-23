from apscheduler.schedulers.blocking import BlockingScheduler
from dbConnect import connect
#import time

schedule = BlockingScheduler()

@schedule.scheduled_job('interval', seconds=1)
def timed_job():
    #start_time = time.time()
    connect()
    #print("--- %s seconds ---" % (time.time() - start_time)) 

schedule.start()