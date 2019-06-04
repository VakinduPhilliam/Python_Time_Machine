# Python Datetime
# time — Time access and conversions.
# This module provides various time-related functions. For related functionality, see also the datetime and calendar modules.
# Although this module is always available, not all functions are available on all platforms. Most of the functions defined in this module call platform
# C library functions with the same name. It may sometimes be helpful to consult the platform documentation, because the semantics of these functions
# varies among platforms.
#
# time.strftime(format[, t]). 
# Convert a tuple or struct_time representing a time as returned by gmtime() or localtime() to a string as specified by the format argument.
# If t is not provided, the current time as returned by localtime() is used. format must be a string. ValueError is raised if any field in t is outside of
# the allowed range.
#

from time import gmtime, strftime

strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())

# OUTPUT: 'Thu, 28 Jun 2001 14:17:15 +0000'
