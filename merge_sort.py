def merge_sort(array):
    if len(array) > 1:
        mid = len(array) // 2
        left = merge_sort(array[:mid])
        print(f"Left half: {left}")
        right = merge_sort(array[mid:])
        print(f"Right half: {right}")
        length_left = len(left)
        length_right = len(right)
        
        i = 0
        j = 0
        k = 0
        while i < length_left and j < length_right:
            if left[i] <= right[j]:
                array[k] = left[i]
                i += 1

            else:
                array[k] = right[j]
                j += 1
            k += 1
        
        while i < length_left:
            array[k] = left[i]
            i += 1
            k += 1
        
        while j < length_right:
            array[k] = right[j]
            j += 1
            k += 1

    return array



if __name__ == "__main__":
    unsorted_array = [2, 4, 1, 6, 8, 5, 3, 7]
    sorted_array = merge_sort(unsorted_array)
    print(sorted_array)

    unsorted_array = [3, 3, 6, 7, 2, 19, 3, 15]
    sorted_array = merge_sort(unsorted_array)
    print(sorted_array)

    # Notes:
#   Merge sort is recursive and divide-and-conquer algorithm.
#   It's also a stable sorting and not-inplace algorithm.
#   Θ(n) space complexity.
#   Θ(n log n) time complexity.
#
#
#
#
