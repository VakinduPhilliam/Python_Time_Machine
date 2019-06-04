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
# When DST ends (the “end” line), there’s a potentially worse problem: there’s an hour that can’t be spelled unambiguously in local wall time: the last hour
# of daylight time. In Eastern, that’s times of the form 5:MM UTC on the day daylight time ends. The local wall clock leaps from 1:59 (daylight time) back 
# to 1:00 (standard time) again. Local times of the form 1:MM are ambiguous. astimezone() mimics the local clock’s behavior by mapping two adjacent UTC
# hours into the same local hour then. In the Eastern example, UTC times of the form 5:MM and 6:MM both map to 1:MM when converted to Eastern, but earlier
# times have the fold attribute set to 0 and the later times have it set to 1.
#
# For example, at the Fall back transition of 2016, we get;
# 

u0 = datetime(2016, 11, 6, 4, tzinfo=timezone.utc)

for i in range(4):
        u = u0 + i*HOUR
        t = u.astimezone(Eastern)

        print(u.time(), 'UTC =', t.time(), t.tzname(), t.fold)
