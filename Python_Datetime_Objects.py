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
# datetime.__format__(format). 
# Same as datetime.strftime(). This makes it possible to specify a format string for a datetime object in formatted string literals and when using str.format
# (). 
#
# Examples of working with datetime objects:
# 

from datetime import datetime, date, time

# Using datetime.combine()

d = date(2005, 7, 14)
t = time(12, 30)

datetime.combine(d, t)

# OUTPUT: 'datetime.datetime(2005, 7, 14, 12, 30)'

# Using datetime.now() or datetime.utcnow()

datetime.now()   

# OUTPUT: 'datetime.datetime(2007, 12, 6, 16, 29, 43, 79043)'   # GMT +1

datetime.utcnow()   

# OUTPUT: 'datetime.datetime(2007, 12, 6, 15, 29, 43, 79060)'

# Using datetime.strptime()

dt = datetime.strptime("21/11/06 16:30", "%d/%m/%y %H:%M")
dt

# OUTPUT: 'datetime.datetime(2006, 11, 21, 16, 30)'

# Using datetime.timetuple() to get tuple of all attributes

tt = dt.timetuple()

     for it in tt:   
        print(it)

# 2006    # year
# 11      # month
# 21      # day
# 16      # hour
# 30      # minute
# 0       # second
# 1       # weekday (0 = Monday)
# 325     # number of days since 1st January
# -1      # dst - method tzinfo.dst() returned None

# Date in ISO format

ic = dt.isocalendar()

    for it in ic:   
        print(it)

# 2006    # ISO year
# 47      # ISO week
# 2       # ISO weekday

# Formatting datetime

dt.strftime("%A, %d. %B %Y %I:%M%p")

# OUTPUT: 'Tuesday, 21. November 2006 04:30PM'

'The {1} is {0:%d}, the {2} is {0:%B}, the {3} is {0:%I:%M%p}.'.format(dt, "day", "month", "time")

# OUTPUT: 'The day is 21, the month is November, the time is 04:30PM.'
 
#
# Using datetime with tzinfo:
# 

from datetime import timedelta, datetime, tzinfo

class GMT1(tzinfo):

        def utcoffset(self, dt):
            return timedelta(hours=1) + self.dst(dt)

        def dst(self, dt):

            # DST starts last Sunday in March

            d = datetime(dt.year, 4, 1)   # ends last Sunday in October
            self.dston = d - timedelta(days=d.weekday() + 1)

            d = datetime(dt.year, 11, 1)
            self.dstoff = d - timedelta(days=d.weekday() + 1)

            if self.dston <=  dt.replace(tzinfo=None) < self.dstoff:
                return timedelta(hours=1)

            else:
                return timedelta(0)

        def tzname(self,dt):
             return "GMT +1"

    class GMT2(tzinfo):

        def utcoffset(self, dt):
            return timedelta(hours=2) + self.dst(dt)

        def dst(self, dt):
            d = datetime(dt.year, 4, 1)
            self.dston = d - timedelta(days=d.weekday() + 1)

            d = datetime(dt.year, 11, 1)
            self.dstoff = d - timedelta(days=d.weekday() + 1)

            if self.dston <=  dt.replace(tzinfo=None) < self.dstoff:
                return timedelta(hours=1)

            else:
                return timedelta(0)

        def tzname(self,dt):
            return "GMT +2"

gmt1 = GMT1()

# Daylight Saving Time

dt1 = datetime(2006, 11, 21, 16, 30, tzinfo=gmt1)
dt1.dst()

# OUTPUT: 'datetime.timedelta(0)'

dt1.utcoffset()

# OUTPUT: 'datetime.timedelta(seconds=3600)'

dt2 = datetime(2006, 6, 14, 13, 0, tzinfo=gmt1)
dt2.dst()

# OUTPUT: 'datetime.timedelta(seconds=3600)'

dt2.utcoffset()

# OUTPUT: 'datetime.timedelta(seconds=7200)'

# Convert datetime to another time zone

dt3 = dt2.astimezone(GMT2())
dt3     # doctest: +ELLIPSIS

# OUTPUT: 'datetime.datetime(2006, 6, 14, 14, 0, tzinfo=<GMT2 object at 0x...>)'

dt2     # doctest: +ELLIPSIS

# OUTPUT: 'datetime.datetime(2006, 6, 14, 13, 0, tzinfo=<GMT1 object at 0x...>)'

dt2.utctimetuple() == dt3.utctimetuple()

# OUTPUT: 'True'
