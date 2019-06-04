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
# datetime.isoformat(sep='T', timespec='auto'). 
# Return a string representing the date and time in ISO 8601 format, YYYY-MM-DDTHH:MM:SS.ffffff or, if microsecond is 0, YYYY-MM-DDTHH:MM:SS
# 
# If utcoffset() does not return None, a string is appended, giving the UTC offset: YYYY-MM-DDTHH:MM:SS.ffffff+HH:MM[:SS[.ffffff]] or, if microsecond is
# 0 YYYY-MM-DDTHH:MM:SS+HH:MM[:SS[.ffffff]].
# 
# The optional argument sep (default 'T') is a one-character separator, placed between the date and time portions of the result. For example,
# 

from datetime import tzinfo, timedelta, datetime

class TZ(tzinfo):
        def utcoffset(self, dt): return timedelta(minutes=-399)

datetime(2002, 12, 25, tzinfo=TZ()).isoformat(' ')

# OUTPUT: '2002-12-25 00:00:00-06:39'

#
# ValueError will be raised on an invalid timespec argument.
# 

from datetime import datetime

datetime.now().isoformat(timespec='minutes')   # doctest: +SKIP

# OUTPUT: '2002-12-25T00:00'

dt = datetime(2015, 1, 1, 12, 30, 59, 0)
dt.isoformat(timespec='microseconds')

# OUTPUT: '2015-01-01T12:30:59.000000'
