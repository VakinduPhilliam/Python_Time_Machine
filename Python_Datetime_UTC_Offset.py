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
# tzinfo.utcoffset(dt). 
# Return offset of local time from UTC, as a timedelta object that is positive east of UTC. If local time is west of UTC, this should be negative.
# Note that this is intended to be the total offset from UTC; for example, if a tzinfo object represents both time zone and DST adjustments, utcoffset()
# should return their sum. If the UTC offset isn’t known, return None. Else the value returned must be a timedelta object strictly between
# -timedelta(hours=24) and timedelta(hours=24) (the magnitude of the offset must be less than one day). Most implementations of utcoffset() will probably
# look like one of these two:
# 

return CONSTANT                 # fixed-offset class

return CONSTANT + self.dst(dt)  # daylight-aware class
 
#
# If utcoffset() does not return None, dst() should not return None either.
#