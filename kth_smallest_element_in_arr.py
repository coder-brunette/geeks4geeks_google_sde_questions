def kth_smallest_element_array(nums, k):
    nums.sort()
    return nums[k-1]


print(kth_smallest_element_array([7, 10, 4, 3, 20, 15],3))
print(kth_smallest_element_array([7, 10, 4, 3, 20, 15],4))