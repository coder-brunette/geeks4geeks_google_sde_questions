
# Naive approach 
# O^2 logn)

def kth_smallest_abs_diff(arr, k):
    n = len(arr)
    abs_diffs = []

    for i in range(n):
        for j in range(i + 1, n):
            abs_diffs.append(abs(arr[i] - arr[j]))

    abs_diffs.sort()
    return abs_diffs[k - 1]

# print(kth_smallest_abs_diff([1, 2, 3, 4],3))


def count_pairs_with_abs_diff_less_than_or_equal_to(arr, mid):
    count = 0
    j = 0
    for i in range(len(arr)):
        while j < len(arr) and arr[j] - arr[i] <= mid:
            j += 1
        count += j - i - 1
    return count


def kth_smallest_abs_diff(arr, k):
    n = len(arr)
    abs_diff = sorted(set([abs(arr[i]-arr[j]) for i in range(n) for j in range(i+1, n)]))

    low, high = 0, max(abs_diff)

    while low < high:
        mid = low + (high - low) // 2
        if count_pairs_with_abs_diff_less_than_or_equal_to(arr, mid) < k:
            low = mid + 1
        else:
            high = mid - 1
    return low

print(kth_smallest_abs_diff([3, 9, 12, 16],5))