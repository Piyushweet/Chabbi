
'''Of date and days
Write a func that takes 2 args:
date - string representing a date in the form of 'yy - mm - dd'
n - integer
Returns the string representation of date n days before 'date'
E.g. f('16 - 12 - 10 ', 11) should return '16 - 11 - 29'''


#datetime is a class that represents a specific point in time
#timedelta help to represents a duration difference between two times


from datetime import datetime, timedelta


def get_date_before(d, n):
    intial = datetime.strptime(d, " % y - % m - % d")
    days = timedelta(days = n)
    return (intial - days).strftime(" % y - % m - % d ")

date = input("Enter the date (yy - mm - dd): ")
n = int(input("Enter the number of days: "))

print("The Date before " + str(n) + " days is " + get_date_before(date, n))
