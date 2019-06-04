# Python datetime
# locale — Internationalization services.
# The locale module opens access to the POSIX locale database and functionality. The POSIX locale mechanism allows programmers to deal with certain cultural
# issues in an application, without requiring the programmer to know all the specifics of each country where the software is executed.
# The locale module is implemented on top of the _locale module, which in turn uses an ANSI C locale implementation if available.
#
# The locale module defines the following exception and functions;
# exception locale.Error:
# Exception raised when the locale passed to setlocale() is not recognized.
#
# locale.setlocale(category, locale=None):
# If locale is given and not None, setlocale() modifies the locale setting for the category.
# The available categories are listed in the data description below. locale may be a string, or an iterable of two strings (language code and encoding). 
# If it’s an iterable, it’s converted to a locale name using the locale aliasing engine. An empty string specifies the user’s default settings.
#
# If the modification of the locale fails, the exception Error is raised. If successful, the new locale setting is returned.
# If locale is omitted or None, the current setting for category is returned.
# setlocale() is not thread-safe on most systems.
#
# Applications typically start with a call of
# 

import locale

locale.setlocale(locale.LC_ALL, '')

#
# This sets the locale for all categories to the user’s default setting (typically specified in the LANG environment variable).
# If the locale is not changed thereafter, using multithreading should not cause problems.
#