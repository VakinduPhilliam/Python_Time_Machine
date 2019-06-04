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
# classmethod datetime.utcfromtimestamp(timestamp). 
# Return the UTC datetime corresponding to the POSIX timestamp, with tzinfo None.
# This may raise OverflowError, if the timestamp is out of the range of values supported by the platform C gmtime() function, and OSError on gmtime()
# failure. It’s common for this to be restricted to years in 1970 through 2038.
# 
# To get an aware datetime object, call fromtimestamp():
# 

datetime.fromtimestamp(timestamp, timezone.utc)

# 
# On the POSIX compliant platforms, it is equivalent to the following expression: except the latter formula always supports the full years range: between
# MINYEAR and MAXYEAR inclusive.
# 

datetime(1970, 1, 1, tzinfo=timezone.utc) + timedelta(seconds=timestamp)
 

