import datetime
import time
import os

# https://www.geeksforgeeks.org/get-current-date-and-time-using-python/

def clock_function():
    while True:
        current_time = datetime.datetime.now()
        current_year = current_time.year
        current_month = current_time.month
        current_day = current_time.day

        current_hour = current_time.hour
        current_minute = current_time.minute
        current_second = current_time.second
        date_string = str(current_year) + "/" + str(current_month) + "/" + str(current_day)
        time_string = str(current_hour) + ":" + str(current_minute) + ":" + str(current_second)
    
        print(time_string)
        time.sleep(1)
    
        # print()
        if os.name == "nt":
            os.system("cls")
        elif os.name == "posix":
            os.system("clear")

clock_function()

    
