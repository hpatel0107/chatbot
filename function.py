import datetime
import pandas as pd

attendance=pd.read_csv("attendance.csv")

def get_current_date():
    date = datetime.datetime.now().strftime('%Y-%m-%d')
    print(f'The current date is: {date}')

def get_current_time():
    time = datetime.datetime.now().strftime('%H:%M:%S')
    print(f'The current time is: {time}')
get_current_date()
get_current_time()

def get_attendance():

    identifier = input("Enter the name or ID of the person: ")
    for row in attendance:
        if row['name'] == identifier:
            print(row['percentage of present day'])
        if  row['id'] == identifier:
            print(row['percentage of present day'])
            break
    else:
        print(f"No data found for identifier '{identifier}'")
get_attendance()