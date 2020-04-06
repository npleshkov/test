import datetime
# from datetime import datetime, date, time
year = 2020
month = 1
day = 10
hour=0
minute=0
second=0
microsecond=0

date1 = datetime.datetime(year, month, day)
timestamp1 = 1584994819
print(f'datetime = {date1}')
print(datetime.datetime.timestamp(date1))
print(datetime.datetime.fromtimestamp(timestamp1))