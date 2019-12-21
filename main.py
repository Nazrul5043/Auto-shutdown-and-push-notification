"""
#Auto shutdown and push notification
#Author: Nazrul
#URI: https://github.com/Nazrul5043
#Email: mdnazrul5043@gmail.com
"""
import platform
import cpuinfo
import psutil
from plyer import notification
import os
import subprocess
from datetime import datetime,timedelta
import time


def main(refresh_time,lunch_time,office_closing_time_string,r):
    #get current time
    now = datetime.now().replace(microsecond=0)
    
    #convert string to datetime formate
    office_closing_date_time = datetime.strptime(office_closing_time_string, "%H:%M:%S")
    time_stamp = now.replace(hour=office_closing_date_time.time().hour, minute=office_closing_date_time.time().minute, second=office_closing_date_time.time().second, microsecond=0)

    #comvert lunch time
    lunch_date_time = datetime.strptime(lunch_time, "%H:%M:%S")
    lunch_time_stamp = now.replace(hour=lunch_date_time.time().hour, minute=lunch_date_time.time().minute, second=lunch_date_time.time().second, microsecond=0)

    #get cpu up time
    uptime = str(check_uptime())

    if now == lunch_time_stamp:
        #push notification
        title = "Warning"
        message = "Stop Workings,Its Lunch time."
        app_name = "Time Checker"
        timeout = 60
        push_notification(title,message,app_name,timeout)
    elif uptime == refresh_time:
        #push notification
        title = "Warning"
        message = "Stop Workings for 5 mins."
        app_name = "Time Checker"
        timeout = 60
        push_notification(title,message,app_name,timeout)
        r+=1
        refresh_time = str(r)+":00:00"
    elif now > time_stamp:
        auto_shutdown()
    else:
        pass
    #again call main function
    time.sleep(1)
    main(refresh_time,lunch_time,office_closing_time_string,r)
    
def check_uptime():
    boot_start_time = datetime.fromtimestamp(psutil.boot_time())
    now_time = datetime.now().replace(microsecond=0)
    uptime = now_time - boot_start_time
    return (now_time - boot_start_time)

def auto_shutdown():
    #shutdown
    #subprocess.call(["shutdown", "-f", "-s", "-t", "1"])
    #restart
    #subprocess.call(["shutdown", "-f", "-r", "-t", "1"])
    print("shutdown")
def push_notification(title,message,app_name,timeout):
    if platform.system() == "Windows":
        app_icon = 'icon/timemachine.ico'
    else:
        app_icon = 'icon/alarm-icon.png'
    notification.notify(
        title = title,
        message = message,
        app_name = app_name,
        app_icon = app_icon,
        timeout =  timeout
        )
        
if __name__ == "__main__":
    office_closing_time_string = "17:30:00"
    lunch_time = "13:00:00"
    refresh_time = "1:00:00"
    r = 1
    while True:
        main(refresh_time,lunch_time,office_closing_time_string,r)
        time.sleep(1)
 

