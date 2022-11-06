from utills import time_it

@time_it
def bubble_sort(array): # Time: O(n^2), Space: O(1)
    size = len(array)

    for k in range(size - 1):
        swapped = False
        for i in range(size - 1 - k):
            if array[i] > array[i + 1]:
                tmp = array[i]
                array[i] = array[i + 1]
                array[i + 1] = tmp
                swapped = True
        if not swapped:
            break
        
    return array


if __name__ == "__main__":
    array_to_sort = [13, 9, 16, 28, 3, 90, 43]
    sorted_array = bubble_sort(array_to_sort)
    print(sorted_array)

