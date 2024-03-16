def find_starting_point(arr):
    starting_point = 0
    petrol_tank = 0
    total_petrol = 0

    for i in range(len(arr)):
        diff = arr[i][0] - arr[i][1]
        total_petrol += diff
        petrol_tank += diff

        if petrol_tank < 0:
            petrol_tank = 0
            starting_point = i + 1

    return starting_point if total_petrol >= 0 else -1

# Example usage
arr = [(4, 6), (6, 5), (7, 3), (4, 5)]
print(find_starting_point(arr))