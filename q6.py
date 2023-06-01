
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
