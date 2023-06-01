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
