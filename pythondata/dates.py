# Class example
from datetime import datetime

raw_date = "2017-01-11"
date_format = "%Y-%m-%d"
parsed_date = datetime.strptime(raw_date, date_format)
date_str = parsed_date.strftime("%m/%d/%y") # 01/11/17
print(date_str)

# Set a variable birthday = "1-May-12".
birthday= "1-May-12"
date_format2="%m-%B-%y"

# Parse the date using datetime.datetime.strptime.
parsed_date2=datetime.strptime(birthday, date_format2)

# Use strftime to output a date that looks like "5/1/2012".
date_str2 = parsed_date2.strftime("%-m/%-d/%Y")
print(date_str2)