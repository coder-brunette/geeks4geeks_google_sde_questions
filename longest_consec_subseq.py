def longest_consecutive_subsequence(arr):
    n = len(arr)
    arr.sort()
    current_length = 1
    max_length = 1
    if not n:
        return -1
    for i in range(1, n):
        if arr[i] == arr[i-1] + 1:
            current_length += 1
            max_length = max(max_length, current_length)
        elif arr[i] - arr[i-1] > 1:
            current_length = 1
    return max_length

#print(longest_consecutive_subsequence([1, 9, 3, 10, 4, 20, 2]))
print(longest_consecutive_subsequence([36, 41, 56, 35, 44, 33, 34, 92, 43, 32, 42]))