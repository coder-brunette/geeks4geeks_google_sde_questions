def majority_element(arr):
    freq = {}

    for i in arr:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1

    for k in freq.keys():
        if freq[k] > len(arr)/2:
            return k
        else:
            return "No Majority Element"

print(majority_element([1, 1, 2, 1, 3, 5, 1]))