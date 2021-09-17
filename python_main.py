"""Contains the Functions for the Lunar Calendar Python Program"""

# Imports
import os
from calendar import monthrange, calendar
import datetime
import calendar
import mysql.connector
from colorama import Fore, Style
import config


def intro():
    """Introduction for the application"""
    os.system('cls')
    print("-------------------------")
    print("   MOON PHASE CALENDAR")
    print("-------------------------")


def get_year():
    """Input the year (for use with a larger dataset beyond 2021)"""
    try:
        year = input("Enter Year: ")
        year = int(year)
        if year > 2021 or year < 2000:
            os.system('cls')
            print("Accepted Values: 2000-2021")
            return get_year()
        else:
            os.system('cls')
            return year
    except ValueError:
        os.system('cls')
        print("Accepted Values: 2000-2021")
        return get_year()


def get_month():
    """Input the month"""
    try:
        month = input("Enter Month: ")
        month = int(month)
        if month > 13 or month < 1:
            os.system('cls')
            print("Accepted Values: 1-12")
            return get_month()
        else:
            os.system('cls')
            return month
    except ValueError:
        os.system('cls')
        print("Accepted Values: 1-12")
        return get_month()


def days_in_month(year, month):
    """Computes the number of days in the specified month"""
    num_days = monthrange(year, month)[1]
    return num_days


def get_month_name(month):
    """Returns string with month name"""
    datetime_object = datetime.datetime.strptime(str(month), "%m")
    month_name = str(datetime_object.strftime("%b"))
    return month_name


def display_month(month_name, num_days):
    """Displays a calendar format of the month so a user can see which days are in a month"""
    print("---------------------------")
    print("            " + str(month_name))
    print("---------------------------")
    for x in range(1, num_days + 1):
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
        elif x < num_days:
            print(str(x) + " ", end=" ")
        elif x == num_days:
            print(str(x) + " ", end=" ")
            print()
    print("---------------------------")


def get_day(month_name, num_days):
    """Input for specific day in month"""
    display_month(month_name, num_days)
    day = input("Enter Day: ")
    try:
        day = int(day)
        if day > num_days or day < 1:
            os.system('cls')
            print("Accepted Values: 1-" + str(num_days))
            return get_day(month_name, num_days)
        else:
            return day
    except ValueError:
        os.system('cls')
        print("Accepted Values: 1-" + str(num_days))
        return get_day(month_name, num_days)


def get_data(year, month_name, day):
    """Retrieves data from MySQL database:Lunar and table:moon_data"""
    os.system('cls')
    print("Retrieving Lunar Data...")
    my_db = mysql.connector.connect(host="localhost", user=config.username, port='3306', password=config.password)
    if my_db:
        print("Connection Successful")
        print()
    else:
        print("Connection Failed")
        print()
    my_cursor = my_db.cursor()
    my_cursor.execute("CREATE DATABASE IF NOT EXISTS Lunar")
    my_cursor.execute("USE Lunar")
    my_cursor.execute(
        "SELECT phase, moon_age from moon_data where year = '{}' AND month = '{}' AND day = '{}'".format(year,
                                                                                                         month_name,
                                                                                                         day))
    dat = my_cursor.fetchall()
    my_cursor.close()
    try:
        phase = str(dat[0][0])
        moon_age = int(dat[0][1].replace(' days', ''))
        moon_list = [phase, moon_age]
        return moon_list
    except IndexError:
        print("---------------------------")
        print("NO LUNAR DATA FOR THAT DATE.")
        print("---------------------------")
        print()
        rerun()


def day_header(year, month, day, month_name):
    """Displays the date as a header in the terminal"""
    print("---------------------------")
    print("    " + str(
        calendar.day_name[
            datetime.date(year, month, day).weekday()]) + ", " + month_name + " " + str(
        day) + ", " + str(year))
    print("---------------------------")


def moons(moon_list):
    """Contains ASCII moons and prints them out"""
    full_moon = """
   _..._     
 .:::::::.    
:::::::::::   FULL  MOON
::::::::::: 
`:::::::::'  
  `':::''
"""
    wain_gibbous = """
  _..._     
 .::::. `.    
:::::::.  :    WAINING GIBBOUS
::::::::  :  
`::::::' .'  
 `'::'-' 
"""
    second_quarter = """
   ..._     
 .::::  `.    
::::::    :    SECOND QUARTER
::::::    :  
`:::::   .'  
  `'::.-' 
"""
    wain_crescent = """
   _..._     
 .::'   `.    
:::       :    WAINING CRESCENT
:::       :  
`::.     .'  
  `':..-'    
"""
    new_moon = """
   _..._     
 .'     `.    
:         :    NEW MOON
:         :  
`.       .'  
  `-...-'  
"""
    wax_crescent = """
   _..._     
 .'   `::.    
:       :::    WAXING CRESCENT
:       :::  
`.     .::'  
  `-..:'' 
"""
    first_quarter = """
   _..._     
 .'  ::::.    
:    ::::::    FIRST QUARTER
:    ::::::  
`.   :::::'  
  `-.::''   
"""
    wax_gibbous = """
    _..._     
 .' .::::.    
:  ::::::::    WAXING GIBBOUS
:  ::::::::  
`. '::::::'  
  `-.::'' 
"""
    phase = moon_list[0]
    moon_age = moon_list[1]
    print(Fore.LIGHTYELLOW_EX)
    if phase == "NE":
        print(new_moon)
        print(Style.RESET_ALL)
        print("---------------------------")
    if phase == "Q1":
        print(first_quarter)
        print(Style.RESET_ALL)
        print("---------------------------")
    if phase == "FU":
        print(full_moon)
        print(Style.RESET_ALL)
        print("---------------------------")
    if phase == "Q3":
        print(second_quarter)
        print(Style.RESET_ALL)
        print("---------------------------")
    elif 1 <= moon_age < 8:
        print(wax_crescent)
        print(Style.RESET_ALL)
        print("---------------------------")
    elif 7 < moon_age < 15:
        print(wax_gibbous)
        print(Style.RESET_ALL)
        print("---------------------------")
    elif 15 <= moon_age < 22:
        print(wain_gibbous)
        print(Style.RESET_ALL)
        print("---------------------------")
    elif 22 <= moon_age <= 29:
        print(wain_crescent)
        print(Style.RESET_ALL)
        print("---------------------------")
    else:
        print(Style.RESET_ALL)
        print("MOON NOT FOUND.")
    rerun()


def rerun():
    """User option to rerun"""
    choice = input("Enter Q to quit, Enter to Run Again: ")
    print(choice)
    if choice == "Q":
        print("f")
        exit()
    else:
        main()


def main():
    """Main method"""
    intro()
    # Creating date variables
    year = get_year()
    month = get_month()
    num_days = days_in_month(year, month)
    month_name = get_month_name(month)
    day = get_day(month_name, num_days)
    data = get_data(year, month_name, day)
    # Active methods
    day_header(year, month, day, month_name)
    moons(data)


main()
