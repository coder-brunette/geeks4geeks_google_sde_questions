from collections import defaultdict

def subarray_sum(arr, k):
    sum_count = defaultdict(int)
    current_sum = 0
    count = 0

    for num in arr:
        current_sum += num
        if current_sum == k:
            count += 1
        if current_sum - k in sum_count:
            count += sum_count[current_sum - k]
        sum_count[current_sum] += 1

    return count

print(subarray_sum([10, 2, -2, -20, 10], -10))