import time
import schedule
import threading
import datetime
from schedule import repeat,every


def get_time() -> str: #return type is specified using -> str meaning return type is string
    return time.strftime("%X (%d/%m/%y)")

#FOR RAMCO
def start_thread():
    job = threading.Thread(target=task)
    job.start()

def task():
   print("doign task at ",get_time())
   schedule.CancelJob


def schedulemytask(scheduled_datetime,dbid,empid,reportName):
    schedule_date,scheduled_time=scheduled_datetime.split(" ")
    #Need to add a check that at the specified scheduled_time , if there is a task with same 3 tags at the same time already= omit scheudling    
    if(datetime.datetime.now().strftime("%Y-%m-%d")==schedule_date and schedule.get_jobs(empid,reportName)==[]):
        schedule.every().day.at(scheduled_time).do(start_thread).tag(dbid,empid,reportName)
    
while True:
    schedule.run_pending()     #run the task that have fallen into that time frame
    time.sleep(1)