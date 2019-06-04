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
# timedelta.total_seconds() 
# Return the total number of seconds contained in the duration. Equivalent to td / timedelta(seconds=1).
# 
# Note that for very large time intervals (greater than 270 years on most platforms) this method will lose microsecond accuracy.
# 
# Example usage:
# 

from datetime import timedelta

year = timedelta(days=365)

       another_year = timedelta(weeks=40, days=84, hours=23,
                             minutes=50, seconds=600)  # adds up to 365 days
year.total_seconds()

# OUTPUT: '31536000.0'

year == another_year

# OUTPUT: 'True'

ten_years = 10 * year
ten_years, ten_years.days // 365

(datetime.timedelta(days=3650), 10)

nine_years = ten_years - year
nine_years, nine_years.days // 365

(datetime.timedelta(days=3285), 9)

three_years = nine_years // 3
three_years, three_years.days // 365

(datetime.timedelta(days=1095), 3)
abs(three_years - ten_years) == 2 * three_years + year

# OUTPUT: 'True'
