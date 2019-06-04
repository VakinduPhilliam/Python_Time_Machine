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
# tzinfo.fromutc(dt). 
# This is called from the default datetime.astimezone() implementation. When called from that, dt.tzinfo is self, and dt’s date and time data are to be
# viewed as expressing a UTC time. The purpose of fromutc() is to adjust the date and time data, returning an equivalent datetime in self’s local time.
# 
# Most tzinfo subclasses should be able to inherit the default fromutc() implementation without problems. It’s strong enough to handle fixed-offset time
# zones, and time zones accounting for both standard and daylight time, and the latter even if the DST transition times differ in different years.
#
# An example of a time zone the default fromutc() implementation may not handle correctly in all cases is one where the standard offset (from UTC) depends
# on the specific date and time passed, which can happen for political reasons. The default implementations of astimezone() and fromutc() may not produce
# the result you want if the result is one of the hours straddling the moment the standard offset changes.
# 
# Skipping code for error cases, the default fromutc() implementation acts like:
# 

def fromutc(self, dt):

    # raise ValueError error if dt.tzinfo is not self

    dtoff = dt.utcoffset()
    dtdst = dt.dst()

    # raise ValueError if dtoff is None or dtdst is None

    delta = dtoff - dtdst  # this is self's standard offset

    if delta:

        dt += delta   # convert to standard local time
        dtdst = dt.dst()

        # raise ValueError if dtdst is None

    if dtdst:
        return dt + dtdst

    else:
        return dt
