from utills import time_it

@time_it # using decorator for measuring a performance
def binary_search(array, number_to_find):
    end_index = len(array) - 1
    start_index = 0

    while start_index <= end_index:
        middle_index = (start_index + end_index) // 2
        mid_number = array[middle_index]
    
        if mid_number == number_to_find:
            return middle_index
        
        if mid_number < number_to_find:
            start_index = middle_index + 1
        
        else:
            end_index = middle_index - 1
    return -1

@time_it
def recursive_binary_search(array, number_to_find, left_index, right_index):
    if right_index < left_index:
        return -1

    middle_index = (left_index + right_index) // 2
    mid_number = array[middle_index]

    if middle_index >= len(array) or middle_index < 0:
        return -1
    
    if mid_number == number_to_find:
        return middle_index
        
    if mid_number < number_to_find:
        left_index = middle_index + 1
        
    else:
        right_index = middle_index - 1

    return recursive_binary_search(array, number_to_find, left_index, right_index)


if __name__ == "__main__":
    array = [12, 15, 17, 19, 21, 24, 45, 67]
    number_to_find = 67

    index = binary_search(array, number_to_find)
    print(index)

    index = recursive_binary_search(array, number_to_find, 0, len(array)) # we need to define pointers as arguments, because due to recursion
    print(index)                                                           # these are going to change.

