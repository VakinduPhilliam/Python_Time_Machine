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
# datetime.timestamp(). 
# Return POSIX timestamp corresponding to the datetime instance. The return value is a float similar to that returned by time.time().
#
# Naive datetime instances are assumed to represent local time and this method relies on the platform C mktime() function to perform the conversion.
# Since datetime supports wider range of values than mktime() on many platforms, this method may raise OverflowError for times far in the past or far in the
# future.
# 
# For aware datetime instances, the return value is computed as:
# 

(dt - datetime(1970, 1, 1, tzinfo=timezone.utc)).total_seconds()

#
# Note:
# 
# There is no method to obtain the POSIX timestamp directly from a naive datetime instance representing UTC time.
# If your application uses this convention and your system timezone is not set to UTC, you can obtain the POSIX timestamp by supplying tzinfo=timezone.utc:
# 

timestamp = dt.replace(tzinfo=timezone.utc).timestamp()

# 
# or by calculating the timestamp directly:
# 

timestamp = (dt - datetime(1970, 1, 1)) / timedelta(seconds=1)
