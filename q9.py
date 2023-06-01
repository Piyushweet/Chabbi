
'''Write a func that takes 3 args:
from_date - string representing a date in the form of 'yy - mm - dd'
to_date - string representing a date in the form of 'yy - mm - dd'
difference - int
Returns True if from_date and to_date are less than 
difference days away from each other,else returns False.'''


#datetime is a class that represents a specific point in time
#timedelta help to represents a duration difference between two times


from datetime import datetime, timedelta


def check_date_diff():
    f = input("Enter the from date (yy - mm - dd): ")
    t = input("Enter the to date (yy - mm - dd): ")
    d = int(input("Enter the difference (in days): "))

    f_o = datetime.strptime(f, ' % y - % m - % d ')
    t_o = datetime.strptime(t, ' % y - % m - % d ')

    d_d = abs(t_o - f_o).days

    return d_d < d


result = check_date_diff()
print(result)
