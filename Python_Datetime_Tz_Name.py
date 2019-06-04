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
# time.tzname(). 
# If tzinfo is None, returns None, else returns self.tzinfo.tzname(None), or raises an exception if the latter doesn’t return None or a string object.
# 
# Example:
# 

from datetime import time, tzinfo, timedelta

class GMT1(tzinfo):

        def utcoffset(self, dt):
            return timedelta(hours=1)

        def dst(self, dt):
            return timedelta(0)

        def tzname(self,dt):
            return "Europe/Prague"

t = time(12, 10, 30, tzinfo=GMT1())
t                               # doctest: +ELLIPSIS

# OUTPUT: 'datetime.time(12, 10, 30, tzinfo=<GMT1 object at 0x...>)'

gmt = GMT1()

t.isoformat()

# OUTPUT: '12:10:30+01:00'

t.dst()

# OUTPUT: 'datetime.timedelta(0)'

t.tzname()

# OUTPUT: 'Europe/Prague'

t.strftime("%H:%M:%S %Z")

# OUTPUT: '12:10:30 Europe/Prague'

'The {} is {:%H:%M}.'.format("time", t)

# OUTPUT: 'The time is 12:10.'
