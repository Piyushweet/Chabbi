# Assignment for internship by Chabbi

Implement 10 question as given 
Now i have attached the screenshot with code so that it will be east to understand and provide necessary details wherever required

Q1.


'''Get your basics right - Implement selection sort algorithm in python. 
The function accepts a list in the input and returns a sorted list.'''



#finding minimum element from the unsorted and putting it to beginning


def selection_sort(lst):
    # Iterate over the list
    for i in range(len(lst)):
        min_index = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[min_index]:
                min_index = j
        # Swap the current element with the minimum element
        lst[i], lst[min_index] = lst[min_index], lst[i]
    return lst

list = list(map(int,input().split(",")))
sort = selection_sort(list)
print(sort)


Q2.


'''Write a program that returns the file type from a file name. The type of the file is determined
from the extension. Initially, a list of values of the form "extension,type"(e.g. xls,spreadsheet;
png,image) will be input.'''


def get_file_type(ext_type, lst):
    types = {}
    for ext_type in ext_type:
        ext, f_type = ext_type.split(',')
        types[ext] = f_type

    result = {}  # Dictionary to store file - name - type mapping
    for file_name in lst:
        if '.' in file_name:
            ext = file_name.split( '.' ) [ - 1 ]
            if ext in types:
                result[file_name] = types[ext]
            else:
                result[file_name] = 'unknown'
        else:
            result[file_name] = 'unknown'

    return result


ext_type = input("Enter extension and type values: ")
file_list = input("Enter the file names: ").split(",")

ext_type_list = ext_type.split(';')
file_types = get_file_type(ext_type_list, file_list)
print(file_types)


Q3.

''' write a program to sort the list according to a key given in input.'''


def sort_list_of_dicts(lst_of_dicts, key):
    sorted_lst = sorted(lst_of_dicts, key = lambda x: x[key])
    return sorted_lst


def f():
    """
    Gets a list of dictionaries from the user and sorts them by the given key.
    Returns:A list of dictionaries sorted by the given key.
    """
    lst_of_dicts = []
    while True:
        dict_input = input("Enter a dictionary (or press Enter to finish): ")
        if dict_input == "":
            break
        dict_items = dict_input.split(",")
        dictionary = {}
        for item in dict_items:
            k, v = item.split(":")
            dictionary[k.strip()] = v.strip()
        lst_of_dicts.append(dictionary)

    sort_key = input("Enter the sort key: ")

    sorted_lst = sort_list_of_dicts(lst_of_dicts, sort_key)
    return sorted_lst

sorted_lst = f()
print(sorted_lst)


Q4.



'''Given a dictionary, switch position of key and values in
the dict, i.e., value becomes the key and
key becomes value. The function's body shouldn't have more than one statement.
'''

my_dict = {}


while True:
    key = input("Enter a key (or press Enter to finish): ")
    if key == "":
        break
    value = input("Enter the corresponding value: ")
    my_dict[key] = value

my_dict = {value: key for key, value in my_dict.items()}

print("The modified dictionary is:", my_dict)


Q5.



'''Given 2 lists in input. Write a program to return the elements, 
which are common to both lists(set intersection) and those which are
not common(set symmetric difference) between the lists.
'''

# The function intersection takes two lists as input and 
# returns a new list containing the common elements between them.


def compare_lists(list1, list2):
    common_elements = set(list1) & set(list2)
    unique_elements = set(list1) ^ set(list2)
    return common_elements, unique_elements


list1 = input("Enter the elements of the first list: ").split(",")
list2 = input("Enter the elements of the second list: ").split(",")

common, unique = compare_lists(list1, list2)

print("Common elements:", common)
print("Unique elements:", unique)


Q6.



'''Given a list and 2 indices as input , return the sub - list
enclosed within these 2 indices. It should contain every second element.'''

#The function get_sublist takes a list and two indices as input and returns
#a sublist containing every second element within the given indices.


def get_sublist(lst, start, end):
    sub = lst[ start:end + 1:2] # Get the sublist of the original list.
    return sub


my_list = list(map(int, input().split(",")))
start = int(input("Starting index: "))
end = int(input("Ending index: "))
result = get_sublist(my_list, start, end)
print(result)


Q7.


'''Calculate the factorial of a number using lambda function.'''

'''The lambda function factorial calculates the factorial of a 
number recursively by multiplying the number with the factorial 
of its predecessor until reaching 0.'''

factorial = lambda n: 1 if n == 0 else n * factorial(n - 1)

number = int(input("Enter the number: "))
result = factorial(number)

print("Factorial of", number, "is:", result)


Q8.




A0 = dict(zip(('a', 'b', 'c', 'd', 'e'), (1, 2, 3, 4, 5)))
# A0 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

A1 = range(10)
# A1 = range(0, 10)

A2 = sorted([i for i in A1 if i in A0])
# A2 = []

A3 = sorted([A0[s] for s in A0])
# A3 = [1, 2, 3, 4, 5]

A4 = [i for i in A1 if i in A3]
# A4 = [1, 2, 3, 4, 5]

A5 = {i: i * i for i in A1}
''' A5 = {0: 0, 1: 1, 2: 4, 3: 9, 4: 16,
5: 25, 6: 36, 7: 49, 8: 64, 9: 81}'''
A6 = [[i, i * i] for i in A1]
''' A6 = [[0, 0], [1, 1], [2, 4], [3, 9], [4, 16], 
[5, 25], [6, 36], [7, 49], [8, 64], [9, 81]]'''

A7 = reduce(lambda x, y: x + y, [10, 23, - 45, 33])
# A7 = 21

A8 = list(map(lambda x: x * 2, [1, 2, 3, 4]))
# A8 = [2, 4, 6, 8]

A9 = list(filter(lambda x: len(x) > 3, ["I", "want", "to", "learn", "python"]))
# A9 = ['want', 'learn', 'python']



Q9.



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


q10.



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




Q11.



'''Something fishy there -
Find output of following:'''


def f(x,l=[]):
    for i in range(x):
        l.append(i*i)
    print(l)

# f(2)
'''This give us the result [0,1] 
as intially the list is emppty and 0*0 | 1*1'''

# f(3,[3,2,1])
'''this give the output as [3,2,1,0,1,4] 
as intially the list is given [3,2,1] 
and now it append the previous one so that 0*0|1*1|2*2]'''

# f(3)
'''this give us the [0,1,0,1,4] 
as the previous state of the list is retained due to the default argument 
and now the list continue to append to 0*0|1*1|2*2'''

'''So the overall result 
[0, 1]
[3, 2, 1, 0, 1, 4]
[0, 1, 0, 1, 4]'''
