def floor_of_element_x(arr, x):
    low = 0
    high = len(arr) -1
    floor = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            if arr[mid] > arr[0]:
                return arr[mid]
        else:
            if arr[mid] < x:
                floor = arr[mid]
                low = mid + 1
            else:
                high = mid - 1
    return floor

print(floor_of_element_x([1,2,8,10,10,12,19],5))


def find_floor(arr, x):
    floor_val = float('-inf')  # Initialize floor to negative infinity

    for num in arr:
        if num <= x and num > floor_val:
            floor_val = num

    return floor_val if floor_val != float('-inf') else None

print(find_floor([1,2,8,10,10,12,19],5))