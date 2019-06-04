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
# 'timedelta' Objects:
# 
# A timedelta object represents a duration, the difference between two dates or times.
# class datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0).
# All arguments are optional and default to 0. Arguments may be integers or floats, and may be positive or negative.
#
# Note that normalization of negative values may be surprising at first.
#
# For example,
# 

from datetime import timedelta

d = timedelta(microseconds=-1)

(d.days, d.seconds, d.microseconds)

#
# OUTPUT: '(-1, 86399, 999999)'
#