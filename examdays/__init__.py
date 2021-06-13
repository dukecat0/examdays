import pendulum
import sys


class style:
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"


def exam(end_year, end_month, end_day):
    start = pendulum.now()
    end = pendulum.datetime(end_year, end_month, end_day)
    period = end - start
    print(style.YELLOW + "You still have: " + str(period.days) + " days! ")
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
    try:
        change_colour = sys.argv[4]
    except IndexError:
        print("You still have: " + str(period.days) + " days!")
        print("Good Luck! ")
        return False
    if change_colour == "BLACK" or change_colour == "black":
        print(style.BLACK + "You still have: " + str(period.days) + " days!")
        print(style.BLACK + "Good Luck! ")
    elif change_colour == "RED" or change_colour == "red":
        print(style.RED + "You still have: " + str(period.days) + " days!")
        print(style.RED + "Good Luck! ")
    elif change_colour == "GREEN" or change_colour == "green":
        print(style.GREEN + "You still have: " + str(period.days) + " days!")
        print(style.GREEN + "Good Luck! ")
    elif change_colour == "YELLOW" or change_colour == "yellow":
        print(style.YELLOW + "You still have: " + str(period.days) + " days!")
        print(style.YELLOW + "Good Luck! ")
    elif change_colour == "BLUE" or change_colour == "blue":
        print(style.BLUE + "You still have: " + str(period.days) + " days!")
        print(style.BLUE + "Good Luck! ")
    elif change_colour == "MAGENTA" or change_colour == "magenta":
        print(style.MAGENTA + "You still have: " + str(period.days) + " days!")
        print(style.MAGENTA + "Good Luck! ")
    elif change_colour == "CYAN" or change_colour == "cyan":
        print(style.CYAN + "You still have: " + str(period.days) + " days!")
        print(style.CYAN + "Good Luck! ")
    elif change_colour == "WHITE" or change_colour == "white":
        print(style.WHITE + "You still have: " + str(period.days) + " days!")
        print(style.WHITE + "Good Luck! ")
    else:
        print("PLease Enter A Correct Colour.")
