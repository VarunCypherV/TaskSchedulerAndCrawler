import pypyodbc as odbc #pip install pypyodbc
#pip install schedule
import time
import schedule
from helper import schedulemytask,get_time

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

#==========================================

def format_datetime(dt):
    return dt.strftime('%Y-%m-%d %H:%M:%S')

def ExecuteQuery():
    print("fetched at " ,get_time )
    cursor = conn.cursor()
    query = "SELECT * FROM Test2"
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    for row in rows:
        dbidd, empid, reportname, needtime = row
        formatted_needtime = format_datetime(needtime)
        print(f"DBidd: {dbidd}, EmpId: {empid}, ReportName: {reportname}, NeedTime: {formatted_needtime}")
        schedulemytask(formatted_needtime,dbidd,empid,reportname)

schedule.every().minute.do(ExecuteQuery)


while True:
    schedule.run_pending()
    time.sleep(1)





