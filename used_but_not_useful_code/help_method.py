import calendar
import datetime


# a method to transfer a datetime to timestamp
# in python3 do not need this method
def timestamp(year, mounth, day, hour, min):
    dt = datetime(year, mounth, day, hour, min)
    return int(calendar.timegm(dt.timetuple()))