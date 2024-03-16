def load_weights_d_days(arr, d):
    low = max(arr)
    high = sum(arr)

    while low < high:
        mid = low + (high - low) //2
        if is_possible(arr, d, mid):
            high = mid
        else:
            low = mid + 1

    return low

def is_possible(arr, d, mid):
    days = 1
    current_weight = 0
    
    for weight in arr:
        if weight + current_weight > mid:
            days += 1
            current_weight = 0
        current_weight += weight
    return days <= d

print(load_weights_d_days([1,2,1],2))