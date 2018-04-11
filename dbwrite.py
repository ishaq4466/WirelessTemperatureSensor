#==========DISPLAYING AND WRITING DATA TO THE DATABASE=======
#This script is similar to the 'dispdata.py' however in this 
#script we not only display the data to the console screen
#but also write it to the 'tempdb' database please make sure that the 
#mysqldb is installed with creation of the 'tempdb' database
#(for installation of MySQLdb and configuring it please check the dbconf.txt)

import time
import datetime
import glob
import MySQLdb
from time import strftime

#os.system('modprobe w1-gpio')
#os.system('modprobe w1-therm')
temp_sensor = '/var/www/html/temp'

# connecting to the database, do enter the passwd 
db = MySQLdb.connect(host="localhost", user="root",passwd="pswd", db="tempdb")
cur = db.cursor()

def tempRead():
    t = open(temp_sensor, 'r')
    lines = t.readlines()
    t.close()

    temp_output = lines[1].find('t=')
    if temp_output != -1:
        temp_string = lines[1].strip()[temp_output+2:]
        temp_c = float(temp_string)/1000.0
    return round(temp_c,1)


# In the while loop do remember the data is inserted into 
#'tempdb.templog' table
while True:
    temp = tempRead()
    print temp
    datetimeWrite = (time.strftime("%Y-%m-%d ") + time.strftime("%H:%M:%S"))
    print datetimeWrite
    sql = ("""INSERT INTO templog (date,temperature) VALUES (%s,%s)""",(datetimeWrite,temp))
    try:
        print "Writing to database..."
        # Execute the SQL command
        cur.execute(*sql)
        # Commit your changes in the database
        db.commit()
        print "Write Complete"

    except:
        # Rollback in case there is any error
        db.rollback()
        print "Failed writing to database"

    cur.close()
    db.close()
    break
