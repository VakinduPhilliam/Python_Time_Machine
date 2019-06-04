# Python datetime
# locale — Internationalization services.
# The locale module opens access to the POSIX locale database and functionality. The POSIX locale mechanism allows programmers to deal with certain cultural
# issues in an application, without requiring the programmer to know all the specifics of each country where the software is executed.
# The locale module is implemented on top of the _locale module, which in turn uses an ANSI C locale implementation if available.
#
# locale.CHAR_MAX 
# This is a symbolic constant used for different values returned by localeconv().
# 
# Example:
# 

import locale

loc = locale.getlocale()  # get current locale

# use German locale; name might vary with platform

locale.setlocale(locale.LC_ALL, 'de_DE')
locale.strcoll('f\xe4n', 'foo')  # compare a string containing an umlaut

locale.setlocale(locale.LC_ALL, '')   # use user's preferred locale
locale.setlocale(locale.LC_ALL, 'C')  # use default (C) locale

locale.setlocale(locale.LC_ALL, loc)  # restore saved locale
