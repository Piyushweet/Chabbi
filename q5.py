
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
