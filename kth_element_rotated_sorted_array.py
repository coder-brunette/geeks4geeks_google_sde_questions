def find_kth_element_rotated_sorted_array(nums, k):
    left = 0
    right = len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == k:
            return mid
        
        if nums[left] <= mid:
            if nums[left] <= k < nums[mid]:
                right = mid - 1 
            else:
                left = mid + 1
        else:
            if nums[mid] < k <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1

# print(find_kth_element_rotated_sorted_array([4, 5, 6, 7, 8, 9, 1, 2, 3],6))
print(find_kth_element_rotated_sorted_array([5, 6, 7, 8, 9, 10, 1, 2, 3],30))
