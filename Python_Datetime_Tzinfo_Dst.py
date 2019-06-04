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
# tzinfo.dst(dt) 
# Return the daylight saving time (DST) adjustment, as a timedelta object or None if DST information isn’t known. Return timedelta(0) if DST is not in
# effect. If DST is in effect, return the offset as a timedelta object (see utcoffset() for details).
# Note that DST offset, if applicable, has already been added to the UTC offset returned by utcoffset(), so there’s no need to consult dst() unless you’re
# interested in obtaining DST info separately. For example, datetime.timetuple() calls its tzinfo attribute’s dst() method to determine how the tm_isdst
# flag should be set, and tzinfo.fromutc() calls dst() to account for DST changes when crossing time zones.
#
# An instance tz of a tzinfo subclass that models both standard and daylight times must be consistent in this sense:
# 

tz.utcoffset(dt) - tz.dst(dt).

# 
# must return the same result for every datetime dt with dt.tzinfo == tz For sane tzinfo subclasses, this expression yields the time zone’s “standard offset”
# , which should not depend on the date or the time, but only on geographic location.
#
# Most implementations of dst() will probably look like one of these two:
# 

def dst(self, dt):

    # a fixed-offset class:  doesn't account for DST

    return timedelta(0)
 
#
# or
# 

def dst(self, dt):

    # Code to set dston and dstoff to the time zone's DST
    # transition times based on the input dt.year, and expressed
    # in standard local time.  Then

    if dston <= dt.replace(tzinfo=None) < dstoff:
        return timedelta(hours=1)

    else:
        return timedelta(0)
