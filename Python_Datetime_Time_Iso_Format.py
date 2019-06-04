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
# time.isoformat(timespec='auto'). 
# Return a string representing the time in ISO 8601 format, HH:MM:SS.ffffff or, if microsecond is 0, HH:MM:SS If utcoffset() does not return None, a string
# is appended, giving the UTC offset: HH:MM:SS.ffffff+HH:MM[:SS[.ffffff]] or, if self.microsecond is 0, HH:MM:SS+HH:MM[:SS[.ffffff]].
#
# The optional argument timespec specifies the number of additional components of the time to include (the default is 'auto').
# It can be one of the following:
# >'auto': Same as 'seconds' if microsecond is 0, same as 'microseconds' otherwise.
# >'hours': Include the hour in the two-digit HH format.
# >'minutes': Include hour and minute in HH:MM format.
# >'seconds': Include hour, minute, and second in HH:MM:SS format.
# >'milliseconds': Include full time, but truncate fractional second part to milliseconds. HH:MM:SS.sss format.
# >'microseconds': Include full time in HH:MM:SS.ffffff format.
# 
# Note:
# 
# Excluded time components are truncated, not rounded.
# 
# ValueError will be raised on an invalid timespec argument.
# 

from datetime import time

time(hour=12, minute=34, second=56, microsecond=123456).isoformat(timespec='minutes')

# OUTPUT: '12:34'

dt = time(hour=12, minute=34, second=56, microsecond=0)
dt.isoformat(timespec='microseconds')

# OUTPUT: '12:34:56.000000'

dt.isoformat(timespec='auto')

# OUTPUT: '12:34:56'
