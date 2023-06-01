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