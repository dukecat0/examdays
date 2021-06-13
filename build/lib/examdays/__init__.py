import pendulum
import sys

def exam(end_year, end_month, end_day):
    start = pendulum.now()
    end = pendulum.datetime(end_year, end_month, end_day)
    period = end - start
    print("You still have: " + str(period.days) + " days! ")
    return "Good Luck! "

def cli():
    end_year = sys.argv[1]
    end_month = sys.argv[2]
    end_day = sys.argv[3]
    new_end_year = int(end_year)
    new_end_month = int(end_month) 
    new_end_day = int(end_day)
    start = pendulum.now()
    end = pendulum.datetime(new_end_year, new_end_month, new_end_day)
    period = end - start
    print("You still have: " + str(period.days) + " days!")
    print("Good Luck! ")
