def min_painter_for_boards(boards, n, k):
    dp = [[0 for _ in range(k+1)] for _ in range(n+1)]

    # Base case: 0 boards, 0 painter
    for i in range(1, n+1):
        dp[i][1] = sum(boards[0:i])
    
    for i in range(1, n+1):
        for j in range(2, k+1):
            dp[i][j] = float('inf')
            for p in range(1, i+1):
                dp[i][j] = min(dp[i][j], max(dp[p][j-1], sum(boards[p:i])))
        

    return dp[n][k]


print(min_painter_for_boards([10, 20, 60, 50, 30, 40],6,3))