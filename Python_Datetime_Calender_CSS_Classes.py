# Python Datetime
# calendar — General calendar-related functions.
# This module allows you to output calendars like the Unix cal program, and provides additional useful functions related to the calendar.
# By default, these calendars have Monday as the first day of the week, and Sunday as the last (the European convention). Use setfirstweekday() to set the
# first day of the week to Sunday (6) or to any other weekday. Parameters that specify dates are given as integers.
# The functions and classes defined in this module use an idealized calendar, the current Gregorian calendar extended indefinitely in both directions.
# This matches the definition of the “proleptic Gregorian” calendar in Dershowitz and Reingold’s book “Calendrical Calculations”, where it’s the base
# calendar for all computations. Zero and negative years are interpreted as prescribed by the ISO 8601 standard. Year 0 is 1 BC, year -1 is 2 BC, and so on.
#
# cssclasses. 
# A list of CSS classes used for each weekday. The default class list is:
 
cssclasses = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]

# 
# more styles can be added for each day:
# 

cssclasses = ["mon text-bold", "tue", "wed", "thu", "fri", "sat", "sun red"]

# 
# Note that the length of this list must be seven items.
#
# Note that although the naming for the above described class attributes is singular (e.g. cssclass_month cssclass_noday), one can replace the single
# CSS class with a space separated list of CSS classes, for example:
# 

"text-bold text-red"

# 
# Here is an example how HTMLCalendar can be customized:
# 

class CustomHTMLCal(calendar.HTMLCalendar):

    cssclasses = [style + " text-nowrap" for style in
                  calendar.HTMLCalendar.cssclasses]

    cssclass_month_head = "text-center month-head"
    cssclass_month = "text-center month"

    cssclass_year = "text-italic lead"


