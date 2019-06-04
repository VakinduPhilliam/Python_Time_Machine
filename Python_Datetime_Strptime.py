# Python Datetime
# time — Time access and conversions.
# This module provides various time-related functions. For related functionality, see also the datetime and calendar modules.
# Although this module is always available, not all functions are available on all platforms. Most of the functions defined in this module call platform
# C library functions with the same name. It may sometimes be helpful to consult the platform documentation, because the semantics of these functions
# varies among platforms.
#
# time.strptime(string[, format]).
# Parse a string representing a time according to a format. The return value is a struct_time as returned by gmtime() or localtime().
# The format parameter uses the same directives as those used by strftime(); it defaults to "%a %b %d %H:%M:%S %Y" which matches the formatting returned by
# ctime(). If string cannot be parsed according to format, or if it has excess data after parsing, ValueError is raised. The default values used to fill in
# any missing data when more accurate values cannot be inferred are (1900, 1, 1, 0, 0, 0, 0, 1, -1). Both string and format must be strings.
#
# For example:
# 

import time

time.strptime("30 Nov 00", "%d %b %y")   # doctest: +NORMALIZE_WHITESPACE

time.struct_time(tm_year=2000, tm_mon=11, tm_mday=30, tm_hour=0, tm_min=0,
                 tm_sec=0, tm_wday=3, tm_yday=335, tm_isdst=-1)
