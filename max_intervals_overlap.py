def max_intervals_overlap(enter, exit):
    dp = [0] * (max(exit)+2)
    n = len(enter)
    
    for i in range(n):
        dp[enter[i]] += 1
        dp[exit[i]+1] -= 1

    max_guests_time = 0
    max_guests_count = 0
    guests_count = 0

    for i in range(len(dp)):
        guests_count += dp[i]
        if guests_count > max_guests_count:
            max_guests_count = guests_count
            max_guests_time = i

    return max_guests_time

print(max_intervals_overlap([1, 2, 10, 5, 5],[4, 5, 12, 9, 12]))

# time complexity is O(N + M)
# where N is the number of entries in the log register (or the length of the arrl and exit arrays) and 
# M is the maximum exit time in the log register