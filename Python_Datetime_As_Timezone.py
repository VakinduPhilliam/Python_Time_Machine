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
# datetime.astimezone(tz=None). 
# Return a datetime object with new tzinfo attribute tz, adjusting the date and time data so the result is the same UTC time as self, but in tz’s local time.
# If provided, tz must be an instance of a tzinfo subclass, and its utcoffset() and dst() methods must not return None. If self is naive, it is presumed to
# represent time in the system timezone.
# If called without arguments (or with tz=None) the system local timezone is assumed for the target timezone. The .tzinfo attribute of the converted datetime
# instance will be set to an instance of timezone with the zone name and offset obtained from the OS.
# If self.tzinfo is tz, self.astimezone(tz) is equal to self: no adjustment of date or time data is performed. Else the result is local time in the timezone
# tz, representing the same UTC time as self: after astz = dt.astimezone(tz), astz - astz.utcoffset() will have the same date and time data as dt - dt.utcoff
# set().
# If you merely want to attach a time zone object tz to a datetime dt without adjustment of date and time data, use dt.replace(tzinfo=tz).
# If you merely want to remove the time zone object from an aware datetime dt without conversion of date and time data, use dt.replace(tzinfo=None).
# 
# Note that the default tzinfo.fromutc() method can be overridden in a tzinfo subclass to affect the result returned by astimezone(). Ignoring error cases, 
# astimezone() acts like:
# 

def astimezone(self, tz):

    if self.tzinfo is tz:
        return self

    # Convert self to UTC, and attach the new time zone object.

    utc = (self - self.utcoffset()).replace(tzinfo=tz)

    # Convert from UTC to tz's local time.

    return tz.fromutc(utc)
