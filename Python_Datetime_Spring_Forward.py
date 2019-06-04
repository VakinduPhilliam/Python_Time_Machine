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
# When DST starts (the “start” line), the local wall clock leaps from 1:59 to 3:00. A wall time of the form 2:MM doesn’t really make sense on that day, so
# astimezone(Eastern) won’t deliver a result with hour == 2 on the day DST begins.
#
# For example, at the Spring forward transition of 2016, we get;
# 

from datetime import datetime, timezone
from tzinfo_examples import HOUR, Eastern

u0 = datetime(2016, 3, 13, 5, tzinfo=timezone.utc)

for i in range(4):
        u = u0 + i*HOUR
        t = u.astimezone(Eastern)
