import datetime 
birthdate =input("Please enter birthdate in MM/DD/YYYY format :\n")
month,day,year=birthdate.split("/")
month=int(month)
day=int(day)
year=int(year)
now=datetime.datetime.now()

print("You born on {} in the month of {}.".format(datetime.datetime(year,month,day).strftime("%A"),datetime.datetime(year,month,day).strftime("%B")))
print("You are {} years, {} months and {} days old.".format(abs(now.year-year),abs(now.month-month), abs(now.day-day)))