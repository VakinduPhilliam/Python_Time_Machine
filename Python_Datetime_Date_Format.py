# Python Datetime
# datetime — Basic date and time types.
# The datetime module supplies classes for manipulating dates and times in both simple and complex ways. While date and time arithmetic is supported, the
# focus of the implementation is on efficient attribute extraction for output formatting and manipulation.
# There are two kinds of date and time objects: “naive” and “aware”.
# An aware object has sufficient knowledge of applicable algorithmic and political time adjustments, such as time zone and daylight saving time information,
# to locate itself relative to other aware objects. An aware object is used to represent a specific moment in time that is not open to interpretation.
# A naive object does not contain enough information to unambiguously locate itself relative to other date/time objects. Whether a naive object represents
# Coordinated Universal Time (UTC), local time, or time in some other timezone is purely up to the program, just like it is up to the program whether a
# particular number represents metres, miles, or mass. Naive objects are easy to understand and to work with, at the cost of ignoring some aspects of
# reality.
#
# date.__format__(format). 
# Same as date.strftime(). This makes it possible to specify a format string for a date object in formatted string literals and when using str.format().
#
# Example of counting days to an event:
# 

import time
from datetime import date

today = date.today()
today
datetime.date(2007, 12, 5)

today == date.fromtimestamp(time.time())

# OUTPUT: 'True'

my_birthday = date(today.year, 6, 24)
if my_birthday < today:

my_birthday = my_birthday.replace(year=today.year + 1)

my_birthday
datetime.date(2008, 6, 24)

time_to_birthday = abs(my_birthday - today)
time_to_birthday.days

# OUTPUT: '202'
 
#
# Example of working with date:
# 

from datetime import date

d = date.fromordinal(730920) # 730920th day after 1. 1. 0001

d

# OUTPUT: 'datetime.date(2002, 3, 11)'

t = d.timetuple()

       for i in t:     
        print(i)

# 2002                # year
# 3                   # month
# 11                  # day
# 0
# 0
# 0
# 0                   # weekday (0 = Monday)
# 70                  # 70th day in the year
# -1

ic = d.isocalendar()

       for i in ic:    
        print(i)

# 2002                # ISO year
# 11                  # ISO week number
# 1                   # ISO day number ( 1 = Monday )

d.isoformat()

# OUTPUT: '2002-03-11'

d.strftime("%d/%m/%y")

# OUTPUT: '11/03/02'

d.strftime("%A %d. %B %Y")

# OUTPUT: 'Monday 11. March 2002'

'The {1} is {0:%d}, the {2} is {0:%B}.'.format(d, "day", "month")

# OUTPUT: 'The day is 11, the month is March.'
