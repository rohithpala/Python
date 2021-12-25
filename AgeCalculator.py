import datetime as dt
birthday = dt.datetime(2000,10,10)
time_alive = dt.datetime.today() - birthday
print(time_alive.days//365, "years")
print(time_alive.days, "days")
