
#https://github.com/code4policy/modules/blob/5c43a372fba41d83eab4af1e425566dd82007ab3/data/03-4-python-datetime.md
#Try it: Changing the format of date & time

import datetime

raw_date = "1-May-12"
date_format = "%d-%B-%y"

parsed_date = datetime.datetime.strptime(raw_date, date_format)
date_str = parsed_date.strftime("%-m-%-d-%Y") 
print(date_str)

