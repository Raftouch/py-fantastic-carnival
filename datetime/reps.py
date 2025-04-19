import datetime

# UTC time
utc_time = datetime.datetime.now(datetime.UTC)

current_time = datetime.datetime.now()

# ISO format
current_time_iso = datetime.datetime.now().isoformat()

# print(current_time.year)
# print(current_time.month)
# print(current_time.day)
# print(current_time.hour)
# print(current_time.minute)

some_datetime = datetime.datetime(year=2025, month=4, day=11, hour=11, minute=11)

current_date = datetime.date.today()

current_time_day_ago = current_time - datetime.timedelta(days=1)


current_time.strftime("%A, %d %B %Y") # Saturday, 19 April 2025

isoformatdatetime = "2025-04-19T15:31:27.959669"
my_datetime = datetime.datetime.fromisoformat(isoformatdatetime)
# print(my_datetime)