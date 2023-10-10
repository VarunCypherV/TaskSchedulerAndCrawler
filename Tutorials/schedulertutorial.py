import helper
import schedule
import time
import threading
import datetime
from schedule import repeat,every

# def task():
#     print("doign task at ",helper.get_time())

#do task every 5 sec/hours/etc
# schedule.every(5).seconds.do(task)
# schedule.every(5).minutes.do(task)
# schedule.every(5).hours.do(task)
# schedule.every(5).days.do(task)
# schedule.every(5).weeks.do(task)

#each time at 15 second mark/minutes
# schedule.every().minute.at(':15').do(task) 
# schedule.every().hour.at(':15').do(task)
# schedule.every(10).hour.at(':15').do(task) #every 10 hours when min is 15

#schedule.every().day.at('15:15').do(task) every day at 15:15:00 time

# schedule.every().monday.do(task) , day sepecfici allows allowed

#going to do every 10 seconds 
# @repeat(every(10).seconds)
# def task2():
#     print("hi")
#==========================================
#Passing Aruguements to the task

# def task(arg1,arg2):
#     print("Doing task...",f'args={arg1,arg2}',helper.get_time())

# schedule.every(5).seconds.do(task , 10 ,"Mario")


# @repeat(every(10).seconds,5,'luigi)
# def task2(arg1,arg2):
#     print(f'args={arg1,arg2}',helper.get_time())
#=======================================================
#cancelling job
# job = schedule.every().hour.at(":30").do(task)
# schedule.cancel_job(job)
#=====================================================
#get all jobs
# print(schedule.get_jobs)
#print(len(schedule.get_jobs))
#======================================================
# def task():
#     print("doign task at ",helper.get_time())
#     schedule.CancelJob 
#running only once 
#=====================================================

# schedule.clear() deletes  all jobs

#=====================================================
#ASSOCIATION WITH TAGS

# def task():
#     print("doign task at ",helper.get_time())
# schedule.every().minute.do(task).tag("work","ramco","3")

# ramco=schedule.get_jobs("Ramco")
#=====================================================
#Running at random time
# schedule.every(1).to(10).seconds.do(task)
#every 1 to 10 second of gap this task happens
#=====================================================
#do task until specified time
# schedule.every(1).seconds.until("19:18").do(task)

# schedule.every(1).seconds.until(datetime(2024,12,31,10,20,15)).do(task)
#=====================================================
# schedule.run_all(delay_seconds=10)
#delay optional
#runs all tasks immediately but id delay then with delay gaps
#=====================================================
#performing threaded tasks
#OUR PREFERRED WAY RAMCO
# def start_thread(func):
#     job_one=threading.Thread(target=func)
#     job_one.start()

# def task():
#     print("doign task at ",helper.get_time())
#     time.sleep(5) #a alternate to api here so we impor threading
# schedule.every(1).seconds.do(start_thread,task)
#=====================================================

#====================================================
#FOR RAMCO
def start_thread():
    job_one = threading.Thread(target=task)
    job_one.start()

def task():
   print("doign task at ",helper.get_time())
   schedule.CancelJob


scheduled_datetime="2023-10-10 13:25:00"
schedule_date,scheduled_time=scheduled_datetime.split(" ")

if(datetime.datetime.now().strftime("%Y-%m-%d")==schedule_date):
    schedule.every().day.at(scheduled_time).do(start_thread)
    


#===========================================================
#MANDATORY CODE IN EVERY
while True:
    schedule.run_pending()
    #run the task that have fallen into that time frame
    time.sleep(1)