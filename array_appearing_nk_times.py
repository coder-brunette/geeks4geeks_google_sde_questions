def num_appearing_nk_times(arr,k):
    n = len(arr)
    ele_map = {}
    for i in arr:
        if i in ele_map:
            ele_map[i] += 1
        else:
            ele_map[i] = 1
    print(ele_map)
    for key,v in ele_map.items():
        if v > n/k:
            print(key)
       
# print(num_appearing_nk_times([3, 4, 4, 5, 5, 5, 5],4))
# Time complexity: O(n^2)

def num_appearing_nk_times_sort(arr,k):
    n = len(arr)
    arr.sort()
    i = 0
    while i < n:
        count = 1
        while (i+1) < n and arr[i] == arr[i+1]:
            count += 1
            i += 1
        if count > n/k:
            print(arr[i], end=" ")
        i += 1

print(num_appearing_nk_times_sort([3, 4, 4, 5, 5, 5, 5],4))
# Time complexity: O(n*logn)