def largest_sum(arr):
    
    current_sum = 0
    max_sum = 0

    for num in arr:
        current_sum = max(num, current_sum+num)
        max_sum = max(current_sum, max_sum) 
    return max_sum


# Kadane's algorithm - O(N)

# print(largest_sum([-2, -3, 4, -1, -2, 1, 5, -3]))


# Using DP

def largest_sum_dp(arr):

    dp = [0]*len(arr)
    dp[0] = arr[0]
    max_sum = dp[0]

    for i in range(1,len(arr)):
        dp[i] = max(arr[i], arr[i]+dp[i-1])
        max_sum = max(max_sum, dp[i])

    return max_sum

print(largest_sum_dp([-2, -3, 4, -1, -2, 1, 5, -3]))