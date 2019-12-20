"""
#Auto shutdown and push notification
#Author: Nazrul
#URI: https://github.com/Nazrul5043
#Email: mdnazrul5043@gmail.com
"""
import platform
import cpuinfo
import psutil
import os
import subprocess
from datetime import datetime


def main(office_closing_time_string,lunch_time):
    #get current time
    now = datetime.now().replace(microsecond=0)
    #convert string to datetime formate
    office_closing_date_time = datetime.strptime(office_closing_time_string, "%H:%M:%S")
    time_stamp = now.replace(hour=office_closing_date_time.time().hour, minute=office_closing_date_time.time().minute, second=office_closing_date_time.time().second, microsecond=0)
    #get cpu up time
    uptime = check_uptime()

    if(now.time() == lunch_time):
        #push notification
        print("Stop Workings,Its Lunch time.")
    if(now > time_stamp):
        auto_shutdown()
    else:
        print("Up Time",uptime)
            
    
def check_uptime():
    boot_start_time = datetime.fromtimestamp(psutil.boot_time())
    now_time = datetime.now().replace(microsecond=0)
    uptime = now_time - boot_start_time
    #print("Up Time",now_time -boot_start_time)
    return (now_time - boot_start_time)

def auto_shutdown():
    #shutdown
    subprocess.call(["shutdown", "-f", "-s", "-t", "1"])
    #print("shutdown")

        
if __name__ == "__main__":
    office_closing_time_string = "17:30:00"
    lunch_time = "13:00:00"
    main(office_closing_time_string,lunch_time)
 

