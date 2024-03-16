def search_element(arr):
    smallest = arr[0]
    for i in range(1,len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]

    return smallest

print(search_element([5, 6, 1, 2, 3, 4]))

# Time Complexity: O(N)

# If the array is not rotated, i.e., the first element is less than or equal to the last element, then the first element is returned 
# as the minimum element. 
# Condition to check when the array is rotated - If the element at the mid index is less than the element at mid-1 index, then the 
# element at the mid index is returned as the minimum element.