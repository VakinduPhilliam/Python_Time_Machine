# Python Datetime
# calendar — General calendar-related functions.
# This module allows you to output calendars like the Unix cal program, and provides additional useful functions related to the calendar.
# By default, these calendars have Monday as the first day of the week, and Sunday as the last (the European convention). Use setfirstweekday() to set the
# first day of the week to Sunday (6) or to any other weekday. Parameters that specify dates are given as integers.
# The functions and classes defined in this module use an idealized calendar, the current Gregorian calendar extended indefinitely in both directions.
# This matches the definition of the “proleptic Gregorian” calendar in Dershowitz and Reingold’s book “Calendrical Calculations”, where it’s the base
# calendar for all computations. Zero and negative years are interpreted as prescribed by the ISO 8601 standard. Year 0 is 1 BC, year -1 is 2 BC, and so on.
# calendar.setfirstweekday(weekday). 
# Sets the weekday (0 is Monday, 6 is Sunday) to start each week. The values MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, and SUNDAY are provided
# for convenience.
#
# For example, to set the first weekday to Sunday:
#
 
import calendar

calendar.setfirstweekday(calendar.SUNDAY)
