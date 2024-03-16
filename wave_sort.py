# def wave_sort(arr):
#     arr.sort()
#     n = len(arr)
#     for i in range(0, n-1, 2):
#         arr[i], arr[i+1] = arr[i+1], arr[i]

#     return arr

def wave_sort(arr):
    arr.sort()
    n = len(arr)
    for i in range(0, n-1, 2):
        if i > 0 and arr[i] < arr[i-1]:
            arr[i], arr[i-1] = arr[i-1], arr[i]
        if i < (n-1) and arr[i] < arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]    
    return arr


print(wave_sort([10, 90, 49, 2, 1, 5, 23]))

# The idea is based on the fact that if we make sure that all even positioned (at index 0, 2, 4, ..)
# elements are greater than their adjacent odd elements, we don’t need to worry about oddly positioned elements.