import pendulum

def exam(end_year, end_month, end_day):
    start = pendulum.now()
    end = pendulum.datetime(end_year, end_month, end_day)
    period = end - start
    print("You still have: " + str(period.days) + " days! ")
    return "Good Luck! "