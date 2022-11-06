#def quick_sort(array):
#    if len(array) < 2:
#        return array

#    start = 0
#    end = len(array) - 1
#    pivot = array[end]
#    p_index = start

#    print(array)
#    for i in range(start, end):
#        if array[i] <= pivot:
#            tmp = array[i]
#            array[i] = array[p_index]
#            array[p_index] = tmp
#            p_index += 1
                
#    tmp = array[p_index]
#    array[p_index] = pivot
#    array[end] = tmp

 #   left = quick_sort(array[0:p_index])
#    right = quick_sort(array[p_index + 1 : end + 1])

#    array = left + [array[p_index]] + right

#    return array


def quick_sort(array):
    length = len(array)
    if length <= 1:
        return array
    else:
        pivot = array.pop()

    elements_greater = []
    elements_lower = []
    for element in array:
        if element > pivot:
            elements_greater.append(element)
        else:
            elements_lower.append(element)
    
    return quick_sort(elements_lower) + [pivot] + quick_sort(elements_greater)


def randomised_quick_sort(array):
    return array


if __name__ == "__main__":
    unsorted_array = [14, 6, 17, 3, 2, 2, 0, 19]
    sorted_array = quick_sort(unsorted_array)
    print("Sorted array: ", sorted_array)

    unsorted_array = [7, 2, 1, 6, 8, 5, 3, 4]
    sorted_array = quick_sort(unsorted_array)
    print("Sorted array: ", sorted_array)



# Notes
# Quick sort is a divide and conquer, recursive algortihm.
# Additionally, the quick sort is not stable.
# Time complexity: Θ(n log n), Omega(n log n), O(n^2)
# Worst case can be almost always avoided by using a randomised version of quick sort.
# Space complexity: Θ(log n), O(n)
#
#
#