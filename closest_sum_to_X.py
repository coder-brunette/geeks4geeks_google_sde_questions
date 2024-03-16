def closest_sum_to_X(arr, X):
    arr.sort()
    closest_sum = float('inf')

    for i in range(len(arr)-2):
        left = i+1
        right = len(arr) - 1
        while left<right:
            currSum = arr[i] + arr[left] + arr[right]
            if abs(currSum - X) < abs(closest_sum - X):
                closest_sum = currSum
            if currSum < X:
                left += 1
            elif currSum > X:
                right -= 1
            else:
                return currSum
    return closest_sum


print("Output: ",closest_sum_to_X([-1,2,1,4], 1))

# O(N**2)
