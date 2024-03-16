def element_appears_once(arr):
    element_dict = {}

    for i in arr:
        if i in element_dict:
            element_dict[i] += 1
        else:
            element_dict[i] = 1

    for k,v in element_dict.items():
        if v == 1:
            return k
        
# print(element_appears_once([10, 20, 10, 30, 10, 30, 30]))
# Time complexity : O(N)
# Space complexity: O(N) // because of dict
        

def element_appears_once_bitwise(arr):
    ones = 0
    twos = 0

    for i in arr:
        ones = (ones ^ i) & ~twos
        twos = (twos ^ i) & ~ones
    
    return ones

print(element_appears_once_bitwise([2,2,2,3]))

# Time complexity : O(N)
# Space complexity: O(1) // because of bitwise 


# We will use two variables, ones and twos, to keep track of the bits that have appeared once and twice, respectively.
# Initially, both ones and twos are 0.

# Now, let's iterate through the array arr:

# First iteration (num = 2):
# ones is 0 and num is 2.
# ones ^ num is 0 ^ 2, which is 2 in binary 10.
# ~twos is the bitwise NOT of twos, which is ~0 (since twos is 0), resulting in 1 in binary 01.
# (ones ^ num) & ~twos is 10 & 01, which is 00.
# After this step, ones becomes 0.
# Second iteration (num = 2):
# ones is 0 and num is 2.
# ones ^ num is 0 ^ 2, which is 2 in binary 10.
# ~twos is the bitwise NOT of twos, which is ~0 (since twos is 0), resulting in 1 in binary 01.
# (ones ^ num) & ~twos is 10 & 01, which is 00.
# After this step, ones remains 0.
# Third iteration (num = 2):
# ones is 0 and num is 2.
# ones ^ num is 0 ^ 2, which is 2 in binary 10.
# ~twos is the bitwise NOT of twos, which is ~0 (since twos is 0), resulting in 1 in binary 01.
# (ones ^ num) & ~twos is 10 & 01, which is 00.
# After this step, ones remains 0.
# Fourth iteration (num = 3):
# ones is 0 and num is 3.
# ones ^ num is 0 ^ 3, which is 3 in binary 11.
# ~twos is the bitwise NOT of twos, which is ~0 (since twos is 0), resulting in 1 in binary 01.
# (ones ^ num) & ~twos is 11 & 01, which is 01.
# After this step, ones becomes 1.
# After iterating through the array, ones will be 1, which represents the element that appears only once, i.e., 3.

# In this example, the XOR operation (^) toggles the bits in ones that are set in num, effectively adding num to ones.
# The use of bitwise AND (&) with the negation of twos ensures that the bits in ones are only those that have appeared once and not twice.