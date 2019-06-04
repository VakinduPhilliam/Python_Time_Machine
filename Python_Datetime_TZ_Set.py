# Python Datetime
# time — Time access and conversions.
# This module provides various time-related functions. For related functionality, see also the datetime and calendar modules.
# Although this module is always available, not all functions are available on all platforms. Most of the functions defined in this module call platform
# C library functions with the same name. It may sometimes be helpful to consult the platform documentation, because the semantics of these functions
# varies among platforms.
#
# time.tzset(). 
# Reset the time conversion rules used by the library routines. The environment variable TZ specifies how this is done. It will also set the variables
# tzname (from the TZ environment variable), timezone (non-DST seconds West of UTC), altzone (DST seconds west of UTC) and daylight (to 0 if this timezone
# does not have any daylight saving time rules, or to nonzero if there is a time, past, present or future when daylight saving time applies).
# The standard format of the TZ environment variable is (whitespace added for clarity):
# 
# std offset [dst [offset [,start[/time], end[/time]]]].
#
# Where the components are:
# std and dst Three or more alphanumerics giving the timezone abbreviations. These will be propagated into time.tzname offset The offset has the
# form: ± hh[:mm[:ss]]. This indicates the value added the local time to arrive at UTC. If preceded by a ‘-‘, the timezone is east of the Prime Meridian;
# otherwise, it is west. If no offset follows dst, summer time is assumed to be one hour ahead of standard time. start[/time], end[/time].
# Indicates when to change to and back from DST. The format of the start and end dates are one of the following:
# Jn The Julian day n (1 <= n <= 365). Leap days are not counted, so in all years February 28 is day 59 and March 1 is day 60.
# n The zero-based Julian day (0 <= n <= 365). Leap days are counted, and it is possible to refer to February 29. Mm.n.d The d’th day (0 <= d <= 6) of
# week.
# n of month m of the year (1 <= n <= 5, 1 <= m <= 12, where week 5 means “the last d day in month m” which may occur in either the fourth or the fifth
# week).
# Week 1 is the first week in which the d’th day occurs. Day zero is a Sunday. 
# time has the same format as offset except that no leading sign (‘-‘ or ‘+’) is allowed. The default, if time is not given, is 02:00:00.
# 

os.environ['TZ'] = 'EST+05EDT,M4.1.0,M10.5.0'

time.tzset()
time.strftime('%X %x %Z')

# OUTPUT: '02:07:36 05/08/03 EDT'

os.environ['TZ'] = 'AEST-10AEDT-11,M10.5.0,M3.5.0'

time.tzset()
time.strftime('%X %x %Z')

# OUTPUT: '16:08:12 05/08/03 AEST'

# 
# On many Unix systems (including *BSD, Linux, Solaris, and Darwin), it is more convenient to use the system’s zoneinfo (tzfile(5)) database to specify the
# timezone rules. To do this, set the TZ environment variable to the path of the required timezone datafile, relative to the root of the systems
# ‘zoneinfo’ timezone database, usually located at /usr/share/zoneinfo.
#
# For example, 'US/Eastern', 'Australia/Melbourne', 'Egypt' or 'Europe/Amsterdam'.
# 

os.environ['TZ'] = 'US/Eastern'

time.tzset()
time.tzname

# OUTPUT: '('EST', 'EDT')'

os.environ['TZ'] = 'Egypt'

time.tzset()
time.tzname

# OUTPUT: '('EET', 'EEST')'
