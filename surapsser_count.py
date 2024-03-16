from collections import defaultdict

def surapsser_count_of_element(arr):
    element_map = {}
    for i in range(0, len(arr)):
        element_map[arr[i]] = 0
        for j in range(i+1, len(arr)):
            if arr[j] > arr[i]:
                element_map[arr[i]] += 1
    return list(element_map.values())           
    

print(surapsser_count_of_element([2, 7, 5, 3, 0, 8, 1]))