# Group: PSITTACOSAURUS
# Members:
#   Ben Meister
#   Samman Regmi
#   Trisha Carter
#   Calvin Idom
#   Cameron McCarthey
#   Nabinta Niraula
#   Reese Seals

import sys                      # For stdin and stdout
import datetime                 # For working with datetimes
from math import floor          # Flooring...
from hashlib import md5         # For hashing


# Debugger constant to use a past 'current' time
DEBUG = False
DATE = "2017 04 26 15 14 30"
msg = ""


# To exit with/without a message cleanly. 
def exit():
    global msg
    sys.exit(msg)


# Generate the passcode.
def getPassCode(string):
    passcode = ""
    for c in string:                        # Iterate through the hash string,
        if(len(passcode) >= 2):             # Until we have 2 letters, i.e. a length of two.
            break
        if(c.isalpha()):                    # Determines if character is a letter.
            passcode += c                   # Adds character to passcode.
    
    for c in reversed(string):              # Iterate through the hash string reversed
        if(len(passcode) >= 4):             # Until we have two numbers, i.e. a length of four.
            break
        if(c.isdigit()):                    # Determines if the character is a digit 0-9.
            passcode += c                   # Adds the character to passcode.
    return                                  # return...


# Determines if the datetime is in dst and if so, sets the date back 1 hour.
def dst(date):
    year = date.year        # Gets the year we are looking at.
    startmonth = 3          # variable for March.
    endmonth = 11           # Variable for November.
    # DST ALWAYS starts on the SECOND SUNDAY of MARCH at 2:00 AM and ends on the FIRST SUNDAY of NOVEMBER at 2:00 AM. 
    # Since the earliest the second Sunday can occur is the 8th, we guess this date for March. 
    # Since the earliest the first Sunday can occur is the 1st, we guess this date for November.
    dststart = datetime.datetime(year, startmonth, 8, 2, 0, 0)
    dstend = datetime.datetime(year, endmonth, 1, 2, 0, 0)
    m = dststart.weekday()      # Get the day of the week for March 8th.
    if(m != 6):                 # If the weekday is not Sunday, then change it to be the next Sunday.
        dststart = dststart.replace(day=(8 + (6 - m) % 7))
    n = dstend.weekday()        # Get the day of the week for November 1st.
    if(n!= 6):                  # If the weekday is not Sunday, then change it to be the next Sunday.
        dstend = dstend.replace(day=(1 + (6 - n) % 7))
    # If the date falls in between the start and end, turn the time back 1 hour to be in non-dst time.
    if(dststart <= date <= dstend):
        date -= datetime.timedelta(hours=1)
    # return the correct non-dst datetime
    return date


# Main
def main(debug, date):
    global msg
    if(not debug):                      # Changes date to Systems Current Time otherwise date will stay as is.
        date = datetime.datetime.now()
    date = dst(date)                    # Changes date time to non-dst time
    # For every given epoch time...
    for line in sys.stdin:
        try:
            epoch = datetime.datetime.strptime(line, "%Y %m %d %H %M %S")       # If the string does not contain a new line.
        except ValueError:
            epoch = datetime.datetime.strptime(line[:-1], "%Y %m %d %H %M %S")  # If the string does contain a new line.
        
        epoch = dst(epoch)              # Changes epoch time to non-dst time

        # If-else is used for reverting to the correct starting second of the epoch time. Allows for a passcode to be valid for 60s.
        if(date.second >= epoch.second):
            date = date.replace(second=epoch.second)
        else:
            date = date - datetime.timedelta(minutes=1)
            date = date.replace(second=epoch.second)

        diff = floor((date - epoch).total_seconds())            # Determines the seconds elapsed and cuts off anything less than seconds (i.e. milliseconds...)
        # print(f'Start: {epoch}\nEnd: {date}\nDiff: {diff}')

        # Just in case someone tries to use an epoch time in the future. 
        # Although this could be another aspect for security if the epoch time is not limited to just the past. Something to think about....
        if(diff < 0):
            msg = "TIME TRAVELING ARE WE?......\nMAYBE SUPPORT FOR YOUR KIND OF TRAVEL WILL BE ADDED IN THE FUTURE, BUT YOU WOULD KNOW THAT AY....."
            exit()

        # Hashing...
        hasher = md5(str(diff).encode()).hexdigest()
        hashed = md5(str(hasher).encode()).hexdigest()
        # print(hashed)
        passcode = getPassCode(hashed)          # Generate passcode
        sys.stdout.write(passcode)              # Output passcode to stdout (print).

    exit()                                      # exit...




DATE = datetime.datetime.strptime(DATE, "%Y %m %d %H %M %S")
main(DEBUG, DATE)