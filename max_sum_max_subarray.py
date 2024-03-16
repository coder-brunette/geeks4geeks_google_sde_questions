
def max_sum_of_max_subarray(arr,m,k):

    n = len(arr)
    dp = [[0]* (n+1) for _ in range(m+1)]
    prefix_sum = [0] * (n+1)

    for i in range(1,n+1):
        prefix_sum[i] = prefix_sum[i-1] + arr[i-1]

    for i in range(1,m+1):
        for j in range(i*k, n+1):
            dp[i][j] = max(dp[i][j-1], dp[i-1][j-k] + prefix_sum[j] - prefix_sum[j-k])

    return dp[m][n]

print(max_sum_of_max_subarray([1, 2, 1, 2, 6, 7, 5, 1],2,2))