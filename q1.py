
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