# from datetime import datetime


# now=datetime.now()
# print(now)


# print(now.date())   #2025-04-05
# print(now.time())   #01:32:53.670634

# print(now.year)     # 2025
# print(now.month)    # 4
# print(now.day)      # 5
# print(now.hour)     # 1
# print(now.minute)   # 29
# print(now.second)   # 58



# today = datetime.today()
# print(today.date())  # Output: 2025-04-05



# my_date = datetime(2025, 12, 25, 10, 30, 0)
# print(my_date)  # Output: 2025-12-25 10:30:00



# import datetime
# my_date = datetime.date(2025, 12, 25)
# print(my_date)  # 2025-12-25

# my_time = datetime.time(14, 30, 0)
# print(my_time)  # 14:30:00





# from datetime import timedelta, datetime

# now = datetime.now()
# formatted = now.strftime("%Y-%m-%d %H:%M:%S")
# print(formatted)  # 2025-04-05 21:03:00


# print(now.strftime("%Y-%m-%d"))      # 2025-04-05
# print(now.strftime("%d/%m/%Y"))      # 05/04/2025
# print(now.strftime("%I:%M %p"))      # 02:23 AM
# print(now.strftime("%A, %B %d"))     # Saturday, April 05








# from datetime import datetime

# date_string = "25/12/2023 10:30 AM"
# parsed_date = datetime.strptime(date_string, "%d/%m/%Y %I:%M %p")
# print(parsed_date)  # Output: 2023-12-25 10:30:00



# now = datetime.now()
# print(now.year)    # 2025
# print(now.month)   # 4
# print(now.day)     # 5
# print(now.hour)    # 21
# print(now.minute)  # 0






from datetime import datetime
import pytz

# Current local time
print(datetime.now())

# Specifying time zone
tz = pytz.timezone("US/Pacific")
print(datetime(2025, 12, 13, tzinfo=tz))

         #or

print(datetime.now(tz))  # Current time in US/Pacific





