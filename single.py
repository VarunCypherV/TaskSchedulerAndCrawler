import pypyodbc as odbc 
#pip install pypyodbc
#pip install schedule
import time
import schedule
import threading
import datetime


#====================================MS SQL CONNECTION
DRIVER_NAME = 'SQL SERVER'
SERVER_NAME ='VARUN'
DATABASE_NAME='RAMCO_TESTDB'

    # uid=<username>;
    # pwd=<password>;

connection_string = f"""
    DRIVER={{{DRIVER_NAME}}};
    SERVER={SERVER_NAME};
    DATABASE={{{DATABASE_NAME}}};
    Trusted_Connection=yes;
"""

conn = odbc.connect(connection_string)
print(conn)

#==========================================UTILITY FUNCTIONS

def get_time() -> str: #return type is specified using -> str meaning return type is string
    return time.strftime("%X (%d/%m/%y)")

def format_datetime(dt):
    return dt.strftime('%Y-%m-%d %H:%M:%S')

def create_tag(scheduled_datetime,empid,reportName):
    return str(scheduled_datetime)+str(empid)+reportName+str(reportName)
#=================================================THREADING AND CRAWLER (TASK WILL BE MODIFIED TO CRAWLER)=======
def start_thread():
    job = threading.Thread(target=task)
    job.start()

def task():
   print("doign task at ",get_time())
   return schedule.CancelJob 

#==========================================PROJECT OBJECTIVE DRIVEN FUNCTIONS
def ExecuteQuery():
    print("fetched at " ,get_time())
    cursor = conn.cursor()
    query = "SELECT * FROM Test2"
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    for row in rows:
        dbidd, empid, reportname, needtime = row
        formatted_needtime = format_datetime(needtime)
        print(f"DBidd: {dbidd}, EmpId: {empid}, ReportName: {reportname}, NeedTime: {formatted_needtime}")
        schedulemytask(formatted_needtime,empid,reportname)

schedule.every().minute.do(ExecuteQuery) #ENTRY POINT IN THE CODE 

def schedulemytask(scheduled_datetime,empid,reportName):
    schedule_date,scheduled_time=scheduled_datetime.split(" ")
    generated_tag=create_tag(scheduled_datetime,empid,reportName)
    if(datetime.datetime.now().strftime("%Y-%m-%d")==schedule_date and schedule.get_jobs(generated_tag)==[]):
        schedule.every().day.at(scheduled_time).do(start_thread).tag(generated_tag)
    

while True:
    schedule.run_pending()
    time.sleep(1)





