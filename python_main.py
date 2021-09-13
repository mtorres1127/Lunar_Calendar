from calendar import monthrange
import datetime

month_outer = 0
year_outer = 0
num_days_outer = 0
day_outer = 0


def intro():
    print("-------------------------")
    print("MOON PHASE CALENDAR 2021 ")
    print("-------------------------")


def get_year():
    print("Enter Year (2000-2021): ")
    year = int(input())
    if year > 2021 or year < 2000:
        print("Enter 2000-2021")
        get_year()
    else:
        global year_outer
        year_outer = year


def get_month():
    print("Enter Month (1-12): ")
    month = int(input())
    if month > 13 or month < 1:
        print("Enter 1-12")
        get_month()
    else:
        global month_outer
        month_outer = month


def days_in_month():
    num_days = monthrange(year_outer, month_outer)[1]
    global num_days_outer
    num_days_outer = num_days


def display_month():
    datetime_object = datetime.datetime.strptime(str(month_outer), "%m")
    month_name = datetime_object.strftime("%b")

    print("---------------------------")
    print("            " + month_name)
    print("---------------------------")
    # print(num_days)
    for x in range(1, num_days_outer + 1):
        if x < 7:
            print(str(x) + "  ", end=" ")
        elif x == 7:
            print(str(x) + "  ", end=" ")
            print()
        elif x < 10:
            print(str(x) + "  ", end=" ")
        elif x < 14:
            print(str(x) + " ", end=" ")
        elif x == 14:
            print(str(x) + " ", end=" ")
            print()
        elif x < 21:
            print(str(x) + " ", end=" ")
        elif x == 21:
            print(str(x) + " ", end=" ")
            print()
        elif x < 28:
            print(str(x) + " ", end=" ")
        elif x == 28:
            print(str(x) + " ", end=" ")
            print()
        elif x < num_days_outer:
            print(str(x) + " ", end=" ")
        elif x == num_days_outer:
            print(str(x) + " ", end=" ")
            print()
    print("---------------------------")


def get_day():
    print("Enter Day: ")
    day = int(input())
    if day > num_days_outer or day < 1:
        print("Enter 1-" + str(day))
        get_day()
    else:
        global day_outer
        day_outer = day


def get_phase():
    print()


intro()
get_year()
get_month()
days_in_month()
display_month()
get_day()
